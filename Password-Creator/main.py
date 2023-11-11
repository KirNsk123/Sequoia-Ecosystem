from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror
import random
import pyperclip

# Пароль

letters = "abcdefghigklmnopqrstuvwxyz"
big_letters = "ANCDEFGHIGKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = ":;.-_!?/,'*-&"


def create_password(pass_lenth, let, biglet, num, sym):
    # len - показатель длины, принимаются параметры 6 - 20
    # let - переключатель букв, принимаются значения True/False
    # biglet - переключатель больших букв, принимаются значения True/False
    # num - переключатель цифр, принимаются значения True/False
    # sym - переключатель символов, принимаются значения True/False

    password_list = list()

    if let and biglet and num and sym:
        for i in range(pass_lenth):  # 1
            form = random.randint(0, 3)
            if form == 0:
                password_list.append(str(random.choice(letters)))
            if form == 1:
                password_list.append(str(random.choice(big_letters)))
            if form == 2:
                password_list.append(str(random.choice(numbers)))
            if form == 3:
                password_list.append(str(random.choice(symbols)))
        return "".join(password_list)
    elif let and biglet and num and not sym:  # 2
        for i in range(pass_lenth):
            form = random.randint(0, 2)
            if form == 0:
                password_list.append(str(random.choice(letters)))
            if form == 1:
                password_list.append(str(random.choice(big_letters)))
            if form == 2:
                password_list.append(str(random.choice(numbers)))
        return "".join(password_list)
    elif let and biglet and not num and not sym:  # 3
        for i in range(pass_lenth):
            form = random.randint(0, 1)
            if form == 0:
                password_list.append(str(random.choice(letters)))
            if form == 1:
                password_list.append(str(random.choice(big_letters)))
        return "".join(password_list)
    elif let and not biglet and not num and not sym:  # 4
        for i in range(pass_lenth):
            form = 0
            if form == 0:
                password_list.append(str(random.choice(letters)))
        return "".join(password_list)
    elif let and not biglet and not num and sym:  # 5
        for i in range(pass_lenth):
            form = random.randint(0, 1)
            if form == 0:
                password_list.append(str(random.choice(letters)))
            if form == 1:
                password_list.append(str(random.choice(symbols)))
        return "".join(password_list)
    elif let and biglet and not num and sym:
        for i in range(pass_lenth):
            form = random.randint(0, 2)
            if form == 0:
                password_list.append(str(random.choice(letters)))
            if form == 1:
                password_list.append(str(random.choice(big_letters)))
            if form == 2:
                password_list.append(str(random.choice(symbols)))
        return "".join(password_list)
    elif let and not biglet and num and sym:  # 7
        for i in range(pass_lenth):
            form = random.randint(0, 2)
            if form == 0:
                password_list.append(str(random.choice(letters)))
            if form == 1:
                password_list.append(str(random.choice(numbers)))
            if form == 2:
                password_list.append(str(random.choice(symbols)))
        return "".join(password_list)
    elif let and not biglet and num and not sym:  # 8
        for i in range(pass_lenth):
            form = random.randint(0, 1)
            if form == 0:
                password_list.append(str(random.choice(letters)))
            if form == 1:
                password_list.append(str(random.choice(numbers)))
        return "".join(password_list)

    elif not let and not biglet and not num and not sym:
        showerror(title="Ошибка", message="Ошибка 1: не из чего составлять пароль")
    elif not let and not biglet and not num and sym:
        for i in range(pass_lenth):
            form = 0
            if form == 0:
                password_list.append(str(random.choice(symbols)))
        return "".join(password_list)
    elif not let and not biglet and num and sym:  # 3
        for i in range(pass_lenth):
            form = random.randint(0, 1)
            if form == 0:
                password_list.append(str(random.choice(numbers)))
            if form == 1:
                password_list.append(str(random.choice(symbols)))
        return "".join(password_list)
    elif not let and biglet and num and sym:  # 4
        for i in range(pass_lenth):
            form = random.randint(0, 2)
            if form == 0:
                password_list.append(str(random.choice(big_letters)))
            if form == 1:
                password_list.append(str(random.choice(numbers)))
            if form == 2:
                password_list.append(str(random.choice(symbols)))
        return "".join(password_list)
    elif not let and biglet and num and not sym:  # 5
        for i in range(pass_lenth):
            form = random.randint(0, 1)
            if form == 0:
                password_list.append(str(random.choice(big_letters)))
            if form == 1:
                password_list.append(str(random.choice(numbers)))
        return "".join(password_list)
    elif not let and not biglet and num and not sym:  # 6
        for i in range(pass_lenth):
            form = 0
            if form == 0:
                password_list.append(str(random.choice(numbers)))
        return "".join(password_list)
    elif not let and biglet and not num and not sym:  # 7
        for i in range(pass_lenth):
            form = 0
            if form == 0:
                password_list.append(str(random.choice(big_letters)))
        return "".join(password_list)
    elif not let and biglet and not num and sym:  # 8
        for i in range(pass_lenth):
            form = random.randint(0, 1)
            if form == 0:
                password_list.append(str(random.choice(big_letters)))
            if form == 1:
                password_list.append(str(random.choice(symbols)))
        return "".join(password_list)


def make_password():
    try:
        int(lenSpinBox.get())
    except ValueError:
        showerror(title="Ошибка",
                  message="Ошибка 2: недопустимая длина пароля. Должна быть 6-20")
    end_password = create_password(int(lenSpinBox.get()), enabled_1.get(),
                                   enabled_2.get(), enabled_3.get(),
                                   enabled_4.get())
    passwordListbox.insert(0, end_password)


def copy_password():
    pyperclip.copy(passwordListbox.get(0))


# Tkinter. Графический интерфейс.

root = Tk()  # Создаем окно
root.title("Генератор паролей")
root.geometry("240x180")
root.resizable(False, False)

enabled_1 = BooleanVar()
enabled_2 = BooleanVar()
enabled_3 = BooleanVar()
enabled_4 = BooleanVar()

chbut_1 = ttk.Checkbutton(text="Маленькие буквы",
                          offvalue=False,
                          onvalue=True,
                          variable=enabled_1)
chbut_2 = ttk.Checkbutton(text="Большие буквы",
                          offvalue=False,
                          onvalue=True,
                          variable=enabled_2)
chbut_3 = ttk.Checkbutton(text="Цифры",
                          offvalue=False,
                          onvalue=True,
                          variable=enabled_3)
chbut_4 = ttk.Checkbutton(text="Символы",
                          offvalue=False,
                          onvalue=True,
                          variable=enabled_4)

chbut_1.place(x=10, y=10)
chbut_2.place(x=10, y=30)
chbut_3.place(x=10, y=50)
chbut_4.place(x=10, y=70)

letst = enabled_1.get()

lenLabel = ttk.Label(text="Длина пароля:")
lenLabel.place(x=10, y=90)
lenSpinBox = ttk.Spinbox(from_=6.0, to=20.0, width=5, state="readonly")
lenSpinBox.place(x=95, y=90)
lenth = lenSpinBox.get()

passwordListbox = Listbox(height=1, width=23)
passwordListbox.place(x=90, y=111)

resultLabel = ttk.Label(text="Ваш пароль: ")
resultLabel.place(x=10, y=110)

resultButton = ttk.Button(text="Сгенерировать пароль", command=make_password)
resultButton.place(x=10, y=135)

copyButton = ttk.Button(text="Копировать", command=copy_password)
copyButton.place(x=150, y=135)

mainloop()
