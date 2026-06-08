from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('campus.db')
    c = conn.cursor()

    # Buildings table
    c.execute("""
    CREATE TABLE IF NOT EXISTS buildings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        lat REAL,
        lon REAL,
        type TEXT
    )
    """)

    # Library table
    c.execute("""
    CREATE TABLE IF NOT EXISTS library (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_name TEXT,
        author TEXT,
        price REAL,
        year INTEGER
    )
    """)

    conn.commit()
    conn.close()

# ---------- FUNCTIONS ----------
def get_buildings():
    conn = sqlite3.connect('campus.db')
    c = conn.cursor()
    c.execute("SELECT * FROM buildings")
    data = c.fetchall()
    conn.close()
    return data


# ---------- ROUTES ----------

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/map')
def map_page():
    buildings = get_buildings()
    return render_template('map.html', buildings=buildings)


@app.route('/route')
def route_page():
    buildings = get_buildings()
    return render_template('route.html', buildings=buildings)
@app.route('/add_building', methods=['GET', 'POST'])
def add_building():
    message = ""

    if request.method == 'POST':
        name = request.form['name']
        lat = request.form['lat']
        lon = request.form['lon']
        type = request.form['type']
        print(name,type,lat,lon)
        conn = sqlite3.connect('campus.db')
        c = conn.cursor()

        c.execute("INSERT INTO buildings (name, lat, lon,type) VALUES (?, ?, ?, ?)",
                  (name, lat, lon,type))

        conn.commit()
        conn.close()

        message = "Building added successfully!"
    

    return render_template('add_building.html', message=message)
@app.route('/delete/<int:id>')
def delete_building(id):
    import sqlite3

    conn = sqlite3.connect('campus.db')
    c = conn.cursor()

    # Delete building using ID
    c.execute("DELETE FROM buildings WHERE id = ?", (id,))

    conn.commit()
    conn.close()

    return redirect('/map')
def get_books():
    conn = sqlite3.connect('campus.db')
    c = conn.cursor()
    c.execute("SELECT * FROM library")
    data = c.fetchall()
    conn.close()
    return data
        

# existing routes above...

@app.route('/library')
def library_page():
    books = get_books()
    return render_template('library.html', books=books)
@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        book_name = request.form['book_name']
        author = request.form['author']
        price = request.form['price']
        year = request.form['year']

        conn = sqlite3.connect('campus.db')
        c = conn.cursor()

        c.execute("INSERT INTO library (book_name, author, price, year) VALUES (?, ?, ?, ?)",
                  (book_name, author, price, year))

        conn.commit()
        conn.close()

        return redirect('/library')

    return render_template('add_book.html')

# ✅ ADD SEARCH ROUTE HERE
@app.route('/search_book', methods=['GET','POST'])
def search_book():
    if request.method == 'POST':
        name = request.form['book_name']

        conn = sqlite3.connect('campus.db')
        c = conn.cursor()
        c.execute("""
        SELECT * FROM library 
        WHERE book_name LIKE ? OR author LIKE ?
        """, ('%'+name+'%', '%'+name+'%'))
        data = c.fetchall()
        conn.close()

        return render_template('library.html', books=data)

    return render_template('search_book.html')
@app.route('/delete_book/<int:id>')
def delete_book(id):
    conn = sqlite3.connect('campus.db')
    c = conn.cursor()
    c.execute("DELETE FROM library WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return redirect('/library')

# ---------- RUN APP ----------
if __name__ == "__main__":
    init_db()
    app.run(debug=True,use_reloader=False)