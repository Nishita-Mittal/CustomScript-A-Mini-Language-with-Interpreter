# AST Node Definitions
class ASTNode:
    pass

class Program(ASTNode):
    def __init__(self, statements):
        self.statements = statements

class PrintNode(ASTNode):
    def __init__(self, expr):
        self.expr = expr

class AssignNode(ASTNode):
    def __init__(self, var, expr):
        self.var = var
        self.expr = expr

class BinOp(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class NumNode(ASTNode):
    def __init__(self, value):
        self.value = value

class VarNode(ASTNode):
    def __init__(self, name):
        self.name = name
