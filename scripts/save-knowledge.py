import argparse
import os
import re
import sys
from datetime import datetime

# Ensure UTF-8 output on all platforms
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

VALID_CATEGORIES = ['gotchas', 'patterns', 'decisions', 'context']
BASE_DIR = '.agent/memory/entries'
MAX_FILENAME_LENGTH = 80


def slugify(text):
    """Convert text to a URL/filename-safe slug."""
    slug = text.lower().strip()
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[\s_]+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    slug = slug.strip('-')
    return slug[:MAX_FILENAME_LENGTH]


def generate_frontmatter(category, title, tags=None):
    """Generate standard frontmatter for a memory entry."""
    date_str = datetime.now().strftime('%Y-%m-%d')
    tags_str = ', '.join(tags) if tags else ''
    return (
        f'# {title}\n'
        f'**Category:** {category}\n'
        f'**Severity:** INFO\n'
        f'**Tags:** [{tags_str}]\n'
        f'**Date:** {date_str}\n'
        f'**Source:** Chat session\n'
        f'\n---\n\n'
    )


def has_frontmatter(content):
    """Check if content already has the standard frontmatter."""
    required_fields = ['**Category:**', '**Date:**']
    return all(field in content for field in required_fields)


def extract_title(content):
    """Extract title from markdown content (first # heading)."""
    match = re.match(r'^#\s+(.+)', content.strip())
    if match:
        return match.group(1).strip()
    return None


def save_knowledge(category, content, title=None, tags=None):
    """Save a knowledge entry to the memory system."""
    # Validate category
    if category not in VALID_CATEGORIES:
        print(f'Error: Invalid category "{category}". Must be one of: {VALID_CATEGORIES}')
        return False

    # Check category directory exists
    cat_dir = os.path.join(BASE_DIR, category)
    if not os.path.exists(cat_dir):
        print(f'Error: Category directory "{cat_dir}" not found.')
        return False

    # Extract or validate title
    if not title:
        title = extract_title(content)
    if not title:
        print('Error: No title found. Content must start with "# Title" or provide --title.')
        return False

    # Generate filename from title
    filename = slugify(title)
    if not filename:
        print('Error: Could not generate filename from title.')
        return False

    file_path = os.path.join(cat_dir, f'{filename}.md')

    # Check for duplicates
    if os.path.exists(file_path):
        print(f'Warning: File already exists at "{file_path}". Overwriting.')

    # Add frontmatter if missing
    if not has_frontmatter(content):
        frontmatter = generate_frontmatter(category, title, tags)
        content = frontmatter + content

    # Write file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f'Saved: {file_path}')
    return True


def main():
    parser = argparse.ArgumentParser(
        description='Save knowledge entry to memory system.'
    )
    parser.add_argument(
        '--category', required=True, choices=VALID_CATEGORIES,
        help='Category: gotchas, patterns, decisions, or context'
    )
    parser.add_argument(
        '--title', help='Entry title (auto-extracted from content if not provided)'
    )
    parser.add_argument(
        '--tags', nargs='+', help='Tags for the entry (e.g., nextjs tailwind)'
    )
    parser.add_argument(
        '--file', help='Path to file containing the content'
    )
    parser.add_argument(
        'content', nargs='?', help='Knowledge content string'
    )
    args = parser.parse_args()

    # Get content
    content = args.content
    if args.file:
        if not os.path.exists(args.file):
            print(f'Error: File "{args.file}" not found.')
            return
        with open(args.file, 'r', encoding='utf-8') as f:
            content = f.read()

    if not content:
        print('Error: No content provided. Use --file or pass content as argument.')
        return

    # Save
    success = save_knowledge(args.category, content, args.title, args.tags)
    if success:
        # Auto-sync stats
        os.system(f'python {os.path.join("scripts", "sync-agents-stats.py")}')


if __name__ == '__main__':
    main()
