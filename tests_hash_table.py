from hash_table_chaining import HashTable

def run_tests():
    h = HashTable(capacity=4, max_load_factor=0.75)
    # Insert/search
    for i in range(100):
        h.insert(f"k{i}", i)
    assert len(h) == 100
    for i in range(100):
        assert h.search(f"k{i}") == i
    # Update
    h.insert("k10", 999)
    assert h.search("k10") == 999
    # Delete
    assert h.delete("k10") is True
    assert h.search("k10") is None
    # Missing delete
    assert h.delete("missing") is False
    print("All hash table tests passed.")

if __name__ == "__main__":
    run_tests()
