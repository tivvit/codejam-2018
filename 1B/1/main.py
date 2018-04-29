CASE_FMT = "Case #{}: {}"


def main():
    t = int(input())
    for i in range(1, t + 1):
        n, l = list(map(int, input().split()))
        c = list(map(int, input().split()))
        s = 0
        missing = n - sum(c)
        print(missing)
        print(n, l, c)
        print(100 / n)
        print("---")
        for j in c:
            p = (j / n) * 100
            print(p)
            s += round(p)
        print(CASE_FMT.format(i, s))


if __name__ == "__main__":
    main()
