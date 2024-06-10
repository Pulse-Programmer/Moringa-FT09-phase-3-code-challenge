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
    # def test_author_init(self):
    #     author = Author(1, "John Doe")
    #     self.assertEqual(author.id, 1)
    #     self.assertEqual(author.name, "John Doe")

    def test_author_str_representation(self):
        author = Author(1, "John Doe")
        self.assertEqual(str(author), "<Author John Doe>")

    def test_author_equality(self):
        author1 = Author(1, "John Doe")
        author2 = Author(1, "John Doe")
        self.assertEqual(author1, author2)

    def test_author_inequality(self):
        author1 = Author(1, "John Doe")
        author2 = Author(2, "Jane Doe")
        self.assertNotEqual(author1, author2)

class TestMagazine(unittest.TestCase):
    # def test_magazine_init(self):
    #     magazine = Magazine(1, "Tech Monthly", "Technology")
    #     self.assertEqual(magazine.id, 1)
    #     self.assertEqual(magazine.name, "Tech Monthly")
    #     self.assertEqual(magazine.category, "Technology")

    def test_magazine_str_representation(self):
        magazine = Magazine(1, "Tech Monthly", "Technology")
        self.assertEqual(str(magazine), "<Magazine Tech Monthly>")

    def test_magazine_equality(self):
        magazine1 = Magazine(1, "Tech Monthly", "Technology")
        magazine2 = Magazine(1, "Tech Monthly", "Technology")
        self.assertEqual(magazine1, magazine2)

    def test_magazine_inequality(self):
        magazine1 = Magazine(1, "Tech Monthly", "Technology")
        magazine2 = Magazine(2, "Fashion Weekly", "Fashion")
        self.assertNotEqual(magazine1, magazine2)

class TestArticle(unittest.TestCase):
    # def test_article_init(self):
    #     article = Article(1, "Test Article", "This is a test article", 1, 1)
    #     self.assertEqual(article.id, 1)
    #     self.assertEqual(article.title, "Test Article")
    #     self.assertEqual(article.content, "This is a test article")
    #     self.assertEqual(article.author_id, 1)
    #     self.assertEqual(article.magazine_id, 1)

    def test_article_str_representation(self):
        article = Article(1, "Test Article", "This is a test article", 1, 1)
        self.assertEqual(str(article), "<Article Test Article>")

    def test_article_equality(self):
        article1 = Article(1, "Test Article", "This is a test article", 1, 1)
        article2 = Article(1, "Test Article", "This is a test article", 1, 1)
        self.assertEqual(article1, article2)

    def test_article_inequality(self):
        article1 = Article(1, "Test Article", "This is a test article", 1, 1)
        article2 = Article(2, "Another Article", "This is another article", 2, 2)
        self.assertNotEqual(article1, article2)

if __name__ == "__main__":
    unittest.main()
