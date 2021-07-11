# twint-server
Scrapes Twitter using Twint and returns a JSON response

## Tools
- FastAPI
- Twint
- Uvicorn

## Setup
Install:
```
pip install -r requirements.txt
```

Run:
```
uvicorn main:app --reload
```

Open:
```
http://localhost:8000/user/(user_id)
```