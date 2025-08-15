import sqlite3
from .database import get_db_cursor

TABLE_NAME = "printers"


def get_printers():
    with get_db_cursor() as cursor:

        stmt = cursor.execute(f"SELECT * FROM {TABLE_NAME};")
        return stmt.fetchall()


def get_printers_by_location_id(location_id: int):
    with get_db_cursor() as cursor:
        stmt = cursor.execute(
            f"SELECT * FROM {TABLE_NAME} WHERE location_id = (?)", (location_id,)
        )

        return stmt.fetchall()


def get_printer_by_id(id: int):
    with get_db_cursor() as cursor:
        stmt = cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE id = (?)", (id,))

        return stmt.fetchone()


def get_printer_by_name(name: str):
    with get_db_cursor() as cursor:
        stmt = cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE name = (?)", (name,))

        return stmt.fetchone()


def get_printer_by_dns(dns: str):
    with get_db_cursor() as cursor:
        stmt = cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE dns = (?)", (dns,))

        return stmt.fetchone()


def create_printer(data: dict):

    new_printer_id = None

    try:
        with get_db_cursor() as cursor:
            cursor.execute(
                f"INSERT INTO {TABLE_NAME} ({", ".join(data.keys())}) VALUES (?,?,?,?,?,?)",
                tuple(data.values()),
            )
            new_printer_id = cursor.lastrowid

        if new_printer_id:
            return get_printer_by_id(new_printer_id)

    except sqlite3.IntegrityError:
        return


def delete_printer(id: int):
    with get_db_cursor() as cursor:
        cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE id = (?)", (id,))


def update_printer(id: int, data: dict):
    try:
        with get_db_cursor() as cursor:
            set_clause = ", ".join([f"{key} = ?" for key in data.keys()])
            cursor.execute(
                f"UPDATE {TABLE_NAME} SET {set_clause} WHERE id = ?",
                (*data.values(), id),
            )

    except sqlite3.IntegrityError:
        return
