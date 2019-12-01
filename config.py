import os


if os.getenv('PROD', True):
    DATABASE_URL = os.getenv(
        'DATABASE_URL', 'postgres://localhost:5432/loftsix')
else:
    db = 'loftsix'
    port = os.getenv('DB_PORT', 5433)
    user = os.getenv('DB_USER', 'postgres')
    pw = os.getenv('DB_PASSWORD', 'postgres')
    host = os.getenv('DB_HOST', 'localhost')
    DATABASE_URL = f'postgresql+psycopg2://{user}:{pw}@{host}:{port}/{db}'
