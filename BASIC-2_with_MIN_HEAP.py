import math
import random

P = [[1, 1], [1, 3], [4, 4], [5, 4], [3, 3], [6, 7], [8, 9], [9, 11], [15, 3], [15, 6], [13, 12], [10, 10], [11, 6]]

# IT works with a large input also but is very slow
#P = [[random.randint(0, 1000000), random.randint(0, 1000000)] for i in range(100000)]


def Initial_Sort(P):
    Px = sorted(P, key=lambda x: x[0])
    Py = sorted(P, key=lambda x: x[1])
    return Px, Py


Px, Py = Initial_Sort(P)


def Euclidean_Distance(P1, P2):
    return math.sqrt((P1[0] - P2[0])**2 + (P1[1] - P2[1])**2)


def min_heapify(A, k):
    l = left(k)
    r = right(k)
    if l < len(A) and A[l][1] < A[k][1]:
        smallest = l
    else:
        smallest = k
    if r < len(A) and A[r][1] < A[smallest][1]:
        smallest = r
    if smallest != k:
        A[k][1], A[smallest][1] = A[smallest][1], A[k][1]
        min_heapify(A, smallest)


def left(k):
    return 2 * k + 1


def right(k):
    return 2 * k + 2


def build_min_heap(A):
    n = int((len(A)//2)-1)
    for k in range(n, -1, -1):
        min_heapify(A, k)
    return A


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

   #print(ll, lr)
    #print(Qy, Ry)

    for point in Qy:
        if point[0] >= ll:
            Yl.append(point)

    for point in Ry:
        if point[0] <= lr:
            Yr.append(point)
    d_min = min_distance[0]
    if (len(Yl) < 1) or (len(Yr) < 1):
        return d_min, Target_Pair
    #Yl_sort = sorted(Yl, key=lambda x: x[1])
    #Yr_sort = sorted(Yr, key=lambda x: x[1])

    Yl_sort = build_min_heap(Yl)
    Yr_sort = build_min_heap(Yr)

    print("min Heaped left value : ", Yl_sort)
    print("min Heaped right value : ", Yr_sort)
    left = Yl_sort[0]
    right = Yr_sort[0]

    i, j = 0, 0

    #print(Yl_sort, Yr_sort)
    while len(Yl_sort) > 1 and len(Yr_sort) > 1:
        dist = Euclidean_Distance(left, right)
        if dist < d_min:
            Target_Pair = [left, right]
            d_min = dist

        if left[1] <= right[1]:
            if len(Yr_sort) > 0:
                t = Yr_sort
                t.pop(0)
                t = build_min_heap(t)
                dist = Euclidean_Distance(left, t[0])
                if dist < d_min:
                    Target_Pair = [left, t[0]]
                    d_min = dist

                Yl_sort.pop(0)
                Yl_sort = build_min_heap(Yl_sort)
                left = Yl_sort[0]
                i += 1

        elif len(Yl_sort) > 0:
            t = Yl_sort
            t.pop(0)
            t = build_min_heap(t)
            dist = Euclidean_Distance(t[0], right)
            if dist < d_min:
                Target_Pair = [t[0], right]
                d_min = dist
            Yr_sort.pop(0)
            Yr_sort = build_min_heap(Yr_sort)
            right = Yr_sort[0]
            j += 1
        print("min Heaped left value : ", Yl_sort)
        print("min Heaped right value : ", Yr_sort)
        print(left, right)
        print(len(Yl_sort), len(Yr_sort))

    return d_min, Target_Pair


sol = Closest_Pair(Px, Py)
print()
print("The distance is:", sol[0])
print("The closest pairs are: ", sol[1])
