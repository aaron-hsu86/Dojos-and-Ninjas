from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    
    DB = 'dojos_and_ninjas_schema'
    table = 'ninjas'

    def __init__(self, data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    @classmethod
    def get_all(cls):
        query = f"SELECT * FROM {cls.table};"
        results = connectToMySQL(cls.DB).query_db(query)

        ninjas = []

        if results:
            for ninja in results:
                ninjas.append( cls(ninja) )

        return ninjas
    
    @classmethod
    def save(cls, data):
        query = f'''INSERT INTO {cls.table} (first_name, last_name, dojo_id) 
                VALUES ( %(first_name)s , %(last_name)s , %(dojo_id)s );'''

        return connectToMySQL(cls.DB).query_db(query, data)
    
    # only grabs identified student info
    @classmethod
    def get_one(cls, id):
        query = f'SELECT * FROM {cls.table} WHERE id = %(id)s;'
        data = {'id' : id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])
    
    
    @classmethod
    def get_dojo_class(cls, id):
        query = f'SELECT * FROM {cls.table} WHERE dojo_id = %(id)s;'
        data = {'id' : id}
        results = connectToMySQL(cls.DB).query_db(query, data)

        ninjas = []

        if results:
            for ninja in results:
                ninjas.append( cls(ninja) )
        return ninjas

    @classmethod
    def update(cls, data):
        query = f'''UPDATE {cls.table} SET name = %(name)s WHERE id = %(id)s;'''
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def delete(cls, id):
        query = f'DELETE FROM {cls.table} WHERE id = %(id)s;'
        data = {'id' : id}
        return connectToMySQL(cls.DB).query_db(query, data)