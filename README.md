# Agentic creative coding

Prompt-based creative coding. Using LLMs to generate p5.js sketches.

## Backend

FastAPI app using LangGraph for agentic flow. Get your API keys from LangGraph and OpenAI, and put them in `.env`. 

### Backend setup

```
cd back
python -m venv <path_to_your_env>

```

### Backend dev

```
cd back
source <path_to_your_env>/bin/activate
uvicorn api:app --reload
```

## Frontend

### Frontend setup

```
cd front
npm i
```

### Frontend dev

```
cd front
npm start
```

