import sys
from typing import List

def recurse(pt:str, path: List[str], connections: dict) -> int:
    result = 0
    options = connections[pt]
    for o in options:
        if o == "out":
            result += 1
        else:
            if o not in path:
                np = path.copy()
                np.append(pt)
                result += recurse(o,np,connections)
    return result

def solution(connections: dict) -> int:
    start = "you"
    path = []
    return recurse(start,path,connections)

if __name__ == '__main__':
    print(f"*** Advent of Code 2025, Day 11, Part 1 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample.txt'

    df = open(fname, "r")
    boxes = []
    lines = [l.strip() for l in df.read().splitlines() if len(l.strip())>0]

    connections = {}
    for l in lines:
        ft = l.split(':')
        f = ft[0].strip()
        t = ft[1].strip().split(' ')
        connections[f] = t

    result = solution(connections)
    print(f"Result: {result}")
