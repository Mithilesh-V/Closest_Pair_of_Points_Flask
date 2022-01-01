import math
import random
import matplotlib.pyplot as plt


# Uncomment this for a basic idea of this  BASIC-2 Algorithm
P = [[1, 1], [1, 3], [4, 4], [5, 4], [3, 3], [6, 7], [8, 9], [9, 11], [15, 3], [15, 6], [13, 12], [10, 10], [11, 6]]

# UNcomment this for the 1.25 million value input
# P = [[random.randint(0, 1250000), random.randint(0, 1250000)] for i in range(1250000)]

# ox = [i[0] for i in P]
# oy = [i[1] for i in P]

# plt.plot(ox, oy, "bo")
# plt.show()


def Initial_Sort(P):
    Px = sorted(P, key=lambda x: x[0])
    Py = sorted(P, key=lambda x: x[1])
    return Px, Py


Px, Py = Initial_Sort(P)


def Euclidean_Distance(P1, P2):
    return math.sqrt((P1[0] - P2[0])**2 + (P1[1] - P2[1])**2)


def Closest_Pair(Px, Py):
    if len(Px) <= 3:
        Array = Px
        size = len(Array)
        minimum_distance = Euclidean_Distance(Array[0], Array[1])
        Target_Pair = [Array[0], Array[1]]
        if len(Array) == 2:
            return Euclidean_Distance(Array[0], Array[1]), [Array[0], Array[1]]
        for i in range(0, size):
            for j in range(i+1, size):
                distance = Euclidean_Distance(Array[i], Array[j])
                if distance < minimum_distance:
                    minimum_distance = distance
                    Target_Pair = [Array[i], Array[j]]

        return minimum_distance, Target_Pair

    midpoint_x = len(Px) // 2
    Qx = Px[:midpoint_x]
    Rx = Px[midpoint_x:]
    median_x = Px[midpoint_x]
    Qy, Ry = [], []

    for point in Py:
        if point[0] < int(median_x[0]):
            Qy.append(point)
        else:
            Ry.append(point)

    min_distance_Left = Closest_Pair(Qx, Qy)
    min_distance_Right = Closest_Pair(Rx, Ry)
    min_distance = min(min_distance_Left, min_distance_Right)
    Target_Pair = min_distance[1]
    Yl, Yr = [], []
    x_bar = Qx[-1][0]

    ll = x_bar - min_distance[0]
    lr = x_bar + min_distance[0]

    print(ll, lr)
    print(Qy, Ry)

    for point in Qy:
        if point[0] >= ll:
            Yl.append(point)

    for point in Ry:
        if point[0] <= lr:
            Yr.append(point)
    Yl_sort = sorted(Yl, key=lambda x: x[1])
    Yr_sort = sorted(Yr, key=lambda x: x[1])
    d_min = min_distance[0]
    if (len(Yl_sort) < 1) or (len(Yr_sort) < 1):
        return d_min, Target_Pair
    left = Yl_sort[0]
    right = Yr_sort[0]

    i, j = 0, 0
    print(Yl_sort, Yr_sort)
    while i+1 < len(Yl_sort) and j+1 < len(Yr_sort):
        dist = Euclidean_Distance(left, right)
        if dist < d_min:
            Target_Pair = [left, right]
            d_min = dist
        if left[1] <= right[1]:
            if j < len(Yr_sort):
                dist = Euclidean_Distance(left, Yr_sort[j+1])
                if dist < d_min:
                    Target_Pair = [left, Yr_sort[j+1]]
                    d_min = dist

                left = Yl_sort[i+1]
                i += 1
        elif i < len(Yl_sort):
            dist = Euclidean_Distance(Yl_sort[i+1], right)
            if dist < d_min:
                Target_Pair = [Yl_sort[i+1], right]
                d_min = dist
            right = Yr_sort[j+1]
            j += 1
            print(i, j)
    return d_min, Target_Pair


soln = Closest_Pair(Px, Py)

print("\n\n\nThe minimum Distance is : ", soln[0])
print("\n\nThe Closest Pairs are : ", soln[1])
