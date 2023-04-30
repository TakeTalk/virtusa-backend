from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context


app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://192.168.0.101:39160"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)