# Neamo Web 

This is a Flask-based web application designed for managing and analyzing offshore fish farming data. It currently provides an interface for interacting with geospatial and environmental data.

---

### **Prerequisites**
Before running the application, ensure you have the following installed:
- **Python 3.7+** ([Download Python](https://www.python.org/downloads/))
- **pip** (Python package manager)
- **Virtual Environment** (optional but recommended)
- **SQLite** (included with Python)
- **Node.js** (for frontend development, optional)

---

## Installation Steps

### 1: Clone the Repository
```bash
git clone https://github.com/your-repo/website-for-neamo.git
cd neamo-webapp/Wed-App
```

### 2: Install Python and Dependencies

To ensure all required dependencies are installed, run:
```bash
pip install flask pandas flask_login sqlalchemy werkzeug
```

These libraries are used for:
- **Flask**: Web framework for building the application.
- **Pandas**: Data manipulation and analysis.
- **Flask-Login**: User authentication and session management.
- **SQLAlchemy**: Database ORM for managing database interactions.
- **Werkzeug**: Security and utility functions for handling authentication.

Additionally, built-in modules such as `os`, `json`, and `website.models` are used and require no installation.
If Python is not installed, download and install it from [python.org](https://www.python.org/downloads/).

Verify Python installation:
```bash
python --version
```

Verify pip installation:
```bash
pip --version
```

### 3: Create and Activate a Virtual Environment (Recommended to avoid dependency conflicts)
#### For Windows (PowerShell):
```powershell
python -m venv venv
venv\Scripts\Activate
```
#### For Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Running the Application

### 5: Set Environment Variables
#### For Windows (PowerShell):
```powershell
$env:FLASK_APP="main.py"
$env:FLASK_ENV="development"
```
#### For Mac/Linux:
```bash
export FLASK_APP=main.py
export FLASK_ENV=development
```

### 6: Start the Flask Server
```bash
flask run
```
The app should now be running at (copy in any browser):
```
http://127.0.0.1:5000
```

---

## 🗂 Folder Structure
```
neamo-webapp/
│── Wed-App/
│   ├── main.py             # Flask application entry point
│   ├── website/            # Main application folder
│   │   ├── __init__.py     # Flask app factory
│   │   ├── views.py        # Routes and logic
│   │   ├── models.py       # Database models
│   │   ├── static/         # CSS, JS, Images
│   │   ├── templates/      # HTML templates
│   ├── data/               # CSV and datasets
│   ├── raw_data/           # Raw NetCDF files
│   ├── output/             # Processed data output
│   ├── README.md           # Setup instructions
```

---

## 👥 Contributors
- **Viktors H** - Lead Developer
- **Aija Monika V** - Project Contributor

