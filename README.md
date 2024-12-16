Personal Diary Project:
The Personal Diary project is a Django-based web application where users can securely manage their personal diary entries. It includes user authentication, CRUD operations for diary entries, and both API and browser-based dashboard functionality. This project uses the Django REST Framework (DRF) for API endpoints and integrates JWT-based authentication to ensure data privacy and security.
Features:
Authentication: JWT-based user authentication (login and logout).

CRUD Operations: Users can create, read, update, and delete their own diary entries.

User-Specific Access: Only authenticated users can access their entries.

Dashboard: Displays all entries for the logged-in user in the browser.

API Endpoints

Login/Register: API for user authentication.

Diary Entries:

GET /api/entries/: List all diary entries for the logged-in user.

POST /api/entries/: Add a new entry.

GET /api/entries/<id>/: Retrieve a specific entry.

PUT /api/entries/<id>/: Update an entry.

DELETE /api/entries/<id>/: Delete an entry.

