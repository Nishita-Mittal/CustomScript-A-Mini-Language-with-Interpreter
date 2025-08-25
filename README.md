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
CustomScript/<br>
│── compiler/<br>
│ ├── lexer.l # Lexical Analyzer<br>
│ ├── parser.y # Grammar & Parsing Rules<br>
│ ├── tokens.h # Token definitions<br>
│ └── ast.h # Abstract Syntax Tree structures<br>
│
│── interpreter/<br>
│ ├── interpreter.c # Interpreter implementation<br>
│ └── interpreter.py # (Optional) Python-based interpreter<br>
│
│── main.c # Entry point<br>
│── test.mini # Sample CustomScript program<br>
│── Makefile # Build instructions<br>
│── README.md # Project documentation<br>


---

## ⚡ Installation & Usage  

### 🔨 Build  
cd CustomScript<br>
make
---
### ▶️ Run
./customscript test.mini
---
### 📝 Example Code (test.mini)
- Variable & arithmetic<br>
let x = 5;<br>
let y = 10;<br>
print(x + y);<br>

- Conditional<br>
if (x < y) {<br>
    print("x is smaller");<br>
}<br>

- Loop<br>
while (x < 8) {<br>
    x = x + 1;<br>
    print(x);<br>
}<br>

- Function<br>
func add(a, b) {<br>
    return a + b;<br>
}<br>

- print(add(3, 7));<br>

---

## 🛠️ Tools & Technologies

-C, Flex, Bison → Compiler & Parser

-C/Python → Interpreter

-GTK / Tkinter (Optional) → GUI

---

## 📌 Future Improvements

-Better error handling

-More data types (float, arrays, lists)

-File I/O support

-Optimizations for speed

---

## 👨‍💻 Author<br>
Nishita Mittal<br>
📧 nishita.mittal@example.com

---

## 📜 License

This project is for educational purposes and part of a university Compiler Design project.
