import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine

class TestModels(unittest.TestCase):
    def test_author_creation(self):
        author = Author(1, "John Doe")
        self.assertEqual(author.name, "John Doe")

    def test_article_creation(self):
        article = Article(1, "Test Title", "Test Content", 1, 1)
        self.assertEqual(article.title, "Test Title")

    def test_magazine_creation(self):
        magazine = Magazine(1, "Tech Weekly")
        self.assertEqual(magazine.name, "Tech Weekly")

class TestAuthor(unittest.TestCase):

    def test_author_str_representation(self):
        author = Author(1, "John Doe")
        self.assertEqual(str(author), "<Author John Doe>")

    

    def test_author_inequality(self):
        author1 = Author(1, "John Doe")
        author2 = Author(2, "Jane Doe")
        self.assertNotEqual(author1, author2)

class TestMagazine(unittest.TestCase):

    def test_magazine_str_representation(self):
        magazine = Magazine(1, "Tech Monthly", "Technology")
        self.assertEqual(str(magazine), "<Magazine Tech Monthly>")

    
    def test_magazine_inequality(self):
        magazine1 = Magazine(1, "Tech Monthly", "Technology")
        magazine2 = Magazine(2, "Fashion Weekly", "Fashion")
        self.assertNotEqual(magazine1, magazine2)
    
    def test_article_titles_multiple_articles(self):
        # Arrange: Create Magazine, Articles, and Authors instances
        magazine = Magazine(1, "Test Magazine", "Test Category")
        author1 = Author(1, "Author 1")
        author2 = Author(2, "Author 2")
        article1 = Article(1, "Article 1", "Content 1", author1.id, magazine.id)
        article2 = Article(2, "Article 2", "Content 2", author2.id, magazine.id)
        article3 = Article(3, "Article 3", "Content 3", author1.id, magazine.id)

        # Act: Call the article_titles method
        result = magazine.article_titles()

        # Assert: Verify that the method returns a list of titles for multiple articles
        self.assertEqual(result, ["Article 1", "Article 2", "Article 3"])
        
    
    
class TestArticle(unittest.TestCase):

    def test_article_str_representation(self):
        article = Article(1, "Test Article", "This is a test article", 1, 1)
        self.assertEqual(str(article), "<Article Test Article>")


    def test_article_inequality(self):
        article1 = Article(1, "Test Article", "This is a test article", 1, 1)
        article2 = Article(2, "Another Article", "This is another article", 2, 2)
        self.assertNotEqual(article1, article2)
        
    def test_article_titles_no_articles(self):
        # Arrange: Create a Magazine instance
        magazine = Magazine(1, "Test Magazine", "Test Category")

        # Act: Call the article_titles method
        result = magazine.article_titles()

        # Assert: Verify that the method returns None when no articles are associated with the magazine
        self.assertIsNone(result)
        
        
if __name__ == "__main__":
    unittest.main()
