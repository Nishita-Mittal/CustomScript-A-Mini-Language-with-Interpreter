from my_lexer import tokenize

code = """
var x = 5;
var y = x + 3;
print(y);
"""

tokens = tokenize(code)

for t in tokens:
    print(t)
def test_edge_cases_lexer():
    # Edge case 1
    code1 = "var x = ;"
    tokens1 = tokenize(code1)
    print("Edge case 1 tokens:", tokens1)
    
    # Edge case 2
    code2 = "var x = 10\nvar y = x + 5;"
    tokens2 = tokenize(code2)
    print("Edge case 2 tokens:", tokens2)
    
    # Edge case 3
    code3 = "print(z);"
    tokens3 = tokenize(code3)
    print("Edge case 3 tokens:", tokens3)

if __name__ == "__main__":
    test_edge_cases_lexer()
