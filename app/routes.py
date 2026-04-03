from fastapi import APIRouter, UploadFile, File, HTTPException
import shutil
import os

from app.services.speech_to_text import transcribe_audio
from app.services.summarizer import summarize_text
from app.services.sop_checker import check_sop
from app.services.payment_classifier import classify_payment
from app.services.rejection_detector import detect_rejection
from app.services.keyword_extractor import extract_keywords

router = APIRouter()   # 🔥 THIS LINE IS IMPORTANT

UPLOAD_DIR = "temp"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/analyze-call")
async def analyze_call(file: UploadFile = File(...)):
    try:
        file_path = os.path.join(UPLOAD_DIR, file.filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        transcript = transcribe_audio(file_path)
        summary = summarize_text(transcript)
        sop = check_sop(transcript)
        payment = classify_payment(transcript)
        rejection = detect_rejection(transcript)
        keywords = extract_keywords(transcript)

        return {
            "transcript": transcript,
            "summary": summary,
            "sop_compliance": sop,
            "payment_type": payment,
            "rejection_reason": rejection,
            "keywords": keywords
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))