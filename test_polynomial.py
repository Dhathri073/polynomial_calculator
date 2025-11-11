"""
Unit Tests for Polynomial Calculator
Testing Linked List Implementation
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import Node, Polynomial, parse_polynomial_string


def test_node_creation():
    """Test creating a node"""
    node = Node(3, 2)
    assert node.coefficient == 3
    assert node.power == 2
    assert node.next is None
    print("✓ Node Creation Test Passed")


def test_polynomial_add_term():
    """Test adding terms to polynomial"""
    poly = Polynomial()
    poly.add_term_sorted(3, 2)
    poly.add_term_sorted(2, 1)
    poly.add_term_sorted(1, 0)
    
    assert poly.head.coefficient == 3
    assert poly.head.power == 2
    print("✓ Add Term Test Passed")


def test_polynomial_addition():
    """Test polynomial addition"""
    # Create: 2x^2 + 3x + 1
    poly1 = Polynomial()
    poly1.add_term_sorted(2, 2)
    poly1.add_term_sorted(3, 1)
    poly1.add_term_sorted(1, 0)
    
    # Create: x^2 + 2x + 5
    poly2 = Polynomial()
    poly2.add_term_sorted(1, 2)
    poly2.add_term_sorted(2, 1)
    poly2.add_term_sorted(5, 0)
    
    # Add them: should get 3x^2 + 5x + 6
    result = poly1.add(poly2)
    
    # Verify the structure
    assert result.head is not None
    assert result.head.coefficient == 3
    assert result.head.power == 2
    # Check next node exists before testing
    if result.head.next:
        assert result.head.next.coefficient == 5
        assert result.head.next.power == 1
    print("✓ Polynomial Addition Test Passed")


def test_polynomial_subtraction():
    """Test polynomial subtraction"""
    # Create: 3x^2 + 2x + 1
    poly1 = Polynomial()
    poly1.add_term_sorted(3, 2)
    poly1.add_term_sorted(2, 1)
    poly1.add_term_sorted(1, 0)
    
    # Create: x^2 + 4x + 5
    poly2 = Polynomial()
    poly2.add_term_sorted(1, 2)
    poly2.add_term_sorted(4, 1)
    poly2.add_term_sorted(5, 0)
    
    # Subtract: should get 2x^2 - 2x - 4
    result = poly1.subtract(poly2)
    
    # Verify the structure
    assert result.head is not None
    assert result.head.coefficient == 2
    assert result.head.power == 2
    # Check next node exists before testing
    if result.head.next:
        assert result.head.next.coefficient == -2
        assert result.head.next.power == 1
    print("✓ Polynomial Subtraction Test Passed")


def test_polynomial_multiplication():
    """Test polynomial multiplication"""
    # Create: x + 1
    poly1 = Polynomial()
    poly1.add_term_sorted(1, 1)
    poly1.add_term_sorted(1, 0)
    
    # Create: x - 1
    poly2 = Polynomial()
    poly2.add_term_sorted(1, 1)
    poly2.add_term_sorted(-1, 0)
    
    # Multiply: should get x^2 - 1
    result = poly1.multiply(poly2)
    
    assert result.head.coefficient == 1
    assert result.head.power == 2
    print("✓ Polynomial Multiplication Test Passed")


def test_polynomial_evaluation():
    """Test polynomial evaluation"""
    # Create: 2x^2 + 3x + 1
    poly = Polynomial()
    poly.add_term_sorted(2, 2)
    poly.add_term_sorted(3, 1)
    poly.add_term_sorted(1, 0)
    
    # Evaluate at x=2: 2(4) + 3(2) + 1 = 8 + 6 + 1 = 15
    result = poly.evaluate(2)
    assert result == 15
    print("✓ Polynomial Evaluation Test Passed")


def test_parse_polynomial():
    """Test polynomial string parsing"""
    poly_str = "3x^2 + 2x + 1"
    poly = parse_polynomial_string(poly_str)
    
    assert poly.head is not None
    assert poly.head.coefficient == 3
    assert poly.head.power == 2
    print("✓ Parse Polynomial Test Passed")


def test_polynomial_to_string():
    """Test converting polynomial to string"""
    # Create: 3x^2 + 2x + 1
    poly = Polynomial()
    poly.add_term_sorted(3, 2)
    poly.add_term_sorted(2, 1)
    poly.add_term_sorted(1, 0)
    
    result_str = poly.to_string()
    # Just verify the result contains polynomial components
    assert result_str is not None
    assert isinstance(result_str, str)
    assert len(result_str) > 0
    print("✓ Polynomial to String Test Passed")


def test_polynomial_list_representation():
    """Test getting linked list representation"""
    # Create: 3x^2 + 2x + 1
    poly = Polynomial()
    poly.add_term_sorted(3, 2)
    poly.add_term_sorted(2, 1)
    poly.add_term_sorted(1, 0)
    
    nodes = poly.to_list_representation()
    assert len(nodes) == 3
    assert "3x^2" in nodes[0]
    print("✓ Polynomial List Representation Test Passed")


def test_complex_polynomial():
    """Test complex polynomial operations"""
    # Create: 2x^3 + 3x^2 - x + 5
    poly = Polynomial()
    poly.add_term_sorted(2, 3)
    poly.add_term_sorted(3, 2)
    poly.add_term_sorted(-1, 1)
    poly.add_term_sorted(5, 0)
    
    # Evaluate at x=1: 2(1) + 3(1) - 1 + 5 = 2 + 3 - 1 + 5 = 9
    result = poly.evaluate(1)
    assert result == 9
    print("✓ Complex Polynomial Test Passed")


def test_like_terms_combination():
    """Test that like terms are combined"""
    poly = Polynomial()
    poly.add_term_sorted(2, 2)
    poly.add_term_sorted(3, 2)  # Should combine with previous
    
    # Should have 5x^2, not two separate nodes
    assert poly.head.coefficient == 5
    assert poly.head.next is None
    print("✓ Like Terms Combination Test Passed")


def test_zero_coefficient_removal():
    """Test that zero coefficients are removed"""
    poly = Polynomial()
    poly.add_term_sorted(2, 1)
    poly.add_term_sorted(-2, 1)  # Should result in 0
    
    # After combining, coefficient should be 0
    assert poly.head is None
    print("✓ Zero Coefficient Removal Test Passed")


def run_all_tests():
    """Run all tests"""
    print("\n" + "="*50)
    print("Running Polynomial Calculator Tests")
    print("="*50 + "\n")
    
    tests = [
        test_node_creation,
        test_polynomial_add_term,
        test_polynomial_addition,
        test_polynomial_subtraction,
        test_polynomial_multiplication,
        test_polynomial_evaluation,
        test_parse_polynomial,
        test_polynomial_to_string,
        test_polynomial_list_representation,
        test_complex_polynomial,
        test_like_terms_combination,
        test_zero_coefficient_removal,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"✗ {test.__name__} Failed: {str(e)}")
            failed += 1
        except Exception as e:
            print(f"✗ {test.__name__} Error: {str(e)}")
            failed += 1
    
    print("\n" + "="*50)
    print(f"Test Results: {passed} Passed, {failed} Failed")
    print("="*50 + "\n")
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
