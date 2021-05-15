import tkinter as tk
import network
import os

Data = network.Data
path = os.getcwd()

def test_function(entry):
    print("This is the entry:", entry)


root = tk.Tk()

# Setting up a dynamic window screen
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
root.title("Weather App")

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Changing a background image/color
# def updateBackground(desc):
#     if desc == "Clouds":
#         background_image = tk.PhotoImage(file=path + '/images/cloud.png')
#     elif desc == "Clear":
#         background_image = tk.PhotoImage(file=path + '/images/sun.png')
#     elif desc == "Rain":
#         background_image = tk.PhotoImage(file=path + '/images/rain.png')
#     else:
#         background_image = tk.PhotoImage(file=path + '/images/landscape.png')
#
#     background_label = tk.Label(root, image=background_image)
#     background_label.place(relwidth=1, relheight=1)

def updateData(city):
    data = Data.getData(Data, city=city)
    label["text"] = data[0]

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=60, command=lambda: updateData(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Sans', 30))
label.place(relwidth=1, relheight=1)

root.mainloop()
