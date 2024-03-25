from models.mountain import Mountain
from models.review import Review

from models.__init__ import CONN, CURSOR

if __name__ == "__main__":
    Mountain.create_table()
    Review.create_table()

    CURSOR.execute("DELETE FROM mountains")
    CURSOR.execute("DELETE FROM reviews")
    CONN.commit()

    Mountain.create("Mt. Elbert")
    Mountain.create("Mt. Massive")
    Mountain.create("Mt. Harvard")

    Review.create(5, "Best trip ever!", 1)
    Review.create(4, "Pretty good views!", 2)
    Review.create(5, "Mt. Harvard is the best mountain!", 3)
    Review.create(3, "Not as good as the last time.", 1)