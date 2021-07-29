class HashTable:
    def __init__(self, size=0):
        """

        """
        # make dummy memory space of size=size
        self.data = [[]] * size
        for i in range(0, size):
            self.data[i] = []
        # assume size is fixed

    def __hash(self, key):
        # _hash is used to allot address in data to store key and value.
        # address is same for same input
        # constraints:
        # address cannot exceed size of data space
        h = 0
        for i in range(0, len(key)):
            h = (h + ord(key[i]) * i) % len(self.data)
        return h

    def set(self, key, value):
        # find address
        address, bucket_i = self.get_index(key)
        pair = [key, value]
        if bucket_i is None:
            self.data[address].append(pair)
        else:
            self.data[address][bucket_i] = pair

    def get_index(self, key):
        address = self.__hash(key)
        index = 0
        bucket = self.data[address]
        for pair in bucket:
            if pair[0] == key:
                break
            index += 1
        if index == len(bucket):
            index = None
        return address, index

    def get(self, key):
        # find address
        address, bucket_i = self.get_index(key)
        if bucket_i is None:
            print("Key not found")
        else:
            pair = self.data[address][bucket_i]
            return pair[1]

    def __repr__(self):
        return '{}'.format(self.data)

    def keys(self):
        k = []
        for bucket in self.data:
            for pair in bucket:
                k.append(pair[0])
        return k


if __name__ == "__main__":
    test_table = HashTable(5)
    # print(len(test_table.keys()))
    print("Expected 'Key not found")
    test_table.get('b')
    test_table.set('a', 123)
    print('Expected test_table with pair[a, 123]')
    print(test_table)
    print('Expected 123')
    print(test_table.get('a'))
    print('Expected 0, 0')
    print(test_table.get_index('a'))
    # print(test_table)
    test_table.set('b', 456)
    print('Expected 2 elements')
    print(test_table)
    test_table.set('a', [])
    print('Expected new value in key a')
    print(test_table)
    # test_table.set('abc', 74)
    # print(test_table)
    print(test_table._HashTable__hash('adb'))
    print('Expected all keys')
    print(test_table.keys())
