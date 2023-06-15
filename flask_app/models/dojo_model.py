from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:

    DB = 'dojos_and_ninjas_schema'
    tables = 'dojos'

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = f"SELECT * FROM {cls.tables};"
        results = connectToMySQL(cls.DB).query_db(query)

        ninjas = []

        if results:
            for ninja in results:
                ninjas.append( cls(ninja) )

        return ninjas
    
    @classmethod
    def save(cls, data):
        query = f'INSERT INTO {cls.tables} (name) VALUES (%(name)s);'

        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def get_one(cls, id):
        query = f'SELECT * FROM {cls.tables} WHERE id = %(id)s;'
        data = {'id' : id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def update(cls, data):
        query = f'''UPDATE {cls.tables} SET name = %(name)s WHERE id = %(id)s;'''
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def delete(cls, id):
        query = f'DELETE FROM {cls.tables} WHERE id = %(id)s;'
        data = {'id' : id}
        return connectToMySQL(cls.DB).query_db(query, data)