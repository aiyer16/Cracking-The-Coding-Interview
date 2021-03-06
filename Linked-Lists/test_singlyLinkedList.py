import unittest
import sys
import io

from . import singly_linked_list as sl


class TestSinglyLinkedList(unittest.TestCase):
    def test_append_one_node(self):
        llist = sl.SinglyLinkedList(1)
        llist.append(5)

        capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput     # and redirect stdout.
        llist.print()
        sys.stdout = sys.__stdout__     # Reset redirect.

        self.assertEqual('1-->5\n', capturedOutput.getvalue())

    def test_append_head(self):
        llist = sl.SinglyLinkedList(None)
        llist.append(5)

        self.assertEqual(5, llist.head.data)

    def test_remove_one_node(self):
        llist = sl.SinglyLinkedList(1)
        llist.append(5)
        llist.append(4)
        llist.append(6)
        llist.delete(4)

        capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput     # and redirect stdout.
        llist.print()
        sys.stdout = sys.__stdout__     # Reset redirect.

        self.assertEqual('1-->5-->6\n', capturedOutput.getvalue())

    def test_remove_duplicates(self):
        llist = sl.SinglyLinkedList(1)
        llist.append(5)
        llist.append(4)
        llist.append(6)
        llist.append(4)
        llist.append(6)
        llist.dedupe(use_hash=False)

        capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput     # and redirect stdout.
        llist.print()
        sys.stdout = sys.__stdout__     # Reset redirect.

        self.assertEqual('1-->5-->4-->6\n', capturedOutput.getvalue())

    def test_remove_duplicates_using_hash_table(self):
        llist = sl.SinglyLinkedList(1)
        llist.append(5)
        llist.append(4)
        llist.append(6)
        llist.append(4)
        llist.append(6)
        llist.dedupe(use_hash=True)

        capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput     # and redirect stdout.
        llist.print()
        sys.stdout = sys.__stdout__     # Reset redirect.

        self.assertEqual('1-->5-->4-->6\n', capturedOutput.getvalue())

    def test_find_kth_to_last(self):
        llist = sl.SinglyLinkedList(1)
        llist.append(4)
        llist.append(5)
        llist.append(3)
        llist.append(6)

        kth_node = llist.find_kth_to_last(2)

        self.assertEqual(3, kth_node.data)

    def test_sum_lists_reverse(self):
        llist_1 = sl.SinglyLinkedList(7)
        llist_1.append(1)
        llist_1.append(6)

        llist_2 = sl.SinglyLinkedList(5)
        llist_2.append(9)
        llist_2.append(2)

        result = sl.sum_lists_reverse(llist1=llist_1, llist2=llist_2)

        capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput     # and redirect stdout.
        result.print()
        sys.stdout = sys.__stdout__     # Reset redirect.

        self.assertEqual('2-->1-->9\n', capturedOutput.getvalue())

    def test_merge_sorted_lists(self):
        # Set up
        # Input: (1-->2-->4-->7-->10), (2-->3-->5-->9)
        llist_1 = sl.SinglyLinkedList(None)
        llist_1.append(1)
        llist_1.append(2)
        llist_1.append(4)
        llist_1.append(7)
        llist_1.append(10)

        llist_2 = sl.SinglyLinkedList(None)
        llist_2.append(2)
        llist_2.append(3)
        llist_2.append(5)
        llist_2.append(9)

        merged_llist = sl.merge_sorted_lists(llist_1, llist_2)

        capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput     # and redirect stdout.
        merged_llist.print()
        sys.stdout = sys.__stdout__     # Reset redirect.

        self.assertEqual('1-->2-->2-->3-->4-->5-->7-->9-->10\n',
                         capturedOutput.getvalue())


if __name__ == '__main__':
    unittest.main()
