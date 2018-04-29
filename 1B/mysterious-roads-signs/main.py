CASE_FMT = "Case #{}: {} {}"


def match(sig, subset, cnts, lm, ln, mu, nu):
    mx = 0
    if not sig:
        return subset, cnts[subset]
    d, a, b = sig[0]
    m = d + a
    n = d - b
    print(m, n, mu, nu, lm, ln)
    if mu and m == lm:
        ln = subset + 1
        if ln not in cnts:
            cnts[ln] = 1
        cnts[ln] += 1
        return match(sig[1:], ln, cnts, lm, ln, mu, nu)
    elif nu and n == ln:
        ln = subset + 1
        if ln not in cnts:
            cnts[ln] = 1
        cnts[ln] += 1
        return match(sig[1:], ln, cnts, lm, ln, mu, nu)
    # todo freeze non matching side + try clean iteration on it
        # used any
        # if not mu and not nu:
        #     match(sig[i:], subset + 1, 1, m, n, True, False)
        #     match(sig[i:], subset + 1, 1, m, n, False, True)
        #
        #
        # if not mu and m == lm:
        #     mu = True
        #     print("use m")
        # if not nu and n == ln:
        #     nu = True
        #     print("use n")
        #
        # # nothing matching, free use
        # if mu and m != lm and not nu and n != ln:
        #     nu = True
        #     ln = n
        #     print("use n")
        # if nu and n != ln and not mu and m != lm:
        #     mu = True
        #     lm = m
        #     print("use m")
        #
        # # move free
        # if not mu and m != lm:
        #     lm = m
        # if not nu and n != ln:
        #     ln = n
        #
        # subset += 1
        # if subset > mx:
        #     mx = subset
        #     cnt = 1
        # elif subset == mx:
        #     cnt += 1
    else:
        m_mx, m_cnt = match(sig[1:], 1, cnts, m, n, True, False)
        # todo depcopy of cnts
        n_mx, n_cnt = match(sig[1:], 1, cnts, m, n, False, True)
        if m_mx > n_mx:
            return m_mx, m_cnt
        else:
            return n_mx, n_cnt

        # if t_mx > mx:
        #     mx = t_mx
        #     cnt = t_cnt
        # elif t_mx == mx:
        #     cnt += t_cnt


        # subset = 1
        # lm, ln = m, n
        # mu, nu = False, False
        # if subset > mx:
        #     mx = subset
        #     cnt = 1
        # elif subset == mx:
        #     cnt += 1
    return mx, cnts[mx]


def main():
    t = int(input())
    for i in range(1, t + 1):
        s = int(input())
        sig = []
        for j in range(s):
            d, a, b = list(map(int, input().split()))
            sig.append((d, a, b))
        mx, cnt = match(sig, 0, {}, None, None, False, False)
        print(CASE_FMT.format(i, mx, cnt))
        # d, a, b = sig[0]
        # m_mx, m_cnt = match(sig[i:], 1, 1, m, n, True, False)
        # n_mx, n_cnt = match(sig[i:], 1, 1, m, n, False, True)
        # if m_mx > n_mx:
        #     print(CASE_FMT.format(i, m_mx, m_cnt))
        # else:
        #     print(CASE_FMT.format(i, n_mx, n_cnt))


if __name__ == "__main__":
    main()
