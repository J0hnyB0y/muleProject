import sqlite3
import pyodbc

def main():
    database = r"C:\sqlite\db\pythonsqlite.db"

    # create a database connection
    conn = create_connection(mulesoft.db)

    # create tables
    if conn is not None:
    
        cursor_obj = connection_obj.cursor()
        cursor_obj.execute("DROP TABLE IF EXISTS Movies")

        # Creating table
        table = Movies(
            'Name' str,
            'Actor' str ,
            'Actress' str,
            'Director' str, 'year_or_release' int
        );

        cursor_obj.execute(table)

        print("Table is Ready")
    else:
        print("Error! cannot create the database connection.")
    sql = INSERT INTO Movies(Name, Actor, Actress, Director, year_or_release) VALUES (%s, %s, %s, %s, %d)
val = [
  ('Batman Begins', 'Christian Bale', 'Katie Holmes','Christopher Nolan', 2005),
  ('Iron Man', 'Robert Downey Jr.', 'Gwyneth Paltrow', 'Jon Favreau', 2008),
  ('Thor','Chris Hemsworth','Natalie Portman', 'Kenneth Branagh',2011),
  ('Black Widow','David Harbour','Scarlett Johansson', 'Cate Shortland',2020)]
cursor = conn.cursor()
cursor.execute('SELECT * FROM Movies')
result = cursor.fetchone()
print(result)
cursor.execute('SELECT * FROM Movies WHERE actor=Christian Bale')
result = cursor.fetchone()
print(result)
# Close the coonection
connection_obj.close()
