from database.setup import create_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def main():
    # Initialize the database and create tables
    create_tables()

    # Collect user input
    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title: ")
    article_content = input("Enter article content: ")

    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()


    '''
        The following is just for testing purposes, 
        you can modify it to meet the requirements of your implmentation.
    '''

    # Create an author
    cursor.execute('INSERT INTO authors (name) VALUES (?)', (author_name,))
    author_id = cursor.lastrowid # Use this to fetch the id of the newly created author

    # Create a magazine
    cursor.execute('INSERT INTO magazines (name, category) VALUES (?,?)', (magazine_name, magazine_category))
    magazine_id = cursor.lastrowid # Use this to fetch the id of the newly created magazine

    # Create an article
    cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
                   (article_title, article_content, author_id, magazine_id))

    # Commit the changes

    conn.commit()

    # Query the database for inserted records. 
    # The following fetch functionality should probably be in their respective models

    cursor.execute('SELECT * FROM magazines')
    magazines = cursor.fetchall()

    cursor.execute('SELECT * FROM authors')
    authors = cursor.fetchall()

    cursor.execute('SELECT * FROM articles')
    articles = cursor.fetchall()

    conn.close()

    # Display results
    print("\nMagazines:")
    for magazine in magazines:
        if magazine[0] and magazine[1] and magazine[2]:
            print(Magazine(magazine[0], magazine[1], magazine[2]))  
            
            print("\n Aggregate methods:")
            mag1 = Magazine(magazine[0], magazine[1], magazine[2])
            print("Titles of all articles: ",mag1.article_titles())
            print("Authors with more than two articles: ",mag1.contributing_authors())

    print("\nAuthors:")
    for author in authors:
        if author[0] and author[1]:
            print(Author(author[0], author[1]))  

    print("\nArticles:")
    for article in articles:
        if article[0] and article[1] and article[2] and article[3] and article[4]:
            print(Article(article[0], article[1], article[2], article[3], article[4]))

   

if __name__ == "__main__":
    main()
    
    
    
    
