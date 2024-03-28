from models.__init__ import CONN, CURSOR

class Mountain:

    all = []
    
    def __init__(self, name, elevation, location):
        self.name = name
        self.elevation = elevation
        self.location = location
        self.id = None

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name_parameter):
        if(isinstance(name_parameter, str)) and (3 <= len(name_parameter) <= 25):
            self._name = name_parameter
        else:
            raise ValueError("Name must be between 3 and 25 characters!")

    @property
    def elevation(self):
        return self._elevation
    
    @elevation.setter
    def elevation(self, elevation_parameter):
        if isinstance(elevation_parameter, int):
            self._elevation = elevation_parameter
        else:
            raise ValueError("Elevation must be a number!")

    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, location_parameter):
        if isinstance(location_parameter, str):
            self._location = location_parameter
        else:
            raise ValueError("Location must be a string!")

    def __repr__(self):
        return f"<Mountain {self.id}: Name = {self.name}, Elevation = {self.elevation}, Location = {self.location}>"
    
    # add new ORM methods after existing methods

    @classmethod
    def create_table(cls):
        # Create a new table to persist the attributes of Mountain instances
        sql = """
            CREATE TABLE IF NOT EXISTS mountains (
            id INTEGER PRIMARY KEY,
            name TEXT,
            elevation INTEGER,
            location TEXT)
        """
        CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        # Drop the table that persists Hotel instances
        sql = """
            DROP TABLE IF EXISTS mountains;
        """
        CURSOR.execute(sql)

    def save(self):
        # Insert a new row with the attributes of the current Mountain instance.
        # Update object id attribute using the primary key value of new row.
        sql = """
            INSERT INTO mountains (name, elevation, location)
            VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.elevation, self.location))
        CONN.commit()

        self.id = CURSOR.lastrowid

        Mountain.all.append(self)

    @classmethod
    def create(cls, name, elevation, location):
        # Initialize a new Mountain instance and save the object to the database
        mountain = cls(name, elevation, location)
        mountain.save()
        return mountain
    
    @classmethod
    def instance_from_db(cls, row):
        # Return a Mountain object having the attribute values from the table row.
        mountain = cls(row[1], row[2], row[3])
        mountain.id = row[0]
        return mountain

    @classmethod
    def get_all(cls):
        # Return a list containing a Mountain object per row in the table
        sql = """
            SELECT id, name, elevation, location
            FROM mountains
        """

        rows = CURSOR.execute(sql).fetchall()

        cls.all = [cls.instance_from_db(row) for row in rows]
        return cls.all
    
    @classmethod
    def find_by_id(cls, id):
        # Return a Mountain object corresponding to the table row matching the specified primary key
        sql = """
            SELECT *
            FROM mountains
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()

        if row:
            return cls.instance_from_db(row)
        else:
            return None
        
    def update(self):
        # Update the table row corresponding to the current Mountain instance.
        sql = """
            UPDATE mountains
            SET name = ?, elevation = ?, location = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.elevation, self.location, self.id))
        CONN.commit()

    def delete(self):
        # Delete the table row corresponding to the current Mountain instance and remove it from the all class variable
        sql = """
            DELETE FROM mountains
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Remove the instance from the all class variable
        Mountain.all = [mountain for mountain in Mountain.all if mountain.id != self.id]

    def reviews(self):
        # One-to-many relationship: One Mountain has many Reviews
        from models.review import Review

        sql = """
            SELECT *
            FROM reviews
            WHERE reviews.mountain_id = ?
        """

        rows = CURSOR.execute(sql, (self.id,)).fetchall()

        return [Review.instance_from_db(row) for row in rows]