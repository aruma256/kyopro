import math
from typing import Tuple

T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())
TARGET_POS = (X, Y, 0)

def getCurrentPos(e: int) -> Tuple[float, float, float]:
    return (0, (-L/2) * math.sin((e/T)*2*math.pi), L/2 - L/2 * math.cos((e/T)*2*math.pi))

# print(getCurrentPos(0*T/4))
# print(getCurrentPos(1*T/4))
# print(getCurrentPos(2*T/4))
# print(getCurrentPos(3*T/4))

def main():
    for _ in range(Q):
        e = int(input())
        currentPos = getCurrentPos(e)
        dx, dy, dz = currentPos[0] - TARGET_POS[0], currentPos[1] - TARGET_POS[1], currentPos[2] - TARGET_POS[2]
        dxy = math.sqrt(dx**2 + dy**2)
        print(math.degrees(math.atan2(dz, dxy)))

main()
