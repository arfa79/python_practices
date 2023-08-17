class HashTable(object):
    def __init__(self):
        self.table = [None] * 10000  # create 10000 empty place for hash values

    def store(self, string):
        """Input a string that's stored in the table."""
        hash_value = self.calculate_hash_value(string)
        bucket_index = hash_value % len(self.table)

        # If the bucket is empty, create a list to store items
        if self.table[bucket_index] is None:
            self.table[bucket_index] = []    # when its empty we are make it equal to [] 

        # Append the string to the bucket
        self.table[bucket_index].append(string)   # append the hash value we are looking for in that index

    def lookup(self, string):
        """Return the hash value if the string is already in the table.
        Return -1 otherwise."""
        hash_value = self.calculate_hash_value(string)
        bucket_index = hash_value % len(self.table)  # finding the index of what we are looking for

        # If the bucket is not empty, check if the string is present
        if self.table[bucket_index] is not None and string in self.table[bucket_index]:
            return hash_value

        return -1

    def calculate_hash_value(self, string):
        """Helper function to calculate a hash value from a string."""
        if string:
            hash_string = (ord(string[0]) * 100) + ord(string[1]) # claculate the hash string value . * 100 is for preventing collisions
            return hash_string
        return -1

# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print(hash_table.calculate_hash_value('UDACITY'))

# Test lookup edge case
# Should be -1
print(hash_table.lookup('UDACITY'))

# Test store
hash_table.store('UDACITY')
# Should be 8568
print(hash_table.lookup('UDACITY'))

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print(hash_table.lookup('UDACIOUS'))
