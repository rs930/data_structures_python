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
        """
        if index > self.length - 1 or index < -self.length:
            raise IndexError("Index out of bounds")
        return self.data[index]

    def delete(self, index):
        """
        Deletes element at specified index and returns it
        Assume positive index only
        """
        a = self.data[index]
        if index >= self.length:
            raise IndexError("Index out of bounds")
        elif index == self.length - 1:
            self.pop()
        else:
            self.data = self.data[:index] + self.data[index+1:]
        return a
    
    
