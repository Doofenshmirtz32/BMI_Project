from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(width=300, height=300)
window.config(padx=20, pady=20)

#label
my_label = Label(text="Enter Your Weight (kg)", fg="black", font=('Cooper Black', 10, "normal"))
my_label.config(padx=10, pady=10)
my_label.pack()

#entry
my_entry = Entry()
my_entry.pack()

#label_2
my_label_2 = Label(text="Enter Your Height (cm)", fg="black", font=('Cooper Black', 10, "normal"))
my_label_2.config(padx=10, pady=10)
my_label_2.pack()

#entry_2
my_entry_2 = Entry()
my_entry_2.pack()

#button
def button_clicked():
    try:
        weight = int(my_entry.get())
        height = int(my_entry_2.get())
        BMI = (float(weight) / (float(height) ** 2)) *10000
        if BMI <= 18.5:
            my_label_3 = Label(text="Your BMI is {}. You are underweight.".format(round(BMI,2)), fg="blue", font=('Cooper Black', 10, "normal"))
            my_label_3.config(padx=10, pady=10)
            my_label_3.pack()
        elif BMI > 18.5 and BMI < 24.9:
            my_label_4 = Label(text="Your BMI is {}. You are normal weight.".format(BMI), fg="green", font=('Cooper Black', 10, "normal"))
            my_label_4.config(padx=10, pady=10)
            my_label_4.pack()
        elif BMI > 24.9 and BMI < 29.9:
            my_label_5 = Label(text="Your BMI id {}. You are overweight.".format(BMI), fg="#D5C829", font=('Cooper Black', 10, "normal"))
            my_label_5.config(padx=10, pady=10)
            my_label_5.pack()
        elif BMI > 29.9 and BMI < 39.9:
            my_label_6 = Label(text="Your BMI is {}. You are obesity.".format(BMI), fg="orange", font=('Cooper Black', 10, "normal"))
            my_label_6.config(padx=10, pady=10)
            my_label_6.pack()
        else:
            my_label_7 = Label(text="Your BMI is {}. You are extreme obesity.".format(BMI), fg="red", font=('Cooper Black', 10, "normal"))
            my_label_7.config(padx=10, pady=10)
            my_label_7.pack()
    except:
        last_label.config(text="Enter a valid number please!", fg="black", font=('Cooper Black', 10, "normal"))

my_button = Button(text="Calculate", command=button_clicked)
my_button.config(padx=10, pady=10)
my_button.pack()


last_label = Label()
last_label.pack()

window.mainloop()