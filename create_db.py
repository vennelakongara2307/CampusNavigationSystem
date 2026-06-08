import sqlite3

# Connect to database (creates file if it doesn't exist)
conn = sqlite3.connect('campus.db')
c = conn.cursor()

# Create buildings table
c.execute('''
CREATE TABLE IF NOT EXISTS buildings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    lat REAL,
    lon REAL,
    type TEXT
)
''')


# Create routes table
c.execute('''
CREATE TABLE IF NOT EXISTS routes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    from_building INTEGER NOT NULL,
    to_building INTEGER NOT NULL,
    distance REAL,
    FOREIGN KEY(from_building) REFERENCES buildings(id),
    FOREIGN KEY(to_building) REFERENCES buildings(id)
)
''')
c.execute('''
CREATE TABLE IF NOT EXISTS library (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_name TEXT,
    author TEXT,
    price REAL,
    year INTEGER
)
''')
conn.commit()
conn.close()
print("Database and tables created successfully!")
import sqlite3

conn = sqlite3.connect('campus.db')
c = conn.cursor()

# Sample buildings
#c.execute("INSERT INTO buildings (name, lat, lon, type) VALUES ('Library', 17.412, 80.418, 'Library')")
#c.execute("INSERT INTO buildings (name, lat, lon, type) VALUES ('CSE Dept', 17.413, 80.419, 'Lecture Hall')")
#c.execute("INSERT INTO buildings (name, lat, lon, type) VALUES ('Hostel', 17.414, 80.420, 'Hostel')")

# Sample routes
#c.execute("INSERT INTO routes (from_building, to_building, distance) VALUES (1, 2, 100)")
#c.execute("INSERT INTO routes (from_building, to_building, distance) VALUES (2, 3, 150)")

conn.commit()
conn.close()
print("Sample data inserted!")