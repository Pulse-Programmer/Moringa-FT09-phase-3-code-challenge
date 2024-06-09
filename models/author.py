from database.connection import get_db_connection
class Author:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name
        self.save()

    def __repr__(self):
        return f'<Author {self.name}>'


    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        if isinstance(id, int):
            self._id = id
        else:
            raise TypeError("id must be of type int")

    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) and (hasattr(self, "name")==False):
            self._name = name
        else:
            raise TypeError("Name must be of type str and longer than 0 characters")
       
    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO authors (name) VALUES (?)', (self.name,))
        conn.commit()
        conn.close()
        
        self.id = cursor.lastrowid
        