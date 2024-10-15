from tkinter import *
from tkinter import scrolledtext
import subprocess,threading
import os

class SimpleIDE:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced C/C++ IDE")
        self.root.geometry("700x500")
        self.text_area = scrolledtext.ScrolledText(root, wrap='word', width=80, height=20, font=("Courier New", 12))
        self.text_area.pack(pady=10)

        button_frame = Frame(root)
        button_frame.pack(pady=5)

        self.run_button = Button(button_frame, text="Run", command=self.run_code, bg="lightblue", font=("Arial", 10))
        self.run_button.pack(side=LEFT, padx=5)

        self.clear_button = Button(button_frame, text="Clear Output", command=self.clear_output, bg="lightcoral", font=("Arial", 10))
        self.clear_button.pack(side=LEFT, padx=5)

        self.output_area = scrolledtext.ScrolledText(root, wrap='word', width=80, height=10, font=("Courier New", 10), bg="#f0f0f0")
        self.output_area.pack(pady=10)
    def run_code(self):
        threading.Thread(target=self.run_code_thread,daemon=True).start()
    def run_code_thread(self):
        code = self.text_area.get("1.0", END)
        filename = "temp_code.cpp"
        with open(filename, "w") as f:
            f.write(code)
        compile_command = f"g++ {filename} -o temp_code.exe"
        try:
            subprocess.run(compile_command, check=True, shell=True, stderr=subprocess.PIPE)
            result = subprocess.run("./temp_code.exe", check=True, capture_output=True, text=True)
            output = result.stdout
            self.output_area.delete("1.0", END)
            self.output_area.insert(END, output)
        except subprocess.CalledProcessError as e:
            self.output_area.delete("1.0", END)
            self.output_area.insert(END, e.stderr)
        os.remove(filename)
        if os.path.exists("temp_code.exe"):
            os.remove("temp_code.exe")
    def clear_output(self):
        self.output_area.delete("1.0", END)

if __name__ == "__main__":
    root = Tk()
    ide = SimpleIDE(root)
    root.mainloop()
