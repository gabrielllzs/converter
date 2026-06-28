import customtkinter as ctk
from tkinter import filedialog, messagebox
import threading
from engine import ConverterEngine

class AppInterface(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.engine = ConverterEngine()
        self.title("File Converter Pro")
        self.geometry("450x400")

        # Title
        ctk.CTkLabel(self, text="File Converter", font=("Arial", 20, "bold")).pack(pady=20)

        # Buttons for Mode
        self.btn_to_word = ctk.CTkButton(self, text="Convert to Word (.docx)", command=lambda: self.start_process("word"))
        self.btn_to_word.pack(pady=10)

        self.btn_to_pdf = ctk.CTkButton(self, text="Convert to PDF (.pdf)", command=lambda: self.start_process("pdf"))
        self.btn_to_pdf.pack(pady=10)

        self.status = ctk.CTkLabel(self, text="Ready", text_color="gray")
        self.status.pack(pady=20)

    def start_process(self, mode):
        # Determine file types based on mode
        if mode == "word":
            file_types = [("PDF/Images", "*.pdf *.png *.jpg *.jpeg")]
        else:
            file_types = [("Word/Images", "*.docx *.png *.jpg *.jpeg")]

        files = filedialog.askopenfilenames(filetypes=file_types)
        if not files: return

        output_folder = filedialog.askdirectory(title="Select Output Folder")
        if not output_folder: return

        # Start thread
        threading.Thread(target=self.process_files, args=(files, output_folder, mode), daemon=True).start()

    def process_files(self, files, output_folder, mode):
        self.status.configure(text="Converting...", text_color="orange")
        try:
            if mode == "word":
                self.engine.convert_to_word(files, output_folder)
            else:
                self.engine.convert_to_pdf(files, output_folder)
            
            self.after(0, lambda: messagebox.showinfo("Success", "Conversion finished!"))
            self.after(0, lambda: self.status.configure(text="Done!", text_color="green"))
        except Exception as e:
            self.after(0, lambda: messagebox.showerror("Error", str(e)))
            self.after(0, lambda: self.status.configure(text="Error occurred", text_color="red"))