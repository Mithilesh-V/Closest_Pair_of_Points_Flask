# An Optimized Divide-and-Conquer Algorithm for the Closest-Pair Problem in the Planar Case (BASIC-2 Algorithm)
Also With a Heap Implementaion
-----------------------------------------------------------------
**The paper we have refered also has been uploaded**

In the "BASIC-2.py" program, we implement the Basic-2 Algorithm
using Python lists and undertake the familiar sorting approach to generate 
the halves. We recombine solutions from halves created and finally return 
the minimum distance and the closest pair found in the input data set.

-----------------------------------------------------------------
In the "BASIC-2_with_MIN_HEAP.py" program, we implement the Basic-2 Algorithm
using a min heap which has been defined by our team. Instead of utilising 
the familiar sorting approach, we use the min heap to perform the sorting 
and keep the least element at the root for easy look-up and comparison. 

------------------------------------------------------------------
Since we are performing the heapify operation after each pop in the second 
program using the min heap, the complexity is more than the one obtained in
the original program because, in the first one, we just look at the next point
in the Python list and keep proceeding with our algorithm. This is not the 
case for the second one and hence usage of the min heap is not suited for this
algorithm.

------------------------------------------------------------------
The outputs are generated accordingly for both programs. Do look into it. 
Thank you.
