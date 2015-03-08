
# cross product of vectors OA and OB. 
# positive if ccw turn, negative if cw turn, 0 if collinear
def cross_product(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])       
# return (a1 - or_x) * (b1 - or_x) - (a2 - or_y) * (b2-or_y)


def convex_hull(points):
   
    print points
    
    #sort points by x coord, if tie, by y coord (done implicitly python)
    #remove duplicates to detect case where n=1
    sorted(set(points))

    if len(points) < 2:
        return points

    #lower hull
    lower = []
    for p in points:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)


    #upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)


    #remove last point of each list
    upper.pop()
    lower.pop()

    convex_hull = lower + upper

    return convex_hull







def main():

        level1 = [(0,0)]

        level2 = [(1, 0), (1, 1), (0, 1)]

        level3 = [(0, 2), (1, 2), (2, 2), (2, 1), (2, 0)]


        print convex_hull(level1)

        print convex_hull(level2)

        print convex_hull(level3)

main()

