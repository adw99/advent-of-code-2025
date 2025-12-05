import sys
import re
from typing import List,Tuple

def merge_ranges(fresh_in):
    fresh = sorted(fresh_in, key=lambda x: x[0])
    merged = []
    curr = fresh[0]
    merged.append(curr)
    for f in fresh:
        # if new min is larger than curr max we have a new range
        if f[0] > curr[1]:
            curr = f
            merged.append(f)
        else:
            # new range overlaps with curr range, so update curr range
            # input list is sorted by min value, so should only have to check max
            if f[1] > curr[1]:
                curr[1] = f[1]

    return merged


def solution(lines: List[str])->int:
    _rex = re.compile("(\d+)-(\d+)")

    fresh = []
    print(f"Building lists")
    for l in lines:
        if '-' in l:
            f = _rex.search(l)
            fresh.append( [int(f[1]), int(f[2])] )
    merged = merge_ranges(fresh)
    print(f">> {len(fresh)} ranges merged to {len(merged)}")
    count = 0
    for f in merged:
        min = f[0]
        max = f[1]
        count += (max-min)+1
    return count
        


if __name__ == '__main__':
    print(f"*** Advent of Code 2025, Day 5, Part 2 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample.txt'
    if(len(sys.argv) >=3 and sys.argv[2] == 'debug'):
        debug = True

    df = open(fname, "r")
    lines = [l for l in df.read().splitlines() if len(l.strip())>0]
    result = solution(lines)
    print(f"Result: {result}")