import threading
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from module.speech_to_text import convert_speech_to_text
from module.image_describer import describe_image
from module.doc_reader import read_text_from_image, speak_text

# Helper to select file
def select_file(filetypes):
    filepath = filedialog.askopenfilename(filetypes=filetypes)
    return filepath

# Handlers
def handle_speech_to_text():
    output_box.delete("1.0", tk.END)
    filepath = select_file([("Audio Files", "*.wav *.mp3 *.m4a")])
    if filepath:
        try:
            result = convert_speech_to_text(filepath)
            output_box.delete("1.0", tk.END)
            output_box.insert(tk.END, result)
        except Exception as e:
            messagebox.showerror("Error", f"Speech-to-text failed:\n{e}")

def handle_image_caption():
    output_box.delete("1.0", tk.END)
    filepath = select_file([("Image Files", "*.png *.jpg *.jpeg")])
    if filepath:
        caption = describe_image(filepath)
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, f"Image Description:\n{caption}")

def handle_doc_reader():
    output_box.delete("1.0", tk.END)
    filepath = select_file([("Image Files", "*.png *.jpg *.jpeg")])
    if filepath:
        text = read_text_from_image(filepath)
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, f"Extracted Text:\n{text}")

        #Run speech in background so GUI doesn't wait
        threading.Thread(target=speak_text, args=(text,), daemon=True).start()

# GUI Setup
root = tk.Tk()
root.title("One For All: AI Accessibility Assistant")
root.geometry("700x500")
root.resizable(False, False)

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(fill="both", expand=True)

heading = tk.Label(frame, text="One For All - AI Accessibility Assistant", font=("Helvetica", 16, "bold"))
heading.pack(pady=(0, 10))

btn1 = tk.Button(frame, text="1. Convert Speech to Text", width=30, command=handle_speech_to_text)
btn1.pack(pady=5)

btn2 = tk.Button(frame, text="2. Describe Image", width=30, command=handle_image_caption)
btn2.pack(pady=5)

btn3 = tk.Button(frame, text="3. Read Document", width=30, command=handle_doc_reader)
btn3.pack(pady=5)

btn_exit = tk.Button(frame, text="Exit", width=30, command=root.destroy)
btn_exit.pack(pady=10)

output_label = tk.Label(frame, text="\nOutput:", font=("Helvetica", 12, "bold"))
output_label.pack()

output_box = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=80, height=15)
output_box.pack(pady=(0, 10))

root.mainloop()
