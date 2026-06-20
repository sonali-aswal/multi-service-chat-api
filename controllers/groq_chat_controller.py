import os
from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException
from groq import Groq

from models.chat_model import ChatRequest

load_dotenv()

router = APIRouter()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


@router.post("/api/chat/groq")
def chat_with_groq(request: ChatRequest):
    try:
        # 1. Check API key
        if not GROQ_API_KEY:
            raise HTTPException(
                status_code=500,
                detail="GROQ_API_KEY is missing in .env"
            )

        # 2. Validate input
        if not request.message or not request.message.strip():
            raise HTTPException(
                status_code=400,
                detail="Message cannot be empty"
            )

        # 3. Create Groq client
        client = Groq(api_key=GROQ_API_KEY)

        # 4. Call Groq model
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": request.message
                }
            ],
            temperature=0.7
        )

        # 5. Extract answer
        answer = completion.choices[0].message.content

        # 6. Return response
        return {
            "response": answer
        }

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Groq API error: {str(e)}"
        )