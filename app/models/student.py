from app import db

class Students(object):
    def __init__(self, id=None, avatar_url=None, id_number=None, first_name=None, last_name=None, course_id=None, year=None, gender=None):
        self.id = id
        self.avatar_url = avatar_url
        self.id_number = id_number
        self.first_name = first_name
        self.last_name = last_name
        self.course_id = course_id
        self.year = year
        self.gender = gender

    def all(keyword):
        cursor = db.cursor()
        query = f"SELECT students.id, students.avatar_url, students.id_number, students.first_name, students.last_name, courses.name, students.year, students.gender FROM students JOIN courses ON courses.id=students.course_id WHERE students.id_number LIKE '%{keyword}%' OR students.first_name LIKE '%{keyword}%' OR students.last_name LIKE '%{keyword}%' OR courses.name LIKE '%{keyword}%' OR students.year LIKE '%{keyword}%' OR students.gender LIKE '%{keyword}%'"
        cursor.execute(query)

        return cursor.fetchall()

    def add(self):
        cursor = db.cursor()
        query = f"INSERT INTO students(avatar_url, id_number, first_name, last_name, course_id, year, gender) VALUES('{self.avatar_url}', '{self.id_number}', '{self.first_name}', '{self.last_name}', '{self.course_id}', '{self.year}', '{self.gender}')"
        cursor.execute(query)
        db.commit()

    def edit(id):
        cursor = db.cursor()
        query = f"SELECT * FROM students WHERE id = {id}"
        cursor.execute(query)

        return cursor.fetchone()
    
    def update(id, avatar_url, id_number, first_name, last_name, course_id, year, gender):
        cursor = db.cursor()
        query = f"UPDATE students SET  avatar_url = '{avatar_url}', id_number = '{id_number}', first_name = '{first_name}', last_name = '{last_name}', course_id = {course_id}, year = '{year}', gender = '{gender}' WHERE id = {id}"
        cursor.execute(query)
        db.commit()

    def delete(id):
        cursor = db.cursor()
        query = f"DELETE from students WHERE id = {id}"
        cursor.execute(query)
        db.commit()

    def get_by_id(id):
        cursor = db.cursor()
        query = f"SELECT avatar_url FROM students WHERE id = %s"
        cursor.execute(query, (id,))
        return cursor.fetchone()