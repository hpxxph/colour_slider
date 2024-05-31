import tkinter as tk 


win = tk.Tk()
win.title("Colour Slider")

### CENTERING THE WINDOW ### 
def center_window (root, width=410, height=180):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    
    win.geometry(f'{width}x{height}+{x}+{y}')

### UPDADING BACKGROUND COLOR ON BUTTON ###
def my_upd(v):
    color_c='#%02x%02x%02x' % (scale_1.get(), scale_2.get(), scale_3.get())
    bg_button.config(bg=color_c) 
    bg_button.config(text=color_c)
    
font_for_button = ('Times', 18, 'normal')
    
### FIRST SLIDER ###
scale_1 = tk.Scale(win, from_=0, to=255, bg='red', orient='horizontal', length=250, command=my_upd)
scale_1.grid(row=0, column=0, padx=5, pady=10)

### SECOND SLIDER ###
scale_2 = tk.Scale(win, from_=0, to=255, bg='green', orient='horizontal', length=250, command=my_upd)
scale_2.grid(row=1, column=0, padx=5, pady=10)

### THEREED SLIDR ###
scale_3 = tk.Scale(win, from_=0, to=255, bg='blue', orient='horizontal', length=250, command=my_upd)
scale_3.grid(row=2, column=0, padx=5, pady=10)

### BUTTON WITH COLOR ###
bg_button = tk.Button(win, text='My Color', font=font_for_button, width=8, )
bg_button.grid(row=1, column=1, padx=7)

if __name__ == "__main__":
    center_window(win, 410, 200)
    win.mainloop()