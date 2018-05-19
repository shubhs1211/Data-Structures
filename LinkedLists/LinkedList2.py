class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:

	def __init__(self):
		self.head = None

	def print_linked_list(self):
		temp = self.head
		while temp:
			print(temp.data)
			temp = temp.next

	def push(self, data):
		new_node = Node(data)
		new_node.next = linked_list.head
		linked_list.head = new_node

	def insert_after(self, node, data):
		if node is None:
			print("The node does not exist.")
			return
		new_node = Node(data)
		
		new_node.next = node.next
		node.next = new_node

	def append(self, data):
		new_node = Node(data)
		temp = self.head
		while temp.next:
			temp = temp.next
		temp.next = new_node


if __name__ == '__main__':

	linked_list = LinkedList()

	linked_list.head = Node(1)
	second = Node(2)
	third = Node(3)

	linked_list.head.next = second
	second.next = third

	print("Linked List")
	linked_list.print_linked_list()
	
	print("Linked List after pushing 4")
	linked_list.push(4)
	linked_list.print_linked_list()

	print("Linked List after inserting 5 after second")
	linked_list.insert_after(second, 5)
	linked_list.print_linked_list()

	print("Linked List after append 9")
	linked_list.append(9)
	linked_list.print_linked_list()
