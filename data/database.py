import sqlite3

from typing import Optional

conn = sqlite3.connect("data/database.db")
cur = conn.cursor()

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        user_name TEXT,
        game_activity BOOLEAN
    )
    """
)
conn.commit()

async def insert_users(user_id: int, user_name: str) -> None:
    cur.execute("INSERT INTO users (user_id, user_name, game_activity) VALUES (?, ?, ?)", (user_id, user_name, False))
    conn.commit()
    
async def get_user(user_id: int) -> Optional[int]:
    cur.execute("SELECT user_id FROM users WHERE user_id = ?", (user_id,))
    return cur.fetchone()

async def get_name(user_id: int) -> Optional[str]:
    cur.execute("SELECT user_name FROM users WHERE user_id = ?", (user_id,))
    result = cur.fetchone()
    return result[0] if result else None

async def get_game_activity(user_id: int) -> bool:
    cur.execute("SELECT game_activity FROM users WHERE user_id = ?", (user_id,))
    return cur.fetchone()[0]

async def set_name(user_id: int, new_name: str) -> None:
    cur.execute("UPDATE users SET user_name = ? WHERE user_id = ?", (new_name, user_id))
    conn.commit()
    
async def set_game_activity(user_id: int, is_active: bool) -> None:
    cur.execute("UPDATE users SET game_activity = ? WHERE user_id = ?", (is_active, user_id))
    conn.commit()