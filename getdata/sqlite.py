import os
import sqlite3
import scrap
"""
Create relational database
"""
DTABASE_PATH = os.path.join(os.getcwd(), 'book_data.db')

conn = sqlite3.connect(DTABASE_PATH)
cur = conn.cursor()

# Create tabel
creat_table = """
                CREATE TABLE Book (
                    ranking INTEGER PRIMARY KEY,
                    item_id INTEGER,
                    sales_point TEXT,
                    rating FLOAT,
                    genre TEXT
                );"""
drop_table_if_exists = 'DROP TABLE IF EXISTS Book;'


# Execute
cur.execute(drop_table_if_exists)
cur.execute(creat_table)



bestseller_id = scrap.get_id() # Get id of bestseller books

ranking = 1 # Set the ranking based on the order of bestseller ids
for ItemId in bestseller_id:
    try: # Put data into table using book id
        cur.execute(
            'INSERT INTO Book VALUES (?,?,?,?,?);',
            (ranking, ItemId, scrap.info(ItemId)[0], scrap.info(ItemId)[1], scrap.info(ItemId)[2])
        )
        ranking += 1
    except AttributeError: # Exclude R-rated books
        continue

conn.commit()
cur.close()