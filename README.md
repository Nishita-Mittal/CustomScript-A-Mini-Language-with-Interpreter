# 🚀 CustomScript Programming Language  

CustomScript is a **mini programming language** designed as part of a **Compiler Design project**.  
It includes a **lexer, parser, AST, and interpreter** with a simple **GUI**, supporting variables, expressions, conditionals, loops, functions, and error handling.  

---

## 📌 Features  
- ✨ Lexical Analysis using **Flex**  
- 🧩 Parsing using **Bison/Yacc**  
- 🌳 Abstract Syntax Tree (AST)  
- ⚙️ Interpreter with **expression evaluation**  
- 🔤 Support for **strings, integers, booleans**  
- 🔗 Operators: arithmetic, comparison, logical  
- 🔁 Control flow: `if-else`, `while`, `for`  
- 🏷️ Variables & Assignments  
- 📦 Functions with return values  
- 📌 Nested Scopes  
- ⚡ Basic error messages  

---

## 🗂️ Project Structure  
CustomScript/
│── compiler/
│ ├── lexer.l # Lexical Analyzer
│ ├── parser.y # Grammar & Parsing Rules
│ ├── tokens.h # Token definitions
│ └── ast.h # Abstract Syntax Tree structures
│
│── interpreter/
│ ├── interpreter.c # Interpreter implementation
│ └── interpreter.py # (Optional) Python-based interpreter
│
│── main.c # Entry point
│── test.mini # Sample CustomScript program
│── Makefile # Build instructions
│── README.md # Project documentation


---

## ⚡ Installation & Usage  

### 🔨 Build  
```bash
cd CustomScript
make
▶️ Run
./customscript test.mini
📝 Example Code (test.mini)
// Variable & arithmetic
let x = 5;
let y = 10;
print(x + y);

// Conditional
if (x < y) {
    print("x is smaller");
}

// Loop
while (x < 8) {
    x = x + 1;
    print(x);
}

// Function
func add(a, b) {
    return a + b;
}
print(add(3, 7));
🛠️ Tools & Technologies

C, Flex, Bison → Compiler & Parser

C/Python → Interpreter

GTK / Tkinter (Optional) → GUI

📌 Future Improvements

Better error handling

More data types (float, arrays, lists)

File I/O support

Optimizations for speed
👨‍💻 Author

Nishita Mittal
📧 nishita.mittal@example.com

📜 License

This project is for educational purposes and part of a university Compiler Design project.
