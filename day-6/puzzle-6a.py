import sys


def solution(lines):
    grid = []
    for l in range(len(lines)-1):
        row = []
        for n in lines[l].split(' '):
            if len(n.strip())>0:
                row.append(int(n))
        grid.append(row)
    # rotate the grid
    ng = []
    for x in range(len(grid[0])):
        row = []
        for y in range(len(grid)):
            row.append(grid[y][x])
        ng.append(row)
    # get the list of operands
    ops = []
    for l in lines[-1].strip().split(' '):
        if len(l.strip())>0:
            ops.append(l.strip())
    total = 0
    for i in range(len(ops)):
        op = ops[i]
        vals = ng[i]
        num = vals[0]
        for x in range(1,len(vals)):
            next = vals[x]
            if op == '*':
                num *= next
            elif op == "+":
                num += next
        total += num
        # print(f">{i}: {num}")

    return total

if __name__ == '__main__':
    print(f"*** Advent of Code 2025, Day 6, Part 1 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample.txt'
    if(len(sys.argv) >=3 and sys.argv[2] == 'debug'):
        debug = True

    df = open(fname, "r")
    lines = [l.strip() for l in df.read().splitlines() if len(l.strip())>0]
    result = solution(lines)
    print(f"Result: {result}")