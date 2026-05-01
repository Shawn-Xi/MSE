from database import create_connection
import sqlite3


def add_student(name, age, gender):
    """Adds a new student to the student table."""
    sql = "INSERT INTO student (name, age, gender) VALUES (?, ?, ?)"
    with create_connection() as conn:
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (name, age, gender))
            conn.commit()
            print("✅ Student added successfully.")
        except sqlite3.Error as e:
            print(f"❌ Database error: {e}")


def view_students():
    """Retrieves all students from the student table."""
    sql = "SELECT * FROM student"
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()


def search_student(name):
    """Searches for students by name."""
    sql = "SELECT * FROM student WHERE name LIKE ?"
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(sql, ('%' + name + '%',))
        return cursor.fetchall()


def delete_student(student_id):
    """Deletes a student from the student table by their ID."""
    sql = "DELETE FROM student WHERE id = ?"
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(sql, (student_id,))
        conn.commit()
        print("🗑️ Student deleted.")
