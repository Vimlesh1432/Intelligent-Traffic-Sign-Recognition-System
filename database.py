import sqlite3
from datetime import datetime

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

    # ================= PREDICTION HISTORY =================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS detection_history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sign_name TEXT NOT NULL,
        confidence REAL NOT NULL,
        image_path TEXT NOT NULL,
        prediction_time TEXT NOT NULL
    )
    """)

    # Migration: purani DB (auth wali) me user_id column ho toh usko
    # data ke saath nayi clean table me convert karo
    columns = [row[1] for row in cursor.execute(
        "PRAGMA table_info(detection_history)"
    ).fetchall()]

    if "user_id" in columns:
        cursor.execute("DROP TABLE IF EXISTS detection_history_old")
        cursor.execute("ALTER TABLE detection_history RENAME TO detection_history_old")
        cursor.execute("""
            CREATE TABLE detection_history(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sign_name TEXT NOT NULL,
                confidence REAL NOT NULL,
                image_path TEXT NOT NULL,
                prediction_time TEXT NOT NULL
            )
        """)
        cursor.execute("""
            INSERT INTO detection_history (id, sign_name, confidence, image_path, prediction_time)
            SELECT id, sign_name, confidence, image_path, prediction_time
            FROM detection_history_old
        """)
        cursor.execute("DROP TABLE detection_history_old")

    conn.commit()
    conn.close()


def get_prediction_history():

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
        ORDER BY id DESC
    """)

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


def clear_all_history():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM detection_history")

    conn.commit()
    conn.close()


def save_prediction(sign_name, confidence, image_path):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO detection_history(
            sign_name,
            confidence,
            image_path,
            prediction_time
        )
        VALUES (?, ?, ?, ?)
    """, (
        sign_name,
        confidence,
        image_path,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()


def get_total_predictions():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM detection_history
        """
    )

    total = cursor.fetchone()[0]

    conn.close()

    return total


def get_today_predictions():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM detection_history
        WHERE DATE(prediction_time)=DATE('now')
        """
    )

    total = cursor.fetchone()[0]

    conn.close()

    return total


def get_average_confidence():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT AVG(confidence)
        FROM detection_history
        """
    )

    value = cursor.fetchone()[0]

    conn.close()

    if value is None:
        return 0

    return round(value * 100, 2)


def get_sign_distribution():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            sign_name,
            COUNT(*) as total
        FROM detection_history
        GROUP BY sign_name
        ORDER BY total DESC
    """)

    data = cursor.fetchall()

    conn.close()

    return data


def get_recent_predictions(limit=5):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            sign_name,
            confidence,
            prediction_time
        FROM detection_history
        ORDER BY id DESC
        LIMIT ?
    """, (limit,))

    data = cursor.fetchall()

    conn.close()

    return data


def get_weekly_predictions():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            DATE(prediction_time),
            COUNT(*)
        FROM detection_history
        GROUP BY DATE(prediction_time)
        ORDER BY DATE(prediction_time) DESC
        LIMIT 7
    """)

    data = cursor.fetchall()

    conn.close()

    return data


def get_top_signs(limit=5):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            sign_name,
            COUNT(*) AS count
        FROM detection_history
        GROUP BY sign_name
        ORDER BY count DESC
        LIMIT ?
    """, (limit,))

    data = cursor.fetchall()

    conn.close()

    return data


def get_best_prediction():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            sign_name,
            confidence,
            prediction_time
        FROM detection_history
        ORDER BY confidence DESC
        LIMIT 1
    """)

    data = cursor.fetchone()

    conn.close()

    return data