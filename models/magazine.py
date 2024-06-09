from database.connection import get_db_connection
class Magazine:
    def __init__(self, name, category, id=None):
        self.id = id
        self.name = name
        self.category = category
        self.save()

    def __repr__(self):
        return f'<Magazine {self.name}>'


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
        if isinstance(name, str) and (2<=len(name)<=16):
            self._name = name
        else:
            raise TypeError("Name must be of type str and longer than 0 characters")
        
        
        
    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('INSERT INTO magazines (name, category) VALUES (?,?)', (self.name, self.category))
        conn.commit()
        conn.close()
        
        self.id = cursor.lastrowid