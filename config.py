import os

DATABASE_URL = os.getenv('DATABASE_URL', 'postgres://localhost:5432/loftsix')
