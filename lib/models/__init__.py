import sqlite3

CONN = sqlite3.connect('mountain_reviews.db')
CURSOR = CONN.cursor()