# Node class to represent each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList class to manage the nodes
class LinkedList:
    def __init__(self):
        self.head = None
    
    # Method to add a node to the end of the list
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    # Method to print the linked list
    def display(self):
        if not self.head:
            print("Linked List is empty")
            return
        
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
    # Method to delete the nth node (1-based index)
    def delete_nth(self, n):
        if not self.head:
            raise ValueError("Cannot delete from an empty list")
        
        if n < 1:
            raise ValueError("Index must be at least 1")
        
        # If deleting the head node
        if n == 1:
            self.head = self.head.next
            return
        
        current = self.head
        position = 1
        
        # Traverse to the node before the one to be deleted
        while current and position < n - 1:
            current = current.next
            position += 1
        
        # Check if index is out of range
        if not current or not current.next:
            raise IndexError("Index out of range")
        
        # Delete the nth node
        current.next = current.next.next

# Test the implementation
def test_linked_list():
    try:
        # Create a new linked list
        ll = LinkedList()
        
        # Test empty list
        print("Testing empty list:")
        ll.display()
        
        # Add elements
        print("\nAdding elements 10, 20, 30, 40:")
        ll.append(10)
        ll.append(20)
        ll.append(30)
        ll.append(40)
        ll.display()
        
        # Delete 2nd node
        print("\nDeleting 2nd node:")
        ll.delete_nth(2)
        ll.display()
        
        # Delete 1st node
        print("\nDeleting 1st node:")
        ll.delete_nth(1)
        ll.display()
        
        # Test error handling
        print("\nTesting error cases:")
        # Try to delete from empty list
        empty_ll = LinkedList()
        empty_ll.delete_nth(1)  # Should raise ValueError
        
    except ValueError as e:
        print(f"ValueError: {e}")
    except IndexError as e:
        print(f"IndexError: {e}")

# Run the test
if __name__ == "__main__":
    test_linked_list()