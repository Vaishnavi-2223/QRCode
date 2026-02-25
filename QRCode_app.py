import qrcode
from PIL import Image
import customtkinter as ctk
from tkinter import colorchooser, messagebox, filedialog

# ---------------- App setup ---------------- #

ctk.set_appearance_mode("light")

app = ctk.CTk()
app.geometry("500x650")
app.title("Your QR Generator")
app.configure(fg_color='#F3E8FF')

# ---------------- Background Wallpaper ---------------- #

original_bg = Image.open("img.png")

bg_label = ctk.CTkLabel(app, text="")
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# ---------------- Background Wallpaper ---------------- #

window_width = 500
window_height = 650

original_bg = Image.open("img.png")
resized_bg = original_bg.resize((window_width, window_height))

bg_image = ctk.CTkImage(
    light_image=resized_bg,
    size=(window_width, window_height)
)

bg_label = ctk.CTkLabel(app, image=bg_image, text="")
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# ---------------- Variables ---------------- #

qr_color = "black"
bg_color = "white"
preview_image = None

# ---------------- Functions ---------------- #

def choose_qr_color():
    global qr_color
    color = colorchooser.askcolor()[1]
    if color:
        qr_color = color

def choose_bg_color():
    global bg_color
    color = colorchooser.askcolor()[1]
    if color:
        bg_color = color

def generate_qr():
    global preview_image

    data = link_entry.get()
    size_value = size_entry.get()

    if not data or not size_value:
        messagebox.showerror("Error 💔", "Please fill all fields!")
        return

    try:
        size = int(size_value)
    except ValueError:
        messagebox.showerror("Error 💔", "Size must be a number!")
        return

    # Create QR
    qr = qrcode.QRCode(
        version=1,
        box_size=size,
        border=5
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=qr_color, back_color=bg_color)

    # -------- QR PREVIEW -------- #
    preview = img.resize((200, 200))
    preview_image = ctk.CTkImage(light_image=preview, size=(200, 200))
    preview_label.configure(image=preview_image)

    # -------- FILE SAVE DIALOG -------- #
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG Files", "*.png")],
        title="Save your QR Code"
    )

    if file_path:
        img.save(file_path)
        messagebox.showinfo("Success 💜", "QR Code saved successfully!")

# ---------------- Card Frame ---------------- #

card = ctk.CTkFrame(
    app,
    width=470,
    height=600,
    corner_radius=5,
    fg_color="#E9D5FF"
)
card.place(relx=0.5, rely=0.5, anchor="center")

# ---------------- UI Elements ---------------- #

title = ctk.CTkLabel(
    card,
    text="QR Code Generator",
    font=("Candy Planet", 25, "bold"),
    text_color="#4C1D95"
)
title.pack(pady=20)

link_entry = ctk.CTkEntry(
    card,
    width=350,
    height=40,
    corner_radius=15,
    fg_color="#F5F3FF",
    text_color="#4C1D95",
    placeholder_text="Enter your link here🔗..."
)
link_entry.pack(pady=10)

size_entry = ctk.CTkEntry(
    card,
    width=200,
    height=40,
    corner_radius=15,
    fg_color="#F5F3FF",
    text_color="#4C1D95",
    placeholder_text="Enter size (10 recommended)"
)
size_entry.pack(pady=10)

qr_color_btn = ctk.CTkButton(
    card,
    text="Choose QR Color",
    fg_color="#C084FC",
    hover_color="#A855F7",
    corner_radius=20,
    command=choose_qr_color
)
qr_color_btn.pack(pady=8)

bg_color_btn = ctk.CTkButton(
    card,
    text="Choose Background Color",
    fg_color="#C084FC",
    hover_color="#A855F7",
    corner_radius=20,
    command=choose_bg_color
)
bg_color_btn.pack(pady=8)

generate_btn = ctk.CTkButton(
    card,
    text="Generate QR Code ✨",
    fg_color="#A855F7",
    hover_color="#9333EA",
    corner_radius=25,
    height=45,
    command=generate_qr
)
generate_btn.pack(pady=15)

# -------- QR Preview Area -------- #

preview_label = ctk.CTkLabel(card, text="")
preview_label.pack(pady=15)

app.mainloop()