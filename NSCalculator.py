# Калькулятор систем счисления 

import tkinter as tk
from tkinter import messagebox as mb
import os

# Функция закрытия окна
def do_close():
    root.destroy()

def do_table_sum():
    # Считывание данных из полей ввода
    base_num_sys = int(entBaseNumSys.get())

    # Проверка данных из полей ввода
    if base_num_sys<=1 or base_num_sys>36:
        mb.showerror(title="Ошибка", message="Введите число от 2 до 36")
        return
    
    # Открытие окна результатов
    popup_window_sum(base_num_sys)
    

def do_table_mult():
    # Считывание данных из полей ввода
    base_num_sys = int(entBaseNumSys.get())

    # Проверка данных из полей ввода
    if base_num_sys<=1 or base_num_sys>36:
        mb.showerror(title="Ошибка", message="Введите число от 2 до 36")
        return
    
    # Открытие окна результатов
    popup_window_mult(base_num_sys)

    
def convert(num, base_num_sys):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if num < base_num_sys:
        return alphabet[num]
    else:
        return convert(num // base_num_sys, base_num_sys) + alphabet[num % base_num_sys]
    
def popup_window_sum(base_num_sys):
    window_sum=tk.Toplevel()
    # ~ w1 = 16*(4*base_num_sys-2)
    # ~ h1 = 20*(base_num_sys+4)
    # ~ w1_h1 = str(w1)+"x"+str(h1)
    # ~ window_sum.geometry(w1_h1)
    window_sum.geometry("500x500")
    window_sum.title("Таблица сложения")
    
    # Добавление окна вывода текста
    # ~ w2 = 15*(4*base_num_sys-2)
    # ~ h2 = 15*(base_num_sys+4)
    txtOutput = tk.Text(window_sum, font = ('Courier New', 10, 'bold'))
    # ~ txtOutput.place(x=15, y=115, width=w2, height=h2)
    txtOutput.place(x=15, y=115, width=470, height=300)
    
    i=1
    j=1
    Zagolovok = "Таблица сложения в " + str(base_num_sys) + " - ичной системе:"
    # Добавление заголовка
    txtOutput.insert(tk.END, f" {Zagolovok:^60}" + os.linesep)
    while i<base_num_sys:
        j=1
        while j<base_num_sys:
            # Добавление вывода 
            txtOutput.insert(tk.END, f" {convert(i+j, base_num_sys):^3}")
            j+=1
        txtOutput.insert(tk.END, "" + os.linesep)
        i+=1
    
    # Добавление кнопки закрытия окна
    btnClosePopup = tk.Button(window_sum, text="Закрыть", font = ('Helvetica', 10, 'bold'), command=window_sum.destroy)
    btnClosePopup.place(x=190, y=450, width=90, height=30)
    
    # Перевод фокуса на созданное окно
    window_sum.focus_force()
    
def popup_window_mult(base_num_sys):
    window_mult=tk.Toplevel()
    window_mult.geometry("500x500")
    window_mult.title("Таблица умножения")
    
    # Добавление окна вывода текста
    # ~ w2 = 15*(4*base_num_sys-2)
    # ~ h2 = 15*(base_num_sys+4)
    txtOutput = tk.Text(window_mult, font = ('Courier New', 10, 'bold'))
    # ~ txtOutput.place(x=15, y=115, width=w2, height=h2)
    txtOutput.place(x=15, y=115, width=470, height=300)
    
    i=1
    j=1
    Zagolovok = "Таблица умножения в " + str(base_num_sys) + " - ичной системе:"
    # Добавление заголовка
    txtOutput.insert(tk.END, f" {Zagolovok:^60}" + os.linesep)
    while i<base_num_sys:
        j=1
        while j<base_num_sys:
            # Добавление вывода 
            txtOutput.insert(tk.END, f" {convert(i*j, base_num_sys):^3}")
            j+=1
        txtOutput.insert(tk.END, "" + os.linesep)
        i+=1
    
    # Добавление кнопки закрытия окна
    btnClosePopup = tk.Button(window_mult, text="Закрыть", font = ('Helvetica', 10, 'bold'), command=window_mult.destroy)
    btnClosePopup.place(x=190, y=450, width=90, height=30)
    
    # Перевод фокуса на созданное окно
    window_mult.focus_force()


# Создание главного окна
root=tk.Tk()
root.geometry("400x400")
root.title("Number System's Calculator")

# Добавление метки заголовка
lblTitle = tk.Label(text="Калькулятор систем счисления ", font = ('Helvetica', 14, 'bold'), fg = '#0000cc')
lblTitle.place(x=25, y=20)

# Добавление полей ввода основания
lblBaseNumSys = tk.Label(text="Основание системы счисления: ", font = ('Helvetica', 10, 'bold'))
lblBaseNumSys.place(x=25, y=60)

entBaseNumSys = tk.Entry(font = ('Helvetica', 10, 'bold'), justify = 'center')
entBaseNumSys.place(x=265, y=60, width=50, height=20)
entBaseNumSys.insert(tk.END, '0')

# Добавление метки 
lblBaseNumSys = tk.Label(text="Вывод таблицы :", font = ('Helvetica', 10, 'bold'))
lblBaseNumSys.place(x=25, y=100)

# Добавление кнопки вывода таблицы сложения
btnClose = tk.Button(root, text="Сложения", font = ('Helvetica', 10, 'bold'), command=do_table_sum)
btnClose.place(x=190, y=100, width=130, height=30)

# Добавление кнопки вывода таблицы умножения
btnClose = tk.Button(root, text="Умножения", font = ('Helvetica', 10, 'bold'), command=do_table_mult)
btnClose.place(x=190, y=140, width=130, height=30)

# Добавление кнопки закрытия программы
btnClose = tk.Button(root, text="Закрыть", font = ('Helvetica', 10, 'bold'), command=do_close)
btnClose.place(x=250, y=320, width=90, height=30)

# Запуск цикла mainloop
root.mainloop()
