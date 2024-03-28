from models.__init__ import CONN, CURSOR

class Review:

    all = []
    
    def __init__(self, rating, text, mountain_id):
        self.rating = rating
        self.text = text
        self.mountain_id = mountain_id
        self.id = None

    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, rating_parameter):
        if isinstance(rating_parameter, int) and 1 <= rating_parameter <= 10:
            self._rating = rating_parameter
        else:
            raise ValueError("Rating must be an integer between 1 and 10!")

    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, text_parameter):
        if(isinstance(text_parameter, str)) and (3 <= len(text_parameter) <= 80):
            self._text = text_parameter
        else:
            raise ValueError("Text must be a string between 3 and 80 characters long!")

    @property
    def mountain_id(self):
        return self._mountain_id
    
    @mountain_id.setter
    def mountain_id(self, mountain_id_parameter):
        if isinstance(mountain_id_parameter, int):
            self._mountain_id = mountain_id_parameter
        else:
            raise ValueError("Mountain ID must be an integer!")

    def __repr__(self):
        return f"<Review {self.id}: Mountain ID #{self.mountain_id}, {self.text}, Rating = {self.rating}>\n"

    # add new ORM methods after existing methods

    @classmethod
    def create_table(cls):
        # Create a new table to persist the attributes of Review instances
        sql = """
            CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY,
            rating INTEGER,
            text TEXT,
            mountain_id INTEGER)
        """
        CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        # Drop the table that persists Review instances
        sql = """
            DROP TABLE IF EXISTS reviews;
        """
        CURSOR.execute(sql)

    def save(self):
        # Insert a new row with the name value of the current Review instance.
        # Update object id attribute using the primary key value of new row.
        sql = """
            INSERT INTO reviews (rating, text, mountain_id)
            VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.rating, self.text, self.mountain_id))
        CONN.commit()

        self.id = CURSOR.lastrowid

        Review.all.append(self)

    @classmethod
    def create(cls, rating, text, mountain_id):
        # Initialize a new Review instance and save the object to the database
        review = cls(rating, text, mountain_id)
        review.save()
        return review
    
    @classmethod
    def instance_from_db(cls, row):
        # Return a Review object having the attribute values from the table row.
        review = cls(row[1], row[2], row[3])
        review.id = row[0]
        return review
    
    @classmethod
    def get_all(cls):
        # Return a list containing a Review object per row in the table
        sql = """
            SELECT *
            FROM reviews
        """

        rows = CURSOR.execute(sql).fetchall()

        cls.all = [cls.instance_from_db(row) for row in rows]
        return cls.all
    
    @classmethod
    def find_by_id(cls, id):
        # Return a Review object corresponding to the table row matching the specified primary key
        sql = """
            SELECT *
            FROM reviews
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()

        if row:
            return cls.instance_from_db(row)
        else:
            return None
        
    def update(self):
        # Update the table row corresponding to the current Review instance.
        sql = """
            UPDATE reviews
            SET mountain_id = ?, text = ?, rating = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.mountain_id, self.text, self.rating, self.id))
        CONN.commit()

    def delete(self):
        # Delete the table row corresponding to the current Review instance and remove it from the all class variable
        sql = """
            DELETE FROM reviews
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Remove the instance from the all class variable
        Review.all = [review for review in Review.all if review.id != self.id]
    
    def mountain(self):
        # Belongs to: A Review belongs to a Mountain
        from models.mountain import Mountain

        sql = """
            SELECT mountains.id, mountains.name
            FROM mountains
            INNER JOIN reviews
            ON mountains.id = reviews.mountain_id
            WHERE reviews.mountain_id = ?
        """

        row = CURSOR.execute(sql, (self.mountain_id,)).fetchone()
        
        if row:
            return Mountain.instance_from_db(row)
        else:
            return None