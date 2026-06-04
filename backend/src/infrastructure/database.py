"""
Infrastructure Layer - Database Connection Pool
Quản lý kết nối Postgres với ThreadedConnectionPool.
"""

import psycopg2
from psycopg2.pool import ThreadedConnectionPool
from psycopg2.extras import RealDictCursor
from fastapi import HTTPException
from contextlib import contextmanager

DB_HOST = "localhost"
DB_PORT = "5432"
DB_USER = "postgres"
DB_PASSWORD = "lolmht2003"
DB_NAME = "demo"

db_pool = ThreadedConnectionPool(
    minconn=1,
    maxconn=20,
    host=DB_HOST,
    port=DB_PORT,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME,
    cursor_factory=RealDictCursor,
)


@contextmanager
def get_db():
    conn = None
    cursor = None
    try:
        conn = db_pool.getconn()
        cursor = conn.cursor()
        yield cursor
        conn.commit()
    except Exception as e:
        if conn:
            conn.rollback()
        print(f"Database error: {e}")
        raise HTTPException(status_code=500, detail="Database error occurred")
    finally:
        if cursor:
            cursor.close()
        if conn:
            db_pool.putconn(conn)
