#!/usr/bin/env python3

# Read the file
with open('index.html', 'r') as f:
    content = f.read()

# Find the fixAIArtifactsInSection function and replace it completely
old_function = '''async function fixAIArtifactsInSection(sectionTitle, sectionContent) {
            try {
                const prompt = `Fix AI-generated patterns in this section by replacing artificial phrases with natural, human-like alternatives.

SECTION: ${sectionTitle}
CONTENT: ${sectionContent}

# AI Artifacts to Avoid

## 1. Generic opening phrases
Avoid formulaic intros that signal templated content:
- "In this digital age"
- "In today's world"
- "It's worth noting"
- "At its core"
- "In the realm of"
- "In the landscape of"
- "Ever wondered…?"
- "Let's delve into…"

## 2. Overly formal transitions
Replace stiff connectors with natural flow:
- "Furthermore"
- "Moreover"
- "Additionally"
- "In conclusion"
- "To summarize"
- "It should be noted"

## 3. Redundant phrases
Cut padding phrases that add no real meaning:
- "It's important to note that"
- "It's worth mentioning"
- "It's crucial to understand"
- "It's essential to recognize"
- "Knowledge is power"

## 4. Generic conclusions
Avoid vague, non-specific endings:
- "The future looks bright"
- "Only time will tell"
- "The possibilities are endless"
- "The sky's the limit"
- "Unlock your potential"

## 5. Overly enthusiastic or cliché language
Be confident but not breathless:
- "amazing"
- "incredible"
- "revolutionary"
- "game-changing"
- "groundbreaking"
- "microscopic superheroes"
- "robust warriors"
- "efficiency unleashed"

## 6. AI-typical sentence patterns
- **Repetitive structures:** Sentences of similar length and rhythm back-to-back.  
- **Predictable transitions:** "On the other hand," "In a nutshell," "Remember…" used formulaically.  
- **Overly comprehensive sweeps:** Covering every possible angle in a neat outline (definition → ranges → lifestyle tips → product shopping) without leaving gaps or distinct POV.  
- **Echoing common phrases:** "Architect of your health," "unlock potential," "master your health" repeated across sections.  
- **Lack of voice drift:** Entire piece maintains the same polished cadence; no variation in tone, sentence fragments, or more human-like asides.  
- **Overloaded adjectives:** Stacking descriptors ("intriguing," "pivotal," "comprehensive," "vital") in one section.  
- **Labored clarity:** Explaining obvious concepts in multiple ways (e.g., "lymphocytes fight infections" repeated 3–4 times).  

---

## 7. How to Humanize Content
- **Vary rhythm:** Mix short punchy sentences with longer ones. Use fragments when natural.  
- **Inject idiosyncrasy:** Add metaphors or real-world analogies that reflect Function's POV (e.g., "Think of lymphocytes as bouncers at a crowded concert").  
- **Leave edges:** Don't over-polish; allow space for nuance, uncertainty, or perspective.  
- **Avoid wellness clichés:** Replace "wellness journey" with "100 healthy years" or "whole-body view."  
- **Be concise:** Cut inspirational fluff. Say it directly.  

Make the content sound natural and human-written while preserving the original meaning and information.'''

new_function = '''async function fixAIArtifactsInSection(sectionTitle, sectionContent) {
            try {
                // Get client's AI artifacts or use default
                const clientAIArtifacts = workflowConfig.clientId && CLIENT_DATA[workflowConfig.clientId]?.aiArtifacts 
                    ? CLIENT_DATA[workflowConfig.clientId].aiArtifacts 
                    : CODIFIED_AI_ARTIFACTS;

                const prompt = `Fix AI-generated patterns in this section by replacing artificial phrases with natural, human-like alternatives.

SECTION: ${sectionTitle}
CONTENT: ${sectionContent}

# AI Artifacts to Avoid (Client-Specific)

${clientAIArtifacts}

Make the content sound natural and human-written while preserving the original meaning and information.'''

# Replace the function
content = content.replace(old_function, new_function)

# Write the file back
with open('index.html', 'w') as f:
    f.write(content)

print("Fixed fixAIArtifactsInSection function to use client-specific AI artifacts")
