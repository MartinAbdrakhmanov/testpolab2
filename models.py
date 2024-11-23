from database import get_db_connection

def add_task(title, description):
    """Добавить новую задачу в базу данных."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (title, description, completed) VALUES (?, ?, ?)', 
                   (title, description, 0))
    conn.commit()
    conn.close()

def get_tasks():
    """Получить все задачи из базы данных."""
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return tasks

def update_task(id, title, description, completed):
    """Обновить задачу в базе данных."""
    conn = get_db_connection()
    conn.execute('UPDATE tasks SET title = ?, description = ?, completed = ? WHERE id = ?',
                 (title, description, completed, id))
    conn.commit()
    conn.close()

def delete_task(id):
    """Удалить задачу из базы данных."""
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE id = ?', (id,))
    conn.commit()
    conn.close()

def mark_task_as_completed(id):
    """Пометить задачу как выполненную."""
    conn = get_db_connection()
    conn.execute('UPDATE tasks SET completed = 1 WHERE id = ?', (id,))
    conn.commit()
    conn.close()
