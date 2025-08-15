# HBnB - Part 3: Auth & Database

## 📚 Project Overview

This phase of the HBnB project focuses on adding persistent storage and authentication features to the application. Using SQLAlchemy as the ORM and Flask-JWT-Extended for authentication, this part brings together business logic, API security, and database relationships in a clean and scalable design.

The goal is to manage users, places, reviews, and amenities while enabling secure access and role-based control.

---

## ✨ Learning Objectives

* Define SQLAlchemy models with proper field types and constraints
* Establish one-to-many and many-to-many relationships
* Implement a repository pattern for database access
* Secure API endpoints using JWT authentication
* Hash and verify passwords securely with bcrypt
* Create SQL scripts for schema and seed data
* Visualize the database with Mermaid.js ER diagrams

---

## ✅ Project Requirements

* **Language:** Python 3
* **Framework:** Flask
* **ORM:** SQLAlchemy
* **Authentication:** Flask-JWT-Extended
* **Database:** SQLite (development)
* **Security:** Bcrypt password hashing
* ER diagram must be created using Mermaid.js
* All code must follow clean and modular design patterns
* A `README.md` file is mandatory

---

## 📁 Models & Relationships

| Entity         | Fields                                                        |
| -------------- | ------------------------------------------------------------- |
| User           | id, first\_name, last\_name, email, password, is\_admin       |
| Place          | id, title, description, price, latitude, longitude, owner\_id |
| Review         | id, text, rating, user\_id, place\_id                         |
| Amenity        | id, name                                                      |
| Place\_Amenity | place\_id, amenity\_id (join table for M\:M)                  |

---

## 🗃 Directory Structure

```
part3/
🔽
🔽 app/
🔽👉 models/               # SQLAlchemy models and associations
🔽👉 repositories/         # Business logic layer (repository pattern)
🔽👉 facade.py             # Central logic interface (Facade pattern)
🔽👉 config.py             # Flask configuration
🔽👉 extensions.py         # Bcrypt, JWT, and DB initialization
🔽
🔽 sql/
🔽👉 schema.sql            # Raw SQL table creation
🔽👉 seed.sql              # Admin user and amenities
🔽
🔽 hbnb_schema_diagram.md    # Mermaid.js ER diagram
🔽 requirements.txt
```

---

## 🧪 Testing

* Use `flask shell` to create tables and interact with the database
* Use Postman or cURL to test endpoints (e.g., `/auth/login`, `/places`, `/reviews`)
* Verify JWT protection and admin-only restrictions
* Run `sqlite3` to test SQL scripts manually

---

## 🖼 ER Diagram (Mermaid.js)

Diagram stored in [`hbnb_schema_diagram.md`](./hbnb_schema_diagram.md).
Visualizes:

* One-to-many relationships between User → Place → Review
* Many-to-many relationship between Place and Amenity

---

## 🛠 Initial Data

* Admin user inserted via `seed.sql` with:

  * Email: `admin@hbnb.io`
  * Password: `admin1234` (bcrypt-hashed)
* Amenities: WiFi, Swimming Pool, Air Conditioning

---

## 🧑‍💻 Authors

Shahad Aljahdali – @shahadFawaz99

Donna Almadani – @donnasaud

Munirah Faqihi – @MuFaqihi
