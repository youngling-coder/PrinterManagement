import os
import sqlite3
from typing import Iterator
from contextlib import contextmanager

DB_NAME: str = "dv.db"
SCHEMA_FILE: str = "structure.sql"


def dict_factory(cursor, row):

    d = {}

    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]

    return d


@contextmanager
def get_db_cursor() -> Iterator[sqlite3.Cursor]:

    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = dict_factory
    cursor = conn.cursor()

    try:
        yield cursor
    except sqlite3.Error as e:
        # If any database error occurs, roll back the transaction
        conn.rollback()
        # raise # Re-raise the exception so the caller knows about the error
    else:
        # If the 'with' block completed without error, commit the transaction
        conn.commit()
    finally:
        # Always close the connection
        if conn:
            conn.close()


def create_db_from_schema():
    """
    Sets up the database from a schema file.
    Removes the old DB file first for a clean setup.
    """

    with get_db_cursor() as cursor:

        # Read the schema file
        with open(SCHEMA_FILE, "r") as f:
            sql_script = f.read()

        # Execute the entire script
        cursor.executescript(sql_script)
