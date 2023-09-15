class PCBWithLinkedList:
    def __init__(self, parent=None):
        self.parent = parent
        self.children = []

def create_with_linked_list(parent, pcb_list):
    new_pcb = PCBWithLinkedList(parent)
    pcb_list.append(new_pcb)
    parent.children.append(new_pcb)

def destroy_with_linked_list(pcb, pcb_list):
    for child in pcb.children:
        destroy_with_linked_list(child, pcb_list)
        pcb_list.remove(child)

class PCBWithoutLinkedList:
    def __init__(self, parent=None):
        self.parent = parent
        self.first_child = None
        self.younger_sibling = None
        self.older_sibling = None

def create_without_linked_list(parent, pcb_list):
    new_pcb = PCBWithoutLinkedList(parent)
    pcb_list.append(new_pcb)

    if parent:
        if not parent.first_child:
            parent.first_child = new_pcb
        else:
            sibling = parent.first_child
            while sibling.younger_sibling:
                sibling = sibling.younger_sibling
            sibling.younger_sibling = new_pcb
            new_pcb.older_sibling = sibling

def destroy_without_linked_list(pcb, pcb_list):
    while pcb.first_child:
        destroy_without_linked_list(pcb.first_child, pcb_list)
    pcb_list.remove(pcb)
    if pcb.parent:
        if pcb.parent.first_child == pcb:
            pcb.parent.first_child = pcb.younger_sibling
        if pcb.older_sibling:
            pcb.older_sibling.younger_sibling = pcb.younger_sibling
        if pcb.younger_sibling:
            pcb.younger_sibling.older_sibling = pcb.older_sibling

# Test program
pcb_list_with_linked_list = [PCBWithLinkedList()]  # Initialize with PCB[0]
pcb_list_without_linked_list = [PCBWithoutLinkedList()]  # Initialize with PCB[0]

# Create processes
create_with_linked_list(pcb_list_with_linked_list[0], pcb_list_with_linked_list)  # PCB[1]
create_with_linked_list(pcb_list_with_linked_list[0], pcb_list_with_linked_list)  # PCB[2]
create_with_linked_list(pcb_list_with_linked_list[2], pcb_list_with_linked_list)  # PCB[3]
create_with_linked_list(pcb_list_with_linked_list[0], pcb_list_with_linked_list)  # PCB[4]

create_without_linked_list(pcb_list_without_linked_list[0], pcb_list_without_linked_list)  # PCB[1]
create_without_linked_list(pcb_list_without_linked_list[0], pcb_list_without_linked_list)  # PCB[2]
create_without_linked_list(pcb_list_without_linked_list[2], pcb_list_without_linked_list)  # PCB[3]
create_without_linked_list(pcb_list_without_linked_list[0], pcb_list_without_linked_list)  # PCB[4]

# Destroy processes
destroy_with_linked_list(pcb_list_with_linked_list[0], pcb_list_with_linked_list)
destroy_without_linked_list(pcb_list_without_linked_list[0], pcb_list_without_linked_list)
