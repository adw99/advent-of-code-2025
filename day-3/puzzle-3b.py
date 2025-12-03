import sys
from typing import List,Tuple

debug = False

def dprint(fs,end='\r\n'):
    if debug:
        print(fs, end=end)


def bank_max(b: List[int], l:12) -> int:
    result = 0
    digits = []
    bank = b.copy()

    for x in range(l,0,-1):
        if x>1:
            work = sorted(bank[:-1 * (x-1)], reverse=True)
        else:
            work = sorted(bank, reverse=True)
        digits.append(work[0])
        p1 = bank.index(work[0])

        dprint(f"({x}) {bank} -> {work[0]} / {work} / {bank[p1+1:]}")
        bank = bank[p1+1:]
    dprint(f"d>{len(digits)}", end='')
    result = 0
    for i in range(len(digits)):
        result += digits[i] * 10**(12-(i+1))
    dprint(f" {result}")
    return result

def solution(banks: List[str]) -> int:
    max = 0
    length = 12
    for bstr in banks:
        b = [ int(x) for x in list(bstr)]
        max += bank_max(b,length)
    return max

if __name__ == '__main__':
    print(f"*** Advent of Code 2025, Day 3, Part 2 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample.txt'
    if(len(sys.argv) >=3 and sys.argv[2] == 'debug'):
        debug = True

    df = open(fname, "r")
    lines = [l for l in df.read().splitlines() if len(l.strip())>0]
    result = solution(lines)
    print(f"Solution: {result}")