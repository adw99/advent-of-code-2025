import sys
from typing import List,Tuple

debug = False

def dprint(fs,end='\r\n'):
    if debug:
        print(fs, end=end)

def bank_max(bank: List[int]) -> int:
    work = sorted(bank[:-1], reverse=True)
    dprint(f"? {work}")
    d1 = work[0]
    p1 = bank.index(d1)
    dprint(f"p1: {p1}")
    dprint(f"> {bank[p1+1:]}")
    d2 = max( bank[p1+1:] )
    bmax = d1*10 + d2
    dprint(f"{bank} -> {bmax}")
    return bmax

def solution(banks: List[str]) -> int:
    max = 0
    for bstr in banks:
        b = [ int(x) for x in list(bstr)]
        max += bank_max(b)
    return max

if __name__ == '__main__':
    print(f"*** Advent of Code 2025, Day 3, Part 1 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample.txt'
    if(len(sys.argv) >=3 and sys.argv[2] == 'debug'):
        debug = True

    df = open(fname, "r")
    lines = [l for l in df.read().splitlines() if len(l.strip())>0]
    result = solution(lines)
    print(f"Solution: {result}")