
import re

# Read the content of the spelling_errors.md file
with open('spelling_errors.md', 'r') as f:
    lines = f.readlines()

# Prepare the header for the Markdown table
table = "| Spelling Error | File Path | Line Number |\n"
table += "|---|---|---|\n"

# Process each line to extract the required information and format it as a table row
for line in lines:
    match = re.search(r'- (.*) \(found in (.*) at line (\d+)\)', line)
    if match:
        word, filepath, line_number = match.groups()
        table += f"| {word.strip()} | {filepath.strip()} | {line_number.strip()} |\n"

# Write the formatted table back to the spelling_errors.md file
with open('spelling_errors.md', 'w') as f:
    f.write(table)
