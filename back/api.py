from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agents import stream_graph_updates

# FastAPI app instance
app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Define the request and response models
class UserMessage(BaseModel):
    message: str

class P5CodeResponse(BaseModel):
    code: str

# Mock LLM interaction function (replace with your actual LLM API call)
def generate_p5_code_from_message(message: str) -> str:
    prompts = message

    # Replace this logic with a call to your preferred LLM
    # Example: OpenAI API, HuggingFace, etc.
    llm_message = stream_graph_updates(prompts)

    return llm_message

    return f"""
    window.__P5_SKETCH__ = function(p) {{
        p.setup = function() {{
            p.createCanvas(800, 600);
            p.background(200);
            p.text('{llm_message}', 10, 50);
        }};
    }};
    """

# Endpoint to receive user messages and generate p5.js code
@app.post("/generate-p5", response_model=P5CodeResponse)
async def generate_p5_code(user_message: UserMessage):
    try:
        p5_code = generate_p5_code_from_message(user_message.message)
        return {"code": p5_code}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
