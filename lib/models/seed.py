from models.mountain import Mountain
from models.review import Review

from models.__init__ import CONN, CURSOR

if __name__ == "__main__":
    Mountain.create_table()
    Review.create_table()

    CURSOR.execute("DELETE FROM mountains")
    CURSOR.execute("DELETE FROM reviews")
    CONN.commit()

