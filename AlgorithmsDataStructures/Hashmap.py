# Create a hash table data structure from python arrays
# Hash table: key => value lookup


class Hashmap:
    def __init__(self, size):
        self.size = size
        self.map = [None] * self.size

    def _get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    def add(self, key, value):
        keyHash = self._get_hash(key)
        if self.map[keyHash] is None:
            self.map[keyHash] = [[key, value]]
            return
        for pair in self.map[keyHash]:
            if pair[0] == key:
                pair[1] = value
                return
        self.map[keyHash].append([key, value])

    def get(self, key):
        keyHash = self._get_hash(key)
        if self.map[keyHash] is None:
            return None
        for pair in self.map[keyHash]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        keyHash = self._get_hash(key)
        if self.map[keyHash] is None:
            return None
        for index, pair in enumerate(self.map[keyHash]):
            if pair[0] == key:
                del self.map[keyHash][index]
                return

    def debugPrint(self):
        print("---HASHMAP---")
        for index, item in enumerate(self.map):
            if item is not None and len(item) != 0:
                print(f"{index}: {item}")

    def print(self):
        printString = "{"
        for bucket in self.map:
            if bucket is None or len(bucket) == 0:
                continue
            for item in bucket:
                printString += f"'{item[0]}': {item[1]}, "
        printString += "}"
        print(printString)


if __name__ == "__main__":
    pairs = [
        ["alice", 111],
        ["bob", 222],
        ["charles", 33],
        ["danny", 44],
        ["eric", 55]
    ]

    hashmap = Hashmap(10)
    # Add
    for pair in pairs:
        hashmap.add(pair[0], pair[1])
        if hashmap.get(pair[0]) == pair[1]:
            print(f"Successfully added: [{pair[0]} : {pair[1]}]")

    hashmap.debugPrint()
    hashmap.print()

    # Update + Add
    updates = [
        ["alice", 122],
        ["bob", 222],
        ["charles", 33],
        ["danny", 44],
        ["eric", 55],
        ["frank", 66],
        ["greg", 77]
    ]

    for pair in updates:
        hashmap.add(pair[0], pair[1])
        if hashmap.get(pair[0]) == pair[1]:
            print(f"Successfully updated: [{pair[0]} : {pair[1]}]")

    hashmap.debugPrint()
    hashmap.print()

    # Deletions
    deletions = ["charles", "bob", "eric"]
    for item in deletions:
        hashmap.delete(item)
        if hashmap.get(item) is None:
            print(f"Successfully deleted: [{item}]")

    hashmap.debugPrint()
    hashmap.print()
