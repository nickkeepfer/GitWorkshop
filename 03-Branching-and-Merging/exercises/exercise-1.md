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

### Part 2: Handling a Merge Conflict

In real-world development scenarios, you'll often encounter merge conflicts. These occur when Git cannot automatically reconcile differences in code between two commits. Your task is to resolve these conflicts manually.

1. **Create a New Branch for a New Feature**: From your main branch, create another branch named `feature-y`:

    ```bash
    git checkout -b feature-y
    ```

2. **Make Changes in the New Feature Branch**: In this branch, let's modify an existing file. For example, if you have a file named `feature-x.txt`, open it and add the following line:

    ```bash
    echo "Feature Y improvement" >> feature-x.txt
    git add feature-x.txt
    git commit -m "Improve feature-x with feature-y"
    ```

3. **Create a Conflicting Change in the Main Branch**: Switch back to your main branch and make a conflicting change to the same line in the same file.

    ```bash
    git checkout main
    echo "Main branch's improvement" >> feature-x.txt
    git add feature-x.txt
    git commit -m "Modify feature-x in main branch"
    ```

4. **Attempt to Merge the `feature-y` Branch**: Now, try to merge `feature-y` into the main branch. Git will detect a conflict because the same parts of the file have been modified differently in each branch.

    ```bash
    git merge feature-y
    ```

    Git will output a message indicating that there is a merge conflict.

5. **Resolve the Conflict**: Open `feature-x.txt` in your text editor. You'll see the conflict markers indicating the conflicting changes. It will look something like this:

    ```plaintext
    <<<<<<< HEAD
    Main branch's improvement
    =======
    Feature Y improvement
    >>>>>>> feature-y
    ```

    Decide which change to keep (or combine them in a way that makes sense for your project), and edit the file to resolve the conflict. For example, you might decide to keep both changes:

    ```plaintext
    Main branch's improvement
    Feature Y improvement
    ```

    Save your changes and close the editor.

6. **Finalize the Merge**: After resolving the conflict in the file, stage the file and commit the merge:

    ```bash
    git add feature-x.txt
    git commit -m "Resolved merge conflict between main and feature-y"
    ```

    This commit will complete the merge process, incorporating the changes from `feature-y` into the main branch while resolving the conflict.

## Deliverable

Prepare a `merge-exercise-summary.txt` documenting:
- The specific commands you used for creating branches, making changes, merging, and handling the conflict.
- A brief explanation of how you decided to resolve the conflict, including the final state of `feature-x.txt`.

## Conclusion

Congratulations on successfully completing the exercise on branching and merging with Git! Through this hands-on practice, you've not only learned how to effectively manage multiple lines of development but also how to navigate the challenges of merging these changes back into a main line of development.

