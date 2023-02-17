def main():
    H, W = map(int, input().split())
    if 1 in {H, W}:
        print(max(H, W))
        return
    H += (H & 1)
    W += (W & 1)

    print((H//2) * (W//2))

main()
