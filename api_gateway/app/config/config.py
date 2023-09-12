import os

from dotenv import load_dotenv

load_dotenv()

SV_HOST = os.getenv("SV_HOST", default="0.0.0.0")
SV_PORT = int(os.getenv("SV_PORT", default="8000"))
SV_NAME = os.getenv("SV_NAME", default="app")
SV_VERSION = os.getenv("SV_VERSION", default="0.0.1")

DB_HOST = os.getenv("DB_HOST", default="localhost")
DB_USER = os.getenv("DB_USER", default="postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="postgres")
DB_PORT = os.getenv("DB_PORT", default="5432")
DB_NAME = os.getenv("DB_NAME", default="postgres")
DB_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

IS_DOCS = os.getenv("IS_DOCS", default="TRUE").upper() == "TRUE"

ALLOW_ORIGINS = os.getenv("ALLOW_ORIGINS", default="*")
