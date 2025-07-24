from parser import parse

sample_code = """
var x = 5;
var y = x + 3;
print(y);
"""

ast = parse(sample_code)

def print_ast(node, indent=0):
    space = '  ' * indent
    if isinstance(node, Program):
        print(f"{space}Program:")
        for stmt in node.statements:
            print_ast(stmt, indent + 1)
    elif isinstance(node, PrintNode):
        print(f"{space}Print:")
        print_ast(node.expr, indent + 1)
    elif isinstance(node, AssignNode):
        print(f"{space}Assign: {node.var} =")
        print_ast(node.expr, indent + 1)
    elif isinstance(node, BinOp):
        print(f"{space}BinOp: {node.op}")
        print_ast(node.left, indent + 1)
        print_ast(node.right, indent + 1)
    elif isinstance(node, NumNode):
        print(f"{space}Number: {node.value}")
    elif isinstance(node, VarNode):
        print(f"{space}Variable: {node.name}")

print_ast(ast)
