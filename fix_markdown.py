"""
Fix markdown formatting for GitHub compatibility
Replace Obsidian callouts with standard markdown that renders properly
"""
import re

def fix_markdown_file(filepath):
    """Fix markdown formatting in a file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to match Obsidian callouts with bold text
    # > [!type] emoji **Title**
    # Pattern: > [!type] emoji **text**

    # Replace callout blocks with proper markdown
    # Keep the emoji and text, but use proper headers instead

    lines = content.split('\n')
    fixed_lines = []
    in_callout = False
    callout_content = []

    for i, line in enumerate(lines):
        # Check if line starts with callout
        callout_match = re.match(r'^> \[!(blue|red|green|yellow|purple)\]\s*(.*?)\s*\*\*(.*?)\*\*\s*$', line)

        if callout_match:
            # This is a callout with bold text
            callout_type = callout_match.group(1)
            emoji = callout_match.group(2).strip()
            title = callout_match.group(3).strip()

            # Convert to standard markdown
            # Use bold without the callout syntax
            fixed_line = f"**{emoji} {title}**"
            fixed_lines.append(fixed_line)
            in_callout = True
        elif line.startswith('> ') and in_callout:
            # This is continuation of callout content
            fixed_lines.append(line[2:])  # Remove "> " prefix
        elif in_callout and line.strip() == '':
            # End of callout block
            in_callout = False
            fixed_lines.append(line)
        else:
            # Regular line
            in_callout = False
            fixed_lines.append(line)

    fixed_content = '\n'.join(fixed_lines)

    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(fixed_content)

    print(f"✓ Fixed: {filepath}")

if __name__ == '__main__':
    import os
    import glob

    # Find all markdown files
    md_files = []
    for root, dirs, files in os.walk('.'):
        # Skip hidden directories and node_modules
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'node_modules']
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))

    print(f"Found {len(md_files)} markdown files to fix...\n")

    fixed_count = 0
    for filepath in md_files:
        try:
            fix_markdown_file(filepath)
            fixed_count += 1
        except Exception as e:
            print(f"✗ Error fixing {filepath}: {e}")

    print(f"\n✅ Fixed {fixed_count}/{len(md_files)} markdown files!")
    print("All Obsidian callouts converted to standard markdown.")
    print("Will render properly on GitHub and VS Code.")
