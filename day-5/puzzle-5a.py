import sys
import re
from typing import List,Tuple

def solution(lines: List[str])->int:
    _rex = re.compile("(\d+)-(\d+)")

    fresh = []
    available = []
    print(f"Building lists")
    for l in lines:
        if '-' in l:
            f = _rex.search(l)
            fresh.append( (int(f[1]),int(f[2])) )
        else:
            available.append(int(l))
    print("Sorting list")
    fresh = sorted(fresh)
    count = 0
    print("Checking ingredients")
    for a in available:
        for (min,max) in fresh:
            if min <= a <=max:
                count +=1
                break
    return count
        


if __name__ == '__main__':
    print(f"*** Advent of Code 2025, Day 5, Part 1 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample.txt'
    if(len(sys.argv) >=3 and sys.argv[2] == 'debug'):
        debug = True

    df = open(fname, "r")
    lines = [l for l in df.read().splitlines() if len(l.strip())>0]
    result = solution(lines)
    print(f"Result: {result}")