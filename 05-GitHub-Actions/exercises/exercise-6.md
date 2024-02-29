# Exercise 6: Create a Simple CI Workflow with Hello World

In this exercise, you'll create a very simple GitHub Actions workflow. This workflow will print "Hello World" to the console whenever code is pushed to your repository. This is a foundational step to understand how GitHub Actions workflows are structured and triggered.

## Objective

- Create a GitHub Actions workflow that prints "Hello World" upon any code push to the repository.

## Instructions

1. **Prepare Your Repository**: If you haven't done so already, create a new GitHub repository or choose an existing one where you have administrative access.

2. **Create the Workflow File**: Inside your repository, navigate to the `.github/workflows` directory. If it doesn't exist, create it. Then, create a new file named `hello-world.yml`. Note that this is **NOT** your `.git` directory. 

3. **Define the Workflow**:

    Below is some content for your `hello-world.yml` file. This workflow is triggered by any `push` event to the repository and simply executes a script to print "Hello World" running on a cloud PC with the latest Linux Ubuntu OS:

    ```yaml
    name: Hello World CI

    on: [push]

    jobs:
      greet:
        runs-on: ubuntu-latest

        steps:
        - name: Print Hello World
          run: echo "Hello World!"
    ```

4. **Commit and Push Your Workflow**: After creating the `hello-world.yml` file, commit it to your repository and push the changes to GitHub.

5. **Check the Execution**: Navigate to the "Actions" tab of your GitHub repository to view the execution of your workflow. You should see a completed job that prints "Hello World" in the console output.

## Conclusion
Congratulations, now you understand how Github actions work you can integrate CI/CD into your projects. It is reccomended you create lots of unit testing scripts that are run via CI, that way you can see when any change you make to your codebase breaks something unexpected elsewhere.
