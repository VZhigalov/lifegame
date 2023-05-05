# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 17:36:20 2020

@author: V
"""
from tkinter import *

GRID_SIZE = int(input('Введи размер поля '))
SQUARE_SIZE = 50

clicked = set() #Множество черных клеток

def check_blacks(neighbors): #Возвращает количество черных клеток среди соседей
    return len(clicked.intersection(neighbors))

def generate_neighbors(square): #Возвращает соседей
    """ Возвращает клетки соседствующие с square """
    # Левая верхняя клетка
    if square == 1:
        data = {GRID_SIZE + 1, 2, GRID_SIZE + 2}
    # Правая нижняя 
    elif square == GRID_SIZE ** 2:
        data = {square - GRID_SIZE, square - 1, square - GRID_SIZE - 1}
    # Левая нижняя
    elif square == GRID_SIZE:
        data = {GRID_SIZE - 1, GRID_SIZE * 2, GRID_SIZE * 2 - 1}
    # Верхняя правая
    elif square == GRID_SIZE ** 2 - GRID_SIZE + 1:
        data = {square + 1, square - GRID_SIZE, square - GRID_SIZE + 1}
    # Клетка в левом ряду
    elif square < GRID_SIZE:
        data = {square + 1, square - 1, square + GRID_SIZE,
                square + GRID_SIZE - 1, square + GRID_SIZE + 1}
    # Клетка в правом ряду
    elif square > GRID_SIZE ** 2 - GRID_SIZE:
        data = {square + 1, square - 1, square - GRID_SIZE,
                square - GRID_SIZE - 1, square - GRID_SIZE + 1}
    # Клетка в нижнем ряду
    elif square % GRID_SIZE == 0:
        data = {square + GRID_SIZE, square - GRID_SIZE, square - 1,
                square + GRID_SIZE - 1, square - GRID_SIZE - 1}
    # Клетка в верхнем ряду
    elif square % GRID_SIZE == 1:
        data = {square + GRID_SIZE, square - GRID_SIZE, square + 1,
                square + GRID_SIZE + 1, square - GRID_SIZE + 1}
    # Любая другая клетка
    else:
        data = {square - 1, square + 1, square - GRID_SIZE, square + GRID_SIZE,
                square - GRID_SIZE - 1, square - GRID_SIZE + 1,
                square + GRID_SIZE + 1, square + GRID_SIZE - 1}
    return data

def click(event):
    ids = c.find_withtag(CURRENT)[0]  # Определяем по какой клетке кликнули
    clicked.add(ids)
    c.itemconfig(CURRENT, fill="black") # Красим в черный
    c.update()
    
def click_button():
    global clicked
    n_clicked = clicked.copy()    
    for item in range(1, GRID_SIZE**2 + 1):
        if item not in clicked and check_blacks(generate_neighbors(item)) == 3:#Белая клетка с тремя черными соседями
            c.itemconfig(item, fill= "black")
            n_clicked.add(item)
        elif item in clicked and check_blacks(generate_neighbors(item)) not in [2, 3]:#Черная клетка с ненужным числом черных соседей
            c.itemconfig(item, fill = "white")
            n_clicked.remove(item)
    clicked = n_clicked
    c.update()

root = Tk() # Основное окно программы
root.title("Life") #Заголовок
c = Canvas(root, width=GRID_SIZE * SQUARE_SIZE, height=GRID_SIZE * SQUARE_SIZE) # Задаем область на которой будем рисовать
c.bind("<Button-1>", click)
b = Button(text = "Start", command = click_button)
b.pack()
c.pack()
    

 
# Следующий код отрисует решетку из клеточек белого цвета на игровом поле
for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        c.create_rectangle(i * SQUARE_SIZE, j * SQUARE_SIZE,
                           i * SQUARE_SIZE + SQUARE_SIZE,
                           j * SQUARE_SIZE + SQUARE_SIZE, fill='white')
 
root.mainloop() 


