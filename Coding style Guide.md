# Coding Style Guide 

This guide helps our team write clean, consistent, and easy-to-read code. All code should follow this style so that our project looks like it was written by one person — even when we work on it together.

---

## Python Style

- Follow [PEP 8](https://peps.python.org/pep-0008/)
- Use 4 spaces for indentation (not tabs)
- Keep lines under 100 characters
- Use blank lines between functions and classes
- Add docstrings to all functions and classes
- Use comments to explain tricky logic or important steps

### Naming Conventions

| Item        | Format Example            |
|-------------|----------------------------|
| Variables   | `user_id`, `vehicle_list`  |
| Functions   | `create_user()`, `get_vehicle()` |
| Classes     | `User`, `VehicleInventory` |
| Constants   | `DEFAULT_SHIPPING_COST`    |
| Files       | `user_routes.py`, `sales_data.py` |

---

## Flask Structure

| Folder         | Purpose                          |
|----------------|----------------------------------|
| `/routes/`     | Flask blueprints and route logic |
| `/templates/`  | HTML templates with Jinja2       |
| `/static/`     | CSS, JS, and image files         |
| `/data/`       | JSON files for storing data      |
| `/tests/`      | Test files using `pytest`        |
| `config.py`    | App configuration and settings   |
| `app.py`       | Main application entry point     |

Use [Jinja2 syntax](https://jinja.palletsprojects.com/en/3.1.x/templates/) in all `.html` files.

---

## Testing

- Use `pytest`
- Test files go in the `tests/` folder
- Name test functions like: `test_function_expectedResult()`
  - Example: `test_create_user_validInput_addsUser()`

---

## Git & Branching Rules

- Use [GitFlow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)

### Branch Names

| Type     | Format Example             |
|----------|----------------------------|
| Feature  | `feature/login-page`       |
| Bug Fix  | `bugfix/fix-price-format`  |
| Hotfix   | `hotfix/homepage-crash`    |

### Commit Messages

-  `add: user login route`
-  `fix: price display bug`

### Pull Requests

- Always create a new branch (never work on `main`)
- Open a PR and assign at least one reviewer
- Only merge into `develop` or `main` after approval

---

## Resources

- [PEP 8 – Python Style Guide](https://peps.python.org/pep-0008/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [PullRequest Style Guide Tips](https://www.pullrequest.com/blog/create-a-programming-style-guide/)
