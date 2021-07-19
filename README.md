# twint-server
Open Source Intelligence Tool that scrapes Twitter using Twint and returns a JSON response via FastAPI.

## Features
- [x] get last 100 tweets by (username)
- [ ] extend API to support more [Twint features](https://github.com/twintproject/twint/wiki/Basic-usage)

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