# Exercise 5: Starting Your Git Project and Linking it to GitHub

This exercise will guide you through the process of creating a new Git project, initializing a Git repository, and linking it to a new GitHub repository.

## Objectives

- Create a new repository on GitHub.
- Initialize a local Git repository.
- Link your local repository to GitHub.
- Push your initial commit to GitHub.

## Instructions

### 1. Create a New Repository on GitHub

1. **Go to GitHub**: Open your web browser and navigate to [GitHub](https://github.com).
2. **New Repository**: Click on the "+" icon in the top-right corner and select "New repository".
3. **Repository Details**: Enter your repository name as `username/demo`. Replace `username` with your actual GitHub username. Leave other settings as default or adjust according to your preference. Click "Create repository".

### 2. Initialize Your Local Git Repository

Open your terminal or command prompt and execute the following commands:

```bash
echo "# demo" >> README.md
git init
git add README.md
git commit -m "first commit"
```

This sequence creates a new file README.md, initializes a Git repository, stages the README.md file, and commits it with a message "first commit".

### 3. Link Your Local Repository to GitHub

Replace username with your actual GitHub username in the URL:
```bash
git remote add origin https://github.com/username/demo.git
git branch -M main
git push -u origin main
```
These commands add a remote named origin pointing to your GitHub repository, rename the current branch to main, and push your commits to GitHub.

### 4. Verify Your Repository on GitHub

1. Navigate to Your Repository: Go to `https://github.com/username/demo` in your web browser. Replace username with your GitHub username.
2. Check Your Files: You should see the README.md file and your commit message.

## If You Already Have a Full Repository

If your repository is already initialized and you're looking to link and push it to GitHub, use the following commands after creating your GitHub repository:
```bash
cd myworkingdir
git init
git remote add origin https://github.com/username/demo.git
git branch -M main
git push -u origin main
```

## Conclusion

Congratulations! You have successfully created a new Git project, initialized a Git repository, linked it to GitHub, and pushed your initial commit. From here on you can just push any updates with
```bash
git push
```
making sure you have stages any changes and committed them first!
