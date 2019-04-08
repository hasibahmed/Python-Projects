import ctypes
""" Create a dynamic array
"""


class DynamicArray():

    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        """ Returns the size of the array
        """
        return self.n

    def __getitem__(self, key):
        """ Get an element of the array
        """
        if not 0 <= key <= self.n:
            raise IndexError('index out of range')
        return self.A[key]

    def append(self, value):
        """ Append an element to the array
            resize the array if capacity reaches maximum
        """
        if self.capacity == self.n:
            self._resize(2 * self.capacity)
        self.A[self.n] = value
        self.n += 1

    def _resize(self, _capacity):
        """ Resize the array
        """
        B = self.make_array(_capacity)
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B
        self.capacity = _capacity

    def make_array(self, _capacity):
        """ Assign an array of memory with certain size
        """
        return (_capacity*ctypes.py_object)()


if __name__ == "__main__":

    import sys

    array = DynamicArray()
    default_array = []
    n = 50

    for i in range(n):
        a = len(array)
        b = sys.getsizeof(array)
        array.append(i)
        default_array.append(i)
        value = array[i]
        print(
            f'Length of array: {a}; Size in bytes: {b}; value {value}')
        print(
            f'Length of default array: {len(default_array)}; Size in bytes: {sys.getsizeof(default_array)}; value {value}')
