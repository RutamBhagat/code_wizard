import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from code_wizard.routers import code_wizard_endpoint


load_dotenv()

app = FastAPI()

# Add CORS middleware to allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(
    code_wizard_endpoint.router,
    prefix="/code_wizard_endpoint",
    tags=["code_wizard_endpoint"],
)

PORT = 8000
HOST = "0.0.0.0"

if __name__ == "__main__":
    uvicorn.run("main:app", host=HOST, port=PORT, reload=True)
