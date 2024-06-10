from database.connection import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()
class Author:
    
    all = {}
    def __init__(self, id=None, name="author_name"):
        self.id = id
        self.name = name
        self.save()

    def __repr__(self):
        return f'<Author {self.name}>'

    
    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Author):
            return False
        return self.id == value.id and self.name == value.name
    
    
    def __hash__(self) -> int:
        return hash((self.id, self.name))
    
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
        
        cursor.execute('INSERT INTO authors (name) VALUES (?)', (self.name,))
        conn.commit()
        
        self.id = cursor.lastrowid
        
        
    @classmethod
    def instance_from_db(cls, row):
        """Return an author object having the attribute values from the table row."""

        # Check the dictionary for  existing instance using the row's primary key
        author = cls.all.get(row[0])
        if author:
            # ensure attributes match row values in case local instance was modified
            author.name = row[1]
            
        else:
            # not in dictionary, create new instance and add to dictionary
            author = cls(row[1])
            author.id = row[0]
            cls.all[author.id] = author
        return author
        
        
    def articles(self):
        """Returns all articles associated with an author"""
        from models.article import Article
        
        sql = """
        SELECT * FROM articles
        WHERE author_id = ?
        """
        
        rows = cursor.execute(sql, (self.id,)).fetchall()
        
        return [Article.instance_from_db(row) for row in rows]
    
    def magazines(self):
        """Returns all magazines associated with an author"""
        
        from models.magazine import Magazine
        
        sql = """
        SELECT magazines.id, magazines.name, magazines.category FROM magazines
        INNER JOIN articles
        ON magazines.id = articles.magazine_id
        INNER JOIN authors
        ON articles.author_id = authors.id
        WHERE authors.id = ?
        """
        
        rows = cursor.execute(sql, (self.id,)).fetchall()
        
        return [Magazine.instance_from_db(row) for row in rows]
    
    