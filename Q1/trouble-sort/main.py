CASE_FMT = "Case #{}: {}"
OK = "OK"


def main():
    t = int(input())
    for i in range(1, t + 1):
        n = int(input())
        v = list(map(int, input().split()))
        odd = sorted([val for p, val in enumerate(v) if p % 2 == 1])
        even = sorted([val for p, val in enumerate(v) if p % 2 == 0])
        trouble_sorted = []
        # print(odd, even)
        for j in range(0, max(len(odd), len(even))):
            if j < len(odd) and j < len(even):
                trouble_sorted.append(even[j])
                trouble_sorted.append(odd[j])
            elif j < len(odd):
                trouble_sorted.append(odd[j])
            elif j < len(even):
                trouble_sorted.append(even[j])
        # print(trouble_sorted)
        ok = True
        for p, (j, k) in enumerate(zip(trouble_sorted, sorted(v))):
            if j != k:
                print(CASE_FMT.format(i, p))
                ok = False
                break
        if ok:
            print(CASE_FMT.format(i, OK))


if __name__ == "__main__":
    main()
