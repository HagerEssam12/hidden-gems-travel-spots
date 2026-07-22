# Hidden Gems – Travel Spots

## Description

Hidden Gems – Travel Spots is a Flask web application where users can discover, share, and manage travel destinations.

The application allows users to:

- Register and log in.
- Add new travel spots with images.
- Search travel spots by name or location.
- Filter travel spots by category.
- Save and remove favorite travel spots.
- Edit and delete only the spots they created.

### New Feature

This project introduces a travel destination management system that allows users to:

- Add custom travel destinations.
- Save favorite destinations.
- Search and filter travel spots.
- Edit and delete only their own posts.
- Store application data using JSON files.

---
# Prerequisites

Install the required packages:

```bash
pip install -r requirements.txt
```

or

```bash
pip install Flask
```

---

# Running the Project

1. Clone the repository.
2. Open the project folder.
3. Install the requirements.
4. Run:

```bash
python app.py
```

5. Open your browser and navigate to:

```
http://127.0.0.1:5000
```

---

## Project Checklist
- [x] It is available on GitHub.
- [x] It uses the Flask web framework.
- [x] It uses at least one module from the Python Standard Library other than the random module. 
  - Module name: `json` (and `os`)
- [x] It contains at least one class written by you that has both properties and methods. It uses `__init__()` to let the class initialize the object's attributes.
  - File name for the class definition: `logic/spot.py`
  - Line number(s) for the class definition: Lines 1–45
  - Name of two properties: `name`, `category` (also `id`, `location`, `description`, `image_url`)
  - Name of two methods: `to_dict()`, `from_dict()`
  - File name and line numbers where the methods are used: 
    - `to_dict()`: `logic/spot_logic.py`, Line 31 & Line 47
    - `from_dict()`: `logic/spot_logic.py`, Line 12
- [x] It makes use of JavaScript in the front end and uses the `localStorage` of the web browser.
  - File name: `js/main.js`
  - Line number(s): Lines 1-13 (manages saving and retrieving favorite spots using `localStorage`)
- [x] It uses modern JavaScript (for example, `let` and `const` rather than `var`).
  - File name: `js/main.js`
  - Line number(s): Lines 1-5
- [x] It makes use of the reading and writing to the same file feature.
  - File name: `logic/spot_logic.py`
  - Line number(s): Reading in `load_spots()` (Lines 8–13) and Writing in `save_spots()` (Lines 16–18) to `data/spots.json`.
- [x] It contains conditional statements.
  - File name: `routes/spot_routes.py`
  - Line number(s): Line 18 (`if request.method == 'POST':`)
- [x] It contains loops.
  - File name: `logic/spot_logic.py`
  - Line number(s): Line 22 (`for spot in spots:`)
- [x] It lets the user enter a value in a text box at some point. This value is received and processed by your back end Python code.
  - File name: `templates/add_spot.html` (Lines 8–25) processed by `routes/spot_routes.py` (Lines 18–33)
- [x] It doesn't generate any error message even if the user enters a wrong input.
  - Graceful fallback and field validation handled in routes (`routes/spot_routes.py` Line 20).
- [x] It is styled using your own CSS.
  - File name: `static/css/style.css`
- [x] The code follows the code and style conventions as introduced in the course, is fully documented using comments and doesn't contain unused or experimental code. In particular, the code should not use `print()` or `console.log()` for any information the app user should see. Instead, all user feedback needs to be visible in the browser.
- [x] All exercises have been completed as per the requirements and pushed to the respective GitHub repository.

# Technologies Used

- Python
- Flask
- HTML5
- CSS3
- JavaScript
- JSON

---

# Project Structure

```text
hidden-gems-travel-spots/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── spots.json
│   └── users.json
│
├── logic/
│   ├── spot.py
│   ├── spot_logic.py
│   └── user_logic.py
│
├── routes/
│   ├── auth_routes.py
│   └── spot_routes.py
│
├── static/
│   └── css/
│       └── style.css
│
└── templates/
    ├── base.html
    ├── home.html
    ├── login.html
    ├── register.html
    ├── add_spot.html
    ├── edit_spot.html
    └── favorites.html
```