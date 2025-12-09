import sys
from typing import List,Tuple
from shapely import LineString, Polygon, polygonize

def solution(pts: List[Tuple[int,int]])->int:

    print(f"Creating lines")
    lines = []
    # Add our points and connect them
    for p in range(len(pts)):
        if p>0:
            lines.append( LineString( (pts[p],pts[p-1]) ))
    # wrap around
    lines.append( LineString( (pts[-1], pts[0])) )
    print(f"Lines formed: {len(lines)}")

    print(f"Finding polygons")
    polys = list(polygonize(lines).geoms)
    print(f"Polygons found: {len(polys)}")

    print(f"Looking for rectangles in polygons")
    max = 0
    for x in range(len(pts)):
         for y in range(x+1,len(pts)):
            (x1,y1) = pts[x]
            (x2,y2) = pts[y]
            if x1 != x2 and y1 !=y2:
                area = ( abs(x1-x2) + 1 ) * ( abs(y1-y2) + 1)
                if area>max:
                    # check if rectangle is contained in any polys
                    rect = Polygon( [ (x1,y1),(x1,y2),(x2,y2),(x2,y1)])
                    for p in polys:
                        if p.contains(rect):
                            max = area
    return max

if __name__ == '__main__':
    print(f"*** Advent of Code 2025, Day 9, Part 2 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample.txt'

    df = open(fname, "r")
    boxes = []
    lines = [l.strip() for l in df.read().splitlines() if len(l.strip())>0]
    
    points = []
    for l in lines:
        pts = tuple([int(x) for x in l.split(',')])
        points.append( pts )
    result = solution(points)
    print(f"Result: {result}")