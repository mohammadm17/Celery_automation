from celery import Celery
from classification_module import classify_category
from database_module import DatabaseError

# Define the Celery app
celery = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/1')


# Define Celery task for article classification
@celery.task
def classify_article(title, content):
    try:
        category = classify_category(content)
        return category
    except Exception as e:
        print(f"Error classifying article '{title}': {e}")
        return "Error"

