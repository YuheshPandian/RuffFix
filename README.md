# RuffFix - A GitHub action to lint and format python code

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

- Enabling read and write permissions for GitHub actions
  - First go to the settings for the repository you are going to use RuffFix on
    ![image](https://github.com/user-attachments/assets/14fc994f-10a6-4532-873f-ac34b0d8207e)
  - Then click on action tab and then click general option
    ![image](https://github.com/user-attachments/assets/f5d63fe2-2831-4e41-937f-4e968a374dc5)
    ![image](https://github.com/user-attachments/assets/ef3f9432-235c-45df-9465-e0832e82fc93)

  - Finally enable read and write permission for Github Actions to commit changes to the repo
    ![image](https://github.com/user-attachments/assets/0b88d29b-9df0-48c9-9615-b0fe1d55e80f)


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

Give a ⭐ if this action helped you.

---
