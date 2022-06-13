import sqlite3

def main():
    con = sqlite3.connect(':memory:')
    cur = con.cursor()
    cur.executescript("""
        CREATE TABLE numbers (number INTEGER NOT NULL);
        CREATE INDEX number_index ON numbers (number);
    """)

    Q = int(input())
    for _ in range(Q):
        t, *args = map(int, input().split())
        if t == 1:
            x = args[0]
            cur.execute('INSERT INTO numbers VALUES (?)', (x,))
        elif t == 2:
            x, t = args
            cur.execute('DELETE FROM numbers WHERE number = ? LIMIT ?', (x, t))
        else:
            mi = cur.execute('SELECT min(number) FROM numbers').fetchone()[0]
            ma = cur.execute('SELECT max(number) FROM numbers').fetchone()[0]
            print(ma - mi)

main()
