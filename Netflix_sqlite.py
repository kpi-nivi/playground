import sqlite3
import pandas as pd

# Creates netflix.db if it doesn't exist
conn = sqlite3.connect("netflix.db")
cursor = conn.cursor()

# Create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS shows (
        show_id     TEXT PRIMARY KEY,
        type        TEXT,
        title       TEXT,
        release_year INTEGER,
        rating      TEXT,
        country     TEXT
    )
""")

conn.commit()

cursor.execute(""" SELECT name FROM sqlite_master
               WHERE type='table' AND name ='shows'
""")

result = cursor.fetchone()
if result:
    print("Table exists:",result[0])
else:
    print("Table not exists")

df = pd.read_csv('/Users/hakunamatata/Documents/Nivi/netflix_titles.csv')

df.to_sql("shows",conn ,if_exists='replace', index=False)

print("\nTable loaded with ",len(df),"rows")

df_result = pd.read_sql_query("SELECT count(*) FROM shows",conn)
print("\nTotal rows in table\n",df_result)

df_type =pd.read_sql_query(""" 
                           SELECT type,COUNT(*) AS total
                           FROM shows
                           GROUP BY type
                           ORDER BY type DESC
                           """,conn)

print("\nCount by type\n",df_type)

df_country = pd.read_sql_query(""" SELECT
                               country, COUNT(*) as total
                               FROM shows
                               WHERE country IS NOT NULL
                               GROUP BY country
                               ORDER BY total DESC
                               LIMIT 10
                               """,conn)

print("\nTop 10 country by content\n",df_country )

df_movies = pd.read_sql_query(""" SELECT
                              title,release_year,rating
                              FROM shows
                              WHERE upper(type) = 'MOVIE' and release_year >=2015
                              ORDER BY release_year
                              """,conn)
print("\nMovies released after 2015\n",df_movies)

cursor.execute("""INSERT OR IGNORE INTO shows (show_id ,type ,title ,release_year ,rating ,country)
               VALUES(? ,? ,? ,? ,? ,?)
               """,("t9999","Movie","Blue Sky","2026","PG","United States"))

conn.commit()

df_check = pd.read_sql_query("""SELECT * FROM shows
                             WHERE show_id IN ('s9999','t9999')
                             """,conn)

print("\nCheck if row inserted\n",df_check)

conn.close()