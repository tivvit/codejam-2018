import sys

CASE_FMT = "{} {}"


def pos(x, y):
    if x == -1 and y == -1:
        return 0
    if x == -1 and y == 0:
        return 1
    if x == -1 and y == 1:
        return 2
    if x == 0 and y == -1:
        return 3
    if x == 0 and y == 0:
        return 4
    if x == 0 and y == 1:
        return 5
    if x == 1 and y == -1:
        return 6
    if x == 1 and y == 0:
        return 7
    if x == 1 and y == 1:
        return 8


def main():
    t = int(input())
    for i in range(1, t + 1):
        a = int(input())
        positions = [0 for _ in range(9)]
        wp = [(3 * x - 1, 2) for x in range(1, 1000 // 9 + 1)]
        wanted = wp.pop()
        while True:
            if sum(positions) == 9:
                positions = [0 for _ in range(9)]
                wanted = wp.pop()
            print(CASE_FMT.format(wanted[0], wanted[1]))
            sys.stdout.flush()
            k, m = list(map(int, input().split()))
            if k == -1 and m == -1:
                exit(1)
            if k == 0 and m == 0:
                break
            positions[pos(wanted[0] - k, wanted[1] - m)] = 1


if __name__ == "__main__":
    main()
