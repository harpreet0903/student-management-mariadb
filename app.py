from flask import Flask, render_template, request, redirect
import mariadb

app = Flask(__name__)


DB_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "YOUR_MARIADB_PASSWORD",
    "database": "college_db"
}

def get_connection():
    return mariadb.connect(**DB_CONFIG)

@app.route("/")
def index():
    search = request.args.get("search", "")

    conn = get_connection()
    cursor = conn.cursor()

    if search:
        cursor.execute("""
            SELECT student_id, name, course, marks, city
            FROM students
            WHERE name LIKE ? OR course LIKE ? OR city LIKE ?
            ORDER BY student_id
        """, (f"%{search}%", f"%{search}%", f"%{search}%"))
    else:
        cursor.execute("""
            SELECT student_id, name, course, marks, city
            FROM students
            ORDER BY student_id
        """)

    students = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template("index.html", students=students, search=search)


@app.route("/add", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        name = request.form["name"]
        course = request.form["course"]
        marks = request.form["marks"]
        city = request.form["city"]

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO students (name, course, marks, city)
            VALUES (?, ?, ?, ?)
        """, (name, course, marks, city))

        conn.commit()
        cursor.close()
        conn.close()

        return redirect("/")

    return render_template("student_form.html", student=None, title="Add Student")


@app.route("/edit/<int:student_id>", methods=["GET", "POST"])
def edit_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    if request.method == "POST":
        name = request.form["name"]
        course = request.form["course"]
        marks = request.form["marks"]
        city = request.form["city"]

        cursor.execute("""
            UPDATE students
            SET name = ?, course = ?, marks = ?, city = ?
            WHERE student_id = ?
        """, (name, course, marks, city, student_id))

        conn.commit()
        cursor.close()
        conn.close()

        return redirect("/")

    cursor.execute("""
        SELECT student_id, name, course, marks, city
        FROM students
        WHERE student_id = ?
    """, (student_id,))

    student = cursor.fetchone()

    cursor.close()
    conn.close()

    return render_template("student_form.html", student=student, title="Edit Student")


@app.route("/delete/<int:student_id>")
def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE student_id = ?",
        (student_id,)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
