from main import PCBWithLinkedList
from main import create_with_linked_list
from main import destroy_with_linked_list
from main import PCBWithoutLinkedList
from main import create_without_linked_list
from main import destroy_without_linked_list

import time

# Test program with timing measurements
iterations = 1000000

# Test with linked list
start_time = time.time()
for _ in range(iterations):
    pcb_list_with_linked_list = [PCBWithLinkedList()]  # Initialize with PCB[0]
    create_with_linked_list(pcb_list_with_linked_list[0], pcb_list_with_linked_list)  # PCB[1]
    destroy_with_linked_list(pcb_list_with_linked_list[0], pcb_list_with_linked_list)
end_time = time.time()
print(f"Time taken with linked list: {end_time - start_time} seconds")

# Test without linked list
start_time = time.time()
for _ in range(iterations):
    pcb_list_without_linked_list = [PCBWithoutLinkedList()]  # Initialize with PCB[0]
    create_without_linked_list(pcb_list_without_linked_list[0], pcb_list_without_linked_list)  # PCB[1]
    destroy_without_linked_list(pcb_list_without_linked_list[0], pcb_list_without_linked_list)
end_time = time.time()
print(f"Time taken without linked list: {end_time - start_time} seconds")