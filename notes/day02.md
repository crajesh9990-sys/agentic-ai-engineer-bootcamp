# 📚 Interview Preparation

---

## Q1. Why is Python preferred for AI?

### Key Points to Cover:

- **Rich Ecosystem**
  - LangChain
  - Transformers
  - PyTorch
  - NumPy, Pandas, Scikit-learn

- **Fast Development**
  - Quick prototyping
  - Rapid iteration cycles

- **Strong Community**
  - Extensive documentation
  - Active forums and support
  - Large AI/ML community

- **Readability**
  - Clean, intuitive syntax
  - Easy to understand and maintain
  - Reduces bugs

---

## Q2. Difference between List and Tuple

| Feature | List | Tuple |
|---------|------|-------|
| **Mutability** | Mutable (can be changed) | Immutable (cannot be changed) |
| **Syntax** | `[]` | `()` |
| **Use Case** | Good for changing/growing data | Good for fixed, constant data |
| **Performance** | Slightly slower | Slightly faster |
| **Hashable** | No (cannot be dict keys) | Yes (can be dict keys) |

### Example:
```python
# List - can modify
my_list = [1, 2, 3]
my_list[0] = 10  # ✅ Works

# Tuple - cannot modify
my_tuple = (1, 2, 3)
my_tuple[0] = 10  # ❌ TypeError

---

## Q3. What is a Dictionary?

**Key Concepts:**

- 🔑 Key-value pair storage
- ⚡ O(1) average lookup time
- 📊 Commonly used for JSON and API responses
- 🔄 Ordered (Python 3.7+)

### Example:

user = {"name": "John", "age": 30, "city": "NYC"}

## Q4. Why are list comprehensions popular?
Be ready to explain:

Advantage	Benefit
Concise syntax	Less boilerplate code
Readability	Pythonic and clean
Performance	Often faster than explicit loops
Flexibility	Can include conditions
Example Comparison:

❌ Traditional approach (verbose):

Python
squares = []
for x in range(10):
    squares.append(x ** 2)
✅ List comprehension (preferred):

Python
squares = [x ** 2 for x in range(10)]
With condition:

Python
# Get only even squares
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
Why it's faster: List comprehensions are optimized in CPython and avoid the overhead of repeated method calls.