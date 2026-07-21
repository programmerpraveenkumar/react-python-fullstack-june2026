from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
load_dotenv()

DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_USER_NAME = os.getenv("DB_USER_NAME")
DB_NAME= os.getenv("DB_NAME")
DB_HOSTNAME= os.getenv("DB_HOSTNAME")

DATABASE_URL = f"mysql+pymysql://{DB_USER_NAME}:{DB_PASSWORD}@{DB_HOSTNAME}:3306/{DB_NAME}"
# 3. Create the engine instance
engine = create_engine(
    DATABASE_URL,
    pool_size=10,         # Maximum number of persistent connections to keep
    max_overflow=20,      # Maximum temporary connections beyond pool_size
    pool_recycle=3600,    # Avoid 'MySQL server has gone away' by recycling idle connections
    pool_pre_ping=True    # Check connection validity prior to checking it out
)

SessionLocal = sessionmaker(bind=engine)

db = SessionLocal()

# connection(),cursor.open()
# //exceuction()
# connection.close(),cursor.close()
# # 4. Test the database connection safely
# try:
#     with engine.connect() as connection:
#         result = connection.execute(text("SELECT VERSION();"))
#         print(f"Connection successful! MySQL Version: {result.fetchone()[0]}")
# except Exception as e:
#     print(f"An error occurred: {e}")
