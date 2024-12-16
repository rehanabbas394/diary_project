# Personal Diary Project

## Description
The **Personal Diary** project is a Django-based web application where users can securely manage their personal diary entries. It includes user authentication, CRUD operations for diary entries, and both API and browser-based dashboard functionality. This project uses the Django REST Framework (DRF) for API endpoints and integrates JWT-based authentication to ensure data privacy and security.

---

## Features

### Core Features
- **Authentication**: JWT-based user authentication (login and logout).
- **CRUD Operations**: Users can create, read, update, and delete their own diary entries.
- **User-Specific Access**: Only authenticated users can access their entries.
- **Dashboard**: Displays all entries for the logged-in user in the browser.

### API Endpoints
- **Login/Register**: API for user authentication.
- **Diary Entries**:
  - `GET /api/entries/`: List all diary entries for the logged-in user.
  - `POST /api/entries/`: Add a new entry.
  - `GET /api/entries/<id>/`: Retrieve a specific entry.
  - `PUT /api/entries/<id>/`: Update an entry.
  - `DELETE /api/entries/<id>/`: Delete an entry.

---

## Installation

### Prerequisites
Ensure you have the following installed on your machine:
- Python (>= 3.8)
- Django (>= 4.0)
- Django REST Framework
- djangorestframework-simplejwt

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/personal-diary.git
   cd personal-diary
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the application in your browser at [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## Usage

### API Usage (via Postman)
1. **Login**:
   - URL: `/api/token/`
   - Method: POST
   - Body: `{ "username": "your_username", "password": "your_password" }`
   - Response:
     ```json
     {
       "access": "<access_token>",
       "refresh": "<refresh_token>"
     }
     ```

2. **Set Authorization Header**:
   Add the following header for authenticated requests:
   ```
   Authorization: Bearer <access_token>
   ```

3. **Test CRUD Operations**:
   Use the endpoints listed in the "Features" section.

### Browser Usage
- Register and log in using the provided forms.
- Access the dashboard to view, add, update, or delete your diary entries.
- Log out using the logout button in the navbar.

---

## File Structure

```
personal-diary/
├── diary/
│   ├── templates/          # HTML templates
│   │   ├── base.html       # Main layout
│   │   ├── login.html      # Login page
│   │   ├── register.html   # Registration page
│   │   ├── dashboard.html  # User dashboard
│   ├── views.py            # Views for API and frontend
│   ├── urls.py             # URL routing
├── manage.py
└── requirements.txt        # Project dependencies
```


---

## Contributions
Contributions are welcome! Feel free to fork this repository and submit a pull request with your changes.

---

## Contact
For any questions or support, please contact:
- **Name**: Kashif Noor
- **Email**: [kashnoor022@gmail.com](mailto:kashnoor022@gmail.com)
- **GitHub**: [kashifnoor1](https://github.com/kashifnoor1)


