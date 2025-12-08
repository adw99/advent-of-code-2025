import sys
import math
from typing import List,Tuple

def dist_3d(p1: Tuple[int,int,int], p2:Tuple[int,int,int]) -> float:
    (x1,y1,z1) = p1
    (x2,y2,z2) = p2
    return math.sqrt( (x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2  )

def calc_all_distances(boxes:List[dict]) -> List[tuple]:
    distances = []
    for x in range(len(boxes)):
        b = boxes[x]
        id = b['id']
        bpos = b['pos']      
        for y in range(x+1,len(boxes)):
            b2 = boxes[y]
            if b2['id'] != id:
                b2pos = b2['pos']
                dist = dist_3d(bpos,b2pos)
                distances.append( (id,b2['id'],dist))

    distances = sorted(distances, key=lambda x:x[2])
    print(f"min_dist: {distances[0][2]}")
    return distances


def find_id_in_set(id,sets):
    result = None
    for s in sets:
        if id in s:
           result = s
           break
    return result

def solution(boxes:List[dict],max_connect:int) -> int:
    # boil the ocean - find all distances between points
    print(f"Calculating all distances, points: {len(boxes)}")
    distances = calc_all_distances(boxes)

    connections = 0
    sets = []
    dx = 0
    print("Building sets")
    # start making connections....and sets
    while connections<max_connect:
        (b0,b1,_) = distances[dx]
        connections += 1
        dx += 1
        found = False
        s0 = find_id_in_set(b0,sets)
        s1 = find_id_in_set(b1,sets)

        if s0 == None and s1 == None:
            # new set
            sets.append(set([b0,b1]))
        elif s1 == None:
            s0.add(b1)
        elif s0 == None:
            s1.add(b0)
        else:
            # the values are both in sets, are they already in the same set or in two different sets?
            # same set? No operation needed
            # different sets? merge the sets
            if s0 != s1:
                s3 = s0.union(s1)
                sets.remove(s0)
                sets.remove(s1)
                sets.append(s3)

    print(f"Sets created: {len(sets)}")
    sizes = [len(s) for s in sets]
    sizes.sort(reverse=True)

    result = sizes[0] * sizes[1] * sizes[2]

    return result

if __name__ == '__main__':
    print(f"*** Advent of Code 2025, Day 8, Part 1 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample.txt'
    if(len(sys.argv) >=3 and sys.argv[2] == 'debug'):
        debug = True

    df = open(fname, "r")
    boxes = []
    lines = [l.strip() for l in df.read().splitlines() if len(l.strip())>0]
    count = 0
    for l in lines:
        boxes.append( {
            'id': count,
            'pos': tuple([int(x) for x in l.split(',')])
        })
        count += 1
    # number of connections is different for solution vs sample data
    max_connect = 10 if len(lines)<100 else 1000
    result = solution(boxes,max_connect)
    print(f"Result: {result}")