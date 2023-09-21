class PCBWithLinkedList:
    def __init__(self, parent=None):
        self.parent = parent
        self.children = []

def create_with_linked_list(parent, pcb_list):
    new_pcb = PCBWithLinkedList(parent)
    pcb_list.append(new_pcb)
    if parent is not None:
        parent.children.append(new_pcb)

def destroy_with_linked_list(pcb, pcb_list):
    for child in pcb.children:
        destroy_with_linked_list(child, pcb_list)
    pcb_list.remove(pcb)

class PCBWithoutLinkedList:
    def __init__(self, parent=None):
        self.parent = parent
        self.first_child = None
        self.younger_sibling = None
        self.older_sibling = None

def create_without_linked_list(parent, pcb_list):
    new_pcb = PCBWithoutLinkedList(parent)
    pcb_list.append(new_pcb)
    if parent is not None:
        if parent.first_child is None:
            parent.first_child = new_pcb
        else:
            sibling = parent.first_child
            while sibling.younger_sibling is not None:
                sibling = sibling.younger_sibling
            sibling.younger_sibling = new_pcb
            new_pcb.older_sibling = sibling

def destroy_without_linked_list(pcb, pcb_list):
    if pcb.first_child is not None:
        destroy_without_linked_list(pcb.first_child, pcb_list)
    if pcb.older_sibling is not None:
        pcb.older_sibling.younger_sibling = pcb.younger_sibling
    if pcb.younger_sibling is not None:
        pcb.younger_sibling.older_sibling = pcb.older_sibling
    pcb_list.remove(pcb)

def test_process_creation_destruction(pcb_list):
    create_with_linked_list(None, pcb_list)  # Create the first process
    create_with_linked_list(pcb_list[0], pcb_list)  # Create the second process
    create_with_linked_list(pcb_list[0], pcb_list)  # Create the third process
    create_with_linked_list(pcb_list[2], pcb_list)  # Create the fourth process
    create_with_linked_list(pcb_list[0], pcb_list)  # Create the fifth process

    destroy_with_linked_list(pcb_list[0], pcb_list)  # Destroy all descendants of the first process


pcb_list_with_linked_list = []
test_process_creation_destruction(pcb_list_with_linked_list)