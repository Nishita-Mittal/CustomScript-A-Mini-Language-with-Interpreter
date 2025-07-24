# -----------------------------
# CLI Entry Point for CustomScript
# -----------------------------
from parser.my_parser import parse_code
from interpreter.semantic_interpreter import Interpreter
from pprint import pprint
import sys
import traceback

def main():
    """Main function to load, parse, and interpret code from code.custom or a specified file."""
    try:
        # Support optional filename argument
        filename = "code.custom"
        if len(sys.argv) > 1:
            if sys.argv[1] in ("-h", "--help"):
                print("Usage: python main.py [filename]\nDefault filename is 'code.custom'.")
                return
            filename = sys.argv[1]
        with open(filename, "r") as f:
            code = f.read()

        print(f"\nLoaded code from '{filename}':\n")
        print(code)

        ast = parse_code(code)
        print("\nGenerated AST:")
        pprint(ast)

        print("\nOutput:")
        interpreter = Interpreter()
        interpreter.interpret(ast)

    except FileNotFoundError:
        print(f"Error: File not found: '{filename}'")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
