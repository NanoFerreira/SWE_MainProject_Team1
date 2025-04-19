#  Data Storage Plan 

Our application uses **JSON files** for persistent data storage. This choice was made for its simplicity, readability, and tight integration with Python and Flask. This solution fits our small-scale project and development environment well.

---

##  Storage Format: JSON

We use `.json` files to store all application data such as users, inventory, and transactions. These files live in the `data/` folder and are updated any time a change is made through the application.

| Entity         | File Name                |
|----------------|--------------------------|
| Users          | `data/users.json`        |
| Inventory      | `data/inventory.json`    |
| Sales          | `data/sales.json`        |
| Shipping Types | `data/shipping_types.json` |

---

##  Tools & Technologies

| Tool / Library     | Purpose                                   |
|--------------------|-------------------------------------------|
| Python `json`      | Reading and writing structured data       |
| Python `os.path`   | Dynamic, OS-safe file path handling       |
| Flask              | Route logic that reads/writes from JSON   |
| `with open()`      | Secure file read/write blocks             |

---

## Data Flow: Step-by-Step

1. **Application Startup**
   - JSON files are loaded into Python structures (lists/dictionaries)
   - These are stored in memory and used throughout the app session

2. **Runtime (Create / Update / Delete)**
   - Any time a change is made (e.g., new vehicle listing), the corresponding Python object is updated
   - Immediately after, the updated object is **written back** to its JSON file

3. **App Restart**
   - Since data is stored on disk, the app loads the same persistent state on reboot
   - No data loss between sessions

---

##  Persistence Best Practices

- Always use `with open(filename, 'w')` for saving JSON to avoid data corruption
- Use `try/except` blocks when reading/writing to handle missing or malformed files
- Indent saved files using `indent=4` for readability
- Never store passwords or sensitive data in plaintext JSON

---

##  Why JSON?

- Easy to read and edit manually
- Zero setup required — ideal for small projects
- Integrates seamlessly with Python using the built-in `json` module
- Good fit for file-based persistence in a Flask app

---

## Development Environment

| Component           | Details                        |
|---------------------|--------------------------------|
| Language            | Python 3.x                     |
| Framework           | Flask                          |
| Storage             | JSON (file-based)              |
| OS Compatibility    | Windows 10+, macOS 12+         |
| IDEs                | IntelliJ, VS Code              |
| Project Management  | YouTrack for sprint planning   |

---

## Example: Saving Updated Inventory

```python
import json

def save_inventory(updated_inventory):
    with open("data/inventory.json", "w") as file:
        json.dump(updated_inventory, file, indent=4)
```

This ensures updated data is stored to disk and available on next app launch.

---
