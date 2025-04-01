# Ruff Action

This GitHub Action automatically lints and formats Python code using **Ruff** whenever changes are pushed to the `main` branch. It ensures consistent code style and catches potential errors early.

## Features
- Automatically runs **Ruff** for linting and formatting.
- Executes only when code is pushed to the `main` branch.
- Provides immediate feedback on linting errors and formatting issues.
- Helps maintain a clean and standardized codebase.

## Prerequisites
Ensure you have the following setup before using this action:
- A GitHub repository with Python code.
- A `pyproject.toml` file if you want to configure **Ruff** settings.

## Configuration
### Customizing Ruff Rules
You can customize Ruff settings by creating a `pyproject.toml` file in your repository root:

```toml
[tool.ruff]
line-length = 88  # Set max line length
select = ["E", "F", "I"]  # Choose specific linting rules
```

Refer to the [Ruff documentation](https://beta.ruff.rs/docs/) for more configuration options.

## Troubleshooting
- Ensure the `ruff` package is installed correctly.
- Check if the GitHub token has necessary permissions to push commits.
- Modify `python-version` if your project requires a specific version.

## License
This project is licensed under the MIT License.

---

This GitHub Action helps maintain high code quality and keeps Python code well-formatted without manual intervention!

