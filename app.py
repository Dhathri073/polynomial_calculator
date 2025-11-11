"""
Polynomial Calculator using Linked List
Python Backend with Flask
"""

from flask import Flask, render_template, request, jsonify

# Linked List Node for Polynomial Terms
class Node:
    def __init__(self, coefficient, power):
        self.coefficient = coefficient
        self.power = power
        self.next = None
    
    def __repr__(self):
        if self.coefficient == 1 and self.power != 0:
            return f"x^{self.power}" if self.power != 1 else "x"
        elif self.coefficient == -1 and self.power != 0:
            return f"-x^{self.power}" if self.power != 1 else "-x"
        elif self.power == 0:
            return str(int(self.coefficient))
        elif self.power == 1:
            return f"{int(self.coefficient)}x"
        else:
            return f"{int(self.coefficient)}x^{self.power}"


# Polynomial class using Linked List
class Polynomial:
    def __init__(self):
        self.head = None
    
    def add_term(self, coefficient, power):
        """Add a term to the polynomial (in sorted order by power)"""
        if coefficient == 0:
            return
        
        new_node = Node(coefficient, power)
        
        # If list is empty or new power is greater than head
        if self.head is None or self.head.power < power:
            new_node.next = self.head
            self.head = new_node
            return
        
        # Find the correct position
        current = self.head
        while current.next and current.next.power > power:
            current = current.next
        
        # If same power exists, combine coefficients
        if current.power == power:
            current.coefficient += coefficient
            if current.coefficient == 0:
                self.head = current.next
        else:
            new_node.next = current.next
            current.next = new_node
    
    def add_term_sorted(self, coefficient, power):
        """Add term and maintain sorted order by power (descending)"""
        if coefficient == 0:
            return
        
        new_node = Node(coefficient, power)
        
        if self.head is None:
            self.head = new_node
            return
        
        # If new power is greater than head
        if power > self.head.power:
            new_node.next = self.head
            self.head = new_node
            return
        
        # If same power as head, combine
        if power == self.head.power:
            self.head.coefficient += coefficient
            if self.head.coefficient == 0:
                self.head = self.head.next
            return
        
        # Find insertion point
        current = self.head
        while current.next and current.next.power > power:
            current = current.next
        
        # If same power exists, combine
        if current.next and current.next.power == power:
            current.next.coefficient += coefficient
            if current.next.coefficient == 0:
                current.next = current.next.next
            return
        
        new_node.next = current.next
        current.next = new_node
    
    @staticmethod
    def from_dict(coefficients):
        """Create polynomial from coefficient dictionary"""
        poly = Polynomial()
        for power in sorted(coefficients.keys(), reverse=True):
            if coefficients[power] != 0:
                poly.add_term_sorted(coefficients[power], power)
        return poly
    
    def to_dict(self):
        """Convert polynomial to coefficient dictionary"""
        coeffs = {}
        current = self.head
        while current:
            coeffs[current.power] = current.coefficient
            current = current.next
        return coeffs
    
    def to_string(self):
        """Convert polynomial to string representation"""
        if self.head is None:
            return "0"
        
        terms = []
        current = self.head
        
        while current:
            coeff = current.coefficient
            power = current.power
            
            if power == 0:
                term = str(int(coeff) if coeff == int(coeff) else coeff)
            elif power == 1:
                if coeff == 1:
                    term = "x"
                elif coeff == -1:
                    term = "-x"
                else:
                    term = f"{int(coeff) if coeff == int(coeff) else coeff}x"
            else:
                if coeff == 1:
                    term = f"x^{power}"
                elif coeff == -1:
                    term = f"-x^{power}"
                else:
                    term = f"{int(coeff) if coeff == int(coeff) else coeff}x^{power}"
            
            terms.append((term, coeff))
            current = current.next
        
        # Format with signs - fixed version
        result = ""
        for i, (term, coeff) in enumerate(terms):
            if i == 0:
                result = term
            else:
                if coeff > 0:
                    result += f" + {term}"
                else:
                    result += f" - {str(term).lstrip('-')}"
        
        return result
    
    def to_list_representation(self):
        """Get list of node representations"""
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current))
            current = current.next
        return nodes
    
    def evaluate(self, x):
        """Evaluate polynomial at x using Horner's method"""
        if self.head is None:
            return 0
        
        result = 0
        current = self.head
        
        while current:
            result += current.coefficient * (x ** current.power)
            current = current.next
        
        return result
    
    def add(self, other):
        """Add two polynomials"""
        result = Polynomial()
        
        # Add terms from self
        current = self.head
        while current:
            result.add_term_sorted(current.coefficient, current.power)
            current = current.next
        
        # Add terms from other
        current = other.head
        while current:
            result.add_term_sorted(current.coefficient, current.power)
            current = current.next
        
        return result
    
    def subtract(self, other):
        """Subtract two polynomials (self - other)"""
        result = Polynomial()
        
        # Add terms from self
        current = self.head
        while current:
            result.add_term_sorted(current.coefficient, current.power)
            current = current.next
        
        # Subtract terms from other
        current = other.head
        while current:
            result.add_term_sorted(-current.coefficient, current.power)
            current = current.next
        
        return result
    
    def multiply(self, other):
        """Multiply two polynomials"""
        result = Polynomial()
        
        current1 = self.head
        while current1:
            current2 = other.head
            while current2:
                coeff = current1.coefficient * current2.coefficient
                power = current1.power + current2.power
                result.add_term_sorted(coeff, power)
                current2 = current2.next
            current1 = current1.next
        
        return result


def parse_polynomial_string(poly_str):
    """Parse polynomial string and return Polynomial object"""
    poly_str = poly_str.lower().replace(' ', '')
    
    coefficients = {}
    terms = []
    current_term = ""
    
    for i, char in enumerate(poly_str):
        if char in ['+', '-'] and i > 0:
            terms.append(current_term)
            current_term = char if char == '-' else ""
        else:
            current_term += char
    
    if current_term:
        terms.append(current_term)
    
    for term in terms:
        if not term:
            continue
        
        term = term.strip()
        
        if 'x' not in term:
            coeff = float(term) if '.' in term else int(term)
            power = 0
        else:
            parts = term.split('x')
            
            # Parse coefficient
            coeff_str = parts[0]
            if coeff_str == '' or coeff_str == '+':
                coeff = 1
            elif coeff_str == '-':
                coeff = -1
            else:
                coeff = float(coeff_str) if '.' in coeff_str else int(coeff_str)
            
            # Parse power
            if len(parts) > 1 and parts[1]:
                if parts[1].startswith('^'):
                    power = int(parts[1][1:])
                else:
                    power = 1
            else:
                power = 1
        
        if power in coefficients:
            coefficients[power] += coeff
        else:
            coefficients[power] = coeff
    
    poly = Polynomial.from_dict(coefficients)
    return poly


# Initialize Flask app
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_polynomials', methods=['POST'])
def add_polynomials():
    try:
        data = request.json
        poly1 = parse_polynomial_string(data['poly1'])
        poly2 = parse_polynomial_string(data['poly2'])
        
        result = poly1.add(poly2)
        result_str = result.to_string()
        
        return jsonify({'result': result_str})
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/subtract_polynomials', methods=['POST'])
def subtract_polynomials():
    try:
        data = request.json
        poly1 = parse_polynomial_string(data['poly1'])
        poly2 = parse_polynomial_string(data['poly2'])
        
        result = poly1.subtract(poly2)
        result_str = result.to_string()
        
        return jsonify({'result': result_str})
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/multiply_polynomials', methods=['POST'])
def multiply_polynomials():
    try:
        data = request.json
        poly1 = parse_polynomial_string(data['poly1'])
        poly2 = parse_polynomial_string(data['poly2'])
        
        result = poly1.multiply(poly2)
        result_str = result.to_string()
        
        return jsonify({'result': result_str})
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/evaluate_polynomial', methods=['POST'])
def evaluate_polynomial():
    try:
        data = request.json
        poly = parse_polynomial_string(data['poly'])
        x = float(data['x'])
        
        result = poly.evaluate(x)
        result_value = int(result) if result == int(result) else round(result, 4)
        
        return jsonify({'result': str(result_value)})
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/get_linked_list', methods=['POST'])
def get_linked_list():
    try:
        data = request.json
        poly = parse_polynomial_string(data['poly'])
        
        nodes = poly.to_list_representation()
        
        return jsonify({'nodes': nodes})
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    # Allow configuring port and debug mode via environment (useful in Docker)
    import os
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', 'True').lower() in ('1', 'true', 'yes')
    # Bind to all interfaces so container ports are reachable from host
    app.run(debug=debug, host='0.0.0.0', port=port)
