# Exercise 2 - Handling a Merge Conflict

In real-world development scenarios, you'll often encounter merge conflicts. These occur when Git cannot automatically reconcile differences in code between two commits. Your task is to resolve these conflicts manually. Lets consider an example using Python where we want to introduce some functions that square and cube numbers.


1. **Create a New Branch for a New Feature**: From your main branch, create another branch named `square-feature`:

	```bash
	git checkout -b square-feature
	```

2. **Make Changes in the New Feature Branch**: In this branch, lets create a Python script named `math_operations.py`. Add the following function to calculate the square of a number:

	```python
	def calculate(number):
	    return number ** 2
	```

	Save your changes, and then stage and commit the file with a suitable commit message:

	```bash
	git add math_operations.py
	git commit -m "Add square function"
	```

3. **Create a Conflicting Change in the Main Branch**: Switch back to your main branch to implement a cube function, which will conflict with the square function.

	```bash
	git checkout main
	```

	Now, modify the `math_operations.py` file to include the cube function, using the same function name:

	```python
	def calculate(number):
	    return number ** 3
	```

	Save the file, then stage and commit your changes:
	```
	bash
	git add math_operations.py
	git commit -m "Add cube function"
	```

4. **Attempt to Merge the `square-feature` Branch**: Now, merge square-feature into the main branch. This will result in a merge conflict due to the changes made to the same lines in `math_operations.py`.

```bash
git merge square-feature
```
Git will notify you of a conflict in `math_operations.py`.

5. **Resolve the Conflict**: Open `math_operations.py` in your text editor. You'll see the conflict markers showing the conflicting changes:

	```plaintext
	<<<<<<< HEAD
	def calculate(number):
	    return number ** 3
	=======
	def calculate(number):
	    return number ** 2
	>>>>>>> square-feature
	```

	Decide how to resolve this conflict. For instance, you might choose to keep both functions but rename them:

	```python
	def calculate_square(number):
	    return number ** 2

	def calculate_cube(number):
	    return number ** 3
	```
	All thats left to do is save your changes and close the editor.

6. **Finalize the Merge**: After resolving the conflict in the file, stage the file and commit the merge:

    ```bash
    git add math_operations.py
    git commit -m "Resolve merge conflict by including both square and cube functions"
    ```

    This commit will complete the merge process, incorporating the changes into the main branch while resolving the conflict.

