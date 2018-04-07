CASE_FMT = "Case #{}: {}"
IMPOSSIBLE = "IMPOSSIBLE"


def main():
    t = int(input())
    for i in range(1, t + 1):
        d, p = input().split()
        d = int(d)
        if len([j for j in p if j == 'S']) > d:
            print(CASE_FMT.format(i, IMPOSSIBLE))
            continue
        p = list(p)
        swaps = 0
        while True:
            dmg = 1
            dmg_sum = 0
            for c in p:
                if c == 'C':
                    dmg *= 2
                if c == 'S':
                    dmg_sum += dmg
            # print(dmg_sum, ''.join(p))
            if dmg_sum <= d:
                print(CASE_FMT.format(i, swaps))
                break
            last_c_pos = None
            found = False
            for c in range(len(p) - 1, -1, -1):
                if not found and p[c] == 'S':
                    found = True
                    continue
                if found and p[c] == 'C':
                    last_c_pos = c
                    break
            swaps += 1
            # print(last_c_pos, p[last_c_pos], p[last_c_pos + 1])
            p[last_c_pos], p[last_c_pos + 1] = 'S', 'C'


if __name__ == "__main__":
    main()
