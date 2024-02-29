import tkinter
from tkinter import *
import pandas as pd
import csv
from datetime import datetime
BACKGROUND_COLOR = "#B1DDC6"

today=datetime.today().date()
student_list = []

with open('data/name.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        student_list.append(dict(row))

index = 0
def write_to_csv():
    fieldnames = ['name', 'attendance']
    with open('data/name.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in student_list:
            writer.writerow(row)

def present():
    global index, student_list
    if index == len(student_list)-1:
        student_list[index]["attendance"] =int(student_list[index]["attendance"])+ 1
        canvas.itemconfig(card_word, text="completed", fill="black")
        present_button.config(state=tkinter.DISABLED)
        absent_button.config(state=tkinter.DISABLED)
        write_to_csv()
        data=pd.read_csv("data/name.csv")
        print(f"Date:{today}\n{data}")
    else:
        student_list[index]["attendance"] =int(student_list[index]["attendance"])+ 1
        index += 1
        canvas.itemconfig(card_word, text=student_list[index]["name"], fill="black")

def absent():
    global index,student_list
    if index == len(student_list)-1:
        canvas.itemconfig(card_word, text="completed", fill="black")
        present_button.config(state=tkinter.DISABLED)
        absent_button.config(state=tkinter.DISABLED)
        write_to_csv()
        data = pd.read_csv("data/name.csv")
        print(f"Date:{today}\n{data}")
    else:
        index += 1
        canvas.itemconfig(card_word, text=student_list[index]["name"], fill="black")

def reset():
    input_csv_file = 'data/name.csv'
    single_value = '0'
    column_index_to_change = 1

    with open(input_csv_file, 'r', newline='') as infile:
        reader = csv.reader(infile)
        data = list(reader)
        modified_data=data[1:]

    for row in modified_data:
        row[column_index_to_change] = single_value

    with open(input_csv_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(data)

window = Tk()
window.title("ATTENDANCE")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_word = canvas.create_text(400, 263, font=("Ariel", 40, "bold"))
canvas.itemconfig(card_word, text=student_list[index]["name"], fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
absent_button = Button(text="ABSENT", highlightthickness=0, command=absent)
absent_button.config(width=20, height=5, pady=10, padx=10)
absent_button.grid(row=1, column=0)
present_button = Button(text="PRESENT", highlightthickness=0, command=present)
present_button.config(width=20, height=5, pady=10, padx=10)
present_button.grid(row=1, column=1)
reset_button = Button(text="RESET", highlightthickness=0, command=reset)
reset_button.grid(row=2,column=1)
print("TILL PREVIOUS CLASSES")
data=pd.read_csv("data/name.csv")
print(f"{data}\n\n")
window.mainloop()