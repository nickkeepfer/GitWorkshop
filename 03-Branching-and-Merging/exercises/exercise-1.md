# Exercise 1: Branching and Merging Basics

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

## Conclusion

Congratulations on successfully completing the exercise on branching and merging with Git! Through this hands-on practice, you've not only learned how to effectively manage multiple lines of development but also how to navigate the challenges of merging these changes back into a main line of development. Now proceed to exercise-2 to see what to do when a conflict arises.
