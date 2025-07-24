import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
from parser.my_parser import parse_code
from interpreter.semantic_interpreter import Interpreter
import os

# Color theme (dark with red accents)
BG_COLOR = "#23272e"
FG_COLOR = "#f8f8f2"
EDITOR_BG = "#282c34"
EDITOR_FG = "#f8f8f2"
OUTPUT_BG = "#1e2127"
OUTPUT_FG = "#00ff00"  # green for normal output
OUTPUT_ERROR_FG = "#ff5555"  # red for errors
OUTPUT_WARN_FG = "#ffff00"  # yellow for warnings
OUTPUT_FONT = ("Consolas", 12, "bold")
BUTTON_BG = "#ff5555"  # red button
BUTTON_FG = "#f8f8f2"
STATUS_BG = "#23272e"
STATUS_FG = "#ff5555"

# -----------------------------
# Enhanced GUI for CustomScript (Tkinter)
# -----------------------------
class CustomScriptIDE:
    def __init__(self, root):
        self.root = root
        self.root.title("CustomScript IDE")
        self.root.geometry("900x650")
        self.filename = None

        # Menu bar
        menubar = tk.Menu(root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.new_file)
        filemenu.add_command(label="Open", command=self.open_file)
        filemenu.add_command(label="Save", command=self.save_file)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Manual", command=self.show_manual)
        helpmenu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=helpmenu)
        root.config(menu=menubar)

        # Code editor area
        self.code_area = scrolledtext.ScrolledText(root, height=20, font=("Consolas", 13), undo=True,
                                                   bg=EDITOR_BG, fg=EDITOR_FG, insertbackground=FG_COLOR)
        self.code_area.pack(padx=10, pady=(10,0), fill=tk.BOTH, expand=True)

        # Button frame
        btn_frame = tk.Frame(root, bg=BG_COLOR)
        btn_frame.pack(fill=tk.X, padx=10, pady=5)
        self.run_button = tk.Button(btn_frame, text="Run", command=self.run_code, font=("Arial", 12, "bold"),
                                    bg=BUTTON_BG, fg=BUTTON_FG, width=10, activebackground="#ff3333")
        self.run_button.pack(side=tk.LEFT, padx=5)
        self.clear_button = tk.Button(btn_frame, text="Clear Output", command=self.clear_output, font=("Arial", 12),
                                      width=12, bg=BUTTON_BG, fg=BUTTON_FG, activebackground="#ff3333")
        self.clear_button.pack(side=tk.LEFT, padx=5)

        # Output area
        self.output_area = scrolledtext.ScrolledText(root, height=10, font=OUTPUT_FONT,
                                                     bg=OUTPUT_BG, fg=OUTPUT_FG, state=tk.DISABLED, insertbackground=OUTPUT_FG)
        self.output_area.pack(padx=10, pady=(0,10), fill=tk.BOTH, expand=True)

        # Status bar
        self.status = tk.StringVar()
        self.status.set("Ready.")
        status_bar = tk.Label(root, textvariable=self.status, bd=1, relief=tk.SUNKEN, anchor=tk.W,
                             bg=STATUS_BG, fg=STATUS_FG)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        root.configure(bg=BG_COLOR)

    def run_code(self):
        """Parse and interpret code from the editor, display output or errors."""
        code = self.code_area.get("1.0", tk.END)
        self.output_area.config(state=tk.NORMAL)
        self.output_area.delete("1.0", tk.END)
        try:
            ast = parse_code(code)
            interpreter = Interpreter()
            output_lines = []
            import builtins
            orig_print = print
            def fake_print(*args, **kwargs):
                output_lines.append((' '.join(str(a) for a in args), 'output'))
            builtins.print = fake_print
            interpreter.interpret(ast)
            builtins.print = orig_print
            for line, tag in output_lines:
                self.output_area.insert(tk.END, line + "\n", tag)
            self.status.set("Execution finished successfully.")
        except Exception as e:
            self.output_area.insert(tk.END, f"Error: {e}\n", "error")
            self.status.set("Error during execution.")
        self.output_area.config(state=tk.DISABLED)
        # Tag config for colors
        self.output_area.tag_configure("output", foreground=OUTPUT_FG, font=OUTPUT_FONT)
        self.output_area.tag_configure("error", foreground=OUTPUT_ERROR_FG, font=OUTPUT_FONT)
        self.output_area.tag_configure("warning", foreground=OUTPUT_WARN_FG, font=OUTPUT_FONT)

    def clear_output(self):
        """Clear the output area."""
        self.output_area.config(state=tk.NORMAL)
        self.output_area.delete("1.0", tk.END)
        self.output_area.config(state=tk.DISABLED)
        self.status.set("Output cleared.")

    def new_file(self):
        """Create a new file in the editor."""
        self.code_area.delete("1.0", tk.END)
        self.filename = None
        self.status.set("New file.")

    def open_file(self):
        """Open a .custom file and load its content into the editor."""
        file_path = filedialog.askopenfilename(filetypes=[("CustomScript Files", "*.custom"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as f:
                self.code_area.delete("1.0", tk.END)
                self.code_area.insert(tk.END, f.read())
            self.filename = file_path
            self.status.set(f"Opened: {os.path.basename(file_path)}")

    def save_file(self):
        """Save the current editor content to a .custom file."""
        if not self.filename:
            file_path = filedialog.asksaveasfilename(defaultextension=".custom", filetypes=[("CustomScript Files", "*.custom"), ("All Files", "*.*")])
            if not file_path:
                return
            self.filename = file_path
        with open(self.filename, "w") as f:
            f.write(self.code_area.get("1.0", tk.END))
        self.status.set(f"Saved: {os.path.basename(self.filename)}")

    def show_manual(self):
        """Display the content of manual.txt in a message box."""
        try:
            with open("manual.txt", "r") as f:
                manual = f.read()
            messagebox.showinfo("Manual", manual)
        except Exception:
            messagebox.showerror("Error", "manual.txt not found.")

    def show_about(self):
        """Show information about the IDE in an about dialog."""
        messagebox.showinfo("About", "CustomScript IDE\n\nA simple interpreted language with variables, loops, if-else, and more!\n\nDeveloped with Tkinter.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CustomScriptIDE(root)
    root.mainloop()