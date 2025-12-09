import sys
from typing import List,Tuple

def solution(pts: List[Tuple[int,int]])->int:

    max = 0

    for x in range(len(pts)):
        for y in range(x,len(pts)):
            (x1,y1) = pts[x]
            (x2,y2) = pts[y]
            area = ( abs(x1-x2) + 1 ) * ( abs(y1-y2) + 1)
            if area>max:
                max = area
    return max

if __name__ == '__main__':
    print(f"*** Advent of Code 2025, Day 9, Part 1 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample.txt'
    if(len(sys.argv) >=3 and sys.argv[2] == 'debug'):
        debug = True

    df = open(fname, "r")
    boxes = []
    lines = [l.strip() for l in df.read().splitlines() if len(l.strip())>0]
    pts = []
    for l in lines:
        pts.append( tuple( [int(x) for x in l.split(',')]))
    result = solution(pts)
    print(f"Result: {result}")