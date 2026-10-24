import qrcode as qr
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk

class QRGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry("400x450")
        self.root.configure(bg='#1e1e2e')
        self.root.resizable(False, False)

        self.app_icon = tk.PhotoImage(file="Images/logo.png")
        self.root.iconphoto(False, self.app_icon)

        self.qr_image = None
        self.pil_image = None
        self.placeholder_text = "https://example.com"

        input_frame = tk.Frame(root, bg='#1e1e2e')
        input_frame.pack(pady=15)

        tk.Label(input_frame, text="Enter Text or URL:", font=("Arial", 12, "bold"),
                  bg='#1e1e2e', fg='#cdd6f4').pack(anchor="w", padx=5)
        self.text_entry = tk.Entry(input_frame, width=38, font=("Arial", 11), fg="#bac2de")
        self.text_entry.pack(pady=5, padx=5, ipady=5, ipadx=10)
        self.text_entry.insert(0, self.placeholder_text)

        self.text_entry.bind("<FocusIn>", self.on_focus_in)
        self.text_entry.bind("<FocusOut>", self.on_focus_out)

        button_frame = tk.Frame(root, bg='#1e1e2e')
        button_frame.pack(pady=10)

        generate_button = tk.Button(button_frame, text="Generate QR", bg="#a6e3a1", fg="#1e1e2e", 
                                 font=("Arial", 11, "bold"), width=12, command=self.generate_qr)
        generate_button.grid(row=0, column=0, padx=8)

        generate_button.bind("<Enter>", lambda e: generate_button.config(bg="#40a02b"))
        generate_button.bind("<Leave>", lambda e: generate_button.config(bg="#a6e3a1"))

        save_button = tk.Button(button_frame, text="Save Image", bg="#89b4fa", fg="#1e1e2e", 
                             font=("Arial", 11, "bold"), width=12, command=self.save_qr)
        save_button.grid(row=0, column=1, padx=8)

        save_button.bind("<Enter>", lambda e: save_button.config(bg="#1e66f5"))
        save_button.bind("<Leave>", lambda e: save_button.config(bg="#89b4fa"))

        self.qr_label = tk.Label(root, text="QR Code Preview", fg="grey", bg="#f0f0f0", 
                                 relief="solid", bd=2, width=28, height=14, font=("Arial", 10))
        self.qr_label.pack(pady=20)

    def on_focus_in(self, event):
        if self.text_entry.get() == self.placeholder_text:
            self.text_entry.delete(0, tk.END)
            self.text_entry.config(fg="black")

    def on_focus_out(self, event):
        if not self.text_entry.get().strip():
            self.text_entry.insert(0, self.placeholder_text)
            self.text_entry.config(fg="#1e1e2e")

    def generate_qr(self):
        data = self.text_entry.get().strip()
        if not data:
            messagebox.showerror("Error : No input", "Please enter some text or a URL!")
            return

        qr_code = qr.QRCode(
            version = None,
            error_correction = qr.constants.ERROR_CORRECT_L,
            box_size = 10,
            border = 5,
        )

        qr_code.add_data(data)
        qr_code.make(fit=True)

        self.pil_image = qr_code.make_image(fill_color="black", back_color="white").convert("RGB")
        
        display_image = self.pil_image.resize((200, 200), Image.Resampling.LANCZOS)
        self.current_image = ImageTk.PhotoImage(display_image)

        self.qr_label.config(image=self.current_image, text="", bg="white", width=225, height=225)

    def save_qr(self):
        if not self.pil_image:
            messagebox.showerror("Error : No Output", "No QR code to save!")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")],
            title="Save QR Code"
        )
        if file_path:
            self.pil_image.save(file_path)
            messagebox.showinfo("Success", f"QR code saved successfully to:\n{file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = QRGeneratorApp(root)
    root.mainloop()