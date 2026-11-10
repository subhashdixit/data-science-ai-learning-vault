# NumPy - Numerical Computing

> [!blue] 💙 **What is NumPy?**
> Numerical Python - The foundation library for scientific computing in Python. 10-100x faster than Python lists!

---

## 📚 Topics

### Basics
- [ ] [[arrays-basics|Arrays Basics]] - Creating and inspecting arrays
- [ ] [[array-operations|Array Operations]] - Mathematical operations
- [ ] [[indexing-slicing|Indexing & Slicing]] - Accessing array elements
- [ ] [[broadcasting|Broadcasting]] - Operations on different shapes

### Intermediate
- [ ] [[reshaping|Reshaping]] - reshape, flatten, ravel
- [ ] [[stacking-splitting|Stacking & Splitting]] - Combining arrays
- [ ] [[linear-algebra|Linear Algebra]] - Matrix operations
- [ ] [[statistics|Statistics]] - mean, median, std, etc.

### Advanced
- [ ] [[vectorization|Vectorization]] - Fast operations without loops
- [ ] [[memory-layout|Memory Layout]] - C vs Fortran order
- [ ] [[performance|Performance Tips]] - Speed optimization

---

## 🎯 Why Learn NumPy?

> [!yellow] **Speed Comparison**
> ```python
> # Python list
> import time
> numbers = list(range(1000000))
> start = time.time()
> result = [x**2 for x in numbers]
> print(f"List: {time.time() - start:.3f}s")  # ~0.5s
> 
> # NumPy array
> import numpy as np
> numbers_np = np.arange(1000000)
> start = time.time()
> result_np = numbers_np ** 2
> print(f"NumPy: {time.time() - start:.3f}s")  # ~0.005s
> ```
> 
> **NumPy is 100x faster!** ⚡

---

## 💚 Quick Examples

> [!green] Creating Arrays
> ```python
> import numpy as np
> 
> # From list
> arr = np.array([1, 2, 3, 4, 5])
> 
> # Zeros, ones, empty
> zeros = np.zeros((3, 4))
> ones = np.ones((2, 3))
> 
> # Range
> sequence = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]
> 
> # Linear space
> linspace = np.linspace(0, 1, 5)  # [0, 0.25, 0.5, 0.75, 1]
> ```

> [!green] Array Operations
> ```python
> arr = np.array([1, 2, 3, 4, 5])
> 
> # Element-wise operations
> print(arr + 10)      # [11, 12, 13, 14, 15]
> print(arr * 2)       # [2, 4, 6, 8, 10]
> print(arr ** 2)      # [1, 4, 9, 16, 25]
> 
> # Statistical operations
> print(arr.mean())    # 3.0
> print(arr.std())     # 1.414...
> print(arr.sum())     # 15
> ```

---

## 🚨 Common Pitfalls

> [!red] Shallow Copy Issue
> ```python
> # ❌ WRONG - Creates a view, not a copy!
> arr1 = np.array([1, 2, 3])
> arr2 = arr1
> arr2[0] = 99
> print(arr1)  # [99, 2, 3] - Original changed!
> 
> # ✅ CORRECT - Use .copy()
> arr2 = arr1.copy()
> ```

---

## 🎓 Interview Prep

- [ ] What's the difference between NumPy array and Python list?
- [ ] Explain broadcasting with example
- [ ] How does NumPy achieve speed?
- [ ] What is vectorization?

See: [[../../09-Interview-Prep/ML-Theory/numpy-questions|NumPy Interview Questions]]

---

## 🔗 Related
- [[../Python/README|Python]] (prerequisite)
- [[../Pandas/README|Pandas]] (next step)
- [[../../03-Machine-Learning/README|Machine Learning]] (applications)

---

**Tags:** #numpy #foundations #numerical-computing  
**Status:** 🔴 Not Started  
**Prerequisites:** Python basics
