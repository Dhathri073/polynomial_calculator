# 📤 GitHub Deployment Guide

## Overview
This guide walks you through pushing the **Polynomial Calculator** project to GitHub and optionally enabling GitHub Pages or Docker deployment.

---

## 🚀 Step 1: Initialize Git & Create GitHub Repository

### 1.1 Initialize Git locally
```bash
cd "c:\Users\Dhathri M\OneDrive\Desktop\DS miniproject D\polynomial-calculator"
git init
git add .
git commit -m "Initial commit: Polynomial Calculator with Linked List implementation"
```

### 1.2 Create repository on GitHub
1. Go to [GitHub](https://github.com/new)
2. Create a new repository named: `polynomial-calculator`
3. **Do NOT** initialize with README, .gitignore, or license (we already have them)
4. Click **Create repository**
5. Copy the HTTPS or SSH URL

### 1.3 Add remote and push
Replace `<USERNAME>` with your GitHub username:

```bash
git remote add origin https://github.com/<USERNAME>/polynomial-calculator.git
git branch -M main
git push -u origin main
```

---

## ✅ Verification
After pushing, verify on GitHub:
- Go to: `https://github.com/<USERNAME>/polynomial-calculator`
- You should see all files and folders in the repo

---

## 📚 Optional: Enable GitHub Pages (for documentation)

GitHub Pages can host your README and documentation as a website.

### Steps:
1. Go to your repository on GitHub
2. Click **Settings** → **Pages** (in left sidebar)
3. Under "Build and deployment":
   - **Source**: Select "Deploy from a branch"
   - **Branch**: Select `main`
   - **Folder**: Select `/ (root)`
4. Click **Save**
5. Wait ~1 minute for the build to complete
6. Your site will be live at: `https://<USERNAME>.github.io/polynomial-calculator/`

### What will be hosted:
- README.md (rendered as HTML)
- All markdown documentation files
- Static assets (if configured properly)

**Note:** The app itself (Flask backend) cannot run on GitHub Pages; only static files. For a live app, use Docker Hub or a cloud platform like Heroku, AWS, or DigitalOcean.

---

## 🐳 Optional: Push Docker Image to Docker Hub

If you want to share your Docker image so others can pull and run it:

### Prerequisites:
- Docker Hub account: https://hub.docker.com (free)
- Docker Desktop running locally

### Steps:

1. **Login to Docker Hub**
   ```bash
   docker login
   # Enter your Docker Hub username and password
   ```

2. **Tag your image**
   ```bash
   docker tag polynomial-calculator:latest <USERNAME>/polynomial-calculator:latest
   docker tag polynomial-calculator:latest <USERNAME>/polynomial-calculator:1.0.0
   ```

3. **Push to Docker Hub**
   ```bash
   docker push <USERNAME>/polynomial-calculator:latest
   docker push <USERNAME>/polynomial-calculator:1.0.0
   ```

4. **Verify on Docker Hub**
   - Go to: https://hub.docker.com/repositories
   - You should see `<USERNAME>/polynomial-calculator`

### Others can now run your image:
```bash
docker run -d -p 5000:5000 <USERNAME>/polynomial-calculator:latest
```

---

## 🔄 GitHub Actions (CI/CD)

The repository includes automated workflows (`.github/workflows/`) that:

### `tests.yml`
- Runs on every push and pull request
- Tests code on Python 3.9, 3.10, 3.11
- Executes `test_polynomial.py`
- Optional linting with flake8

### `docker.yml`
- Builds Docker image on push to `main`
- Validates Dockerfile syntax
- (Can be extended to push to Docker Hub)

**View results:**
- Go to your repository → **Actions** tab
- Click any workflow run to see details

---

## 📋 Project Structure for GitHub

Your repository will have:
```
polynomial-calculator/
├── .github/
│   └── workflows/
│       ├── tests.yml
│       └── docker.yml
├── .gitignore
├── app.py
├── requirements.txt
├── test_polynomial.py
├── Dockerfile
├── docker-compose.yml
├── README.md
├── QUICKSTART.md
├── PROJECT_SUMMARY.md
├── VISUAL_GUIDE.md
├── FEATURES.md
├── TESTING_SUMMARY.md
├── TEST_REPORT.md
├── GETTING_STARTED.txt
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── script.js
```

---

## 🎯 Quick Reference Commands

### Clone the repo (for others or on another machine)
```bash
git clone https://github.com/<USERNAME>/polynomial-calculator.git
cd polynomial-calculator
```

### Make changes and push
```bash
git add .
git commit -m "Your message here"
git push origin main
```

### Create a release (tag)
```bash
git tag v1.0.0
git push origin v1.0.0
```

### View remote status
```bash
git remote -v
git status
```

---

## 🔗 Links After Deployment

- **Repository:** `https://github.com/<USERNAME>/polynomial-calculator`
- **GitHub Pages (docs):** `https://<USERNAME>.github.io/polynomial-calculator/`
- **Docker Hub:** `https://hub.docker.com/r/<USERNAME>/polynomial-calculator`

---

## 📝 Additional Notes

### Private vs Public Repository
- **Public** (current setup): Anyone can see and clone
- **Private**: Only you and collaborators can access

To make it private after creation, go to **Settings** → **General** → **Change repository visibility**

### Collaborators
To add collaborators:
1. Go to **Settings** → **Collaborators**
2. Click **Add people**
3. Search for GitHub username and grant access

### Protecting Main Branch
To prevent accidental pushes to main:
1. Go to **Settings** → **Branches**
2. Add branch protection rule for `main`
3. Require pull requests before merging

---

## 🆘 Troubleshooting

### "fatal: remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/<USERNAME>/polynomial-calculator.git
```

### "Permission denied (publickey)"
Ensure you've set up SSH keys:
```bash
ssh -T git@github.com
```
If it fails, use HTTPS instead of SSH:
```bash
git remote set-url origin https://github.com/<USERNAME>/polynomial-calculator.git
```

### GitHub Pages not appearing
- Check **Settings** → **Pages**
- Ensure branch is `main` and folder is `/ (root)`
- Wait 1-2 minutes for the build
- Check the **Actions** tab for build logs

---

## 🎉 You're All Set!

Your Polynomial Calculator is now on GitHub with:
- ✅ Version control
- ✅ Automated tests (GitHub Actions)
- ✅ Docker support
- ✅ Documentation
- ✅ Ready to share with others

Share your repo link and others can:
- View the code
- Clone and run locally
- Pull the Docker image
- Read the documentation

---

**Happy coding! 🚀**
