import sqlite3  
  
con = sqlite3.connect("Items.db")  
print("Database opened successfully")  
  
con.execute("create table items (id INTEGER PRIMARY KEY AUTOINCREMENT, item_name TEXT NOT NULL, cuisine TEXT UNIQUE NOT NULL, address TEXT NOT NULL)")  
  
print("Table created successfully")  
  
con.close() 