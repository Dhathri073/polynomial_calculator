# Polynomial Calculator - Visual Guide & Examples

## 📊 Project Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    WEB BROWSER                              │
│  ┌──────────────────────────────────────────────────────┐   │
│  │        index.html (User Interface)                   │   │
│  │  • Input fields for polynomials                      │   │
│  │  • Operation buttons                                 │   │
│  │  • Results display                                   │   │
│  │  • History section                                   │   │
│  └──────────────────────────────────────────────────────┘   │
│            ↕ (JSON via HTTP)                                │
└─────────────────────────────────────────────────────────────┘
                          ↕
         ┌────────────────────────────────────┐
         │    script.js (Client-Side JS)      │
         │  • Event handlers                  │
         │  • API calls                       │
         │  • Result display                  │
         └────────────────────────────────────┘
                          ↕
         ┌────────────────────────────────────┐
         │   Flask Backend (app.py)           │
         │  • API endpoints                   │
         │  • Request handling                │
         │  • Response generation             │
         └────────────────────────────────────┘
                          ↕
    ┌──────────────────────────────────────────┐
    │  Linked List Data Structure              │
    │  ┌────┐    ┌────┐    ┌────┐             │
    │  │ 3  │───→│ 2  │───→│ 1  │───→ NULL   │
    │  │ x^2│    │ x  │    │    │             │
    │  └────┘    └────┘    └────┘             │
    │                                          │
    │  Represents: 3x^2 + 2x + 1              │
    └──────────────────────────────────────────┘
```

## 🔗 Linked List Node Structure

```python
class Node:
    ┌──────────────────┐
    │   coefficient    │  (e.g., 3)
    ├──────────────────┤
    │      power       │  (e.g., 2)
    ├──────────────────┤
    │      next ──────→│  (pointer to next node)
    └──────────────────┘
```

## 📝 Example 1: Addition

**Visual Representation:**

```
Polynomial 1: 3x^2 + 2x + 1
Linked List 1:
┌────────────┬────────────┬────────────┐
│ Coeff: 3   │ Coeff: 2   │ Coeff: 1   │
│ Power: 2   │ Power: 1   │ Power: 0   │
└────────────┴────────────┴────────────┘
    ↓ 3x^2       ↓ 2x        ↓ 1

Polynomial 2: x^2 + 4x + 5
Linked List 2:
┌────────────┬────────────┬────────────┐
│ Coeff: 1   │ Coeff: 4   │ Coeff: 5   │
│ Power: 2   │ Power: 1   │ Power: 0   │
└────────────┴────────────┴────────────┘
    ↓ x^2       ↓ 4x        ↓ 5

ADDITION PROCESS:
Same powers are combined:
- x^2: 3 + 1 = 4
- x:   2 + 4 = 6
- 1:   1 + 5 = 6

Result: 4x^2 + 6x + 6
Result Linked List:
┌────────────┬────────────┬────────────┐
│ Coeff: 4   │ Coeff: 6   │ Coeff: 6   │
│ Power: 2   │ Power: 1   │ Power: 0   │
└────────────┴────────────┴────────────┘
```

## ✖️ Example 2: Multiplication

**Polynomial 1:** (x + 1)
```
Node 1: coefficient=1, power=1 (x)
Node 2: coefficient=1, power=0 (1)
```

**Polynomial 2:** (x - 1)
```
Node 1: coefficient=1, power=1 (x)
Node 2: coefficient=-1, power=0 (-1)
```

**Multiplication Process:**
```
(x + 1) × (x - 1)

Step 1: x × x = x^2      (coeff=1, power=2)
Step 2: x × (-1) = -x    (coeff=-1, power=1)
Step 3: 1 × x = x        (coeff=1, power=1)
Step 4: 1 × (-1) = -1    (coeff=-1, power=0)

Combine like terms (power 1):
-1 + 1 = 0 (removed)

Result: x^2 - 1
```

## 📊 Example 3: Evaluation

**Polynomial:** 2x^2 + 3x + 1
**Evaluate at x = 2**

```
P(x) = 2x^2 + 3x + 1
P(2) = 2(2)^2 + 3(2) + 1
     = 2(4) + 6 + 1
     = 8 + 6 + 1
     = 15

Result: 15
```

**Linked List Traversal:**
```
Head: [2, 2] → [3, 1] → [1, 0] → NULL

Step 1: 2 * (2^2) = 8
Step 2: 3 * (2^1) = 6
Step 3: 1 * (2^0) = 1

Sum: 8 + 6 + 1 = 15
```

## 🔄 Algorithm: Combine Like Terms

```
Algorithm: Combine(poly1_node, poly2_node)
    result = empty list
    
    while poly1_node != NULL AND poly2_node != NULL:
        if poly1_node.power == poly2_node.power:
            combined_coeff = poly1_node.coeff + poly2_node.coeff
            if combined_coeff != 0:
                add node(combined_coeff, poly1_node.power) to result
            poly1_node = poly1_node.next
            poly2_node = poly2_node.next
        
        else if poly1_node.power > poly2_node.power:
            add node(poly1_node.coeff, poly1_node.power) to result
            poly1_node = poly1_node.next
        
        else:
            add node(poly2_node.coeff, poly2_node.power) to result
            poly2_node = poly2_node.next
    
    // Append remaining nodes
    while poly1_node != NULL:
        add poly1_node to result
        poly1_node = poly1_node.next
    
    while poly2_node != NULL:
        add poly2_node to result
        poly2_node = poly2_node.next
    
    return result
```

## 🧮 Multiplication Algorithm

```
Algorithm: Multiply(poly1, poly2)
    result = empty polynomial
    
    for each node n1 in poly1:
        for each node n2 in poly2:
            new_coeff = n1.coeff * n2.coeff
            new_power = n1.power + n2.power
            add_term(result, new_coeff, new_power)
    
    return result
```

## 📈 Space & Time Complexity

### Space Complexity
```
Polynomial with n terms:
- Array representation: O(max_degree)
- Linked List: O(n)  ← Much better for sparse polynomials!

Example:
Sparse polynomial: x^1000 + 1
- Array: O(1000) space
- Linked List: O(2) space ✓
```

### Time Complexity

| Operation | Formula | Complexity |
|-----------|---------|------------|
| Add | O(m + n) | Linear |
| Subtract | O(m + n) | Linear |
| Multiply | O(m × n) | Quadratic |
| Evaluate | O(n) | Linear |
| Insert | O(n) | Linear |
| Delete | O(n) | Linear |

Where m and n are number of terms in polynomials.

## 🎯 Input Examples

### Valid Inputs
```
✓ 3x^2 + 2x + 1
✓ 3x^2+2x+1
✓ x^2 + x + 1
✓ -x^2 + 2x + 1
✓ 5 (constant)
✓ 2x (linear only)
✓ x^5 - 3x^2 + 2
✓ -2x^3 + x^2 - x + 7
```

### Invalid Inputs
```
✗ Empty string
✗ 3y^2 + 2y (wrong variable)
✗ 3x2 (missing ^)
✗ Special characters except + - ^
```

## 🎨 UI Components

```
┌────────────────────────────────────────┐
│          HEADER (Purple Gradient)      │
│    🔢 Polynomial Calculator            │
│    Using Linked List Data Structure    │
└────────────────────────────────────────┘

┌────────────────────────────────────────┐
│    INPUT SECTION (Light Gray)          │
│  • Polynomial 1 Input Field            │
│  • Polynomial 2 Input Field            │
└────────────────────────────────────────┘

┌────────────────────────────────────────┐
│    OPERATIONS SECTION (Light Gray)     │
│  [Add] [Subtract] [Multiply]           │
│  [Evaluate] [Show List]                │
└────────────────────────────────────────┘

┌────────────────────────────────────────┐
│    RESULTS SECTION (White Box)         │
│  Results display here...               │
└────────────────────────────────────────┘

┌────────────────────────────────────────┐
│    LINKED LIST SECTION (White Box)     │
│  [3x^2] → [2x] → [1] → NULL            │
└────────────────────────────────────────┘

┌────────────────────────────────────────┐
│    HISTORY SECTION (White Box)         │
│  Recent calculations listed here       │
└────────────────────────────────────────┘
```

## 🔌 API Flow Diagram

```
User Input
    ↓
[JavaScript Handler]
    ↓
POST /add_polynomials {poly1, poly2}
    ↓
[Flask Route Handler]
    ↓
[Parse Polynomials] → Create Linked Lists
    ↓
[Combine Terms] → Traverse Lists
    ↓
[Generate Result] → Format Output
    ↓
JSON Response {result}
    ↓
[Display in Browser]
    ↓
Update History & UI
```

## 💾 File Dependencies

```
index.html
├── links to → style.css (CSS styling)
└── links to → script.js (JavaScript)

script.js
├── sends requests to → /add_polynomials
├── sends requests to → /subtract_polynomials
├── sends requests to → /multiply_polynomials
├── sends requests to → /evaluate_polynomial
└── sends requests to → /get_linked_list

app.py
├── imports → Node class
├── imports → Polynomial class
├── imports → parse_polynomial_string function
└── defines → Flask routes & endpoints
```

## 🚀 Performance Characteristics

### Adding Two Polynomials
```
Worst Case: Both polynomials fully dense
Time: O(m + n) where m, n = number of terms
Space: O(m + n) for result

Example:
Poly1: x^100 + x^99 + ... + x + 1 (101 terms)
Poly2: x^100 + x^99 + ... + x + 1 (101 terms)
Result: 2x^100 + 2x^99 + ... + 2x + 2 (101 terms)

Time Complexity: O(101 + 101) = O(202) ✓ Linear
```

### Multiplying Two Polynomials
```
Poly1: x^10 (1 term)
Poly2: x^10 (1 term)
Result: x^20 (1 term)

vs.

Poly1: x^10 + x^9 + ... + 1 (11 terms)
Poly2: x^10 + x^9 + ... + 1 (11 terms)
Result: Potentially many terms

Time Complexity: O(11 × 11) = O(121)
```

---

**This visual guide helps understand how the Polynomial Calculator works internally!**
