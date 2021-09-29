# twint-server
Open Source Intelligence Tool that scrapes Twitter using Twint and returns a JSON response via FastAPI.

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
