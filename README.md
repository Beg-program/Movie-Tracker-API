
# Movie Tracker API

A lightweight, high-performance RESTful API built with **FastAPI** to manage a movie "must-watch" list. This project demonstrates core backend concepts including CRUD operations, data validation with Pydantic, and state management using Python dictionaries.

## 🚀 Features
* **Create Movies**: Add new movies with validation (ensures year is post-1888).
* **Read Movies**: Fetch the entire list or filter by "watched" status.
* **Partial Updates**: Update a movie's watched status using PATCH via query parameters.
* **Delete**: Remove movies from the database with proper 204 No Content responses.
* **Validation**: Robust error handling for non-existent IDs and invalid data types.

## 🛠️ Tech Stack
* **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
* **Validation**: [Pydantic](https://docs.pydantic.dev/)
* **Language**: Python 3.10+


