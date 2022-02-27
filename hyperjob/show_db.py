import sqlite3

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()
# cur.execute('SELECT name FROM sqlite_master WHERE type ="table" AND name NOT LIKE "sqlite_%";')
cur.execute('SELECT * FROM auth_user;')
# cur.execute('SELECT * FROM tournament_player;')
# cur.execute('SELECT * FROM tournament_game;')
print(*cur.fetchall(), sep='\n')
