from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        dojo = cls(results[0])
        for ninja_in_db in results:
            ninja_info = {
                "id" : ninja_in_db["ninjas.id"],
                "first_name" : ninja_in_db["first_name"],
                "last_name" : ninja_in_db["last_name"],
                "age" : ninja_in_db["age"],
                "created_at" : ninja_in_db["ninjas.created_at"],
                "updated_at" : ninja_in_db["ninjas.updated_at"]
            }
            dojo.ninjas.append(ninja_info)
        return dojo

    @classmethod
    def add_dojo(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s,  now(), now());"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)