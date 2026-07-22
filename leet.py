
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

	def __repr__(self):
		return f"ListNode({self.val})"


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
	dummy = ListNode(0)
	curr = dummy
	carry = 0

	p, q = l1, l2
	while p is not None or q is not None or carry:
		x = p.val if p is not None else 0
		y = q.val if q is not None else 0
		total = x + y + carry
		carry = total // 10
		curr.next = ListNode(total % 10)
		curr = curr.next

		if p is not None:
			p = p.next
		if q is not None:
			q = q.next

	return dummy.next


def list_to_nodes(nums):
	dummy = ListNode(0)
	cur = dummy
	for n in nums:
		cur.next = ListNode(n)
		cur = cur.next
	return dummy.next


def nodes_to_list(node):
	out = []
	cur = node
	while cur:
		out.append(cur.val)
		cur = cur.next
	return out


if __name__ == "__main__":
	# Example 1
	l1 = list_to_nodes([2, 4, 3])
	l2 = list_to_nodes([5, 6, 4])
	res = add_two_numbers(l1, l2)
	print(nodes_to_list(res))  # expected [7,0,8]

	# Example 2
	l1 = list_to_nodes([0])
	l2 = list_to_nodes([0])
	res = add_two_numbers(l1, l2)
	print(nodes_to_list(res))  # expected [0]

	# Example 3
	l1 = list_to_nodes([9, 9, 9, 9, 9, 9, 9])
	l2 = list_to_nodes([9, 9, 9, 9])
	res = add_two_numbers(l1, l2)
	print(nodes_to_list(res))  # expected [8,9,9,9,0,0,0,1]

