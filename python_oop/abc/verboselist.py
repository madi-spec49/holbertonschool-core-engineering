#!/usr/bin/env python3
"""
Module that defines a VerboseList class that inherits from built-in list.
This class adds notification messages when the list is modified.
"""


class VerboseList(list):
    """
    A custom list class that prints notifications when modified.

    This class overrides append, extend, remove, and pop methods to provide
    verbose output about the operations being performed.
    """

    def append(self, item):
        """
        Add an item to the end of the list and print a notification.

        Args:
            item: The item to be added to the list
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extend the list by appending all items from the iterable.

        Args:
            iterable: The iterable whose items will be added to the list
        """
        items_count = len(list(iterable))
        super().extend(iterable)
        print(f"Extended the list with [{items_count}] items.")

    def remove(self, item):
        """
        Remove the first occurrence of an item from the list.

        Args:
            item: The item to be removed from the list

        Raises:
            ValueError: If the item is not found in the list
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=None):
        """
        Remove and return an item from the list at the given index.

        Args:
            index (int, optional): The index of the item to remove.
                                  If None, removes and returns the last item.

        Returns:
            The item that was removed from the list

        Raises:
            IndexError: If the list is empty or index is out of range
        """
        if index is None:
            # Pop the last item
            item = super().pop()
            print(f"Popped [{item}] from the list.")
            return item
        else:
            # Pop at specific index
            item = super().pop(index)
            print(f"Popped [{item}] from the list.")
            return item
