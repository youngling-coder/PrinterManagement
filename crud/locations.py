import sqlite3
from .database import get_db_cursor

TABLE_NAME = "locations"


def get_locations():
    with get_db_cursor() as cursor:
        
        stmt = cursor.execute(f"SELECT * FROM {TABLE_NAME};")
        return stmt.fetchall()

def get_location_by_id(id: int):
    with get_db_cursor() as cursor:
        stmt = cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE id = (?)", (id,))
        
        return stmt.fetchone()

def get_location_by_name(name: str):
    with get_db_cursor() as cursor:
        stmt = cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE name = (?)", (name,))
        
        return stmt.fetchone()

def create_location(name: str):
    new_location_id = None 
    
    try:
        with get_db_cursor() as cursor:
            cursor.execute(f"INSERT INTO {TABLE_NAME} (name) VALUES (?)", (name,))
            new_location_id = cursor.lastrowid

        if new_location_id:
            return get_location_by_id(new_location_id)

    except sqlite3.IntegrityError:
        return

def delete_location(id: int):
    with get_db_cursor() as cursor:
        cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE id = (?)", (id,))
