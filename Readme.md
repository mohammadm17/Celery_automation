Celery Automation Task: Website Data Extraction and Classification
Overview

This project automates the process of extracting data from a website's RSS feed, storing it in a SQL database, and classifying it into categories using NLTK (Natural Language Toolkit) within a Celery task.
Features

    Data Extraction: Utilizes FeedParser to parse the RSS feed of a specified website and extract relevant data.
    Database Integration: Stores the extracted data in a SQL database for future analysis and reference.
    Classification: Applies Natural Language Processing (NLP) techniques using NLTK to classify the extracted data into predefined categories.
    Celery Task: Implements Celery, a distributed task queue, for efficient and asynchronous processing of tasks.

Requirements

    Python 3.11
    Celery
    NLTK
    SQL Database (e.g., SQLite, MySQL, PostgreSQL)
    FeedParser

Installation

    Clone the repository:

    bash

git clone https://github.com/mohammadm17/Celery_automation.git
cd celery-automation-task

Install the required dependencies:

bash

    pip install -r requirements.txt

    Set up your SQL database and configure the database connection in config.py.

Usage

    Start the Celery worker:

    bash

celery -A tasks worker --loglevel=info

Run the main script to initiate the data extraction and classification process:

bash

    python main.py

Configuration

    Modify the config.py file to specify database connection details and other configuration parameters.
    Adjust the Celery settings in celeryconfig.py as needed for your environment.

Contributing

Contributions are welcome! Feel free to submit bug reports, feature requests, or pull requests.
License

This project is licensed under the MIT License.
Acknowledgments

    Thanks to the developers of Celery, NLTK, FeedParser, and other open-source libraries used in this project.