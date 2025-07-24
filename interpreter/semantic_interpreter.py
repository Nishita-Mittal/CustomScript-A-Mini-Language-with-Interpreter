# -----------------------------
# Interpreter for CustomScript
# -----------------------------

class Interpreter:
    def __init__(self):
        # Stores variable values
        self.variables = {}

    def interpret(self, ast):
        """Interpret a list of statements (the AST root)."""
        for stmt in ast:
            self.execute(stmt)

    def execute(self, node):
        """Execute a single statement node."""
        node_type = node['type']

        if node_type == 'var_decl':
            # Variable declaration
            value = self.evaluate(node['value'])
            self.variables[node['name']] = value

        elif node_type == 'assignment':
            # Assignment (must already be declared)
            value = self.evaluate(node['value'])
            if node['name'] not in self.variables:
                raise ValueError(f"Runtime Error: Undeclared variable '{node['name']}'")
            self.variables[node['name']] = value

        elif node_type == 'print':
            # Print statement
            value = self.evaluate(node['value'])
            print(value)

        elif node_type == 'while':
            # While loop
            while self.evaluate(node['condition']):
                for stmt in node['body']:
                    self.execute(stmt)

        elif node_type == 'if':
            # If or if-else statement
            if self.evaluate(node['condition']):
                for stmt in node['then']:
                    self.execute(stmt)
            elif 'else' in node:
                for stmt in node['else']:
                    self.execute(stmt)

        elif node_type == 'for':
            # For loop: emulate for(init; cond; update) { body }
            self.execute(node['init'])
            while self.evaluate(node['condition']):
                for stmt in node['body']:
                    self.execute(stmt)
                self.execute(node['update'])

        else:
            raise ValueError(f"Runtime Error: Unknown statement type '{node_type}'")

    def evaluate(self, node):
        """Evaluate an expression node and return its value."""
        node_type = node['type']

        if node_type == 'number':
            return node['value']
        elif node_type == 'var':
            if node['name'] not in self.variables:
                raise ValueError(f"Runtime Error: Undeclared variable '{node['name']}'")
            return self.variables[node['name']]
        elif node_type == 'binop':
            left = self.evaluate(node['left'])
            right = self.evaluate(node['right'])
            op = node['op']

            if op == '+': return left + right
            if op == '-': return left - right
            if op == '*': return left * right
            if op == '/': return left // right
            if op == '>': return left > right
            if op == '<': return left < right
            if op == '>=': return left >= right
            if op == '<=': return left <= right
            if op == '==': return left == right
            if op == '!=': return left != right
            else: raise ValueError(f"Runtime Error: Unknown operator '{op}'")

        else:
            raise ValueError(f"Runtime Error: Unknown expression type '{node_type}'")

# Make Interpreter importable
__all__ = ['Interpreter']
