# Agent Instructions

This repository contains the code for a next-generation ecommerce platform. When working on this project, please adhere to the following guidelines:

## Architecture

- The backend is structured using a service-oriented architecture within a modular monolith (for now).
- External services (Google Cloud, Firebase, Retail, AI) are encapsulated in the `backend/app/services` directory.
- API endpoints are organized by version and domain in `backend/app/api`.

## Technologies

- **Python**: Use Python 3.11+.
- **FastAPI**: Used for building the REST API.
- **Google Cloud**: Use the official Google Cloud client libraries.
- **Firebase**: Use `firebase-admin` for backend interactions.

## Coding Standards

- Follow PEP 8 guidelines.
- Use type hints for all function arguments and return values.
- Ensure all new features have corresponding tests in `backend/tests`.

## Deployment

- The application is containerized using Docker.
- Changes should be verified locally using `uvicorn` or Docker before submitting.
