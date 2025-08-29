# Bajaj Full Stack Project

This project is an implementation of the requirements specified in the question paper.

Refer to the [Full Stack Question Paper - VIT.pdf](./Full%20Stack%20Question%20Paper%20-%20VIT.pdf) for details.

## Running the application

This is a Flask application. To run the application, use the following command:

```bash
uv run app.py
```

## Example request

Once the application is running, you can send a POST request to the `/bfhl` endpoint.

### cURL (Command Prompt / Bash)

```bash
curl -X POST -H "Content-Type: application/json" -d '{"data": ["M", "1", "334", "4", "B"]}' http://127.0.0.1:5000/bfhl
```

### PowerShell

```powershell
curl -Uri http://127.0.0.1:5000/bfhl -Method Post -Body '{"data": ["M", "1", "334", "4", "B"]}' -ContentType "application/json"
```
