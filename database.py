import sqlite3
from datetime import datetime
import bcrypt

from config import DATABASE_NAME


def get_connection():
    """
    Create SQLite connection.
    """
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def create_database():
    """
    Create all required tables.
    """

    conn = get_connection()
    cursor = conn.cursor()

    # ================= USERS =================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT NOT NULL,

        email TEXT UNIQUE NOT NULL,

        password TEXT NOT NULL,

        created_at TEXT NOT NULL

    )
    """)

    # ================= PREDICTION HISTORY =================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS detection_history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        sign_name TEXT NOT NULL,
        confidence REAL NOT NULL,
        image_path TEXT NOT NULL,
        prediction_time TEXT NOT NULL,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    conn.commit()
    conn.close()

def register_user(username, email, password):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email=?",
        (email,)
    )

    if cursor.fetchone():

        conn.close()

        return False, "Email already exists."

    hashed_password = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    ).decode()

    cursor.execute("""

    INSERT INTO users(
        username,
        email,
        password,
        created_at
    )

    VALUES(?,?,?,?)

    """, (

        username,
        email,
        hashed_password,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    ))

    conn.commit()
    conn.close()

    return True, "Registration Successful."

def login_user(email, password):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(

        "SELECT * FROM users WHERE email=?",

        (email,)

    )

    user = cursor.fetchone()

    conn.close()

    if user is None:

        return False, "User not found."

    if bcrypt.checkpw(

        password.encode(),

        user["password"].encode()

    ):

        return True, dict(user)

    return False, "Incorrect Password."


def get_prediction_history(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            sign_name,
            confidence,
            image_path,
            prediction_time
        FROM detection_history
        WHERE user_id=?
        ORDER BY id DESC
    """, (user_id,))

    data = cursor.fetchall()

    conn.close()

    return data


def delete_prediction(prediction_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM detection_history WHERE id=?",
        (prediction_id,)
    )

    conn.commit()
    conn.close()


def save_prediction(user_id, sign_name, confidence, image_path):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO detection_history(
            user_id,
            sign_name,
            confidence,
            image_path,
            prediction_time
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        user_id,
        sign_name,
        confidence,
        image_path,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()

def get_total_predictions(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM detection_history
        WHERE user_id=?
        """,
        (user_id,)
    )

    total = cursor.fetchone()[0]

    conn.close()

    return total


def get_today_predictions(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM detection_history
        WHERE user_id=?
        AND DATE(prediction_time)=DATE('now')
        """,
        (user_id,)
    )

    total = cursor.fetchone()[0]

    conn.close()

    return total


def get_average_confidence(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT AVG(confidence)
        FROM detection_history
        WHERE user_id=?
        """,
        (user_id,)
    )

    value = cursor.fetchone()[0]

    conn.close()

    if value is None:
        return 0

    return round(value * 100, 2)



def get_sign_distribution(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            sign_name,
            COUNT(*) as total
        FROM detection_history
        WHERE user_id=?
        GROUP BY sign_name
        ORDER BY total DESC
    """, (user_id,))

    data = cursor.fetchall()

    conn.close()

    return data

def get_recent_predictions(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            sign_name,
            confidence,
            prediction_time
        FROM detection_history
        WHERE user_id=?
        ORDER BY id DESC
        LIMIT 5
    """, (user_id,))

    data = cursor.fetchall()

    conn.close()

    return data