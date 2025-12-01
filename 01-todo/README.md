# Django TODO Application - Homework Submission

This is a fully functional TODO application built with Django as part of the AI-Assisted Development homework.

## Homework Answers

### Question 1: Install Django
**Command used:**
```bash
pip install django
```

### Question 2: Project and App
**File to edit to include the app in the project:**
- **Answer: `settings.py`**

The app `todos` was added to the `INSTALLED_APPS` list in `todoproject/settings.py`.

### Question 3: Django Models
**Next step after creating models:**
- **Answer: Run migrations**

Commands executed:
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### Question 4: TODO Logic
**Where to put the TODO logic:**
- **Answer: `views.py`**

The TODO application logic (create, edit, delete, toggle resolved) is implemented in `todos/views.py`.

### Question 5: Templates
**Where to register the directory with templates:**
- **Answer: `TEMPLATES['DIRS']` in project's `settings.py`**

Added `BASE_DIR / 'templates'` to the `DIRS` list in the `TEMPLATES` configuration.

### Question 6: Tests
**Command to run tests:**
- **Answer: `python manage.py test`**

In this project, the command is:
```bash
python3 manage.py test
```

All 10 tests pass successfully, covering:
- Model creation and validation
- CRUD operations (Create, Read, Update, Delete)
- Toggle resolved functionality
- View responses and redirects
- Data ordering

## Features

The TODO application includes all required functionality:

✅ **Create TODOs** - Add new tasks with title, description, and due date  
✅ **Edit TODOs** - Modify existing tasks  
✅ **Delete TODOs** - Remove tasks with confirmation  
✅ **Assign Due Dates** - Set deadlines for tasks  
✅ **Mark as Resolved** - Toggle completion status  

## Project Structure

```
01-todo/
├── manage.py
├── todoproject/          # Main project directory
│   ├── settings.py       # Project settings (INSTALLED_APPS, TEMPLATES)
│   ├── urls.py          # Main URL configuration
│   └── ...
├── todos/               # TODO app
│   ├── models.py        # TODO model definition
│   ├── views.py         # View logic (CRUD operations)
│   ├── urls.py          # App URL patterns
│   ├── admin.py         # Admin panel configuration
│   ├── tests.py         # Comprehensive test suite
│   └── templates/       # HTML templates
│       └── todos/
│           ├── home.html
│           ├── todo_form.html
│           └── todo_confirm_delete.html
└── templates/           # Base templates
    └── base.html
```

## Running the Application

1. **Install Django** (if not already installed):
   ```bash
   pip install django
   ```

2. **Run migrations** (if needed):
   ```bash
   python3 manage.py migrate
   ```

3. **Run the development server**:
   ```bash
   python3 manage.py runserver
   ```

4. **Access the application**:
   Open your browser and navigate to: `http://127.0.0.1:8000/`

## Running Tests

Execute the test suite:
```bash
python3 manage.py test
```

Expected output: `Ran 10 tests in X.XXXs - OK`

## Admin Panel

To access the admin panel:

1. Create a superuser:
   ```bash
   python3 manage.py createsuperuser
   ```

2. Navigate to: `http://127.0.0.1:8000/admin/`

3. Log in and manage TODOs through the admin interface

## Technologies Used

- **Python** - Programming language
- **Django 5.2.8** - Web framework
- **SQLite** - Database (default Django database)
- **HTML/CSS** - Frontend templates with modern styling

## Notes

- The application uses Django's built-in SQLite database
- All functionality is tested and working
- Modern, responsive UI with gradient backgrounds and smooth interactions
- Inline CSS styling for simplicity (no external CSS files needed)
