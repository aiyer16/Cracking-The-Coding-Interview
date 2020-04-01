class SinglyLinkedListNode:

    def __init__(self, data: int):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self, data: int):
        self.head = SinglyLinkedListNode(data)

    def append(self, data: int):
        """Appends a node to the tail of the list"""
        end_node = SinglyLinkedListNode(data)
        current_node = self.head

        while (current_node.next is not None):
            current_node = current_node.next

        current_node.next = end_node

    def delete(self, data: int):
        """
        Deletes a node that matches the supplied data value.
        Removes all matches
        """
        if self.head.data == data:
            self.head = self.head.next

        current_node = self.head

        while (current_node.next is not None):
            if(current_node.next.data == data):
                current_node.next = current_node.next.next
            current_node = current_node.next

    def print(self):
        """Prints all elements of the list"""
        current_node = self.head
        list_str = ''

        while (current_node.next is not None):

            if list_str == '':
                list_str = str(current_node.data)
            else:
                list_str = list_str + '-->' + str(current_node.data)

            current_node = current_node.next

        list_str = list_str + '-->' + str(current_node.data)
        print(list_str)

    def find_kth_to_last(self, k: int, approach=1):
        """Finds and returns the Kth to last element of the list """
        # Approach 1
        if approach == 1:
            pointer_1 = self.head
            pointer_2 = self.head

            for i in range(0, k, 1):
                if pointer_1 is None:
                    return None
                else:
                    pointer_1 = pointer_1.next

            while (pointer_1):
                pointer_1 = pointer_1.next
                pointer_2 = pointer_2.next

            return pointer_2

        # Approach 2
        else:
            length = self.length()

            x = length - k
            current_node = None

            for i in range(0, x + 1, 1):
                if current_node is None:
                    current_node = self.head
                else:
                    current_node = current_node.next

            return current_node

    def length(self):
        """Returns the length of the lsit """
        length = 1
        current_node = self.head

        while (current_node.next):
            length = length + 1
            current_node = current_node.next

        return length

    def dedupe(self, use_hash: bool):
        """
        Remove all duplicates from the list.
        Implemented in two ways -
            - With hash table, complexity O(n)
            - Without hash table, complexity O(n^2)

        Parameters:
            use_hash: boolean value that decides if hash table is used
        """
        if (use_hash):

            value_count = {}
            current_node = self.head

            while (current_node.next):
                if current_node.data not in value_count:
                    value_count[current_node.data] = 1
                else:
                    value_count[current_node.data] += 1

                if (current_node.next.data) in value_count:
                    value_count[current_node.next.data] -= 1
                    current_node.next = current_node.next.next
                else:
                    current_node = current_node.next

                if not (current_node):
                    break
        else:
            current_node = self.head

            while (current_node):
                runner_node = current_node

                while (runner_node.next):
                    if (current_node.data == runner_node.next.data):
                        runner_node.next = runner_node.next.next
                    else:
                        runner_node = runner_node.next

                current_node = current_node.next


def sum_lists_reverse(llist1: SinglyLinkedList, llist2: SinglyLinkedList):
    """
    Method to sum two numbers represented by linked lists
    Each node contains 1 digit and digits are stored in reverse order

    Example:
        Input: (7-->1-->6) + (5-->9-->2)
        Output: 2-->1-->9
        Explanation: 617 + 295 = 912
    """

    result_llist = SinglyLinkedList(None)
    result = result_llist.head
    p = llist1.head
    q = llist2.head
    sum = 0
    carry = 0

    while (p is not None) or (q is not None):
        pdata = 0 if p is None else p.data
        qdata = 0 if q is None else q.data

        sum = carry + pdata + qdata

        carry = 1 if sum >= 10 else 0
        sum = sum if sum < 10 else sum % 10

        temp = SinglyLinkedListNode(data=sum)

        if (result.data is not None):
            result.next = temp
            result = result.next
        else:
            result.data = temp.data

        if (p is not None):
            p = p.next

        if (q is not None):
            q = q.next

    if carry > 0:
        temp = SinglyLinkedList(carry)
        result.next = temp

    return result_llist
