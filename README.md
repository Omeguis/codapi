# Sample Read-Only API

This is a simple read-only API built with FastAPI that can be consumed by a single page application.

## Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the API locally:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

- `GET /`: Welcome message
- `GET /items`: Get all items
- `GET /items/{item_id}`: Get a specific item by ID

## API Documentation

FastAPI automatically generates API documentation:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Deployment Options

Here are several options to deploy your API:

1. **Render** (Recommended for beginners):
   - Create an account at render.com
   - Create a new Web Service
   - Connect your GitHub repository
   - Set the build command: `pip install -r requirements.txt`
   - Set the start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

2. **Heroku**:
   - Create a `Procfile` with: `web: uvicorn main:app --host=0.0.0.0 --port=$PORT`
   - Deploy using Heroku CLI or GitHub integration

3. **PythonAnywhere**:
   - Create an account at pythonanywhere.com
   - Upload your code
   - Set up a web app using FastAPI

4. **AWS Lambda + API Gateway**:
   - Use the Mangum adapter to make FastAPI work with AWS Lambda
   - Deploy using AWS SAM or Serverless Framework

## CORS Configuration

The API is currently configured to accept requests from any origin (`*`). In production, you should update the `allow_origins` list in `main.py` to only include your frontend domain(s).

## Security Considerations

1. Update CORS settings to only allow your frontend domain
2. Consider adding rate limiting
3. Add authentication if needed
4. Use HTTPS in production 