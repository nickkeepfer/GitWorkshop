# Exercise 1: Submitting Your First Pull Request

This exercise guides you through the process of submitting a pull request (PR) to the [GitWorkshop repository](https://github.com/nickkeepfer/GitWorkshop). You'll submit the `git_history.txt` file you created in a previous exercise, contributing to an actual project on GitHub.

## Objectives

- Fork the GitWorkshop repository.
- Clone your fork to your local machine.
- Add your `git_history.txt` file to a new branch in your fork.
- Push the branch to your fork on GitHub.
- Submit a pull request to the original GitWorkshop repository.

## Instructions

### 1. Fork the Repository

Navigate to the [GitWorkshop repository](https://github.com/nickkeepfer/GitWorkshop) on GitHub. Click the "Fork" button in the top-right corner of the page to create a copy of the repository in your GitHub account.

### 2. Clone Your Fork

Clone the forked repository to your local machine. Replace `YOUR-USERNAME` with your actual GitHub username:

```bash
git clone https://github.com/YOUR-USERNAME/GitWorkshop.git
cd GitWorkshop
```

### 3. Create a New Branch

Create a new branch in your local repository for your contribution. This helps keep your changes organized and separate from the main project:

```bash
git checkout -b add-git-history-YOUR-USERNAME
```

### 4. Add Your git_history.txt File

Copy your `git_history.txt` file into the *root* of your local GitWorkshop repository. Then, add and commit this file to your branch:

```bash
git add git_history.txt
git commit -m "Add git history for YOUR-USERNAME"
```

### 5. Push Your Changes

Push your branch and the changes to your fork on GitHub:

```bash
git push origin add-git-history-YOUR-USERNAME
```

### 6. Submit a Pull Request

1. **Navigate to Your Fork**: Go to `https://github.com/YOUR-USERNAME/GitWorkshop`.

2. **Start the Pull Request**:
    - Click on "Pull requests" > "New pull request".
    - Ensure the base repository is set to `nickkeepfer/GitWorkshop` and the head repository to your fork.

3. **Select Your Branch**:
    - Base branch: `main`.
    - Compare branch: `add-git-history-YOUR-USERNAME`.

4. **Create Your Pull Request**:
    - Click "Create pull request".
    - Title: `Adding git history for [Your Username]`.
    - Description: Provide a brief summary of your changes and any notes on your submission.

5. **Finalize**:
    - Review your pull request and then click "Create pull request" to submit.


## Conclusion

Submitting a pull request is a fundamental aspect of collaborating on GitHub. Through this exercise, you've taken an important step in your journey as a developer, contributing to a project and practicing essential Git and GitHub workflows. This experience will serve you well in future projects, open-source contributions, and collaborative development efforts.
