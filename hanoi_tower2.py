import sys


class HanoiTower:
    def __init__(self, n):
        self.nMove = 0
        self.disk_count = n
        self.stacks = dict([('A', []), ('B', []), ('C', [])])
        self.stacks['A'] = list(range(n, 0, -1))

    def print(self):
        keys = list(self.stacks.keys())
        keys.sort()
        for k in keys:
            print("%s: " % k, end="")
            print(self.stacks[k])
        print("------------------")

    def moves(self, f, v, t, n):
        if n == 1:
            input("")
            self.nMove += 1
            disk = self.stacks[f].pop()
            self.stacks[t].append(disk)
            print("#%d" % self.nMove)
            print("MOVE DISK#%d From %s TO %s" % (disk, f, t))
            self.print()
        else:
            self.moves(f, t, v, n - 1)
            self.moves(f, v, t, 1)
            self.moves(v, f, t, n - 1)

    def solve(self):
        print("------------------")
        self.print()
        self.moves('A', 'B', 'C', self.disk_count)


nDisk = int(sys.argv[1])
tower = HanoiTower(nDisk)
tower.solve()
