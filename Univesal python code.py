# ✅ Quick Input/Output Template
import sys

def input_list():
    return list(map(int, sys.stdin.readline().split()))

def input_int():
    return int(sys.stdin.readline())

def debug(var, name="DEBUG"):
    print(f"{name}: {var}")

# 🧪 Example usage
if __name__ == "__main__":
    print("Enter numbers separated by space:")
    nums = input_list()
    debug(nums, "Input List")

    print("Enter a single number:")
    n = input_int()
    debug(n, "Single Integer")

    print("Sum:", sum(nums) + n)
