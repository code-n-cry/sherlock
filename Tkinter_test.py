import tkinter

x1 = 20
y1 = 110


def key_pressed(event):
    global treug1
    global treug2
    if event.keysym == 'Up':
        canvas.move(oval1, 0, -10)
        canvas.move(oval2, 0, -10)
        canvas.move(oval4, 0, -10)
        canvas.move(oval5, 0, -10)
        canvas.move(oval6, 0, -10)
        canvas.move(oval7, 0, -10)
        canvas.move(line1, 0, -10, )
        if canvas.coords(oval7)[1] > 270:
            canvas.coords(line1,
                          (canvas.coords(oval7)[0] + 20, canvas.coords(oval7)[1] + 20,
                           canvas.coords(oval2)[0],
                           canvas.coords(oval2)[1] - 140))
        if canvas.coords(oval7)[1] > 240:
            canvas.coords(line1,
                          (canvas.coords(oval7)[0] + 20, canvas.coords(oval7)[1] + 20,
                           canvas.coords(oval2)[0] - 50,
                           canvas.coords(oval2)[1] - 100))
        if canvas.coords(oval7)[1] < 230:
            canvas.coords(line1,
                          (canvas.coords(oval7)[0] + 20, canvas.coords(oval7)[1] + 20, canvas.coords(oval2)[0] - 80,
                           canvas.coords(oval7)[1]))
        if canvas.coords(oval7)[1] < 160:
            canvas.coords(line1,
                          (canvas.coords(oval7)[0] + 20, canvas.coords(oval7)[1] + 20, canvas.coords(oval2)[0] - 100,
                           canvas.coords(oval2)[1] + 140))
        if canvas.coords(oval7)[1] < 110:
            canvas.coords(line1, (
                canvas.coords(oval7)[0] + 20, canvas.coords(oval7)[1] + 20, canvas.coords(oval2)[0] - 20,
                canvas.coords(oval2)[1] + 180))
        # if canvas.cords(oval3)[1] < 100:
    elif event.keysym == 'Down':
        canvas.move(oval1, 0, 10)
        canvas.move(oval2, 0, 10)
        canvas.move(oval4, 0, 10)
        canvas.move(oval5, 0, 10)
        canvas.move(oval6, 0, 10)
        canvas.move(oval7, 0, 10)
        canvas.move(line1, 0, 10, )

        if canvas.coords(oval7)[1] > 240:
            canvas.coords(line1,
                          (canvas.coords(oval7)[0] + 20, canvas.coords(oval7)[1] + 20,
                           canvas.coords(oval2)[0] - 50,
                           canvas.coords(oval2)[1] - 100))

        if canvas.coords(oval7)[1] > 270:
            canvas.coords(line1,
                          (canvas.coords(oval7)[0] + 20, canvas.coords(oval7)[1] + 20,
                           canvas.coords(oval2)[0],
                           canvas.coords(oval2)[1] - 140))
        if canvas.coords(oval7)[1] < 230:
            canvas.coords(line1,
                          (canvas.coords(oval7)[0] + 20, canvas.coords(oval7)[1] + 20, canvas.coords(oval2)[0] - 80,
                           canvas.coords(oval2)[1]))

        if canvas.coords(oval7)[1] < 160:
            canvas.coords(line1,
                          (canvas.coords(oval7)[0] + 20, canvas.coords(oval7)[1] + 20, canvas.coords(oval2)[0] - 100,
                           canvas.coords(oval2)[1] + 140))
        if canvas.coords(oval7)[1] < 110:
            canvas.coords(line1, (
                canvas.coords(oval7)[0] + 20, canvas.coords(oval7)[1] + 20, canvas.coords(oval2)[0] - 20,
                canvas.coords(oval2)[1] + 180))

    elif event.keysym == 'Right':
        canvas.move(oval1, 10, 0)
        canvas.move(oval2, 10, 0)
        canvas.move(oval4, 10, 0)
        canvas.move(oval5, 10, 0)
        canvas.move(oval6, 10, 0)
        canvas.move(oval7, 10, 0)
        canvas.move(line1, 10, 0, )
    elif event.keysym == 'Left':
        canvas.move(oval1, -10, 0)
        canvas.move(oval2, -10, 0)
        canvas.move(oval4, -10, 0)
        canvas.move(oval5, -10, 0)
        canvas.move(oval6, -10, 0)
        canvas.move(oval7, -10, 0)
        canvas.move(line1, -10, 0, )
    if event.char == '1':
        canvas.delete(treug1)
        canvas.delete(treug2)
        treug1 = canvas.create_polygon((650, 390), (700, 400), (650, 410), fill='black', outline='black')
        treug2 = canvas.create_polygon((760, 390), (710, 400), (760, 410), fill='black', outline='black')
    if event.char == '2':
        canvas.delete(treug1)
        canvas.delete(treug2)
        treug1 = canvas.create_polygon((650, 410), (700, 420), (650, 430), fill='black', outline='black')
        treug2 = canvas.create_polygon((760, 410), (710, 420), (760, 430), fill='black', outline='black')
    if event.char == '3':
        canvas.delete(treug1)
        canvas.delete(treug2)
        treug1 = canvas.create_polygon((650, 430), (700, 440), (650, 450), fill='black', outline='black')
        treug2 = canvas.create_polygon((760, 430), (710, 440), (760, 450), fill='black', outline='black')
    if event.char == '4':
        canvas.delete(treug1)
        canvas.delete(treug2)
        treug1 = canvas.create_polygon((650, 450), (700, 460), (650, 470), fill='black', outline='black')
        treug2 = canvas.create_polygon((760, 450), (710, 460), (760, 470), fill='black', outline='black')
    if event.char == '5':
        canvas.delete(treug1)
        canvas.delete(treug2)
        treug1 = canvas.create_polygon((650, 470), (700, 480), (650, 490), fill='black', outline='black')
        treug2 = canvas.create_polygon((760, 470), (710, 480), (760, 490), fill='black', outline='black')
    if event.char == '6':
        canvas.delete(treug1)
        canvas.delete(treug2)
        treug1 = canvas.create_polygon((650, 490), (700, 500), (650, 510), fill='black', outline='black')
        treug2 = canvas.create_polygon((760, 490), (710, 500), (760, 510), fill='black', outline='black')
    if event.char == '7':
        canvas.delete(treug1)
        canvas.delete(treug2)
        treug1 = canvas.create_polygon((650, 510), (700, 520), (650, 530), fill='black', outline='black')
        treug2 = canvas.create_polygon((760, 510), (710, 520), (760, 530), fill='black', outline='black')
    if event.char == '8':
        canvas.delete(treug1)
        canvas.delete(treug2)
        treug1 = canvas.create_polygon((650, 530), (700, 540), (650, 550), fill='black', outline='black')
        treug2 = canvas.create_polygon((760, 530), (710, 540), (760, 550), fill='black', outline='black')
    if event.char == '9':
        canvas.delete(treug1)
        canvas.delete(treug2)
        treug1 = canvas.create_polygon((650, 550), (700, 560), (650, 570), fill='black', outline='black')
        treug2 = canvas.create_polygon((760, 550), (710, 560), (760, 570), fill='black', outline='black')


master = tkinter.Tk()
player1_pic = tkinter.PhotoImage(file="Sherlok.gif")  # загружаем фон
# player_pic = tkinter.PhotoImage(file="pygame_test/target2.gif") # загружаем рисунок мишени, сейсчас не нужно

canvas = tkinter.Canvas(master, bg='white', height=600, width=800)
# canvas.create_line((0, 150), (800, 150), fill='red')
# canvas.create_line((0, 250), (800, 250), fill='red')

Back1 = canvas.create_image(100, 100, image=player1_pic, anchor='nw')  # устанавливаем фон
'''canvas.create_oval((100, 100), (220, 220), fill='orange')
canvas.create_oval((110, 110), (210, 210), fill='black')
canvas.create_oval((120, 120), (200, 200), fill='orange')
canvas.create_oval((130, 130), (190, 190), fill='black')
canvas.create_oval((140, 140), (180, 180), fill='orange')
canvas.create_oval((150, 150), (170, 170), fill='black')'''
line1 = canvas.create_line((x1 - 60, y1 + 65), (x1, y1 + 65), fill='black', width=8)
oval1 = canvas.create_oval((x1, y1), (x1 + 120, y1 + 120), fill='orange')
oval2 = canvas.create_oval((x1 + 10, y1 + 10), (x1 + 110, y1 + 110), fill='black')
oval4 = canvas.create_oval((x1 + 20, y1 + 20), (x1 + 100, y1 + 100), fill='orange')
oval5 = canvas.create_oval((x1 + 30, y1 + 30), (x1 + 90, y1 + 90), fill='black')
oval6 = canvas.create_oval((x1 + 40, y1 + 40), (x1 + 80, y1 + 80), fill='orange')
oval7 = canvas.create_oval((x1 + 50, y1 + 50), (x1 + 70, y1 + 70), fill='black')

treug1 = canvas.create_polygon((650, 390), (700, 400), (650, 410), fill='black', outline='black')
treug2 = canvas.create_polygon((760, 390), (710, 400), (760, 410), fill='black', outline='black')
scale = canvas.create_rectangle(700, 400, 710, 580, outline="#f11", fill="orange", width=2)
A = canvas.coords(oval1)[0]  # координата x1
B = canvas.coords(oval1)[1]  # координата y1
canvas.focus_set()
canvas.pack()
master.bind("<KeyPress>", key_pressed)

master.mainloop()
