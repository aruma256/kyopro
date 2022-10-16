import sqlite3

def main():
    con = sqlite3.connect(':memory:')
    cur = con.cursor()
    cur.executescript("""
        CREATE TABLE blocks (r INTEGER NOT NULL, c INTEGER NOT NULL);
        CREATE INDEX idx_r_c ON blocks (r, c);
        CREATE INDEX idx_c_r ON blocks (c, r);
    """)

    H, W, rs, cs = map(int, input().split())
    N = int(input())
    for _ in range(N):
        r, c = map(int, input().split())
        cur.execute('INSERT INTO blocks VALUES (?,?)', (r, c))
    Q = int(input())
    r, c = rs, cs
    for _ in range(Q):
        d, l = input().split()
        l = int(l)
        if d == 'R':
            tc = min(c+l, W)
            cur.execute('SELECT c FROM blocks WHERE r = ? AND c BETWEEN ? AND ? ORDER BY c ASC LIMIT 1', (r, c, tc))
            res = cur.fetchone()
            if res:
                c = res[0] - 1
            else:
                c = tc
        elif d == 'L':
            tc = max(c-l, 1)
            cur.execute('SELECT c FROM blocks WHERE r = ? AND c BETWEEN ? AND ? ORDER BY c DESC LIMIT 1', (r, tc, c))
            res = cur.fetchone()
            if res:
                c = res[0] + 1
            else:
                c = tc
        elif d == 'D':
            tr = min(r+l, H)
            cur.execute('SELECT r FROM blocks WHERE c = ? AND r BETWEEN ? AND ? ORDER BY r ASC LIMIT 1', (c, r, tr))
            res = cur.fetchone()
            if res:
                r = res[0] - 1
            else:
                r = tr
        elif d == 'U':
            tr = max(r-l, 1)
            cur.execute('SELECT r FROM blocks WHERE c = ? AND r BETWEEN ? AND ? ORDER BY r DESC LIMIT 1', (c, tr, r))
            res = cur.fetchone()
            if res:
                r = res[0] + 1
            else:
                r = tr
        print(r, c)


main()

