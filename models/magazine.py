from database.connection import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()
class Magazine:
    
    all={}
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
        
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category):
            self._category = category
        else:
            raise TypeError("Category must be of type str and longer than 0 characters")
                            
                            
        
    def save(self):
        
        
        cursor.execute('INSERT INTO magazines (name, category) VALUES (?,?)', (self.name, self.category))
        conn.commit()
        conn.close()
        
        self.id = cursor.lastrowid
    

    @classmethod
    def instance_from_db(cls, row):
        """Return a magazine object having the attribute values from the table row."""

        # Check the dictionary for  existing instance using the row's primary key
        magazine = cls.all.get(row[0])
        if magazine:
            # ensure attributes match row values in case local instance was modified
            magazine.name = row[1]
            magazine.category = row[2]
            
        else:
            # not in dictionary, create new instance and add to dictionary
            magazine = cls(row[1], row[2])
            magazine.id = row[0]
            cls.all[magazine.id] = magazine
        return magazine
    
    def articles(self):
        """Returns all articles associated with a magazine"""
        
        from models.article import Article
        
        sql = """
        SELECT articles.id, articles.title, articles.content FROM articles
        INNER JOIN magazines
        ON articles.magazine_id = magazines.id
        WHERE magazines.id = ?
        """
        
        rows = cursor.execute(sql, (self.id,)).fetchall()
        
        return [Article.instance_from_db(row) for row in rows]
    
    def contributors(self):
        """Returns all authors associated with a magazine"""
        
        from models.author import Author
        
        sql = """
        SELECT authors.id, authors.name FROM authors
        INNER JOIN articles
        ON authors.id = articles.author_id
        INNER JOIN magazines
        ON articles.magazine_id = magazines.id
        WHERE magazines.id = ?
        """
        
        rows = cursor.execute(sql, (self.id,)).fetchall()
        
        return [Author.instance_from_db(row) for row in rows]