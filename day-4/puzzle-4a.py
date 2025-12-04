import sys
import os
from typing import List,Tuple
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'helpers')))

from grid import Grid
max_x = 0
max_y = 0

neighbors = [ (-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]

def solution(grid:Grid, bales:List[Tuple[int,int]]) -> int:
    movable = 0

    for (x,y) in bales:
        n = 0
        for (dx,dy) in neighbors:
            nx = x + dx
            ny = y + dy
            if 0 <= nx <=max_x and 0<= ny <= max_y:
                pt = grid.get(nx,ny)
                if pt == '@':
                    n += 1
        if n<4:
            movable += 1

    return movable

if __name__ == '__main__':
    print(f"*** Advent of Code 2025, Day 3, Part 2 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample.txt'
    if(len(sys.argv) >=3 and sys.argv[2] == 'debug'):
        debug = True

    df = open(fname, "r")
    lines = [l for l in df.read().splitlines() if len(l.strip())>0]
    max_x = len(lines[0])-1
    max_y = len(lines)-1
    grid = Grid(max_x=len(lines[0]), max_y=len(lines))
    bales = []
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            grid.set(x,y,lines[y][x])
            if lines[y][x] == '@':
                bales.append( (x,y) )
    grid.print()

    result = solution(grid,bales)
    print(f"Solution: {result}")