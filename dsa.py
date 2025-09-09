#Data Structures and Algorithms (DSA) in Python
#1. Arrays
arr = [1, 2, 3, 4, 5]
print("Array:", arr)
print("First element:", arr[0])
print("Length of array:", len(arr))

#2. Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
# Creating a linked list and displaying it
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.display()  # Output: 1 -> 2 -> 3 -> None
#3. Stack
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print("Stack after pushes:", stack)
print("Popped element:", stack.pop())
print("Stack after pop:", stack)
#4. Queue
from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print("Queue after enqueues:", list(queue))
print("Dequeued element:", queue.popleft())
print("Queue after dequeue:", list(queue))
#5. Binary Search Tree (BST)
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_rec(self.root, key)

    def _insert_rec(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_rec(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_rec(node.right, key)

    def inorder(self):
        return self._inorder_rec(self.root)

    def _inorder_rec(self, node):
        return self._inorder_rec(node.left) + [node.val] + self._inorder_rec(node.right) if node else []
# Creating a BST and displaying its inorder traversal
bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
print("Inorder traversal of BST:", bst.inorder())  # Output: [2, 3, 4, 5, 7]
#6. Sorting Algorithms
# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
unsorted_arr = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted array:", unsorted_arr)
print("Sorted array (Bubble Sort):", bubble_sort(unsorted_arr.copy()))
# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
print("Sorted array (Quick Sort):", quick_sort(unsorted_arr.copy()))
# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr
print("Sorted array (Merge Sort):", merge_sort(unsorted_arr.copy()))
#7. Searching Algorithms
# Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
print("Linear Search for 25:", linear_search(unsorted_arr, 25))  # Output: Index of 25
# Binary Search (requires sorted array)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
sorted_arr = sorted(unsorted_arr)
print("Binary Search for 25:", binary_search(sorted_arr, 25))  # Output
# Output: Index of 25 in the sorted array
# Note: The index returned by binary search corresponds to the position in the sorted array
#8. Graphs (using adjacency list)
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def display(self):
        for node in self.graph:
            print(f"{node} -> {', '.join(map(str, self.graph[node]))}")
# Creating a graph and displaying it
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.display()
# Output:
# 1 -> 2, 3
# 2 -> 4
# 3 -> 4
#9. Hash Table
hash_table = {}
hash_table["name"] = "Alice"
hash_table["age"] = 30
hash_table["city"] = "New York"
print("Hash Table:", hash_table)
print("Name:", hash_table.get("name"))
print("Age:", hash_table.get("age"))
print("City:", hash_table.get("city"))
#10. Recursion (Factorial)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print("Factorial of 5:", factorial(5))  # Output: 120

#Algorithms in python
#1. Dijkstra's Algorithm
import heapq
def dijkstra(graph, start):
    queue = []
    heapq.heappush(queue, (0, start))
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances
# Example graph represented as an adjacency list
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
print("Dijkstra's shortest paths from A:", dijkstra(graph, 'A'))
# Output: {'A': 0, 'B': 1, 'C': 3, 'D': 4}
#2. A* Search Algorithm
def a_star(graph, start, goal, heuristic):
    open_set = set([start])
    came_from = {}
    g_score = {node: float('infinity') for node in graph}
    g_score[start] = 0
    f_score = {node: float('infinity') for node in graph}
    f_score[start] = heuristic[start]

    while open_set:
        current = min(open_set, key=lambda node: f_score[node])

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        open_set.remove(current)

        for neighbor, weight in graph[current].items():
            tentative_g_score = g_score[current] + weight

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic[neighbor]
                if neighbor not in open_set:
                    open_set.add(neighbor)

    return None
# Example heuristic (straight-line distance to goal)
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1
}
print("A* path from A to D:", a_star(graph, 'A', 'D', heuristic))
# Output: ['A', 'B', 'C', 'D']

