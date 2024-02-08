import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('news_articles.db')
cursor = conn.cursor()

class DatabaseError(Exception):
    pass

def store_article(title, content, publication_date, source_url):
    """
    Store an article in the database if it does not already exist.
    """
    try:
        cursor.execute('''
            INSERT INTO articles (title, content, publication_date, source_url)
            VALUES (?, ?, ?, ?)
        ''', (title, content, publication_date, source_url))
        conn.commit()
        print(f"Article '{title}' stored successfully.")
    except sqlite3.IntegrityError:
        # Ignore duplicate articles
        print(f"Article '{title}' already exists in the database. Skipping.")
    except Exception as e:
        raise DatabaseError(f"Error storing article '{title}': {e}")
