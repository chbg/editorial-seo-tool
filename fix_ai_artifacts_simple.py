#!/usr/bin/env python3

# Read the file
with open('index.html', 'r') as f:
    lines = f.readlines()

# Find the line with the prompt and add client logic before it
for i, line in enumerate(lines):
    if 'const prompt = `Fix AI-generated patterns in this section by replacing artificial phrases with natural, human-like alternatives.' in line:
        # Insert the client logic before this line
        client_logic = [
            '                // Get client\'s AI artifacts or use default\n',
            '                const clientAIArtifacts = workflowConfig.clientId && CLIENT_DATA[workflowConfig.clientId]?.aiArtifacts \n',
            '                    ? CLIENT_DATA[workflowConfig.clientId].aiArtifacts \n',
            '                    : CODIFIED_AI_ARTIFACTS;\n',
            '\n'
        ]
        lines[i:i] = client_logic
        break

# Find and replace the hardcoded list with client reference
for i, line in enumerate(lines):
    if '# AI Artifacts to Avoid' in line and 'Client-Specific' not in line:
        # Replace the hardcoded list with client reference
        lines[i] = '# AI Artifacts to Avoid (Client-Specific)\n\n${clientAIArtifacts}\n\n'
        # Remove all the hardcoded list lines until we hit the "Make the content" line
        j = i + 1
        while j < len(lines) and 'Make the content sound natural and human-written' not in lines[j]:
            if lines[j].strip().startswith('##') or lines[j].strip().startswith('-') or lines[j].strip().startswith('---') or lines[j].strip() == '':
                lines[j] = ''
            j += 1
        break

# Write the file back
with open('index.html', 'w') as f:
    f.writelines(lines)

print("Fixed fixAIArtifactsInSection function to use client-specific AI artifacts")
