# AI Automation API (Generic)

## Environment
Create `.env` (copied from `.env.sample`):

```
BASE_URL=http://localhost:8000
HF_TOKEN=
LOG_FILE=log.txt
```

## Run locally
```
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Docker
```
docker build -t ai-automation-api .
docker run -p 8000:8000 ai-automation-api
```

## Example AI call
```
curl -X POST http://localhost:8000/ai/task -H "Content-Type: application/json" -d '{"task":"sentiment","text":"I love this API!"}'
```
