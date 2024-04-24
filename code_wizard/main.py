from fastapi import FastAPI
from code_wizard.routers import code_wizard_endpoint
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware


load_dotenv()

app = FastAPI()

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
