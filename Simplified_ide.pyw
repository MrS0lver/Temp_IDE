# import tkinter as tk
# from tkinter import filedialog 
# from tkinter import scrolledtext
# import subprocess
# import threading
# import os
# import webbrowser

# class SimpleIDE:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Advanced C/C++ IDE")
#         self.root.geometry("800x700")
#         self.root.configure(bg="#2b2b2b")  

#         self.menu_bar = tk.Menu(self.root, bg="#1f1f1f", fg="white")

#         self.file_menu = tk.Menu(self.menu_bar, tearoff=0, bg="#333333", fg="white")
#         self.file_menu.add_command(label="New", command=self.new_file)
#         self.file_menu.add_command(label="Open", command=self.open_file)
#         self.file_menu.add_command(label="Save", command=self.save_file)
#         self.file_menu.add_command(label="Save As", command=self.save_file_as)
#         self.file_menu.add_separator()
#         self.file_menu.add_command(label="Exit", command=self.root.quit)
#         self.menu_bar.add_cascade(label="File", menu=self.file_menu)

#         self.social_menu = tk.Menu(self.menu_bar, tearoff=0, bg="#333333", fg="white")
#         self.social_menu.add_command(label="Twitter", command=lambda: webbrowser.open("https://x.com/Mrs0lver"))
#         self.social_menu.add_command(label="Instagram", command=lambda: webbrowser.open("https://www.instagram.com/dev_pico/"))
#         self.social_menu.add_command(label="GitHub", command=lambda: webbrowser.open("https://github.com/MrS0lver"))
#         self.social_menu.add_separator()
#         self.social_menu.add_command(label="Exit", command=self.root.quit)
#         self.menu_bar.add_cascade(label="Social", menu=self.social_menu)

#         self.root.config(menu=self.menu_bar)

#         self.frame = tk.Frame(self.root, bg="#2b2b2b")
#         self.frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

#         self.line_numbers = tk.Text(self.frame, width=4, padx=3, takefocus=0, border=0, background='#282828', fg='#8c8c8c', state='disabled', wrap='none', font=("Courier New", 12))
#         self.line_numbers.pack(side=tk.LEFT, fill=tk.Y)

#         self.text_area = scrolledtext.ScrolledText(self.frame, wrap='word', undo=True, width=80, height=15, font=("Courier New", 12), bg="#1e1e1e", fg="#ffffff", insertbackground="white")
#         self.text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

#         self.text_area.bind('<KeyRelease>', self.update_line_numbers)

#         self.output_area = scrolledtext.ScrolledText(self.root, wrap='word', width=80, height=8, font=("Courier New", 10), bg="#2b2b2b", fg="white")
#         self.output_area.pack(pady=10, padx=10, fill=tk.X)

#         self.run_button = tk.Button(self.root, text="Run", command=self.run_code, bg="#61afef", fg="white", font=("Arial", 10))
#         self.run_button.pack(side=tk.LEFT, padx=10, pady=10)

#         self.clear_button = tk.Button(self.root, text="Clear Output", command=self.clear_output, bg="#e06c75", fg="white", font=("Arial", 10))
#         self.clear_button.pack(side=tk.LEFT, padx=10, pady=10)

#     def update_line_numbers(self, event=None):
#         self.line_numbers.yview_moveto(self.text_area.yview()[0])

#         self.line_numbers.config(state='normal')
#         self.line_numbers.delete('1.0', tk.END)
#         line_count = self.text_area.index(tk.END).split('.')[0]
#         line_numbers_string = "\n".join(str(i) for i in range(1, int(line_count)))
#         self.line_numbers.insert(tk.END, line_numbers_string)
#         self.line_numbers.config(state='disabled')

#     def new_file(self):
#         self.text_area.delete('1.0', tk.END)

#     def open_file(self):
#         pass
#     def save_file(self):
#         pass  
#     def save_file_as(self):
#         pass  

#     def run_code(self):
#         threading.Thread(target=self.run_code_thread, daemon=True).start()

#     def run_code_thread(self):
#         code = self.text_area.get("1.0", tk.END)
#         filename = "temp_code.cpp"
        
#         try:
#             with open(filename, "w") as f:
#                 f.write(code)
#         except Exception as e:
#             self.output_area.delete("1.0", tk.END)
#             self.output_area.insert(tk.END, f"Error writing file: {e}")
#             return

#         compile_command = f"g++ {filename} -o temp_code.exe"
#         try:
#             # Compile the code
#             subprocess.run(compile_command, check=True, shell=True, stderr=subprocess.PIPE)

#             # Run the executable without opening a console window (if on Windows)
#             if os.name == 'nt':  # For Windows
#                 result = subprocess.Popen(
#                     "./temp_code.exe",
#                     stdout=subprocess.PIPE,
#                     stderr=subprocess.PIPE,
#                     creationflags=subprocess.CREATE_NO_WINDOW,
#                     text=True
#                 )
#             else:  # For Unix/Linux
#                 result = subprocess.Popen(
#                     "./temp_code.exe",
#                     stdout=subprocess.PIPE,
#                     stderr=subprocess.PIPE,
#                     text=True
#                 )

#             # Get output and errors
#             output, errors = result.communicate()
            
#             # Display the output
#             self.output_area.delete("1.0", tk.END)
#             if output:
#                 self.output_area.insert(tk.END, output)
#             if errors:
#                 self.output_area.insert(tk.END, errors)

#         except subprocess.CalledProcessError as e:
#             self.output_area.delete("1.0", tk.END)
#             self.output_area.insert(tk.END, e.stderr)

#         finally:
#             # Cleanup temp files
#             if os.path.exists(filename):
#                 os.remove(filename)
#             if os.path.exists("temp_code.exe"):
#                 os.remove("temp_code.exe")



#     def clear_output(self):
#         self.output_area.delete("1.0", tk.END)

# if __name__ == "__main__":
#     root = tk.Tk()
#     ide = SimpleIDE(root)
#     root.mainloop()



import tkinter as tk
from tkinter import filedialog 
from tkinter import scrolledtext
import subprocess
import threading
import os
import webbrowser

class SimpleIDE:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced C/C++ IDE")
        self.root.geometry("800x700")
        self.root.configure(bg="#2b2b2b")  

        self.menu_bar = tk.Menu(self.root, bg="#1f1f1f", fg="white")

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0, bg="#333333", fg="white")
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_file_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        self.social_menu = tk.Menu(self.menu_bar, tearoff=0, bg="#333333", fg="white")
        self.social_menu.add_command(label="Twitter", command=lambda: webbrowser.open("https://x.com/Mrs0lver"))
        self.social_menu.add_command(label="Instagram", command=lambda: webbrowser.open("https://www.instagram.com/dev_pico/"))
        self.social_menu.add_command(label="GitHub", command=lambda: webbrowser.open("https://github.com/MrS0lver"))
        self.social_menu.add_separator()
        self.social_menu.add_command(label="Exit", command=self.root.quit)
        self.menu_bar.add_cascade(label="Social", menu=self.social_menu)

        self.root.config(menu=self.menu_bar)

        self.frame = tk.Frame(self.root, bg="#2b2b2b")
        self.frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.line_numbers = tk.Text(self.frame, width=4, padx=3, takefocus=0, border=0, background='#282828', fg='#8c8c8c', state='disabled', wrap='none', font=("Courier New", 12))
        self.line_numbers.pack(side=tk.LEFT, fill=tk.Y)

        self.text_area = scrolledtext.ScrolledText(self.frame, wrap='word', undo=True, width=80, height=15, font=("Courier New", 12), bg="#1e1e1e", fg="#ffffff", insertbackground="white")
        self.text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.text_area.bind('<KeyRelease>', self.update_line_numbers)

        self.output_area = scrolledtext.ScrolledText(self.root, wrap='word', width=80, height=8, font=("Courier New", 10), bg="#2b2b2b", fg="white")
        self.output_area.pack(pady=10, padx=10, fill=tk.X)

        self.run_button = tk.Button(self.root, text="Run", command=self.run_code, bg="#61afef", fg="white", font=("Arial", 10))
        self.run_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.clear_button = tk.Button(self.root, text="Clear Output", command=self.clear_output, bg="#e06c75", fg="white", font=("Arial", 10))
        self.clear_button.pack(side=tk.LEFT, padx=10, pady=10)

    def update_line_numbers(self, event=None):
        self.line_numbers.yview_moveto(self.text_area.yview()[0])

        self.line_numbers.config(state='normal')
        self.line_numbers.delete('1.0', tk.END)
        line_count = self.text_area.index(tk.END).split('.')[0]
        line_numbers_string = "\n".join(str(i) for i in range(1, int(line_count)))
        self.line_numbers.insert(tk.END, line_numbers_string)
        self.line_numbers.config(state='disabled')

    def new_file(self):
        self.text_area.delete('1.0', tk.END)

    def save_file(self):
        if hasattr(self, 'current_file') and self.current_file:
            try:
                with open(self.current_file, 'w') as file:
                    file.write(self.text_area.get("1.0", tk.END))
                print(f"Saved file: {self.current_file}")
            except Exception as e:
                print(f"Failed to save file: {e}")
        else:
            self.save_file_as()

    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(
            title="Save As",
            defaultextension=".cpp",
            filetypes=(("C/C++ files", "*.c *.cpp"), ("Text files", "*.txt"), ("All files", "*.*"))
        )
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    file.write(self.text_area.get("1.0", tk.END))
                self.current_file = file_path
                print(f"Saved file as: {file_path}")
            except Exception as e:
                print(f"Failed to save file: {e}")

    def open_file(self):
        file_path = filedialog.askopenfilename(
            title="Open",
            filetypes=(("C/C++ files", "*.c *.cpp"), ("Text files", "*.txt"), ("All files", "*.*"))
        )
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    self.text_area.delete('1.0', tk.END)
                    self.text_area.insert(tk.END, file.read())
                self.current_file = file_path
            except Exception as e:
                print(f"Failed to open file: {e}")

    def run_code(self):
        threading.Thread(target=self.run_code_thread, daemon=True).start()

    def run_code_thread(self):
        code = self.text_area.get("1.0", tk.END)
        filename = "temp_code.cpp"
        
        try:
            with open(filename, "w") as f:
                f.write(code)
        except Exception as e:
            self.output_area.delete("1.0", tk.END)
            self.output_area.insert(tk.END, f"Error writing file: {e}")
            return

        compile_command = f"g++ {filename} -o temp_code.exe"
        try:
            # Compile the code
            result = subprocess.run(compile_command, check=True, shell=True, capture_output=True, text=True)
            if result.stderr:
                raise subprocess.CalledProcessError(result.returncode, compile_command, stderr=result.stderr)

            # Run the executable
            if os.name == 'nt':  # For Windows
                result = subprocess.Popen(
                    "./temp_code.exe",
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    creationflags=subprocess.CREATE_NO_WINDOW,
                    text=True
                )
            else:  # For Unix/Linux
                result = subprocess.Popen(
                    "./temp_code.exe",
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )

            output, errors = result.communicate()
            
            # Display the output
            self.output_area.delete("1.0", tk.END)
            if output:
                self.output_area.insert(tk.END, output)
            if errors:
                self.output_area.insert(tk.END, errors)

        except subprocess.CalledProcessError as e:
            self.output_area.delete("1.0", tk.END)
            self.output_area.insert(tk.END, e.stderr)

        finally:
            # Cleanup temp files
            if os.path.exists(filename):
                os.remove(filename)
            if os.path.exists("temp_code.exe"):
                os.remove("temp_code.exe")

    def clear_output(self):
        self.output_area.delete("1.0", tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    ide = SimpleIDE(root)
    root.mainloop()
