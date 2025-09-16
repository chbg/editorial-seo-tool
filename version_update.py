#!/usr/bin/env python3

# Update version.json
with open('version.json', 'r') as f:
    version_data = f.read()

# Update version number
version_data = version_data.replace('"version": "1.3.1"', '"version": "1.3.2"')

# Add new changelog entry
version_data = version_data.replace(
    '"v1.3.1 - Fixed AI Artifacts review to use client-specific memory instead of generic list",',
    '"v1.3.2 - Fixed AI Artifacts regeneration to use client-specific memory for consistency",\n    "v1.3.1 - Fixed AI Artifacts review to use client-specific memory instead of generic list",'
)

with open('version.json', 'w') as f:
    f.write(version_data)

# Update index.html
with open('index.html', 'r') as f:
    html_content = f.read()

# Update title
html_content = html_content.replace('Editorial SEO Tool (Beta) v1.3.1', 'Editorial SEO Tool (Beta) v1.3.2')

# Update sidebar version
html_content = html_content.replace('v1.3.1</div>', 'v1.3.2</div>')

# Update APP_VERSION
html_content = html_content.replace("const APP_VERSION = '1.3.1';", "const APP_VERSION = '1.3.2';")

# Update changelog
html_content = html_content.replace(
    'Fixed AI Artifacts review to use client-specific memory instead of generic list',
    'Fixed AI Artifacts regeneration to use client-specific memory for consistency'
)

with open('index.html', 'w') as f:
    f.write(html_content)

print("Updated version to v1.3.2")
