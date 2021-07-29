class StaticArray:
    def __init__(self):
        """
        Initializes instance of StaticArray
        """
        self.length = 0
        self.data = []

    def insert(self, element, index=0):
        """
        Inserts element at specified index
        :param element:
        :param index:
        :return: None
        """
        if index > self.length - 1:
            raise IndexError("Index out of bounds")
        else:
            # insert a new cell with dummy data at end
            self.data.append(0)
            self.length += 1
            # shift data from index by one unit to right
            for i in range(index, self.length-1):
                self.data[i+1] = self.data[i]
            # insert element at index
            self.data[index] = element

    def push(self, element):
        self.data.append(element)
        self.length += 1

    @property
    def pop(self):
        """
        Removes last element in data and returns it
        :return: last element
        """
        last_element = self.data[self.length - 1]
        self.data = self.data[0:self.length-1]
        self.length -= 1
        return last_element

    def get(self, index):
        """
        Return element at index position in array
        :param index:
        :return: element
        """
        if index > self.length - 1 or index < -self.length:
            raise IndexError("Index out of bounds")
        return self.data[index]

    def delete(self, index):
        """
        Deletes element at specified index and returns it
        Assume positive index only
        :param index:
        :return: element
        """
        a = self.data[index]
        if index >= self.length:
            raise IndexError("Index out of bounds")
        elif index == self.length - 1:
            self.pop()
        else:
            self.data = self.data[:index] + self.data[index+1:]
        return a

    @staticmethod
    def merge_arrays(a, b):
        """
        Merge two sorted array into single sorted array
        """
        c = []
        i_1 = 0
        i_2 = 0
        while i_1 < len(a) and i_2 < len(b):
            current_a = a[i_1]
            current_b = b[i_2]
            if current_a < current_b:
                c.append(current_a)
                i_1 += 1
            elif current_a > current_b:
                c.append(current_b)
                i_2 += 1
            else:
                c.append([current_a, current_b])
                i_1 += 1
                i_2 += 1

        if i_1 < len(a):
            c = c + a[i_1:]
        if i_2 < len(b):
            c = c + b[i_2:]
        return c


if __name__ == "__main__":
    a = [1]
    b = [2]
    ob = StaticArray()
    print(ob.merge_arrays(a, b))
