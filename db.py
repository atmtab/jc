import sqlite3 as sq


class db:
    # через кавычки при объявлении объявляешь бд, которую будем использовать
    def __init__(self, db):
        self.con = sq.connect(db)
        self.cursor = self.con.cursor()

    # это чтобы показать дз
    def show_homework(self, group_id):
        self.cursor.execute("SELECT hw_text FROM homework WHERE group_id =?", (group_id,))
        return self.cursor.fetchall()

    # это чтобы показать ОС
    def show_feedback(self, group_id, student_id):
        self.cursor.execute("SELECT fb_text FROM feedback WHERE group_id =? AND student_id =?", (group_id, student_id,))
        return self.cursor.fetchall()

    # это используй чтобы получить список филиалов для вывода
    def get_branches(self):
        self.cursor.execute("SELECT DISTINCT branch_name FROM groups")
        return self.cursor.fetchall()

    # это используй чтобы получить список групп для вывода
    def get_groups_list(self, branch_id):
        self.cursor.execute("SELECT name FROM groups WHERE branch =?", (branch_id,))
        return self.cursor.fetchall()

    # это используй чтобы получить список учеников для вывода
    def get_students_list(self, group_id):
        self.cursor.execute("SELECT name FROM students WHERE group_id =?", (group_id,))
        return self.cursor.fetchall()

    def add_student(self, id, student):
        self.cursor.execute("INSERT INTO students (id, name) VALUES (?,?)", (id, student))


def tolistview(arr):
    arr2 = []
    for i in arr:
        temp = ''.join(i)
        arr2.append(temp)
    return arr2