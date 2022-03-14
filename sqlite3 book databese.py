import  sqlite3
conn = sqlite3.connect('Gestionarea bazei de date.db')
cursor = conn.cursor()
 
cursor.execute(CREATE TABLE IF NOT EXISTS Books(book_id INT PRIMARY KEY, title TEXT, year INT);)

b_id = input('Book ID')
b_title = input('Title')
b_year = input('Year')
cursor.execute(
INSERT INTO Books(book_id, title, year)
VALUES (,,)
, (b_id, b_title, b_year))
conn.commit ()
print ( 'Ok!' )
cursor.execute(SELECT  FROM Books;)
all_results = cursor.fetchall()
print(all_results)
conn.close()
if (conn)
    conn.close()
    print(nClosed.)