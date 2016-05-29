# Part 1:

"""Runtime"""
# 1. The function's workload is a "for loop", and it's run time is linear.

# 2. Runtimes in ascending order by efficiency as n approaches infinity:
    # O(1)
    # O(log n)
    # O(n)
    # O(n log n)
    # O(n^2)
    # O(2^n)


"""Stacks and Queues"""
# 1.
    # 1. The process of loading and unloading pallets onto a flatbed truck: Best to use a stack --> Last in First Out (LIFO)
    # 2. Putting bottle caps on bottles of beer as they roll down an assembly line: Queue, First in First out (FIFO)
    # 3. Calculating the solution to this mathematical expression: 2 + (7 * 4) - (3 / 2): Queue because first need to calculate the operations that are in parenthesis from left to right, then do the rest of the operations from left to right. It is following the principle of FIFO.

# 2. Queue examples (FIFO):
#     - Taking orders at a restaurant. First come first served.
#     - FasTrak system, first in line gets to pay the toll first.

# 3. Stack examples (LIFO):
#     - Loading and unloading bags of rice in a truck.
#     - When loading drinks in a single file at a Walgreen's fridge. The customer needs to take the first that is closest to the edge of the rack.


"""Linked Lists"""
 # 1. The node has 2 attributes: data and next. The following are the nodes:
 # The boxes that contained ("Apple" + next), 'Apple' is the data for this node.
 # The boxes that contained ("Berry" + next), 'Berry' is the data for this node.
 # The boxes that contained ("Cherry" + next), 'Cherry' is the data for this node.
 # The head is the box that says head and it is pointing to the <node Apple>. The head always points to the first node of the linked list.
 # The tail is pointing to None.

 # 2. The main difference between singly and doubly linked list are the nodes. The nodes of a singly linked list has 2 attributes : data and next. On the other hand, doubly linked list nodes has an extra attribute, which is previous.

 # 3. It is faster to append at the end of a linked list if we keep track of the tail because there is no need to traverse the whole list everytime we add a new node. Thus the runtime, will always be constant o(1).

"""Trees"""

#  1. This is the order that the Breadth First Search (BFS) algorithm will visit each node until finding burrito (starting from food).

#     [food]
#     [+Italian, +Indian, +Mexican]
#     [Indian, Mexican, +lasagna, +pizza]
#     [Mexican, lasagna, pizza, +tikka masala, +saag]
#     [lasagna, pizza, tikka masala, saag, +burrito, +tacos, + enchiladas]
#     [pizza, tikka masala, saag, burrito, tacos, enchiladas]
#     [tikka masala, saag, burrito, tacos, enchiladas, +thin crust, +Chicago-style, +New York-style, +Sicilian]
#     [saag, burrito, tacos, enchiladas, thin crust, Chicago-style, New York-style, Sicilian]
#     [burrito, tacos, enchiladas, thin crust, Chicago-style, New York-style, Sicilian]
#     [tacos, enchiladas, thin crust, Chicago-style, New York-style, Sicilian]
# pop(0) = burrito

# 2. This is the order that the Depth First Search (BFS) algorithm will visit each node until finding Chicago-style (starting from food).

#     [food]
#     [+Italian, +Indian, +Mexican]
#     [Italian, Indian, +burrito, +tacos, +enchiladas]
#     [Italian, Indian, burrito, tacos]
#     [Italian, Indian, burrito]
#     [Italian, Indian]
#     [Italian, +tikka masala, +saag]
#     [Italian, tikka masala]
#     [Italian, +lasagna, +pizza]
#     [Italian, lasagna, +thin crust, +Chicago-style, +New York-style, +Sicilian]
#     [Italian, lasagna, thin crust, Chicago-style, New York-style]
#     [Italian, lasagna, thin crust, Chicago-style]
#     [Italian, lasagna, thin crust]
# pop() = Chicago-style

# 3. The binary tree is made of nodes that only has a left and right child. Thus, it has a rule for arrangement often used for fast searching. Every choice that is made will reduce the number of options by half.
