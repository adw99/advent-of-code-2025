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

def check_sets(sets,size):
    if len(sets) != 1:
        return False
    if len(sets[0]) != size:
        return False
    return True

def solution(boxes:List[dict]) -> int:
    # boil the ocean - find all distances between points
    print(f"Calculating all distances, points: {len(boxes)}")
    distances = calc_all_distances(boxes)

    sets = []
    dx = 0
    set_size = len(boxes)
    print("Building sets")
    # start making connections....and sets
    b0 = None
    b1 = None
    while not check_sets(sets,set_size):
        (b0,b1,_) = distances[dx]
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
    print(f"Last two nodes connected: {b0} / {b1}")
    pos1 = boxes[b0]['pos']
    pos2 = boxes[b1]['pos']

    return pos1[0] * pos2[0]

if __name__ == '__main__':
    print(f"*** Advent of Code 2025, Day 8, Part 2 ***\n")
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
    result = solution(boxes)
    print(f"Result: {result}")