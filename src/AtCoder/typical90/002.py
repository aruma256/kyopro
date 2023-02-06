N = int(input())

def f(stack, depth):
    if len(stack) == N:
        if depth == 0:
            print(''.join(stack))
        return
    # (
    stack.append('(')
    f(stack, depth+1)
    stack.pop()
    # )
    if depth > 0:
        stack.append(')')
        f(stack, depth-1)
        stack.pop()

def main():
    f([], 0)

main()
