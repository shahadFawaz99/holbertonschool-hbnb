# HBnB Evolution - Part 1: Technical Documentation

## 📘 Overview

This repository contains the comprehensive technical documentation for **Part 1** of the HBnB Evolution project. The goal of this phase is to establish a clear architectural and design foundation for an AirBnB-like application, focusing on the system's structure, core entities, and API interaction flows.

---

## 🎯 Project Objectives

The main objectives of this part are:

- Design a **high-level package diagram** illustrating the application’s layered architecture and inter-layer communication using the **facade pattern**.
- Develop a **detailed class diagram** for the **Business Logic Layer** representing entities such as `User`, `Place`, `Review`, and `Amenity`.
- Create **sequence diagrams** for key API calls to capture the interaction between system components.
- Compile a **complete technical document** including all diagrams and explanatory notes.

---

## 🧱 Architecture Overview

### 🔄 Layered Architecture

The application is structured using a traditional **three-layered architecture**:

1. **Presentation Layer**
   - Interfaces with users through API endpoints and services.
   - Validates requests and responses.
2. **Business Logic Layer**
   - Contains core application logic and domain models (`User`, `Place`, etc.).
   - Enforces business rules and coordinates operations.
3. **Persistence Layer**
   - Handles data storage and retrieval.
   - Interfaces with the underlying database.

All interactions between layers are facilitated via a **facade interface**, simplifying the coupling between components.

---

## 📦 Task 0: High-Level Package Diagram

### ✅ Deliverables:
- High-level UML package diagram.
- Explanation of how layers communicate through the facade pattern.

### 🗂 Layers and Components:

- `PresentationLayer`
  - `UserAPI`, `PlaceAPI`, `ReviewAPI`
- `BusinessLogicLayer`
  - `UserService`, `PlaceService`, `ReviewService`, `AmenityService`
- `PersistenceLayer`
  - `UserRepository`, `PlaceRepository`, `ReviewRepository`, `AmenityRepository`

### 🧩 Facade Pattern
Facilitates interaction between Presentation and Business Logic layers, abstracting internal complexities from the API.

---

## 🧪 Task 1: Class Diagram - Business Logic Layer

### ✅ Deliverables:
- UML class diagram for core models.
- Description of relationships and key attributes/methods.

### 📌 Core Entities:

#### `User`
- Attributes: `id`, `first_name`, `last_name`, `email`, `password`, `is_admin`, `created_at`, `updated_at`
- Methods: `register()`, `update_profile()`, `delete()`

#### `Place`
- Attributes: `id`, `title`, `description`, `price`, `latitude`, `longitude`, `owner_id`, `created_at`, `updated_at`
- Methods: `create()`, `update()`, `delete()`, `add_amenity()`

#### `Review`
- Attributes: `id`, `place_id`, `user_id`, `rating`, `comment`, `created_at`, `updated_at`
- Methods: `create()`, `update()`, `delete()`

#### `Amenity`
- Attributes: `id`, `name`, `description`, `created_at`, `updated_at`
- Methods: `create()`, `update()`, `delete()`

### 🔗 Relationships:
- One `User` can own many `Places`.
- One `Place` can have many `Amenities`.
- One `Place` can have many `Reviews`.
- One `User` can submit many `Reviews`.

---

## 🔁 Task 2: Sequence Diagrams - API Interactions

### ✅ Deliverables:
- Four sequence diagrams.
- Step-by-step interaction flow across layers.

### 📥 API Calls and Diagrams:

#### 1. **User Registration**
- User → API → UserService → UserRepository → DB
- Flow: Validate → Save → Return confirmation

#### 2. **Place Creation**
- User → API → PlaceService → PlaceRepository → DB
- Flow: Authenticate → Validate input → Save → Return created place

#### 3. **Review Submission**
- User → API → ReviewService → ReviewRepository → DB
- Flow: Verify ownership/visit → Save → Return result

#### 4. **Fetching List of Places**
- User → API → PlaceService → PlaceRepository → DB
- Flow: Apply filters → Query DB → Return results

---

## 📄 Task 3: Documentation Compilation

### ✅ Deliverables:
- Complete technical document (PDF or Markdown).
- Structured sections:
  - **Introduction**
  - **High-Level Architecture**
  - **Business Logic Design**
  - **API Sequence Diagrams**
  - **Explanatory Notes**

### 🧠 Purpose
This document serves as a **blueprint** for the development of HBnB Evolution. It provides clarity and consistency across all implementation phases.

---

## 🧰 Tools and Resources

- Diagrams: [Mermaid.js](https://mermaid.js.org/), [draw.io](https://app.diagrams.net/)
- References:
  - UML Class & Sequence Diagrams
  - Facade & Layered Architecture Design Patterns
  - [UML Guide](https://www.uml-diagrams.org/)
  - [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/)

---

## ✅ Expected Outcome

By completing this part, you will have:

- A clear architectural vision for the application.
- Visual and documented representation of the core logic and API workflows.
- A ready-to-implement design blueprint for the upcoming development phases.

---

## 📎 Repo Information

- **Repository**: [holbertonschool-hbnb](https://github.com/shahadFawaz99/holbertonschool-hbnb.git)
- **Directory**: `part1/`
---
## 👨‍💻 Authors
Shahad Aljahdali – @shahadFawaz99

Donna Almadani – @donnasaud

Munirah Faqihi – @MuFaqihi
