import os
import re
import sys

# Ensure UTF-8 output on all platforms
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

# Active categories (aligned with .qoder/rules/memory-usage.md)
CATEGORIES = ['gotchas', 'patterns', 'decisions', 'context']
BASE_DIR = '.agent/memory/entries'
AGENTS_MD = 'AGENTS.md'

# Required frontmatter fields
REQUIRED_FIELDS = ['**Category:**', '**Date:**']

# Valid severity values (plain text only — no emojis)
VALID_SEVERITIES = ['CRITICAL', 'MEDIUM', 'INFO']

# Tags must use bracket format: [tag1, tag2]
TAGS_PATTERN = re.compile(r'\*\*Tags:\*\*\s*\[.+\]')


def count_entries(category):
    """Count valid .md files in a category directory."""
    cat_dir = os.path.join(BASE_DIR, category)
    if not os.path.exists(cat_dir):
        return 0
    return len([f for f in os.listdir(cat_dir) if f.endswith('.md')])


def validate_entry(filepath):
    """Check if a memory entry has proper frontmatter, severity format, and tag format."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        missing = [field for field in REQUIRED_FIELDS if field not in content]

        # Validate severity format (plain text only, no emojis)
        severity_match = re.search(r'\*\*Severity:\*\*\s*(.+)', content)
        if severity_match:
            severity_value = severity_match.group(1).strip()
            # Check for emoji markers
            has_emoji = any(
                c in severity_value
                for c in ['🚨', '⚠️', 'ℹ️', '❌', '✅', '🔥']
            )
            if has_emoji:
                missing.append(
                    f'severity uses emoji (should be plain: {", ".join(VALID_SEVERITIES)})'
                )
            else:
                # Check if it's a valid severity value
                clean_severity = severity_value.replace('**', '').strip()
                if clean_severity not in VALID_SEVERITIES:
                    missing.append(
                        f'severity "{clean_severity}" not in {VALID_SEVERITIES}'
                    )

        # Validate tags format (must use brackets)
        if '**Tags:**' in content and not TAGS_PATTERN.search(content):
            missing.append('tags should use bracket format: [tag1, tag2]')

        # Check for required sections
        if '## Problem / Context' not in content and '## Context' not in content:
            missing.append('missing "## Problem / Context" section')
        if '## Solution / Pattern' not in content:
            missing.append('missing "## Solution / Pattern" section')

        return len(missing) == 0, missing
    except Exception as e:
        return False, [str(e)]


def sync_stats():
    """Scan all categories, count entries, validate format, update AGENTS.md."""
    stats = {}
    total = 0
    warnings = []

    print('Scanning memory entries...')

    for cat in CATEGORIES:
        count = count_entries(cat)
        stats[cat] = count
        total += count

        # Validate each entry
        cat_dir = os.path.join(BASE_DIR, cat)
        if os.path.exists(cat_dir):
            for filename in os.listdir(cat_dir):
                if filename.endswith('.md'):
                    filepath = os.path.join(cat_dir, filename)
                    valid, missing = validate_entry(filepath)
                    if not valid:
                        warnings.append(f'  {cat}/{filename}: {missing}')

    # Update AGENTS.md
    if os.path.exists(AGENTS_MD):
        with open(AGENTS_MD, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update total count
        content = re.sub(
            r'Total Knowledge Entries: \d+',
            f'Total Knowledge Entries: {total}',
            content
        )

        # Update per-category counts
        for cat, count in stats.items():
            content = re.sub(
                fr'\| {cat.capitalize()} \| \d+ \|',
                f'| {cat.capitalize()} | {count} |',
                content
            )

        with open(AGENTS_MD, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f'Updated {AGENTS_MD}')
    else:
        print(f'Warning: {AGENTS_MD} not found. Stats not updated.')

    # Print summary
    print(f'\nKnowledge Stats:')
    print(f'  Total: {total}')
    for cat, count in stats.items():
        print(f'  {cat.capitalize()}: {count}')

    # Print warnings
    if warnings:
        print(f'\nWarnings ({len(warnings)} entries with issues):')
        for w in warnings:
            print(w)
    else:
        print('\nAll entries have valid frontmatter, severity format, and tag format.')


if __name__ == '__main__':
    sync_stats()
