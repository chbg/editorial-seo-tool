#!/usr/bin/env python3

import re

# Read the file
with open('index.html', 'r') as f:
    content = f.read()

# Find the fixAIArtifactsInSection function and replace the hardcoded list
pattern = r'(async function fixAIArtifactsInSection\(sectionTitle, sectionContent\) \{\s+try \{\s+const prompt = `Fix AI-generated patterns in this section by replacing artificial phrases with natural, human-like alternatives\.\n\nSECTION: \$\{sectionTitle\}\nCONTENT: \$\{sectionContent\}\n\n# AI Artifacts to Avoid\n\n)(.*?)(Make the content sound natural and human-written while preserving the original meaning and information\.)'

replacement = r'''\1# AI Artifacts to Avoid (Client-Specific)

${clientAIArtifacts}

\3'''

# First, add the client logic before the prompt
content = re.sub(
    r'(async function fixAIArtifactsInSection\(sectionTitle, sectionContent\) \{\s+try \{\s+)(const prompt = )',
    r'''\1// Get client's AI artifacts or use default
                const clientAIArtifacts = workflowConfig.clientId && CLIENT_DATA[workflowConfig.clientId]?.aiArtifacts 
                    ? CLIENT_DATA[workflowConfig.clientId].aiArtifacts 
                    : CODIFIED_AI_ARTIFACTS;

                \2''',
    content
)

# Then replace the hardcoded list
content = re.sub(pattern, replacement, content, flags=re.DOTALL)

# Write the file back
with open('index.html', 'w') as f:
    f.write(content)

print("Fixed fixAIArtifactsInSection function to use client-specific AI artifacts")
