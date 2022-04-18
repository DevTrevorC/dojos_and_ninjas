from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = ['id']
        self.first_name = ['first_name']
        self.last_name = ['last_name']
        self.age = ['age']
        self.created_at = ['created_at']
        self.updated_at = ['updated_at']
        self.dojo_id = ['dojo_id']

    @classmethod
    def get_ninjas(cls, id):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, id)

    @classmethod
    def add_ninja(cls, data, id):
        query = "INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id VALUES (%(first_name)s, %(last_name)s, %(age)s, now(), now(), %(id)s"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data, id)