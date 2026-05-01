# Full_Stack_Assessment

This project is a **Flask-based backend** designed to work with a pre-built Admin UI.
The frontend (HTML, CSS, JavaScript) is already provided and remains **unchanged**, while this backend powers all functionality such as authentication and opportunity management.

---

## 🚀 Features

* Admin Signup & Login (Session-based authentication)
* Secure password hashing using Bcrypt
* Add, View, Update, and Delete Opportunities
* Data stored using SQLite database
* Fully compatible with existing Admin UI (no frontend changes required)
* RESTful API structure

---

## 🛠️ Tech Stack

* Python
* Flask
* Flask-SQLAlchemy
* Flask-Bcrypt
* Flask-CORS
* SQLite

---

## 📂 Project Structure

```
project/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── admin.css
│   ├── js/
│   │   └── admin.js
│   └── image/
```

---

## ⚙️ Installation & Setup

1. Clone the repository:

```
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the application:

```
python app.py
```

4. Open in browser:

```
http://127.0.0.1:5000/
```

---

## 🔐 Default Login Credentials

```
Email: admin@example.com  
Password: 12345678
```

---

## 📡 API Endpoints

### Authentication

* POST /api/signup
* POST /api/login
* GET /api/logout

### Opportunities

* GET /api/opportunities
* POST /api/opportunities
* PUT /api/opportunities/<id>
* DELETE /api/opportunities/<id>

---

## ⚠️ Important Notes

* Do not modify frontend files (as per project requirement)
* Backend is built to match existing UI functionality
* SQLite database is used for simplicity
* Ensure static files are placed correctly for proper UI rendering

---

## 📌 Future Improvements

* Add JWT authentication
* Use MySQL/PostgreSQL for production
* Deploy on cloud platforms (Render, AWS, etc.)
* Add user roles and permissions

---

