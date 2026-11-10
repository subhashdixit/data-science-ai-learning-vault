# 📦 Push to GitHub

## Step 1: Create GitHub Repository

1. Go to: https://github.com/new
2. **Repository name:** `learning-notes`
3. **Description:** "My complete learning journey - Data Science, ML, AI & Interview Prep with color-coded notes"
4. **Visibility:** ⚠️ **PRIVATE** (your personal notes!)
5. ❌ **DO NOT** initialize with README (you already have one!)
6. Click **"Create repository"**

---

## Step 2: Connect Local Repo to GitHub

Copy your GitHub repo URL and run:

```bash
cd /Users/subhash_dixit/Documents/codex/connected-ai-learning/learning-notes

# Add remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/learning-notes.git

# Push to GitHub
git branch -M main
git push -u origin main
```

---

## Step 3: Daily Updates

Every evening, push your notes:

```bash
cd /Users/subhash_dixit/Documents/codex/connected-ai-learning/learning-notes
git add .
git commit -m "Daily update - $(date +%Y-%m-%d)"
git push
```

---

## Step 4: Auto-Sync with Obsidian Plugin (Optional)

1. In Obsidian: **Settings** → **Community plugins** → **Turn off Restricted Mode**
2. Click **Browse** → Search **"Obsidian Git"**
3. Install and Enable
4. Settings → Obsidian Git → Configure:
   - **Auto backup interval:** 10 minutes
   - **Auto pull interval:** 5 minutes
   - **Commit message:** `vault backup: {{date}}`

Now your notes sync automatically to GitHub every 10 minutes! 🚀

---

## What Gets Synced?

✅ All markdown notes  
✅ Folder structure  
✅ Templates  
✅ CSS snippets  
✅ Daily notes  

❌ Obsidian workspace files (gitignored)  
❌ Cache files  
❌ Temporary files  

---

## Why Keep It Private?

Your notes contain:
- Personal learning progress
- Interview prep strategies
- Project ideas
- Daily reflections

**Keep it private** until you want to share specific parts publicly!

---

## Viewing on GitHub

GitHub renders markdown beautifully! Your colorful callouts will show as:

```markdown
> [!blue] Concept
> Definition here
```

Renders as a blue callout box on GitHub too! 🎨
