CASE_FMT = "Case #{}: {}"
OK = "OK"


def trouble_sort(l):
    done = False
    while not done:
        done = True
        for i in range(0, len(l) - 2):
            if l[i] > l[i + 2]:
                done = False
                l[i], l[i + 2] = l[i + 2], l[i]
    return l


def main():
    t = int(input())
    for i in range(1, t + 1):
        n = int(input())
        v = list(map(int, input().split()))
        ok = True
        for p, (j, k) in enumerate(zip(trouble_sort(v), sorted(v))):
            if j != k:
                print(CASE_FMT.format(i, p))
                ok = False
                break
        if ok:
            print(CASE_FMT.format(i, OK))


if __name__ == "__main__":
    main()
