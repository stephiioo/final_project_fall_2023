import sqlite3

# Initialize the database
DATABASE = 'users.db'

def get_db():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            email TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            profile TEXT
            permissions TEXT DEFAULT 'basic'
        )
    ''')
    db.commit()
    return db

def update_or_create_user(user_info):
    db = get_db()
    cursor = db.cursor()
    try:
        cursor.execute('''
            INSERT INTO users (email, name, profile) VALUES (?, ?, ?)
            ON CONFLICT(email) DO UPDATE SET name = excluded.name, profile = excluded.profile
        ''', (user_info['stephanie.ogbebor@stonybrook.edu'], user_info['stephanie'], user_info['https://steph-test.azureedge.net/finalprojectwolfie/seawolf.png']))
        db.commit()
        print("User added to database: ", user_info['email'])
    except Exception as e:
        print(e)
        db.rollback()        