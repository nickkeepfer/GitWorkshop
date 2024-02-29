# Exercise 3: Understanding Git Stash

In this exercise, you'll learn how to use `git stash` to save changes temporarily without committing them. This is particularly useful when you need to switch contexts quickly, such as addressing a bug on a different branch without losing your current work.

## Objectives

- Learn to use `git stash` to save changes temporarily.
- Practice applying stashed changes back to your working directory.
- Understand how to list and manage multiple stashes.

## Instructions

### Part 1: Stashing Changes

1. **Make a new feature-y branch** Create a new branch to work on `feature-y` using:

    ```bash
    git checkout -b feature-y
    ```

1. **Make Temporary Changes**: In your current branch, make some changes to your project. Do not stage these changes. For instance, modify an existing file or create a new file:

    ```bash
    echo "Temporary changes" > temp.txt
    ```

2. **Stash Your Changes**: Save your changes temporarily using `git stash`:

    ```bash
    git stash
    ```

3. **Verify Clean Working Directory**: Use `git status` to ensure your working directory is clean. The changes you just made should no longer be visible.

### Part 2: Applying Stashed Changes

1. **Create a New Branch for Bug Fix**: Suppose you need to address a bug on a different branch. First, create and switch to a new branch:

    ```bash
    git checkout -b bug-fix
    ```

2. **Apply Stashed Changes**: Once you've squashed the bug and are ready to resume work on your previous task, switch back to your original branch and apply the stashed changes:

    ```bash
    git checkout feature-y
    git stash pop
    ```

3. **List Stashes**: If you have multiple stashes, you can list them to see all your stashed changes:

    ```bash
    git stash list
    ```

4. **Apply a Specific Stash**: If needed, apply a specific stash by using its identifier from the stash list:

    ```bash
    git stash apply stash@{0}
    ```

## Conclusion

`git stash` is a powerful tool for managing your work in progress, allowing you to switch tasks without committing half-done work. This exercise has shown you how to stash changes, apply them, and manage multiple stashes. Understanding how to use `git stash` effectively can greatly enhance your workflow in multi-tasking environments.

