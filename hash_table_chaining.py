from typing import Any, List, Tuple, Optional

class HashTable:
    def __init__(self, capacity: int = 16, max_load_factor: float = 0.75):
        if capacity < 4:
            capacity = 4
        self.capacity = capacity
        self.buckets: List[List[Tuple[Any, Any]]] = [[] for _ in range(self.capacity)]
        self.size = 0
        self.max_load_factor = max_load_factor

    def _index(self, key: Any) -> int:
        # Python's built-in hash is randomized per process which helps with distribution
        return hash(key) % self.capacity

    def _resize(self, new_capacity: int) -> None:
        old = self.buckets
        self.capacity = new_capacity
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        for bucket in old:
            for k, v in bucket:
                self.insert(k, v)

    def _maybe_resize(self) -> None:
        if self.size / self.capacity > self.max_load_factor:
            self._resize(self.capacity * 2)

    def insert(self, key: Any, value: Any) -> None:
        idx = self._index(key)
        bucket = self.buckets[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.size += 1
        self._maybe_resize()

    def search(self, key: Any) -> Optional[Any]:
        idx = self._index(key)
        for k, v in self.buckets[idx]:
            if k == key:
                return v
        return None

    def delete(self, key: Any) -> bool:
        idx = self._index(key)
        bucket = self.buckets[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.size -= 1
                return True
        return False

    def __len__(self):
        return self.size

def demo():
    h = HashTable()
    h.insert("apple", 10)
    h.insert("banana", 20)
    print(h.search("apple"))
    h.delete("apple")
    print(h.search("apple"))

if __name__ == "__main__":
    demo()
