import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from app.routes import router

# ✅ 1. Create FastAPI app FIRST
app = FastAPI(title="Call Center Compliance AI")

# ✅ 2. Add middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ 3. Include API routes
app.include_router(router)

# ✅ 4. Add homepage route (UI)
@app.get("/")
def home():
    return FileResponse(os.path.join("static", "index.html"))