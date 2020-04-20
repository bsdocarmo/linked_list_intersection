class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None

        if nodes is not None:
            node = Node(nodes.pop(0))
            self.head = node

            for element in nodes:
                node.next = Node(element)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next

        nodes.append("None")

        return ' -> '.join(str(x) for x in nodes)


def intersection(head1, head2):

    current1 = head1
    current2 = head2

    len1 = 0
    len2 = 0

    while current1 is not None:
        len1 += 1
        current1 = current1.next

    while current2 is not None:
        len2 += 1
        current2 = current2.next

    current1 = head1
    current2 = head2

    if len1 > len2:
        for i in range(len1 - len2):
            current1 = current1.next

    elif len2 > len1:
        for i in range(len2 - len1):
            current2 = current2.next

    while current1 is not None:
        if current1.data[0] == current2.data[0]:
            return current1
        current1 = current1.next
        current2 = current2.next

    return None


linked_list = LinkedList([["C", "Olá, teste2"], ["A", "Prezado, teste1"], ["E", "Olá, teste2"],
                          ["H", "Olá, teste1 e teste2"], ["J", "aaa"], ["B", "bca"], ["A", "asd"]])

linked_list2 = LinkedList([["D", "Prezado, teste1"], ["F", "Olá, teste2"], ["J", "Prezado, repetiu alguns emails"],
                           ["B", "as"], ["A", ""]])

result = intersection(linked_list.head, linked_list2.head)

if result is not None:
    print(result.data[0], result.data[1])
