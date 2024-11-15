from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker




SQLALCHEMY_DATABASE_URL = f'sqlite:///database.db'

# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
# DB_NAME=os.environ.get("DB_NAME")

# SQLALCHEMY_DATABASE_URL = f"sqlite:///./{DB_NAME}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,echo=True, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()