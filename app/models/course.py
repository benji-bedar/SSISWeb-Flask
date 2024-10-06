from app import db

class Courses(object):
    def __init__(self, id=None, name=None, code=None, college_id=None):
        self.id = id
        self.name = name
        self.code = code
        self.college_id = college_id

    def all(keyword):
        cursor = db.cursor()
        query = f"SELECT courses.id, courses.name, courses.code, colleges.name FROM courses JOIN colleges ON colleges.id=courses.college_id WHERE courses.name LIKE '%{keyword}%' OR courses.code LIKE '%{keyword}%' OR colleges.name LIKE '%{keyword}%'"
        cursor.execute(query)

        return cursor.fetchall()
    
    def add(self):
        cursor = db.cursor()
        query = f"INSERT INTO courses (name, code, college_id) VALUES ('{self.name}', '{self.code}', '{self.college_id}')"
        cursor.execute(query)
        db.commit()

    def edit(id):
        cursor = db.cursor()
        query = f"SELECT * FROM courses WHERE id = {id}"
        cursor.execute(query)

        return cursor.fetchone()

    def update(id, code, name, college_id):
        cursor = db.cursor()
        query = f"UPDATE courses SET code = '{code}', name = '{name}', college_id = {college_id} WHERE id = {id}"
        cursor.execute(query)
        db.commit()

    def delete(id):
        cursor = db.cursor()
        query = f"DELETE FROM courses WHERE id = {id}"
        cursor.execute(query)
        db.commit()
