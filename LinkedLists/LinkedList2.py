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


if __name__ == '__main__':

	linked_list = LinkedList()

	linked_list.head = Node(1)
	second = Node(2)
	third = Node(3)

	linked_list.head.next = second
	second.next = third

	linked_list.push(4)

	linked_list.print_linked_list()
