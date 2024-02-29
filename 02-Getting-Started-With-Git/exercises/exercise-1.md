# Exercise 1: Your First Git Commands

In this exercise, you'll put into practice the basic Git commands to create a repository, track changes, and make your first commit.

## Objectives

- Initialise a new Git repository.
- Understand the workflow of making changes, staging them, and committing.

## Instructions

1. **Create a New Repository**: If you haven't already, create a new directory called `my-first-repo`, navigate into it, and initialise a Git repository.

    ```bash
    mkdir my-first-repo
    cd my-first-repo
    git init
    ```

2. **Create a File**: Inside `my-first-repo`, create a new file called `README.md`. Add a brief description of your repository, for example
	```bash
	echo "I love Git" > README.md
	```

3. **Check Status**: Use the `git status` command to see the status of your changes. You should see Git telling you that the README.md file is not currently staged for commit, let's fix that. 

4. **Stage Your Changes**: Add your `README.md` to the staging area using `git add README.md`. This informs Git to track this file and that it should be added in the next commit. You could have also used `git add .` which will add all changed filed into the staging area.

5. **Commit Your Changes**: Commit your changes with a helpful message using `git commit -m "My very descriptive initial commit message"`. From here onwards, I **STRONGLY** recommend using descripive and intelligent commit messages as they will be invaluable if you ever need to look back through your commits.

6. **Review Your History**: Use the `git log` command to view your commit history.

## Mission Complete
You have successfully pushed your first commit. Understanding these basic Git operations is the first step towards effective version control and collaboration. Show Me, Gary or Tom your git log to verify everything went smoothly or call us over if something looks wrong. 

