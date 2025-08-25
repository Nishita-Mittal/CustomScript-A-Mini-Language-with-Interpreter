💻 CustomScript Compiler & IDE

A lightweight interpreted programming language with support for variables, arithmetic, loops, conditionals, and print statements.
Includes a lexer, parser, interpreter, along with both CLI and GUI (Tkinter) interfaces for running code.

📌 Features

✔️ Core Language Features:

Variable declaration & assignment

Arithmetic expressions

Print statements

While loops (including nesting)

If-else statements

For loops (C-style, including empty init/update and nesting)

Error handling for syntax & runtime errors

✔️ Interface Options:

CLI execution via terminal

GUI editor with Run button & output display

✔️ Extras:

Language manual (manual.txt) with examples

Sample .custom test programs

📂 Project Structure
lexer/my_lexer.py                    # Tokenizer
parser/my_parser.py                  # Parser (PLY)
interpreter/semantic_interpreter.py  # Interpreter
main.py                              # CLI entry point
gui.py                               # Tkinter GUI
manual.txt                           # Language manual & examples
*.custom                             # Sample test programs

▶️ How to Run
CLI
python main.py


👉 Runs code from code.custom.

GUI
python gui.py


👉 Opens a Tkinter-based code editor & output window.

🧑‍💻 Example Programs
🔂 For Loop Example
for (var i = 0; i < 5; i = i + 1) {
    print(i);
}

🔁 While Loop Example
var x = 3;
while (x > 0) {
    print(x);
    x = x - 1;
}

⚙️ Requirements

Python 3.7+

ply

📦 Install dependencies:

pip install -r requirements.txt

👩‍💻 Author

Nishita Mittal
📧 nishitamittal0816@gmail.com

📜 License

MIT License
