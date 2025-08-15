# HBnB – Part 2: BL & API

## 📚 Project Overview
This part brings the **HBnB Evolution** design to life. You’ll build the **Business Logic** and **Presentation (API)** layers in **Python + Flask**, using **flask-restx** for documentation and the **Facade pattern** to keep concerns clean.  
Data is stored using an **in-memory repository** now (simple and fast for iteration), designed to be swapped later with a **database-backed** persistence layer in Part 3.  
Core entities: **User, Place, Review, Amenity** — with relationships, validation, and versioned REST endpoints.

---

## ✨ Learning Objectives
- Structure a modular Flask project with clear layers and packages
- Implement core business models with **UUIDs**, timestamps, validation, and relationships
- Apply the **Facade pattern** to decouple API and business logic
- Build versioned, documented REST endpoints using **flask-restx**
- Return **composed data** (e.g., Place with owner + amenities + reviews)
- Validate inputs and handle errors with consistent **status codes**
- Test endpoints with **cURL**, Swagger UI, and **unittest/pytest**

---

## ✅ Project Requirements
- **Language:** Python 3
- **Framework:** Flask + flask-restx
- **Architecture:** Modular packages; Facade pattern; in-memory repository
- **Code Style:** PEP8
- **API Docs:** Swagger (auto from flask-restx at `/api/v1/`)
- **No Auth in Part 2:** JWT & RBAC come in Part 3
- **Repo:** `holbertonschool-hbnb`  
- **Directory:** `part2`

---

## 🧱 Project Structure

```
hbnb/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── users.py
│   │       ├── places.py
│   │       ├── reviews.py
│   │       └── amenities.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── user.py
│   │   ├── place.py
│   │   ├── review.py
│   │   └── amenity.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── facade.py
│   └── persistence/
│       ├── __init__.py
│       └── repository.py
├── run.py
├── config.py
├── requirements.txt
└── README.md
```

---

## 🧠 Data Models

### Common BaseModel
- `id: str` UUID4
- `created_at: datetime`
- `updated_at: datetime`
- `save()` updates timestamp
- `update()` modifies fields safely

### User
| Field        | Rules                                 |
|--------------|--------------------------------------|
| first_name   | required, ≤ 50                        |
| last_name    | required, ≤ 50                        |
| email        | required, unique, valid format        |
| is_admin     | bool, default False                   |

### Amenity
| Field      | Rules            |
|------------|------------------|
| name       | required, ≤ 50   |

### Place
| Field       | Rules                                  |
|-------------|----------------------------------------|
| title       | required, ≤ 100                        |
| price       | ≥ 0                                    |
| latitude    | -90..90                                |
| longitude   | -180..180                              |
| owner_id    | must exist in User                     |
| amenities   | list of Amenity IDs                    |

### Review
| Field      | Rules                    |
|------------|--------------------------|
| text       | required                  |
| rating     | int 1..5                  |
| user_id    | must exist in User        |
| place_id   | must exist in Place       |

---

## 🚦 API Endpoints

### Users
- `POST /api/v1/users/` → Create user  
- `GET /api/v1/users/` → List users  
- `GET /api/v1/users/<id>` → Get user by id  
- `PUT /api/v1/users/<id>` → Update user  

### Amenities
- `POST /api/v1/amenities/` → Create amenity  
- `GET /api/v1/amenities/` → List amenities  
- `GET /api/v1/amenities/<id>` → Get amenity by id  
- `PUT /api/v1/amenities/<id>` → Update amenity  

### Places
- `POST /api/v1/places/` → Create place  
- `GET /api/v1/places/` → List places  
- `GET /api/v1/places/<id>` → Get place by id (includes amenities & reviews)  
- `PUT /api/v1/places/<id>` → Update place  

### Reviews
- `POST /api/v1/reviews/` → Create review  
- `GET /api/v1/reviews/` → List reviews  
- `GET /api/v1/reviews/<id>` → Get review by id  
- `PUT /api/v1/reviews/<id>` → Update review  
- `DELETE /api/v1/reviews/<id>` → Delete review  
- `GET /api/v1/places/<place_id>/reviews` → List reviews for place  

**Status Codes:**  
`201 Created`, `200 OK`, `400 Bad Request`, `404 Not Found`

---

## 🧪 Testing & Validation

### Validation Rules
- User: names & email required, valid format  
- Place: title required, price ≥ 0, lat/lon ranges  
- Review: text required, rating 1..5  
- Amenity: name required  

### Manual Tests (cURL Examples)

**Create User**
```bash
curl -X POST http://127.0.0.1:5000/api/v1/users/ \
 -H "Content-Type: application/json" \
 -d '{"first_name":"John","last_name":"Doe","email":"john@example.com"}'
```

**Create Amenity**
```bash
curl -X POST http://127.0.0.1:5000/api/v1/amenities/ \
 -H "Content-Type: application/json" \
 -d '{"name":"Wi-Fi"}'
```

**Create Place**
```bash
curl -X POST http://127.0.0.1:5000/api/v1/places/ \
 -H "Content-Type: application/json" \
 -d '{"title":"Cozy Apartment","price":100,"latitude":37.77,"longitude":-122.42,"owner_id":"<user_id>","amenities":["<amenity_id>"]}'
```

**Create Review**
```bash
curl -X POST http://127.0.0.1:5000/api/v1/reviews/ \
 -H "Content-Type: application/json" \
 -d '{"text":"Great stay!","rating":5,"user_id":"<user_id>","place_id":"<place_id>"}'
```

---

## 🔍 Swagger Documentation
Run the server and open:  
```
http://127.0.0.1:5000/api/v1/
```

---

## 🧪 Automated Testing Example

```python
import unittest
from app import create_app

class TestUserEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_user(self):
        res = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@example.com"
        })
        self.assertEqual(res.status_code, 201)

    def test_create_user_invalid(self):
        res = self.client.post('/api/v1/users/', json={
            "first_name": "", "last_name": "", "email": "nope"
        })
        self.assertEqual(res.status_code, 400)
```

---

## 🗂️ Tasks
1. Project Setup & Package Initialization  
2. Core Business Logic Classes  
3. User Endpoints  
4. Amenity Endpoints  
5. Place Endpoints  
6. Review Endpoints  
7. Testing & Validation  

---

## 👥 Authors

Shahad Aljahdali – @shahadFawaz99

Donna Almadani – @donnasaud

Munirah Faqihi – @MuFaqihi
