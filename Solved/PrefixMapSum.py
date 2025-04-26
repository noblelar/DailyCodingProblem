

# Prefix Map Sum my version
class mapSum:
    def __init__(self):
      self.map = {}

    def insert(self, key: str, val: int) -> None:
      self.map[key] = val

    def sum(self, prefix: str) -> int:
      return sum(val for key, val in self.map.items() if key.startswith(prefix))



mapsum = mapSum()
mapsum.insert("columnar", 3)
assert mapsum.sum("col") == 3

mapsum.insert("column", 2)
assert mapsum.sum("col") == 5



# AI Solution
# The AI solution is similar to the one above, but it uses a different class name and method names. 
class PrefixMapSum:
    def __init__(self):
        self.map = {}
        
    def insert(self, key: str, value: int):
        self.map[key] = value
        
    def sum(self, prefix: str) -> int:
        return sum(value for k, value in self.map.items() if k.startswith(prefix))

# Example usage:
mapsum = PrefixMapSum()
mapsum.insert("columnar", 3)
assert mapsum.sum("col") == 3

mapsum.insert("column", 2)
assert mapsum.sum("col") == 5
