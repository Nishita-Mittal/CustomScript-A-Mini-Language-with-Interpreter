# CustomScript Compiler & IDE

## Overview
CustomScript is a simple interpreted language with support for variables, arithmetic, while loops, if-else, and print statements. This project includes a lexer, parser, interpreter, and both CLI and GUI (Tkinter) frontends.

## Features
- Variable declaration and assignment
- Arithmetic expressions
- Print statements
- While loops (including nesting)
- If-else statements
- For loops (C-style, including empty init/update and nesting)
- Error handling for syntax and runtime errors
- GUI editor with Run button and output display

## Project Structure
```
lexer/my_lexer.py         # Tokenizer
parser/my_parser.py       # Parser (PLY)
interpreter/semantic_interpreter.py  # Interpreter
main.py                   # CLI entry point
gui.py                    # Tkinter GUI
manual.txt                # Language manual & examples
*.custom                  # Sample test programs
```

## How to Run
### CLI
```
python main.py
```
- Loads and runs code from `code.custom`.

### GUI
```
python gui.py
```
- Opens a Tkinter-based code editor and output window.

## Language Syntax Guide
See `manual.txt` for full details and examples, including the new C-style `for` loop:

### For Loop Example
```custom
for (var i = 0; i < 5; i = i + 1) {
    print(i);
}
```

## Example Program
```
var x = 3;
while (x > 0) {
    print(x);
    x = x - 1;
}
```

## Requirements
- Python 3.7+
- ply

Install dependencies:
```
pip install -r requirements.txt
```

## Authors
Nishita Mittal 
nishitamittal0816@gmail.com

## License
MIT License

