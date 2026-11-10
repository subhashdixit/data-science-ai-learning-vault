# Mutable vs Immutable - The Most Important Python Concept! ⭐

> [!red] ⚠️ **THIS IS CRITICAL!**
> Understanding this prevents 90% of Python bugs. Read carefully!

---

## 💙 What Are They?

> [!blue] **MUTABLE** = Can be changed after creation
> Objects that can be modified in place without creating a new object
> 
> **Types:** `list`, `dict`, `set`, custom objects

> [!blue] **IMMUTABLE** = Cannot be changed after creation
> Once created, the value stays forever. Any "change" creates a NEW object
> 
> **Types:** `int`, `float`, `str`, `tuple`, `bool`, `frozenset`

---

## 🧠 The Memory Truth

> [!purple] How Python Actually Stores Objects
> ```python
> # IMMUTABLE Example
> x = 10
> print(id(x))  # Memory address: 140234567890
> 
> x = 20        # Doesn't CHANGE 10 to 20!
> print(id(x))  # Memory address: 140234567999 (DIFFERENT!)
> 
> # Python created NEW object 20
> # The original 10 still exists!
> ```

> [!purple] MUTABLE Example
> ```python
> numbers = [1, 2, 3]
> print(id(numbers))  # Address: 140234567890
> 
> numbers.append(4)   # MODIFIES same object
> print(id(numbers))  # Address: 140234567890 (SAME!)
> 
> # Python modified the SAME object in memory
> ```

---

## 🚨 THE DANGER: Shared References

> [!red] 🐛 Problem with Mutable Objects
> ```python
> # DANGER ZONE!
> list1 = [1, 2, 3]
> list2 = list1        # Both point to SAME object!
> 
> list2.append(4)
> print(list1)         # [1, 2, 3, 4] ← list1 changed too!
> print(list2)         # [1, 2, 3, 4]
> 
> print(list1 is list2)  # True - SAME object!
> ```
> 
> **Memory Diagram:**
> ```
> ┌─────────────┐
> │ [1, 2, 3, 4]│ ← Both list1 AND list2 point here
> └─────────────┘
> ```

> [!green] ✅ Solution: Make a Copy
> ```python
> list1 = [1, 2, 3]
> list2 = list1.copy()   # or list1[:] or list(list1)
> 
> list2.append(4)
> print(list1)           # [1, 2, 3] ← Unchanged!
> print(list2)           # [1, 2, 3, 4]
> 
> print(list1 is list2)  # False - DIFFERENT objects
> ```
> 
> **Memory Diagram:**
> ```
> ┌─────────────┐
> │ [1, 2, 3]   │ ← list1 points here
> └─────────────┘
> 
> ┌─────────────┐
> │ [1, 2, 3, 4]│ ← list2 points here
> └─────────────┘
> ```

> [!green] ✅ Safe with Immutable Objects
> ```python
> str1 = "hello"
> str2 = str1
> 
> str2 = str2.upper()  # Creates NEW string
> print(str1)          # "hello" ← Unchanged!
> print(str2)          # "HELLO"
> 
> print(str1 is str2)  # False
> ```

---

## 🐛 The Most Common Python Bug!

> [!red] **THE MUTABLE DEFAULT ARGUMENT BUG**
> This causes bugs in 90% of Python programs!

### The Bug

```python
def add_customer(name, customers=[]):  # 🚨 DANGER!
    customers.append(name)
    return customers

# First call
result1 = add_customer("Raj")
print(result1)  # ["Raj"] ✓

# Second call
result2 = add_customer("Priya")
print(result2)  # ["Raj", "Priya"] ← Where did Raj come from?!

# Third call
result3 = add_customer("Amit")
print(result3)  # ["Raj", "Priya", "Amit"] ← All previous names!
```

### Why It Happens

> [!yellow] 💡 The Explanation
> The default list `[]` is created ONCE when the function is **defined**, NOT each time it's called!
> 
> All function calls share the SAME list object in memory.

**Memory Diagram:**
```
Function Definition Time:
┌─────────────┐
│ []          │ ← Created ONCE, shared by ALL calls!
└─────────────┘
   ↑     ↑     ↑
 call1  call2  call3
```

### The Fix

> [!green] ✅ CORRECT Version
> ```python
> def add_customer(name, customers=None):  # Use None!
>     if customers is None:
>         customers = []  # New list for EACH call
>     customers.append(name)
>     return customers
> 
> result1 = add_customer("Raj")     # ["Raj"]
> result2 = add_customer("Priya")   # ["Priya"]
> result3 = add_customer("Amit")    # ["Amit"]
> # Each call gets its own list!
> ```

> [!yellow] **Golden Rule**
> ```python
> # ❌ NEVER use mutable defaults
> def function(arg=[]):        # Bad
> def function(arg={}):        # Bad
> def function(arg=set()):     # Bad
> 
> # ✅ Always use None
> def function(arg=None):      # Good
>     if arg is None:
>         arg = []
> ```

---

## 🎯 Function Arguments - The Trap

> [!red] Modifying Mutable Arguments
> ```python
> def modify_list(lst):
>     lst.append(99)  # Modifies ORIGINAL list!
> 
> my_list = [1, 2, 3]
> modify_list(my_list)
> print(my_list)  # [1, 2, 3, 99] ← Original changed!
> ```

> [!green] Solution 1: Return New List
> ```python
> def add_to_list(lst, item):
>     return lst + [item]  # Creates NEW list
> 
> my_list = [1, 2, 3]
> new_list = add_to_list(my_list, 99)
> print(my_list)   # [1, 2, 3] ← Original safe!
> print(new_list)  # [1, 2, 3, 99]
> ```

> [!green] Solution 2: Pass a Copy
> ```python
> def modify_list(lst):
>     lst.append(99)
> 
> my_list = [1, 2, 3]
> modify_list(my_list.copy())  # Pass copy!
> print(my_list)  # [1, 2, 3] ← Original safe!
> ```

> [!green] Solution 3: Document Mutation
> ```python
> def modify_list_inplace(lst):
>     """Modifies list IN PLACE (changes original)."""
>     lst.append(99)
>     # No return - signals modification
> ```

---

## 🔄 Shallow vs Deep Copy

> [!yellow] Shallow Copy - Copies Top Level Only
> ```python
> import copy
> 
> original = [[1, 2], [3, 4]]
> shallow = copy.copy(original)  # or original.copy()
> 
> shallow[0].append(999)
> 
> print(original)  # [[1, 2, 999], [3, 4]] ← Inner list changed!
> print(shallow)   # [[1, 2, 999], [3, 4]]
> ```
> 
> **Why:** Inner lists are still shared!
> ```
> original → [list1, list2]
>               ↓      ↓
> shallow  → [list1, list2]  ← Same inner lists!
> ```

> [!green] Deep Copy - Copies Everything Recursively
> ```python
> import copy
> 
> original = [[1, 2], [3, 4]]
> deep = copy.deepcopy(original)
> 
> deep[0].append(999)
> 
> print(original)  # [[1, 2], [3, 4]] ← Unchanged!
> print(deep)      # [[1, 2, 999], [3, 4]]
> ```

---

## 💡 When to Use What

> [!blue] Use MUTABLE Types When:
> - ✅ Data needs to change frequently
> - ✅ Building up a collection
> - ✅ Need efficient in-place modifications
> - ✅ Large datasets (avoid copying overhead)
> 
> **Examples:** Shopping cart, building a list of results

> [!blue] Use IMMUTABLE Types When:
> - ✅ Data should never change (coordinates, dates)
> - ✅ Need dictionary keys
> - ✅ Want to protect function arguments
> - ✅ Thread-safe sharing
> - ✅ Hashing/caching
> 
> **Examples:** GPS coordinates `(19.0760, 72.8777)`, configuration values

---

## 🧪 How to Check

> [!purple] Test if Object is Hashable (Immutable)
> ```python
> def is_immutable(obj):
>     try:
>         hash(obj)
>         return True
>     except TypeError:
>         return False
> 
> print(is_immutable(42))           # True (int)
> print(is_immutable("hello"))      # True (str)
> print(is_immutable((1, 2)))       # True (tuple)
> print(is_immutable([1, 2]))       # False (list)
> print(is_immutable({"a": 1}))     # False (dict)
> ```

---

## 📊 Quick Summary Table

| Aspect | Immutable | Mutable |
|--------|-----------|---------|
| **Can modify?** | ❌ No | ✅ Yes |
| **Creates new object on change?** | ✅ Yes | ❌ No |
| **Safe to share?** | ✅ Yes | ❌ No (use .copy()) |
| **Can be dict key?** | ✅ Yes | ❌ No |
| **Examples** | int, str, tuple | list, dict, set |
| **Memory address changes?** | ✅ Yes | ❌ No |
| **Thread-safe?** | ✅ Yes | ❌ No |

---

## 🎓 Interview Questions

> [!yellow] Common Interview Questions
> 1. What's the difference between mutable and immutable?
> 2. Why can't lists be dictionary keys?
> 3. What's wrong with `def func(lst=[])`?
> 4. Explain shallow vs deep copy
> 5. What does `is` operator check? (`is` vs `==`)

See: [[../../09-Interview-Prep/Python-Questions/mutable-immutable|Interview Answers]]

---

## 🔗 Related Topics

- [[variables-and-types]] - Basic types
- [[lists]] - Mutable sequences
- [[tuples]] - Immutable sequences
- [[dictionaries]] - Mutable mappings
- [[functions]] - Function arguments
- [[memory-and-references]] - How Python stores objects

---

## 📚 Resources

- [Python Docs - Data Model](https://docs.python.org/3/reference/datamodel.html)
- [Common Pitfalls](https://docs.python-guide.org/writing/gotchas/)
- [Real Python - Copying](https://realpython.com/copying-python-objects/)

---

**Tags:** #python #memory #critical #interview  
**Difficulty:** ⭐⭐⭐ (Must Master!)  
**Date Created:** 2026-11-11
