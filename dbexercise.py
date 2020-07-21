import sqlite3

conn = sqlite3.connect('TestDB.db')
c = conn.cursor()

c.execute('''CREATE TABLE CLIENTS
            ([generated_id] INTEGER PRIMARY KEY, [Client_Name] text, [Country_ID] integer, [DATE] date)''')

c.execute('''CREATE TABLE COUNTRY
            ([generated_ID] INTEGER PRIMARY KEY, [Country_ID] integer, [Country_Name] text)''')

c.execute('''CREATE TABLE DAILY_STATUS
            ([Client_Name] text, [Country_Name] text, [DATE] date)''')

conn.commit()
