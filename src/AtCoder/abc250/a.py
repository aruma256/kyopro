H, W = map(int, input().split())
R, C = map(int, input().split())
print(4 - (R==1) - (C==1) - (H==R) - (W==C))
