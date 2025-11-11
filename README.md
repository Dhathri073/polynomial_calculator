# Polynomial Calculator Using Linked List

A web-based polynomial calculator application that demonstrates the use of **Linked List data structure** to represent and manipulate polynomials.

## Features

✨ **Core Features:**
- ➕ **Add Polynomials** - Add two polynomials together
- ➖ **Subtract Polynomials** - Subtract one polynomial from another
- ✖️ **Multiply Polynomials** - Multiply two polynomials
- 📊 **Evaluate Polynomials** - Calculate the value of a polynomial at a given x
- 🔗 **Visualize Linked List** - See the linked list structure of the polynomial
- 📜 **Calculation History** - Keep track of recent calculations

## Project Structure

```
polynomial-calculator/
├── app.py                    # Flask backend with Linked List implementation
├── requirements.txt          # Python dependencies
├── static/
│   ├── style.css            # Styling (CSS3, Responsive)
│   └── script.js            # Client-side logic (JavaScript)
└── templates/
    └── index.html           # Main HTML interface
```

## Technology Stack

- **Frontend:**
  - HTML5
  - CSS3 (with gradients, animations, responsive design)
  - JavaScript (ES6+)

- **Backend:**
  - Python 3.7+
  - Flask 2.3.2
  - Linked List data structure

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Step 1: Clone or Download
Navigate to the project directory:
```bash
cd polynomial-calculator
```

### Step 2: Create Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage

### Step 1: Start the Flask Server
```bash
python app.py
```

The application will start on `http://127.0.0.1:5000`

### Step 2: Open in Browser
Open your web browser and go to:
```
http://127.0.0.1:5000
```

### Step 3: Enter Polynomials
Enter polynomials in the format:
```
3x^2 + 2x + 1
x^2 + 4x + 5
2x^3 - x + 7
```

**Supported Formats:**
- `3x^2` - Polynomial with power
- `2x` - Linear term
- `5` - Constant term
- Terms can be separated by spaces or without spaces
- Support for both positive and negative coefficients

### Step 4: Perform Operations
Click any of the operation buttons:
- **Add Polynomials** - Sum two polynomials
- **Subtract Polynomials** - Difference of two polynomials
- **Multiply Polynomials** - Product of two polynomials
- **Evaluate at x** - Calculate P(x) for given x value
- **Show Linked List** - Visualize the linked list representation

## Linked List Implementation Details

### Node Structure
```python
class Node:
    def __init__(self, coefficient, power):
        self.coefficient = coefficient    # Coefficient of the term
        self.power = power               # Power of x
        self.next = None                 # Pointer to next node
```

### Polynomial Class Operations

#### 1. **add_term_sorted(coefficient, power)**
- Adds a term to the polynomial in sorted order by power
- Combines like terms automatically
- Maintains sorted order (descending powers)

#### 2. **add(other_polynomial)**
- Adds two polynomials
- Returns new polynomial with combined terms
- Time Complexity: O(m + n) where m, n are number of terms

#### 3. **subtract(other_polynomial)**
- Subtracts one polynomial from another
- Negates coefficients of second polynomial and adds
- Time Complexity: O(m + n)

#### 4. **multiply(other_polynomial)**
- Multiplies two polynomials
- Each term of first polynomial multiplies each term of second
- Time Complexity: O(m × n)

#### 5. **evaluate(x)**
- Evaluates polynomial at given x value
- Uses direct substitution method
- Time Complexity: O(n)

## API Endpoints

### 1. GET `/`
- Returns the main HTML page

### 2. POST `/add_polynomials`
- **Request:** `{"poly1": "3x^2 + 2x + 1", "poly2": "x^2 + 4x + 5"}`
- **Response:** `{"result": "4x^2 + 6x + 6"}`

### 3. POST `/subtract_polynomials`
- **Request:** `{"poly1": "3x^2 + 2x + 1", "poly2": "x^2 + 4x + 5"}`
- **Response:** `{"result": "2x^2 - 2x - 4"}`

### 4. POST `/multiply_polynomials`
- **Request:** `{"poly1": "3x^2 + 2x + 1", "poly2": "x^2 + 4x + 5"}`
- **Response:** `{"result": "3x^4 + 14x^3 + 28x^2 + 22x + 5"}`

### 5. POST `/evaluate_polynomial`
- **Request:** `{"poly": "3x^2 + 2x + 1", "x": 2}`
- **Response:** `{"result": "17"}`

### 6. POST `/get_linked_list`
- **Request:** `{"poly": "3x^2 + 2x + 1"}`
- **Response:** `{"nodes": ["3x^2", "2x", "1"]}`

## Example Usage

### Example 1: Add Polynomials
**Input:**
- Polynomial 1: `2x^2 + 3x + 1`
- Polynomial 2: `x^2 + 2x + 5`

**Output:** `3x^2 + 5x + 6`

**Linked List Representation:**
```
[2] → [3] → [1] → NULL   (First polynomial)
[1] → [2] → [5] → NULL   (Second polynomial)
[3] → [5] → [6] → NULL   (Result)
```

### Example 2: Multiply Polynomials
**Input:**
- Polynomial 1: `x + 1`
- Polynomial 2: `x - 1`

**Output:** `x^2 - 1`

### Example 3: Evaluate Polynomial
**Input:**
- Polynomial: `2x^2 + 3x + 1`
- x value: `2`

**Output:** `2(2)^2 + 3(2) + 1 = 8 + 6 + 1 = 15`

## Advantages of Linked List Representation

1. **Memory Efficient** - Only stores non-zero terms
2. **Sparse Polynomials** - Excellent for polynomials with missing terms
3. **Dynamic Size** - No need to pre-allocate memory
4. **Flexible Operations** - Easy addition and removal of terms
5. **Natural Representation** - Each term maps to a node

## Time Complexity Analysis

| Operation | Time Complexity |
|-----------|-----------------|
| Add Term | O(n) |
| Add Polynomials | O(m + n) |
| Subtract Polynomials | O(m + n) |
| Multiply Polynomials | O(m × n) |
| Evaluate | O(n) |
| Display Structure | O(n) |

## Browser Compatibility

- Chrome/Edge (Recommended)
- Firefox
- Safari
- Opera

## Responsive Design

The application is fully responsive and works on:
- Desktop computers
- Tablets
- Mobile devices

## Features Details

### Calculation History
- Stores up to 10 most recent calculations
- Displays timestamp for each calculation
- Click "Clear History" to reset

### Input Validation
- Validates polynomial format
- Provides error messages for invalid input
- Supports various polynomial formats

### Visual Feedback
- Color-coded buttons for different operations
- Success/error messages with colors
- Smooth animations and transitions

## Troubleshooting

### Issue: Port 5000 already in use
**Solution:** Change the port in `app.py` line:
```python
app.run(debug=True, host='127.0.0.1', port=5001)  # Use 5001 instead
```

### Issue: Dependencies not installing
**Solution:** Make sure you're in the virtual environment and try:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Issue: Template not found
**Solution:** Make sure you're running the app from the correct directory with the proper folder structure.

## Future Enhancements

- 📈 Polynomial graphing/visualization
- 🔢 Derivative and integral calculations
- 📱 Mobile app version
- 🌙 Dark mode
- 🔒 Session storage for polynomials
- 📤 Export results to PDF/CSV

## License

This project is open source and available for educational purposes.

## Author

Created as a Data Structures project demonstrating the use of Linked Lists in polynomial representation and computation.

## Contact & Support

For issues or suggestions, please create an issue or contact the developer.

---

**Made with ❤️ for learning Data Structures**
