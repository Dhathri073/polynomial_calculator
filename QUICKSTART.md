# Quick Start Guide

## 🚀 Getting Started in 3 Easy Steps

### Step 1: Install Dependencies
Open PowerShell in the project folder and run:
```powershell
pip install -r requirements.txt
```

### Step 2: Start the Application
```powershell
python app.py
```

You should see:
```
WARNING in app.run() is not recommended for production use...
Running on http://127.0.0.1:5000
```

### Step 3: Open in Browser
Visit: **http://127.0.0.1:5000**

---

## 📝 Example Calculations

### Example 1: Addition
```
Polynomial 1: 2x^2 + 3x + 1
Polynomial 2: x^2 + 2x + 5
Operation: Click "Add Polynomials"
Result: 3x^2 + 5x + 6
```

### Example 2: Multiplication
```
Polynomial 1: x + 1
Polynomial 2: x - 1
Operation: Click "Multiply Polynomials"
Result: x^2 - 1
```

### Example 3: Evaluation
```
Polynomial 1: 2x^2 + 3x + 1
x value: 2
Operation: Click "Evaluate at x", enter 2
Result: 15
```

### Example 4: View Structure
```
Polynomial 1: 3x^2 + 2x + 1
Operation: Click "Show Linked List"
Structure: [3x^2] → [2x] → [1] → NULL
```

---

## ✨ Supported Input Formats

All these formats work:
- `3x^2 + 2x + 1`
- `3x^2+2x+1`
- `3x^2 + 2x + 1` (with spaces)
- `x^2 + x + 1` (omitting coefficient 1)
- `-x^2 + 2x + 1` (negative coefficients)
- `5` (constant only)
- `x` (linear only)

---

## 🔗 About the Linked List

Each polynomial is stored as a **linked list** where:
- Each **node** contains a term (coefficient and power)
- Nodes are **sorted by power** (highest power first)
- **Like terms are combined** automatically
- **NULL pointer** marks the end

Example:
```
Polynomial: 3x^2 + 2x + 1

Linked List:
[Coeff: 3, Power: 2] → [Coeff: 2, Power: 1] → [Coeff: 1, Power: 0] → NULL
       3x^2                   2x                      1
```

---

## 🆘 Troubleshooting

| Problem | Solution |
|---------|----------|
| Port 5000 in use | Change port in app.py (line ~130) to 5001, 5002, etc. |
| ModuleNotFoundError: Flask | Run `pip install flask` |
| Template not found | Make sure you're in the correct directory |
| Can't connect to server | Check that Flask app is running and port is correct |

---

## 📚 Project Structure

```
polynomial-calculator/
├── app.py                    ← Python Backend (Linked List, Flask)
├── requirements.txt          ← Dependencies
├── README.md                 ← Full Documentation
├── QUICKSTART.md             ← This file
├── static/
│   ├── style.css            ← CSS Styling
│   └── script.js            ← JavaScript Frontend
└── templates/
    └── index.html           ← HTML Interface
```

---

## 🎯 Key Operations

| Button | Function |
|--------|----------|
| Add | Adds polynomial 1 + polynomial 2 |
| Subtract | Calculates polynomial 1 - polynomial 2 |
| Multiply | Multiplies polynomial 1 × polynomial 2 |
| Evaluate at x | Calculates P(x) for polynomial 1 |
| Show Linked List | Displays the linked list structure |
| Clear History | Removes calculation history |

---

## ⏱️ Time Complexity

- **Addition:** O(m + n)
- **Subtraction:** O(m + n)
- **Multiplication:** O(m × n)
- **Evaluation:** O(n)

Where m and n are the number of terms in each polynomial.

---

## 🎨 Features

✅ Real-time calculation
✅ Visual linked list representation
✅ Calculation history (last 10)
✅ Input validation
✅ Responsive design
✅ Error handling
✅ Support for complex polynomials
✅ Clean, modern UI

---

## 💡 Tips

1. **Use Format:** Type polynomials exactly like the examples shown
2. **Both Fields:** Always enter both polynomial 1 and 2 for operations
3. **Evaluation:** Use Show Linked List first to understand the structure
4. **History:** Check history for previous calculations
5. **Mobile:** Works on mobile devices too!

---

Enjoy using the Polynomial Calculator! 🎉
