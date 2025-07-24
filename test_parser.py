# test_parser.py
# This script tests the parser with various inputs, including edge cases.

from parser import parse  # Import your parser's main parse function

def test_normal_cases():
    print("Testing normal cases...\n")
    code1 = """
    var x = 10;
    var y = x + 5;
    print(y);
    """
    try:
        parse(code1)
        print("Normal case 1: Parsed successfully.\n")
    except Exception as e:
        print("Normal case 1: Parser error:", e, "\n")

def test_edge_cases():
    print("Testing edge cases...\n")
    
    # Edge Case 1: Missing expression after '='
    code1 = "var x = ;"
    try:
        parse(code1)
        print("Edge case 1: Parsed successfully (unexpected).\n")
    except Exception as e:
        print("Edge case 1: Parser error:", e, "\n")
    
    # Edge Case 2: Missing semicolon after statement
    code2 = "var x = 10\nvar y = x + 5;"
    try:
        parse(code2)
        print("Edge case 2: Parsed successfully (unexpected).\n")
    except Exception as e:
        print("Edge case 2: Parser error:", e, "\n")
    
    # Edge Case 3: Undeclared variable in print (should parse but semantic error later)
    code3 = "print(z);"
    try:
        parse(code3)
        print("Edge case 3: Parsed successfully.\n")
    except Exception as e:
        print("Edge case 3: Parser error:", e, "\n")

if __name__ == "__main__":
    test_normal_cases()
    test_edge_cases()
