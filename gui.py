import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
from parser.my_parser import parse_code
from interpreter.semantic_interpreter import Interpreter
import os

# Color theme
BG_COLOR = "#23272e"
FG_COLOR = "#f8f8f2"
EDITOR_BG = "#282c34"
EDITOR_FG = "#f8f8f2"
OUTPUT_BG = "#1e2127"
OUTPUT_FG = "#00ff00"
OUTPUT_ERROR_FG = "#ff5555"
OUTPUT_WARN_FG = "#ffff00"
OUTPUT_FONT = ("Consolas", 12, "bold")
BUTTON_BG = "#ff5555"
BUTTON_FG = "#f8f8f2"
STATUS_BG = "#23272e"
STATUS_FG = "#ff5555"

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

        # Code editor frame with line numbers
        editor_frame = tk.Frame(root)
        editor_frame.pack(padx=10, pady=(10, 0), fill=tk.BOTH, expand=True)

        self.line_numbers = tk.Text(editor_frame, width=4, padx=4, takefocus=0, border=0,
                                    background=EDITOR_BG, foreground="#888888", state='disabled',
                                    font=("Consolas", 13), wrap='none')
        self.line_numbers.pack(side=tk.LEFT, fill=tk.Y)

        self.code_area = scrolledtext.ScrolledText(editor_frame, height=20, font=("Consolas", 13), undo=True,
                                                   bg=EDITOR_BG, fg=EDITOR_FG, insertbackground=FG_COLOR,
                                                   wrap='none')
        self.code_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.code_area.bind("<KeyRelease>", self.update_line_numbers)
        self.code_area.bind("<MouseWheel>", self.sync_scroll)
        self.code_area.bind("<Button-1>", self.update_line_numbers)

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
        self.update_line_numbers()

    def update_line_numbers(self, event=None):
        self.line_numbers.config(state='normal')
        self.line_numbers.delete(1.0, tk.END)
        line_count = self.code_area.index('end-1c').split('.')[0]
        line_numbers_string = "\n".join(str(i) for i in range(1, int(line_count)))
        self.line_numbers.insert(1.0, line_numbers_string)
        self.line_numbers.config(state='disabled')

    def sync_scroll(self, event):
        self.line_numbers.yview_moveto(self.code_area.yview()[0])

    def run_code(self):
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
        self.output_area.tag_configure("output", foreground=OUTPUT_FG, font=OUTPUT_FONT)
        self.output_area.tag_configure("error", foreground=OUTPUT_ERROR_FG, font=OUTPUT_FONT)
        self.output_area.tag_configure("warning", foreground=OUTPUT_WARN_FG, font=OUTPUT_FONT)

    def clear_output(self):
        self.output_area.config(state=tk.NORMAL)
        self.output_area.delete("1.0", tk.END)
        self.output_area.config(state=tk.DISABLED)
        self.status.set("Output cleared.")

    def new_file(self):
        self.code_area.delete("1.0", tk.END)
        self.filename = None
        self.status.set("New file.")
        self.update_line_numbers()

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CustomScript Files", "*.custom"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as f:
                self.code_area.delete("1.0", tk.END)
                self.code_area.insert(tk.END, f.read())
            self.filename = file_path
            self.status.set(f"Opened: {os.path.basename(file_path)}")
            self.update_line_numbers()

    def save_file(self):
        if not self.filename:
            file_path = filedialog.asksaveasfilename(defaultextension=".custom", filetypes=[("CustomScript Files", "*.custom"), ("All Files", "*.*")])
            if not file_path:
                return
            self.filename = file_path
        with open(self.filename, "w") as f:
            f.write(self.code_area.get("1.0", tk.END))
        self.status.set(f"Saved: {os.path.basename(self.filename)}")

    def show_manual(self):
        try:
            with open("manual.txt", "r") as f:
                manual = f.read()
            messagebox.showinfo("Manual", manual)
        except Exception:
            messagebox.showerror("Error", "manual.txt not found.")

    def show_about(self):
        messagebox.showinfo("About", "CustomScript IDE\n\nA simple interpreted language with variables, loops, if-else, and more!\n\nDeveloped with Tkinter.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CustomScriptIDE(root)
    root.mainloop()
