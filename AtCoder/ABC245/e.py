import sqlite3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    D = list(map(int, input().split()))
    AB = [(a, b, 0) for a, b in zip(A, B)]
    CD = [(c, d, 1) for c, d in zip(C, D)]
    Q = AB + CD
    Q.sort()
    print(Q)
    con = sqlite3.connect(':memory:')
    cur = con.cursor()
    cur.executescript("""
        CREATE TABLE boxes (height INTEGER NOT NULL);
        CREATE INDEX height_index ON boxes (height);
    """)
    while Q:
        a, b, t = Q.pop()
        if t == 1:
            cur.execute('INSERT INTO boxes VALUES (?)', (b,))
        else:
            cur.execute('EXPLAIN QUERY PLAN SELECT rowid FROM boxes WHERE height >= ? ORDER BY height ASC LIMIT 1', (b,))
            print(cur.fetchall())
            cur.execute('SELECT rowid FROM boxes WHERE height >= ? ORDER BY height ASC LIMIT 1', (b,))
            res = cur.fetchone()
            if res:
                rowid = res[0]
                cur.execute('DELETE FROM boxes WHERE rowid = ?', (rowid,))
            else:
                print('No')
                return
    print('Yes')

main()
