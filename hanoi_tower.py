import sys

nMove = 0


def init_tower(n):
    global nMove
    nMove = 0
    s = dict([('A', []), ('B', []), ('C', [])])
    s['A'] = list(range(n, 0, -1))
    return s


def print_tower(s):
    keys = list(s.keys())
    keys.sort()
    for k in keys:
        print("%s: " % k, end="")
        print(s[k])
    print("------------------")


def moves(s, f, v, t, n):
    global nMove
    if n == 1:
        input("")
        nMove += 1
        disk = s[f].pop()
        s[t].append(disk)
        print("#%d" % nMove)
        print("MOVE DISK#%d From %s TO %s" % (disk, f, t))
        print_tower(s)
    else:
        moves(s, f, t, v, n - 1)
        moves(s, f, v, t, 1)
        moves(s, v, f, t, n - 1)


def solve(tw, disk_counts):
    print("------------------")
    print_tower(tw)
    moves(tw, 'A', 'B', 'C', disk_counts)


nDisk = int(sys.argv[1])
tower = init_tower(nDisk)
solve(tower, nDisk)
