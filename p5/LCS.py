class c_():
    def __init__(self):
        self.d = {}


    def add(self, i, j, val, dir):
        self.d[(i, j)] = [val, dir]


    def _dir_and_val(self, m, n):
        for i in range(m):
            row_vals = []
            for j in range(n):
                val = self.return_((i, j), 0)
                dir = self.return_((i, j), 1)
                row_vals.append(f"({val},{dir})")
            print('\t'.join(row_vals))


    def return_(self, loc, typ):
        if loc[0] < 0 or loc[1] < 0:
            return 0 if typ == 0 else 'h'
        return self.d.get(loc, [0, 'h'])[typ]


def lcs(a, b, c_arr):
    m = len(a)
    n = len(b)


    for i in range(m):
        for j in range(n):
            if a[i] != b[j]:
                val_up = c_arr.return_((i - 1, j), 0)
                val_left = c_arr.return_((i, j - 1), 0)
                val = max(val_up, val_left)
                if val_up >= val_left:
                    dir = 'u'
                else:
                    dir = 's'
                c_arr.add(i, j, val, dir)
            else:
                val_diag = c_arr.return_((i - 1, j - 1), 0)
                c_arr.add(i, j, val_diag + 1, 'd')


    i, j = m - 1, n - 1
    lcs_final = []
    while i >= 0 and j >= 0:
        dir = c_arr.return_((i, j), 1)
        if dir == 'd':
            lcs_final.append(a[i])
            i -= 1
            j -= 1
        elif dir == 'u':
            i -= 1
        elif dir == 's':
            j -= 1
        else:
            break


    return ''.join(reversed(lcs_final))


passable_c = c_()
final = lcs(a, b, passable_c)
passable_c._dir_and_val(len(a), len(b))
print(final, len(final))
