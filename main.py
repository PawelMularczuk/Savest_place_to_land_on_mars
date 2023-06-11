from tkinter import *
from tkinter.messagebox import askyesno
from PIL import ImageTk, Image
from tkinter import ttk
import tkinter as tk
import customtkinter as ctk
import functools

# tworzenie funkjci dzięki której zdjęcia będą dynamicznie zmieniały rozmiar do proporcji interfejsu 
def show(img):
    def show_full_image(event):

        global resized_tk

        image_ratio = img.size[0] / img.size[1]

        # aktualne proporcje
        canvas_ratio = event.width / event.height

        # współrzędne zdjęcia
        if canvas_ratio > image_ratio: # canvas jest szersze od zdjecia

            height = int(event.height)
            width = int(height * image_ratio)

        else: # canvas jest węzszy jak zdjecie 
            width = int(event.width)
            height = int(width / image_ratio)   

        resized_image = img.resize((width, height))    
        resized_tk = ImageTk.PhotoImage(resized_image)
        canvas.create_image(int(event.width / 2),int(event.height / 2), anchor='center', image=resized_tk)
    return show_full_image


def mars():

    img1 = Image.open('./pix/mars_og_crop.png')
    canvas.bind('<Configure>', show(img1))
    root.mainloop()

def safest_place_into_landing():

    img2 = Image.open('./pix/Mars_save_place.png')
    canvas.bind('<Configure>', show(img2))
    root.mainloop()


# Tworzenie okna tkinter
root = tk.Tk()

# Dodawanie tytułu aplikacji
root.title('Project Mars')

# definiujemy rozmiary okna aplikacji
window_width = 1000
Window_height = 600

# definiujemy szrokość i wysokość ekranu
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# wyznaczamy środek ekranu
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - Window_height / 2)

#  Ustalenie gdzie aplikacja ma się otwierać(w tym przypadku na samym środku ekranu)
root.geometry(f'{window_width}x{Window_height}+{center_x}+{center_y}')

# Konwersja Zdjęcia na tkinter.PhotoImage
img = PhotoImage(file='./pix/mars_icon.png')

# Dodanie ikonki do aplikacji
root.iconphoto(False, img)

# Miejsca dla przycisków i dla canvas
root.columnconfigure((0,1,2,3), weight=1, uniform='a')
root.rowconfigure(0, weight=1)

buttom_frame = ttk.Frame(root)

buttom_frame.grid(column=0, row=0, sticky='nsew')

canvas = tk.Canvas(root, background='black', bd=0, highlightthickness=0, relief='ridge')
canvas.grid(column = 1, columnspan=3, row=0, sticky='nsew')


buttom_A = ctk.CTkButton(buttom_frame, text='Mars', command=mars)
buttom_A.pack(pady=10)

buttom_B = ctk.CTkButton(buttom_frame, text='Safest place into landing', command= safest_place_into_landing)
buttom_B.pack()


# Definiuje fukncję z potwierdzeniem zamknięcia aplikacji
def confirm_exit():

    exit = askyesno(title='Exit', message='Are you sure you want to exit ?')
    if exit:
        root.destroy()

# protokół który zamuka aplikację gdy funckja się skończy 
root.protocol('WM_DELETE_WINDOW', confirm_exit)
# Tworzenie loopa Który pozwala utrzymać okno i korzystać z eventów
root.mainloop()