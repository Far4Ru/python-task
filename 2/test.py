from collections import deque
from time import perf_counter
from task import BufferList, BufferDeque, BufferNode

N = 100_000
items_list = BufferList()
items_deque = BufferDeque()
items_node = BufferNode()
def average_time(func, times):
    total = 0.0
    for i in range(times):
        start = perf_counter()
        func(i)
        total += (perf_counter() - start) * 1e3
    return total / times
deque_time = average_time(lambda i: items_deque.add(i), N)
list_time = average_time(lambda i: items_list.add(i), N)
node_time = average_time(lambda i: items_node.add(i), N)
print(f"BufferList: {list_time:.6} мс")
print(f"BufferNode: {node_time:.6} мс")
print(f"BufferDeque: {deque_time:.6} мс")
