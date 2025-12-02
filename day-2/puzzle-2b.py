import sys
import re
from typing import List,Tuple

debug = False

def dprint(fs,end='\r\n'):
    if debug:
        print(fs, end=end)

def test(v:int) -> bool:
    vs = str(v)
    half = len(vs)//2
    for i in range(1,half+1):
        if len(vs) % i == 0:
            stub = vs[0:i]
            repeats = len(vs)//len(stub)
            if vs ==  stub * repeats:
                dprint(f"{vs[0:i]} --> {vs}")
                return True
    return False

def solution(ranges: List[Tuple[int,int]]) -> int:
    result = 0

    for r in ranges:
        for v in range(r[0],r[1]+1):
            if test(v):
                result += v
    return result

if __name__ == '__main__':
    print(f"*** Event of Code 2025, Day 2, Part 2 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample1.txt'
    if(len(sys.argv) >=3 and sys.argv[2] == 'debug'):
        debug = True

    df = open(fname, "r")
    lines = [l for l in df.read().splitlines() if len(l.strip())>0]
    ranges = []
    _rex = re.compile("(\d+)-(\d+)")
    pairs = lines[0].split(',')
    for p in pairs:
        g = _rex.search(p)
        ranges.append( (int(g[1]),int(g[2])))
    
    print(f"ranges: {len(ranges)}")

    result = solution(ranges)
    print(f"Solution: {result}")