import qrcode as qr
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk

class QRGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry("400x600")
        self.root.configure(bg='#1e1e2e')
        self.root.resizable(False, False)

        self.app_icon = tk.PhotoImage(file="Images/logo.png")
        self.root.iconphoto(False, self.app_icon)



if __name__ == "__main__":
    root = tk.Tk()
    app = QRGeneratorApp(root)
    root.mainloop()