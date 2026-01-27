# Next Generation Ecommerce Platform

This is a next-generation ecommerce platform built on Google Cloud and Firebase, leveraging Google for Retail and Google AI for agentic flows and timely customer connections.

## Project Structure

- **backend/**: Python backend using FastAPI.
  - **app/**: Application source code.
    - **api/**: API routes and endpoints.
    - **core/**: Core configuration and security.
    - **models/**: Data models.
    - **services/**: Integrations with Google Cloud, Firebase, Retail, and AI.
  - **tests/**: Unit and integration tests.
- **frontend/**: Frontend application (placeholder).
- **infrastructure/**: Infrastructure as Code (Terraform) for Google Cloud deployment.
- **notebooks/**: Jupyter notebooks for data analysis and AI experimentation.

## Tech Stack

- **Backend**: Python, FastAPI
- **Cloud**: Google Cloud Platform (GCP)
- **Database**: Firebase (Firestore), Cloud Storage
- **AI/ML**: Google AI (Gemini/Vertex AI), Google Cloud Retail API
- **Protocols**: Universal Commerce Protocol (UCP)

## Universal Commerce Protocol (UCP)

This platform supports the Universal Commerce Protocol (UCP) for agentic commerce. The following endpoints are available:

- `POST /api/v1/ucp/checkout`: Create a new checkout session.
- `POST /api/v1/ucp/payment`: Handle payment creation/update.
- `POST /api/v1/ucp/fulfillment`: Handle fulfillment options.

## Getting Started

### Backend

1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the server:
   ```bash
   uvicorn app.main:app --reload
   ```

## Infrastructure

See the `infrastructure/` directory for Terraform scripts to provision resources.
