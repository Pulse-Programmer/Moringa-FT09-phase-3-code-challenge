from database.connection import get_db_connection
from models.author import Author
from models.magazine import Magazine

conn = get_db_connection()
cursor = conn.cursor()
class Article:
    
    all = {}
    def __init__(self, id=None, title="title", content="content", author_id=1, magazine_id=1):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id
        self.save()

    def __repr__(self):
        return f'<Article {self.title}>'


    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Article):
            return False
        return (self.id == value.id and self.title == value.title and self.content == value.content and self.author_id == value.author_id and self.magazine_id == value.magazine_id)
    
    def __hash__(self) -> int:
        return hash((self.id, self.title, self.content, self.author_id, self.magazine_id))
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and (5<=len(title)<=50) and (hasattr(self, "title")==False):
            self._title = title
        else:
            raise TypeError("Title must be of type str and longer than 0 characters")
    
    
    
    def save(self):
        
        cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?,?,?,?)', (self.title, self.content, self.author_id, self.magazine_id))
        conn.commit()
        
        self.id = cursor.lastrowid
        
        
    def author(self):
        
        sql = """
        SELECT authors.id, authors.name FROM authors
        INNER JOIN articles
        ON authors.id = articles.author_id
        WHERE authors.id = ?
        """
        
        row = cursor.execute(sql, (self.author_id,)).fetchone()
        
        return Author.instance_from_db(row)
    
    
    def magazine(self):
        
        sql = """
        SELECT magazines.* FROM magazines
        INNER JOIN articles
        ON magazines.id = articles.magazine_id
        WHERE magazines.id = ?
        """
        
        row = cursor.execute(sql, (self.magazine_id,)).fetchone()
        
        return Magazine.instance_from_db(row)
    
    
    
    @classmethod
    def instance_from_db(cls, row):
        """Return an article object having the attribute values from the table row."""

        # Check the dictionary for  existing instance using the row's primary key
        article = cls.all.get(row[0])
        if article:
            # ensure attributes match row values in case local instance was modified
            article.title = row[1]
            article.content = row[2]
            article.author_id = row[3]
            article.magazine_id = row[4]
        else:
            # not in dictionary, create new instance and add to dictionary
            article = cls(row[1], row[2], row[3], row[4])
            article.id = row[0]
            cls.all[article.id] = article
        return article