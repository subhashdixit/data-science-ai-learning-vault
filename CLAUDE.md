# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a **personal learning vault** for Data Science and AI topics, managed as an Obsidian-based knowledge base. The repository contains structured learning notes with a color-coded system designed to mimic handwritten notes with highlighters.

**Key characteristics:**
- **Not a code project** - This is a documentation/notes repository with markdown files
- **Obsidian vault** - Uses Obsidian markdown extensions (callouts, wiki-links)
- **Color-coded learning system** - 5-color system (blue/green/red/yellow/purple) for different content types
- **Structured learning paths** - From foundations (Python, Math) through ML/DL to AI systems and interview prep

## Repository Structure

The vault is organized into numbered topic folders representing a learning journey:

- **01-Foundations/** - Programming (Python, NumPy, Pandas, SQL) and Math (Linear Algebra, Calculus, Probability)
- **02-Statistics-and-Data/** - Statistics, EDA, Data Visualization, Time Series
- **03-Machine-Learning/** - Supervised/Unsupervised Learning, Model Evaluation, Feature Engineering
- **04-Deep-Learning/** - Neural Networks, CNNs, RNNs/LSTMs, Transformers, LLMs
- **05-NLP/** - Basics (tokenization, embeddings), Advanced techniques, Applications
- **06-AI-Systems/** - RAG, AI Agents, Prompt Engineering
- **07-MLOps-Deployment/** - MLOps, LLMOps, Data Engineering
- **08-Projects/** - Practical learning projects
- **09-Interview-Prep/** - Coding practice, ML Theory, System Design, Behavioral questions
- **10-Daily-Notes/** - Daily learning journal (YYYY-MM-DD.md format)
- **11-Resources/** - External resources, books, courses

## Color-Coding System

All notes follow a strict 5-color callout system (see `COLOR-CODING-GUIDE.md`):

| Color | Purpose | Callout Syntax |
|-------|---------|----------------|
| 💙 Blue | Concepts & Definitions | `> [!blue] 💙 **Title**` |
| 💚 Green | Examples & Working Code | `> [!green] ✅ **Title**` |
| ❤️ Red | Warnings & Common Mistakes | `> [!red] ⚠️ **Title**` |
| 💛 Yellow | Important Tips & Best Practices | `> [!yellow] 💡 **Title**` |
| 💜 Purple | Advanced & Deep Dives | `> [!purple] 🔮 **Title**` |

**When creating or editing notes:**
- Use color callouts strategically (don't overuse)
- Each note should follow the template in `00-TEMPLATE.md`
- Include section structure: What is it? → Examples → Pitfalls → Best Practices → Advanced
- Add wiki-links to related topics: `[[topic-name]]`
- End with tags, difficulty level, and date metadata

## Note Templates

**Standard note structure** (from `00-TEMPLATE.md`):
1. Title with emoji
2. Quick definition in blue callout
3. Main concept explanation (blue)
4. Examples section (green callouts with code)
5. Common pitfalls (red callouts)
6. Best practices (yellow callouts)
7. Advanced concepts (purple callouts)
8. Related topics (wiki-links)
9. Resources (external links)
10. Metadata footer (tags, date, difficulty)

**Daily note structure** (in `10-Daily-Notes/`):
- YYYY-MM-DD.md filename format
- Today's focus/goals
- What I learned (with color-coded highlights)
- Mistakes made and lessons
- Tomorrow's plan

## Obsidian-Specific Features

This vault uses Obsidian markdown extensions:

**Callouts:** `> [!type] Title` where type = blue/green/red/yellow/purple
**Wiki-links:** `[[note-name]]` or `[[folder/note-name|Display Text]]`
**Inline highlights:** `==highlighted text==<!--color-->` (requires CSS snippet)
**CSS snippets:** `.obsidian/snippets/handwritten-colors.css` defines color styles

## Git Workflow

The user maintains this vault with regular commits:

```bash
git add .
git commit -m "Daily update - YYYY-MM-DD"
git push
```

**When helping with commits:**
- Default commit messages should be descriptive: "Add [topic] notes" or "Update [topic] with [detail]"
- For daily updates: "Daily update - [date]: [what was learned]"
- Group related changes logically

## Working with Notes

**When creating new notes:**
1. Check if a template structure applies (`00-TEMPLATE.md`)
2. Use appropriate color callouts for content type
3. Include code examples in green callouts with triple backticks
4. Add warnings/gotchas in red callouts
5. Link related concepts with `[[wiki-links]]`
6. Add metadata footer (tags, date, difficulty)

**When editing existing notes:**
- Preserve the color-coding system
- Maintain consistent emoji usage (💙💚❤️💛💜)
- Keep the structure: concept → example → pitfall → best practice → advanced
- Update the "Last Updated" date in metadata

**When searching for notes:**
- Each subfolder has a README.md that describes its contents
- Use wiki-link format when referencing: `[[folder/note-name]]`
- Interview prep content is in `09-Interview-Prep/`

## Common Operations

**Create a new learning note:**
```bash
# Use the template as base
cp 00-TEMPLATE.md "path/to/new-topic.md"
# Then edit with appropriate content
```

**Create a daily note:**
```bash
# Use ISO date format
echo "# 📅 $(date +%Y-%m-%d) - Learning Log" > "10-Daily-Notes/$(date +%Y-%m-%d).md"
```

**Find notes by topic:**
```bash
# Search across all markdown files
grep -r "topic-name" --include="*.md"
```

**List all notes in a category:**
```bash
find 01-Foundations -name "*.md" -type f
```

## Important Files

- **README.md** - Main overview, learning paths, progress tracker
- **COLOR-CODING-GUIDE.md** - Complete color system documentation with examples
- **00-TEMPLATE.md** - Template for new notes (copy this for new topics)
- **QUICK-START.md** - Obsidian setup instructions
- **GITHUB-SETUP.md** - Git workflow documentation
- **.obsidian/snippets/handwritten-colors.css** - CSS for color rendering in Obsidian

## Goals and Context

This vault tracks the user's learning journey from foundations through advanced AI topics with a focus on:
- Building strong fundamentals (Python, Math, Statistics)
- Progressing through ML → DL → LLMs → AI Systems
- Interview preparation for Data Science/ML roles
- Daily learning habits and progress tracking

The user prefers:
- Visual, color-coded notes (like handwritten study notes)
- Structured learning paths with clear progression
- Practical examples with working code
- Interview-focused content with common gotchas
- Daily journaling of learning progress
