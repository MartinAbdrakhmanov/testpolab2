import sqlite3

def init_db():
    """Инициализация базы данных и создание таблиц."""
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        description TEXT,
                        completed BOOLEAN NOT NULL CHECK (completed IN (0, 1))
                    )''')
    conn.commit()
    conn.close()

def get_db_connection():
    """Подключение к базе данных."""
    conn = sqlite3.connect('tasks.db')
    conn.row_factory = sqlite3.Row
    return conn
