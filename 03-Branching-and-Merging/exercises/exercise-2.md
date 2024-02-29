# Exercise 2: Branching and Merging Basics

In this exercise, you'll practice creating branches, making changes in those branches, and merging those changes back into the main branch. You'll also simulate a merge conflict and resolve it.

## Objectives

- Create and switch between branches in a Git repository.
- Merge changes from one branch to another.
- Resolve a simple merge conflict.

## Instructions

### Part 1: Branching and Merging

1. **Create a Feature Branch**: From your repository, create a new branch named `feature-x`:

    ```bash
    git checkout -b feature-x
    ```

2. **Add a Feature**: Make changes to your project in this branch. For example, add a new file named `feature-x.txt` or modify an existing file. Then, stage and commit your changes.

    ```bash
    echo "This is a new feature" > feature-x.txt
    git add feature-x.txt
    git commit -m "Add feature-x"
    ```

3. **Switch Back to Main Branch**: Switch back to your main branch (it might be called `main` or `master`).

    ```bash
    git checkout main
    ```

4. **Merge Feature Branch**: Merge the `feature-x` branch into the main branch.

    ```bash
    git merge feature-x
    ```

5. **Delete the branch**: If you're finished with this branch, you can now safely delete it with

    ```bash
    git branch -d feature-x
    ```

# Note
You can delete branches on remote repositories using 
```bash
git push origin --delete branch-name
```

# Summary
You have successfully created a branch, made some changes, merged these into the main branch and then deleted the feuature branch, nice work! 
