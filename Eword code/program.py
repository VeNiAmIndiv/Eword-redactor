
# Библиотеки
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import time
import random

# Translit Dictionary
alphabetdict = {
    "й": "q",
    "ц": "w",
    "у": "e",
    "к": "r",
    "е": "t",
    "н": "y",
    "г": "u",
    "ш": "i",
    "щ": "o",
    "з": "p",
    "х": "[",
    "ъ": "]",
    "ф": "a",
    "ы": "s",
    "в": "d",
    "а": "f",
    "п": "g",
    "р": "h",
    "о": "j",
    "л": "k",
    "д": "l",
    "ж": ";",
    "э": "'",
    "я": "z",
    "ч": "x",
    "с": "c",
    "м": "v",
    "и": "b",
    "т": "n",
    "ь": "m",
    "б": ",",
    "ю": ".",
    ".": "/",  #
    "Й": "Q",
    "Ц": "W",
    "У": "E",
    "К": "R",
    "Е": "T",
    "Н": "Y",
    "Г": "U",
    "Ш": "I",
    "Щ": "O",
    "З": "P",
    "Х": "{",
    "Ъ": "}",
    "Ф": "A",
    "Ы": "S",
    "В": "D",
    "А": "F",
    "П": "G",
    "Р": "H",
    "О": "J",
    "Л": "K",
    "Д": "L",
    "Ж": ":",
    "Э": '"',
    "Я": "Z",
    "Ч": "X",
    "С": "C",
    "М": "V",
    "И": "B",
    "Т": "N",
    "Ь": "M",
    "Б": "<",
    "Ю": ">",
    ",": "?",
    "!": "!",
    "?": "&",
    "(": "(",
    ")": ")",
    '№': "#",
    ';': "$",
    '%': '%',
    '*': '*',
    '-': '-',
    '_': '_',
    "+": '+',
    "=": "=",
    " ": " ",
    "ё": "`",
    'Ё': '~',
    '/': '|',
    ':': '^'
}

# Функции
def translit(index):
    result = ''
    check = False
    try:
        if index == 0:
            eng_words = dict([[v, k] for k, v in alphabetdict.items()])
            mytext = text.get(0.0, END)
            for elem in mytext:
                for letter in eng_words:
                    if elem == letter:
                        result += eng_words[elem]
                        check = True
            if check:
                text.delete(0.0, END)
                text.insert(0.0, result)
                check = False
        elif index == 1:
            mytext = text.get(0.0, END)
            for elem in mytext:
                for letter in alphabetdict:
                    if elem == letter:
                        result += alphabetdict[elem]
                        check = True
            if check:
                text.delete(0.0, END)
                text.insert(0.0, result)
                check = False
    except:
        pass


# Города
citys = []
playerGo = 1
def game_1():
    global citys, playerGo
    r = Toplevel(root)
    r.geometry('490x310')
    r.resizable(False, False)
    r.title('Города')

    # - * - coding: utf-8 - * -
    a = open('cities.txt', 'r')
    b = a.readlines()
    a.close()


    for i in b:
        citys.append(i.replace('\n', ''))

    gameStart = False

    sti = []

    def instructon():
        roooot = Toplevel(r)
        roooot.geometry('250x160')
        roooot.config(bg='#ed674a')
        roooot.title('Правила')
        roooot.resizable(False, False)
        Label(roooot, width=25, height=8, text='Правила очень просты.\n'
                                               'Первый игрок вбивает\n'
                                               'любой город, следующий\n'
                                               'игрок должен вбить\nгород, '
                                               'который\nначинается с последней\n'
                                               'буквы города\nпредыдущего игрока.',
              bg='#ed674a', fg='#ffffff',
              font=('Bahnschrift SemiBold SemiConden', 13, 'bold')).grid(row=0, column=0)

    def statistics():
        global sti
        rooott = Toplevel(r)
        rooott.geometry('300x300')
        rooott.resizable(False, False)
        rooott.config(bg='#ed674a')
        rooott.title('Статистика')
        l = Listbox(rooott, width = 300, height = 300)
        l.delete(0, END)
        l.insert(END, *sti)
        l.pack()


    def players():
        global gameStart
        global gameplayers
        global sti
        if Players.get()!='':
            WichPlayer.grid(row=2, column=1, pady=5, padx=5)
            playerCity.grid(row=3, column=1, pady=5, padx=5)
            makeGo.grid(row=4, column=1, pady=5, padx=5)
            statistika.grid(row=5, column=1, pady=5, padx=5)
            gameplayers = Players.get()
            gameStart = True
            sti = []
        else:
            messagebox.showinfo('Ошибка!', 'Введите количество игроков!')

    lastLetter = ''
    a = 0
    def check():
        global citys
        global a
        global gameStart
        global gameplayers
        global playerGo
        global sti
        global lastLetter
        if gameStart == True:
            if playerCity.get()!='':
                c = playerCity.get()
                lastLetter = ''
                if a != 0:
                    if ((c not in citys) or (c[0] != lastLetter)) or ((c not in citys) and (c[0] != lastLetter)):
                        gameplayers = int(gameplayers) - 1
                        errorLb.config(text='-1 Игрок(не правилный город)', fg='red')
                        playerGo += 1
                        if int(playerGo) > int(gameplayers):
                            playerGo = 1
                        playerCity.delete(0, END)
                else:
                    errorLb.config(text='Правильно!', fg='green')
                    lastLetter = c[-1].upper()
                    sti.append(playerCity.get())
                    playerGo += 1
                    if int(playerGo) > int(gameplayers):
                        playerGo = 1
                    playerCity.delete(0, END)
                    a = 1

        else:
            errorLb.config(text='Введите количество игроков.')

        if int(gameplayers) == 1:
            errorLb.config(text='Game Over!', fg='red')
            messagebox.showinfo('Конец игры!', 'Игрок, который остался, победил!')
            r.destroy()
            return
        WichPlayer.config(text=('Ход игрока №' + str(playerGo)))

    r.config(bg='#ed674a')

    ima = Label(r,image=im)
    gameName = Label(r,text='Игра "Города"', font=('Bahnschrift SemiBold SemiConden', 20, 'bold'), width=15, bg='#ed674a',
                     fg='#ffffff')
    lbPlayers = Label(r,text='Сколько игроков:', font=('Bahnschrift SemiBold SemiConden', 13, 'bold'), width=20,
                      bg='#ed674a',
                      fg='#ffffff')
    Players = Entry(r,width=25)
    newGame = Button(r,text='Новая игра', width=20, font=('Bahnschrift SemiBold SemiConden', 13, 'bold'), bg='#d42600',
                     fg='#ffffff',
                     command=players)
    rules = Button(r,text='Правила', width=20, font=('Bahnschrift SemiBold SemiConden', 13, 'bold'), bg='#d42600',
                   fg='#ffffff', command=instructon)
    WichPlayer = Label(r,text=('Ход игрока №' + str(playerGo)), font=('Bahnschrift SemiBold SemiConden', 13, 'bold'),
                       width=20
                       , bg='#ed674a', fg='#ffffff')
    playerCity = Entry(r,width=25)
    makeGo = Button(r,text='Сделать ход', width=20, font=('Bahnschrift SemiBold SemiConden', 13, 'bold'), bg='#d42600',
                    fg='#ffffff',
                    command=check)
    statistika = Button(r,text='Статистика', width=20, font=('Bahnschrift SemiBold SemiConden', 13, 'bold'), bg='#d42600',
                        fg='#ffffff', command=statistics)
    errorLb = Label(r,text='', font=('Bahnschrift SemiBold SemiConden', 13, 'bold'), width=25, fg='blue', bg='#ed674a')

    ima.grid(row=0, column=0, pady=5, padx=5, rowspan=2)
    gameName.grid(row=0, column=1, pady=5, padx=0)
    errorLb.grid(row=1, column=1, pady=5, padx=0)
    lbPlayers.grid(row=2, column=0, pady=5, padx=5)
    Players.grid(row=3, column=0, pady=5, padx=5)
    newGame.grid(row=4, column=0, pady=5, padx=5)
    rules.grid(row=5, column=0, pady=5, padx=5)


    r.mainloop()


# 3-х литровая банка
def game_2():
    def start():
        w = Toplevel()

        w.geometry("400x250")
        w.resizable(False, False)
        w["bg"] = "#46211A"
        w.title('3-х литровая банка')
        a = ['абрикос', "апельсин", "арахис", 'абонемент', 'абонент', 'абсент', 'абсорбент', 'аванс'
            , 'авиабилет', 'авоська', 'агитка', 'агат', 'агар-агар', 'агава', 'адамант', 'акрихин', 'аконит'
            , 'аккумулятор', 'акварель', 'аквамарин', 'акация', 'айран', 'айва', 'аир', 'актиния', 'алтей', 'алмаз',
             'аллоскоп', 'алкоголь', 'алеврит', 'амариллис', 'алюминий', 'альбуцид', 'алыча', 'алтын', 'алтын', ]
        b = ["банан", "барометр", "бердак", "барабулька"]
        v = ['воздух', 'вода', 'верёвка', 'водка']
        i = ['яд', "ягоды", "ярона"]
        m = ['макрошка', 'малина', 'Макчикен']
        d = ['дабойя', 'дезерт игл']
        z = ['значок']
        e1 = Entry(w,width = 20, font=("Bahnschrift SemiBold SemiConden", "15"))
        e1.pack(expand = True)

        def ac():
            if e1.get().lower() in a:
                t1.config(text="молодец", fg = 'green')
            elif e1.lower() in b:
                t1.config(text="молодец", fg = 'green')
            elif e1.lower() in v:
                t1.config(text="молодец", fg = 'green')
            elif e1.lower() in i:
                t1.config(text="молодец", fg = 'green')
            elif e1.lower() in m:
                t1.config(text="молодец", fg = 'green')
            elif e1.lower() in d:
                t1.config(text="молодец", fg = 'green')
            elif e1.lower() in z:
                t1.config(text="молодец", fg = 'green')
            else:
                t1.config(text="проигрыш", fg = 'red')

        b1 = Button(w, text="ответ",width = 20, height = 2, bg ='#693D3D', fg = 'white', font=("Bahnschrift SemiBold SemiConden", "15"), command=ac)
        b1.pack(expand = True)
        t1 = Label(w, width = 20, height = 2, bg ='#693D3D', fg = 'white', font=("Bahnschrift SemiBold SemiConden", "15"))
        t1.pack(expand = True)
        b2 = Button(w, text="Выход", width=20, height=2, bg='#693D3D', fg='white',
                    font=("Bahnschrift SemiBold SemiConden", "15"), command=w.destroy)
        b2.pack(expand=True)
        w.mainloop()

    w = Toplevel()
    w["bg"] = "#46211A"
    w.resizable(False, False)
    w.title('3-х литровая банка')
    l1 = Label(w, text="ИНФОРМАЦИЯ об игре 3-х литровая банка\n"
                    "Игроку необходимо вводить слова. Программа после ввода слова пишет: молодец или проигрыш.\n В первом случае это означает верный ответ, а во втором - неверный."
                    " Вводить можно названия предметов,\nкоторые поместятся в 3-х литровую банку, на определённые буквы:а б в я м д з.\n"
                    "База слов в игре на данный момент небольшая.\n", bg ='#693D3D', fg = 'white', font=("Bahnschrift SemiBold SemiConden", "13"))
    l1.pack(padx = 10, pady = 10)

    def im():
        w.destroy()
        start()

    b1 = Button(w, text='Начать игру', width = 20, height = 2, bg ='#693D3D', fg = 'white', font=("Bahnschrift SemiBold SemiConden", "15"), command=im)
    b1.pack(padx = 10, pady = 10)

    def jd():
        w.destroy()

    b2 = Button(w, text="Закрыть игру", width = 20, height = 2, bg ='#693D3D', fg = 'white', font=("Bahnschrift SemiBold SemiConden", "15"), command=jd)
    b2.pack(padx = 10, pady = 10)
    w.mainloop()

# Виселица
def game_3():
    root = Toplevel()
    root.title("Виселица")
    canvas = Canvas(root, width=600, height=600, bg="#693D3D")
    canvas.pack()

    def but():
        y = 0
        while y < 600:
            x = 0
            while x < 600:
                canvas.create_rectangle(x, y, x + 33, y + 27, fill="white", outline="blue")
                x = x + 33
            y = y + 27
        canvas.create_line(10, 10, 10, 350, width=5)
        canvas.create_line(10, 10, 100, 10, width=5)
        canvas.create_line(10, 50, 50, 10, width=5)
        canvas.create_line(100, 10, 100, 70, width=5)
        canvas.create_rectangle(0, 350, 100, 400, fill="black")

    faq = '''Привет, игрок! Давай поиграем!
    Принцип игры:
    Компьютер загадывает слово — пишет на бумаге первую
    и последнюю букву слова и отмечает места для осталь-
    ных букв. Также рисуется виселица.
    Загаданное компьютером слово является именем сущест-
    вительным, нарицательным в именительном падеже един-
    ственного числа, либо множественного числа при отсу-
    тствии у слова формы единственного числа. Игрок пред-
    лагает букву, которая может входить в это слово. Если
    такая буква есть в слове, то компьютер пишет её над
    соответствующими этой букве чертами — столько раз,
    сколько она встречается в слове. Если такой буквы нет,
    то к виселице добавляется круг в петле, изображающий
    голову. Игрок продолжает отгадывать буквы до тех пор,
    пока не отгадает всё слово. За каждый неправильный от-
    вет компьютер добавляет одну часть туловища к виселице
    (их 6: голова, туловище, 2 руки и 2 ноги). Если тулови-
    ще в виселице нарисовано полностью, то игрок проигрыва-
    ет, считается повешенным. Если игроку удаётся угадать
    слово, он выигрывает.'''

    canvas.create_text(310, 260, text=faq, fill="white", font=("Bahnschrift SemiBold SemiConden", "15"))
    slova = ["матрёшка", "радиатор", "фигурист", "акционер", "академия", "бактерия", "близнецы", "гостиная", "директор",
             "единорог", "живопись", "лаборант", "пиццерия", "ресторан", "тренажер", "ценитель", "чечевица", "корзинка",
             "смартфон", "виселица", "мегагерц", "страница", "креветка", "микрофон", "диктофон", "туловище", "лабиринт"]

    def arr():
        but()
        word = random.choice(slova)
        wo = word[1:-1]
        wor = []
        for i in wo:
            wor.append(i)
        a0 = canvas.create_text(282, 40, text=word[0], fill="black", font=("Bahnschrift SemiBold SemiConden", "15"))
        a1 = canvas.create_text(315, 40, text="_", fill="black", font=("Bahnschrift SemiBold SemiConden", "15"))
        a2 = canvas.create_text(347, 40, text="_", fill="black", font=("Bahnschrift SemiBold SemiConden", "15"))
        a3 = canvas.create_text(380, 40, text="_", fill="black", font=("Bahnschrift SemiBold SemiConden", "15"))
        a4 = canvas.create_text(412, 40, text="_", fill="black", font=("Bahnschrift SemiBold SemiConden", "15"))
        a5 = canvas.create_text(444, 40, text="_", fill="black", font=("Bahnschrift SemiBold SemiConden", "15"))
        a6 = canvas.create_text(477, 40, text="_", fill="black", font=("Bahnschrift SemiBold SemiConden", "15"))
        a7 = canvas.create_text(510, 40, text=word[-1], fill="black", font=("Bahnschrift SemiBold SemiConden", "15"))
        list1 = [1, 2, 3, 4, 5, 6]
        alfabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        er = []
        win = []

        def a(v):
            ind_alf = alfabet.index(v)
            key = alfabet[ind_alf]
            if v in wor:
                ind = wor.index(v)
                b2 = list1[ind]
                wor[ind] = '1'

                def kord():
                    if b2 == 1:
                        x1, y1 = 315, 40
                    if b2 == 2:
                        x1, y1 = 347, 40
                    if b2 == 3:
                        x1, y1 = 380, 40
                    if b2 == 4:
                        x1, y1 = 412, 40
                    if b2 == 5:
                        x1, y1 = 444, 40
                    if b2 == 6:
                        x1, y1 = 477, 40
                    return x1, y1

                x1, y1 = kord()
                win.append(v)
                a2 = canvas.create_text(x1, y1, text=wo[ind], fill="black",
                                        font=("Bahnschrift SemiBold SemiConden", "15"))
                btn[key]["bg"] = "green"
                if not v in wor:
                    btn[key]["state"] = "disabled"
                if v in wor:
                    win.append(v)
                    ind2 = wor.index(v)
                    b2 = list1[ind2]
                    x1, y1 = kord()
                    canvas.create_text(x1, y1, text=wo[ind2], fill="black",
                                       font=("Bahnschrift SemiBold SemiConden", "15"))
                if len(win) == 6:
                    canvas.create_text(370, 370, text="Ты победил", fill="black",
                                       font=("Bahnschrift SemiBold SemiConden", "30"))

                    for i in alfabet:
                        btn[i]["state"] = "disabled"

            else:

                er.append(v)
                btn[key]["bg"] = "red"
                btn[key]["state"] = "disabled"

                if len(er) == 1:
                    golova()
                elif len(er) == 2:
                    telo()
                elif len(er) == 3:
                    rukap()
                elif len(er) == 4:
                    rukal()
                elif len(er) == 5:
                    nogal()
                elif len(er) == 6:
                    nogap()
                    end()
                root.update()

        btn = {}

        def gen(u, x, y):

            btn[u] = Button(root, text=u, width=3, height=1, font=("Bahnschrift SemiBold SemiConden", "12"),
                            command=lambda: a(u))
            btn[u].place(x=str(x), y=str(y))

        x = 265
        y = 110
        for i in alfabet[0:8]:
            gen(i, x, y)
            x = x + 33
        x = 265
        y = 137
        for i in alfabet[8:16]:
            gen(i, x, y)
            x = x + 33
        x = 265
        y = 164
        for i in alfabet[16:24]:
            gen(i, x, y)
            x = x + 33
        x = 265
        y = 191
        for i in alfabet[24:33]:
            gen(i, x, y)
            x = x + 33

        def end():
            canvas.create_text(370, 370, text="Ты проиграл", fill="black",
                               font=("Bahnschrift SemiBold SemiConden", "30"))
            for i in alfabet:
                btn[i]["state"] = "disabled"

        def golova():
            canvas.create_oval(85, 70, 115, 100, width=4, fill="white")
            root.update()

        def telo():
            canvas.create_line(100, 100, 100, 220, width=4)
            root.update()

        def rukap():
            canvas.create_line(100, 100, 145, 120, width=4)
            root.update()

        def rukal():
            canvas.create_line(100, 100, 45, 120, width=4)
            root.update()

        def nogal():
            canvas.create_line(100, 220, 45, 320, width=4)
            root.update()

        def nogap():
            canvas.create_line(100, 220, 145, 320, width=4)
            root.update()
            end()

    btn01 = Button(root, text="Начать!", width=10, height=1, fg="white", font=("Bahnschrift SemiBold SemiConden", "15"),
                   activebackground="#46211A", command=lambda: arr())
    btn01.place(x=258, y=542)
    btn01["bg"] = "#693D3D"

    btn02 = Button(root, text="Выйти", width=10, height=1, fg="white", font=("Bahnschrift SemiBold SemiConden", "15"),
                   activebackground="#46211A", command=root.destroy)
    btn02.place(x=400, y=542)
    btn02["bg"] = "#693D3D"

    root.mainloop()



a = False
count = 0
timetime = 15
# Придумай рифму
def game_4():
    global a, count, timetime
    window = Toplevel()
    window.geometry('450x450')
    window.title('ПРИДУМАЙ РИФМУ ЗА 15 СЕКУНД')
    window.resizable('False', 'False')
    window['bg'] = '#46211A'
    count = 0
    # , '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''
    words = ['карандаш', 'тропинка', 'путешествие', 'зайчонок', 'снежинка', 'коробок', 'зеленый', 'мудрец', 'мужчина',
             'женщина', 'брусника', 'панкейк', 'холодец']
    random.shuffle(words)

    timetime = 15

    word = words[2]


    def main(e):
        global word, count, timetime, rec
        if answerEntry.get()[-3:] == word[-3:]:
            random.shuffle(words)
            word = words[1]
            answerEntry.delete(0, END)
            yourwordLabel['text'] = word
            count += 1
            scorecountLabel['text'] = str(count)
            timetime = 15
            timeLabel['text'] = timetime

    #        updatedisplay()

    def updatedisplay():
        global timetime, a
        if not a:
            if timetime > 0:
                timetime -= 1
                timeLabel['text'] = timetime
                window.after(1000, updatedisplay)
            else:
                messagebox.showerror('ВРЕМЯ ИСТЕКЛО!', 'Вы не смогли придумать рифму к слову ' + '"' + str(
                    word) + '"' + ' за заданное время. Ваш счёт: ' + str(count))
                a = False
                window.destroy()

    def start():
        global timetime, count, word
        answerEntry.delete(0, END)
        yourwordLabel.place(x=167, y=180)
        timetime = 15
        
        word = words[2]
        yourwordLabel['text'] = word
        scorecountLabel['text'] = str(count)
        timeLabel['text'] = timetime
        updatedisplay()

    def s():
        yourwordLabel.place_forget()

    def stop():
        global a
        a = False
        messagebox.showinfo('ИГРА ОКОНЧЕНА!', 'Вы вышли из игры. Ваш счёт: ' + str(count))
        window.destroy()

    answerEntry = Entry(window, bg='#A43820', font='Arial 14')
    readyButton = Button(window, bg='#693D3D', text='Готово!', font='Arial 19', fg='#25206e',
                         command=lambda a=1: main(a))
    scorecountLabel = Label(window, text=count, font='Arial 22', bg='#46211A', fg='white')
    timeLabel = Label(window, text=timetime, font='Arial 22', bg='#46211A', fg='white')
    lbl1 = Label(window, text='Ваш счёт:', font='Arial 18', bg='#46211A', fg='#A43825')
    lbl2 = Label(window, text='ВАШЕ СЛОВО:', font='Arial 18', bg='#46211A', fg='#A43825')
    lbl3 = Label(window, text='Время:', font='Arial 18', bg='#46211A', fg='#A43825')
    yourwordLabel = Label(window, text=word, font='Arial 18', bg='#46211A', fg='white')
    startButton = Button(window, bg='#693D3D', text='Старт!', font='Arial 20', fg='#3b7a54', command=start)
    stopButton = Button(window, bg='#693D3D', text='Вернуться в меню', font='Arial 20', fg='#2b8784', command=stop)

    scorecountLabel.place(x=120, y=0)
    timeLabel.place(x=416, y=-2)
    lbl1.place(x=0, y=4)
    answerEntry.place(x=114, y=220)
    readyButton.place(x=168, y=280)
    lbl2.place(x=142, y=140)
    yourwordLabel.place(x=167, y=180)
    lbl3.place(x=330, y=4)
    startButton.place(x=50, y=370)
    stopButton.place(x=150, y=370)

    s()
    answerEntry.bind('<Return>', main)

    window.mainloop()


# Текстовый квест
def game_5():
    window = Toplevel(root)
    window.geometry("900x562")
    window.title("Текстовый квест")
    window.resizable(False, False)
    def c1():
        label1.config(text='Вы добились успеха победив пару рыцарей на турнире!')
        d.pack_forget()
        e.pack_forget()
        b.config(text='Ехать и совершать подвиги.', command=b1)
        c.config(text='Продолжать стремиться по карьере к рыцарям круглого стола.', command=a1)
    def b1():
        b.pack_forget()
        c.pack_forget()
        label1.config(text='У вас ничего не получилось.\n Конец игры!')
        label1.pack(expand=True)
    def a1():
        label1.config(text='Король Артур заинтересован в вас.')
        c.config(text='Нажмите, чтобы пройти финальный бой.', command=d1)
        b.pack_forget()
    def d1():
        label1.config(text='Вы стали главным рыцарем круглого стола и генералом армии.\n Вы прошли игру!')
        c.pack_forget()
        label1.pack(expand=True)
    def e1():
        label1.config(text='Продолжайте.')
        c.pack_forget()
        d.pack_forget()
        e.config(text='Вы можете стать уличным фокусником и заработать свою первую славу.', command=f1)
        b.config(text='Вы можете добиться успеха у короля.', command=g1)
    def f1():
        label1.config(text='И что же дальше?')
        e.config(text='Продолжать стремиться добиваться славы.', command=i1)
        b.config(text='Нажмите, чтобы продолжить карьеру шута.')
    def g1():
        label1.config(text='Вы не добились никакого успеха.\n Конец игры!')
        label1.pack(expand=True)
        b.pack_forget()
        e.pack_forget()
    def h1():
        label1.config(text='Вы стремитесь к провалу, но выхода нет.')
        e.pack_forget()
        b.config('Нажмие сюда.', command=h1)
    def i1():
        label1.config(text='Вы стали известнейшим фокусником Британии.\n И прошли игру!')
        e.pack_forget()
        b.pack_forget()
        label1.pack(expand=True)
    def j1():
        label1.config(text='Выбирайте, что вам по душе.')
        d.pack_forget()
        c.config(text='Вы можете стать синоптиком и ботаником.', command=k1)
        b.config(text='Вы можете производить вещи быта.', command=m1)
        e.config(text='Вы можете производить огнестрельное оружие и давать его армии.', command=t1)
    def k1():
        label1.config(text='У вас мало что получается из-за большой конкурентности, но шансы есть.')
        c.pack_forget()
        b.pack_forget()
        e.config(text='Продолжайте.', command=l1)
    def l1():
        label1.config(text='В итоге вы сообщили глупость и больше вас не воспринимают в серьез.\n Конец игры!')
        e.pack_forget()
        label1.pack(expand=True)
    def m1():
        label1.config(text='Прекрасный выбор!')
        c.pack_forget()
        b.config(text='Вы можете открыть свою собсвенную компанию.', command=n1)
        e.config(text='У вас все отлично получается, продолжайте в том же духе (вы работате на заказ).', command=r1)
    def n1():
        label1.config(text=' ')
        b.config(text='Вы открыли свою компанию и очень быстро набираете популярность во всей стране.', command=p1)
        e.config(text='Или вы можете продать свою компанию и уйти на пенсию.', command=o1)
    def o1():
        label1.config(text='Вы все пропили и потратили. Теперь вы нищий.\n Конец игры!')
        b.pack_forget()
        e.pack_forget()
        label1.pack(expand=True)
    def p1():
        label1.config(text='Вы открыли свои первые магазины в других странах.')
        e.pack_forget()
        b.config(text='Продолжайте в том же духе!', command=q1)
    def q1():
        label1.config(text='У вас самая популярная компания в мире по производству мебели и другого.\n Вы прошли игру!')
        b.pack_forget()
        label1.pack(expand=True)
    def r1():
        label1.config(text='Вы набираете славу, но при этом приходиться много работать из-за большого\n количества заказов и вы сильно устаете.')
        b.pack_forget()
        e.config(text='Удачи!', command=s1)
    def s1():
        label1.config(text='Вы разорились.\n Конец игры!')
        e.pack_forget()
        label1.pack(expand=True)
    def t1():
        label1.config(text='Вы добились немалого успеха, что будете делать дальше?')
        c.pack_forget()
        b.config(text='Вам это надоело, хотите чего-то нового?', command=u1)
        e.config(text='Будете продолжать?', command=v1)
    def u1():
        label1.config(text='Вы ничего не нашли, впали в депрессию и ушли в запой.\n Конец игры!')
        b.pack_forget()
        e.pack_forget()
        label1.pack(expand=True)
    def v1():
        label1.config(text='У вас ничего не получилось, много заказов и не хватило рук\n Конец игры!')
        b.pack_forget()
        e.pack_forget()
        label1.pack(expand=True)
    def w1():
        label1.config(text='К сожалению у вас ничего не получилось, вы не умеете драться и воевать\n Конец игры!')
        c.pack_forget()
        e.pack_forget()
        b.pack_forget()
        d.pack_forget()
        label1.pack(expand=True)
    #Виджеты и их аргументы
    
    l = Label(window, width=900, height=562, image=i)
    l.place(x=0, y=0)
    label1 = Label(window,text='Вы попали в средневековье. Вы сейчас где-то\n'
        'в конце 12-го века. Какие будут дальнейшие действия?',
        justify = CENTER, relief = RAISED,
        bd = 5, bg='chocolate3', fg='white', font=('Bahnschrift SemiBold SemiConden', 13, 'bold'),
        width=75, height=5)
    label1.pack(expand=True)
    b = Button(window, text='Показать какие-нибудь неизвестные фокусы или эксперименты и\n'
                 'понравиться королю.',pady=10, bg='#693D3D', fg='white',width = 70, font=('Bahnschrift SemiBold SemiConden', 13, 'bold'), command=e1)
    b.pack(padx=10, pady=3, expand=True)
    c = Button(window,text='Попробовать поступить в рыцари.',pady=10, bg='#693D3D', fg='white',width = 70, font=('Bahnschrift SemiBold SemiConden', 13, 'bold'), command=c1)
    c.pack(padx=10, pady=3, expand=True)
    d = Button(window,text='Стать великим ученым и изобретателем.',pady=10, bg='#693D3D',fg='white',width = 70, font=('Bahnschrift SemiBold SemiConden', 13, 'bold'), command=j1)
    d.pack(padx=10, pady=3, expand=True)
    e = Button(window,text='Прославиться благодаря подвигам.', pady=10, bg='#693D3D',fg='white',width = 70, font=('Bahnschrift SemiBold SemiConden', 13, 'bold'), command=w1)
    e.pack(padx=10, pady=3, expand=True)
    f = Button(window,text='ВЫХОД', bg='Red',fg='white',width = 70, pady=10, font=('Bahnschrift SemiBold SemiConden', 13, 'bold'), command=window.destroy)
    f.pack(padx=10, pady=3, expand=True)


# Кликер
score = 0
R = 0
R1 = 0
startTime = 0

def game_6():
    global button_word
    def new_button():
        global startTime
        endTime = time.time()
        scoreTime = round(endTime - startTime, 3)
        global score
        global button_word
        button_word.destroy()
        startTime = time.time()
        display_word_on_button = random.choice(
            ["ITGEN.IO", "#HACKATHON \n2020", "Python", "Proggraming", "CLICK ME PLS", "Coding", "Keyboard",
             "Mouse Game", "Text Game", "Keyboard Game"])
        button_word = Button(window, text=display_word_on_button, width=15, height=5, command=new_button,
                             activebackground='#46211A', activeforeground="white")
        button_word["bg"] = "#693D3D"
        button_word["fg"] = "white"
        x_word_pos = random.randint(100, 1000)
        y_word_pos = random.randint(100, 600)
        button_word.place(x=x_word_pos, y=y_word_pos)
        if scoreTime < 1:
            score += 3
        elif scoreTime < 2 and scoreTime > 1:
            score += 2
        else:
            score += 1
        scoreText["text"] = score

    # ==== Function 2 = resetscore() ====
    def resetscore():
        global score
        score = 0
        scoreText["text"] = score

    # ==== Function 3 - showRules() ====
    def showHideRules():
        global R
        if R == 0:
            hideShowRulesButton.config(
                text="Rules: \n 1. You Need to click the button that spawn in a random \n position on the screen with a random word\n 2. If you want to reset the score, click the Reset Score button.\n 3. As Faster You Click the word, you'll get more score.")
            R = 1
        else:
            hideShowRulesButton.config(text="Show Rules")
            R = 0

    # ==== Function 4 - showWordsCanSpawn() ====
    def showHideWordsCanSpawn():
        global R1
        if R1 == 0:
            showHideWordsCanSpawnButton.config(
                text='Words Can Spawn: \n "ITGEN.IO", "#HACKATHON 2020", "Python", "Proggraming"\n "CLICK ME PLS", "Coding", "Keyboard", "Mouse Game",\n "Text Game" And "Keyboard Game"')
            R1 = 1
        else:
            showHideWordsCanSpawnButton.config(text="Show Words Can spawn")
            R1 = 0

    # ==== Function 5 - closeGame() ====
    def closeGame():
        window.destroy()

    # ==== Settings Continue ====

    window = Toplevel(root)
    window.title("WordC | EWord")
    window.geometry("1200x800")
    window.maxsize(1200, 800)
    window.minsize(1200, 800)
    window["bg"] = "#46211A"
    # ==== Codes For Buttons and Labels ====
    hideShowRules = IntVar()
    hideShowRules.set(0)
    hideShowRulesButton = Checkbutton(window, text="Show Rules", font=("Bahnschrift SemiBold SemiConden", "13", "bold"),
                                      variable=hideShowRules, activeforeground="white", activebackground="#46211A",
                                      onvalue=1, offvalue=0, indicatoron=0, height=5, command=showHideRules)
    hideShowRulesButton["bg"] = "#693D3D"
    hideShowRulesButton["fg"] = "#46211A"
    hideShowRulesButton.place(relx=0.6, y="0", relwidth=0.4)
    scoreLabel = LabelFrame(window, text="Score")
    scoreLabel.pack(anchor=N, expand=True)
    scoreText = Label(scoreLabel, text=f"{score}", width=10, height=2)
    home_button = Button(window, text="Quit The Game", width=84, height=5, command=closeGame,
                         activebackground="#46211A", activeforeground="white")
    scoreText.pack()
    home_button["bg"] = "#693D3D"
    home_button.pack(anchor=SE)
    scoreLabel["bg"] = "#46211A"
    scoreText["bg"] = "#46211A"
    scoreText["fg"] = "white"
    scoreLabel["fg"] = "white"
    home_button["fg"] = "white"
    scoreResetButton = Button(window, text="Reset Score", width=85, height=5, activebackground="#46211A", bg="#693D3D",
                              fg="white", activeforeground="white", command=resetscore)
    scoreResetButton.place(x="0", y="714")
    wordsCanSpawnValue = IntVar()
    wordsCanSpawnValue.set(0)
    showHideWordsCanSpawnButton = Checkbutton(window, text="Show Words Can Spawn",
                                              font=("Bahnschrift SemiBold SemiConden", "13", "bold"),
                                              variable=wordsCanSpawnValue, height=5, indicatoron=0,
                                              activeforeground="white", activebackground="#46211A",
                                              command=showHideWordsCanSpawn)
    showHideWordsCanSpawnButton.place(x="0", y="0", relwidth=0.4)
    showHideWordsCanSpawnButton["bg"] = "#693D3D"
    showHideWordsCanSpawnButton["fg"] = "#46211A"
    # ==== Primary Code ====
    display_word_on_button = random.choice(
        ["ITGEN.IO", "#HACKATHON \n2020", "Python", "Proggraming", "CLICK ME PLS", "Coding", "Keyboard", "Mouse Game",
         "Text Game", "Keyboard Game"])
    startTime = time.time()
    button_word = Button(window, text=display_word_on_button, width=15, height=5, command=new_button,
                         activebackground='#46211A', activeforeground="white")
    button_word["bg"] = "#693D3D"
    button_word["fg"] = "white"
    x_word_pos = random.randint(100, 1000)
    y_word_pos = random.randint(100, 600)
    button_word.place(x=x_word_pos, y=y_word_pos)
    # End

abb_score = 0
# Игра Саши
def game_7():
    global abb_score
    a = ["ФСБ", "ЗОЖ",
         "РНО", "США",
         "ВДВ", "АЗС",
         "КНР", "СМИ",
         "МИД", "БТР",
         "БАД", "ОАЭ",
         "ГЭС", "АКПП",
         "ЕС", "АБР"]

    b = ["Федеральная Служба Безопасности",
         "Здоровый Образ Жизни",
         "Работа Над Ошибками",
         "Соединённые Штаты Америки",
         "Воздушно-Десантные Войска",
         "Автомобильная Заправочная Станция",
         "Китайская Народная Республика",
         "Средства Ма́ссовой Информа́ции",
         "Министерство Иностранных Дел",
         "Бронетранспортёр",
         "Биологически Активная Добавка",
         "Объединённые Арабские Эмираты",
         "Гидроэлектроста́нция",
         "Автоматическая Коробка Перемены Передач",
         "Европейский Союз",
         "Ассоциация Банков России"]


    def abb_rule():  # функция создания окна приветствия
        def yes():
            abbroot_1.destroy()
            abb_game()
        abbroot_1 = Toplevel(root)
        abbroot_1.title("Угадай аббревиатуру: Правила.)")
        abbroot_1.geometry("500x500")
        abbroot_1.resizable(False, False)

        c9 = Canvas(abbroot_1, bg="#46211A", width=500, height=500)
        c9.place(x=0, y=0)

        abb_rule_label = Label(abbroot_1, bg="#46211A", fg="white",
                               text="Правила очень просты:\nНа экран выводяться\nаббревиатуры, которые\nты должен расшифровать.\nНапример: СНГ - Союз\nНезависимых Государств.",
                               font="Arial, 25", justify=CENTER)
        abb_rule_label.place(relx=0.5, rely=0.4, anchor=CENTER)

        abb_rule_button = Button(abbroot_1, text="Начать!", bg="#693D3D", fg="white", height=1, width=20, font = font,
                                 command=yes)
        abb_rule_button1 = Button(abbroot_1, text="Выход", bg="#693D3D", fg="white", height=1, width=20,font = font,
                                 command=abbroot_1.destroy)
        abb_rule_button.place(relx=0.5, rely=0.8, anchor=CENTER)
        abb_rule_button1.place(relx=0.5, rely=0.9, anchor=CENTER)

    def abb_game():  # функция игрового окна
        global abb_score
        ran = random.choice(a)
        def check_abb():
            global abb_score  # функция проверки ответа
            text_abb = abb_game_entry.get()
            if text_abb !='':
                if abb_game_label['text'].lower()== str(ran).lower():
                    abb_score += 1
                    abb_game_root.destroy()
                    abb_game()


        abb_game_root = Toplevel(root)
        abb_game_root.title("Игра: Угадай Аббревиатуру.")
        abb_game_root.geometry("400x400")
        abb_game_root.resizable(False, False)

        c9 = Canvas(abb_game_root, bg="#46211A", width=720, height=720)
        c9.place(x=0, y=0)

        abb_game_label = Label(abb_game_root, text=ran, bg="#46211A", fg="white", font="Arial, 100")
        abb_game_label.place(relx=0.5, rely=0.3, anchor=CENTER)

        abb_game_score = Label(abb_game_root, text="Score:" + str(abb_score), bg="#46211A", fg="white",
                               font="Arial, 13")
        abb_game_score.place(relx=0.8, rely=0.05, anchor=CENTER)

        abb_game_entry = Entry(abb_game_root, font = font)
        abb_game_entry.place(relx=0.5, rely=0.6, anchor=CENTER)

        abb_game_button = Button(abb_game_root, text="Проверить!", bg="#693D3D", fg="white", height=2, width=30,font = font,
                                 command=check_abb)
        abb_game_button.place(relx=0.5, rely=0.75, anchor=CENTER)

        abb_game_button1 = Button(abb_game_root, text="Выход", bg="#693D3D", fg="white", height=2, width=30,font = font,
                                 command=abb_game_root.destroy)
        abb_game_button1.place(relx=0.5, rely=0.9, anchor=CENTER)

    abb_rule()


# Первые 6
def command_1(a):
    if text.get(0.0,END)!='\n':
        mytext = text.get(0.0, END)
        text.delete(0.0, END)
        if a == 1:
            mytext = mytext.upper()
        elif a == 2:
            mytext = mytext.lower()
        elif a == 3:
            mytext = mytext.swapcase()
        elif a == 5:
            mytext = mytext.capitalize()
        elif a == 6:
            mytext = mytext.title()
        a = mytext.split('\n')
        del a[-1]
        a = '\n'.join(a)
        text.insert(0.0, a)
    else:
        messagebox.showerror("Ошибка","Отсутствует текст...")


def symbol():
    mytext = text.get(0.0, END)
    x = len(mytext)
    t = ""
    for i in mytext:
        if i != " ":
            t = t + i
    messagebox.showinfo("", "Общее количество символов (с пробелами): " + str(
        x-1) + "\nОбщее количество символов (без пробелов): " + str(len(t)-1))


# Сколько раз встречается
def command_2():
    if ent_command_7.get()!='':
        letter = ent_command_7.get()
        mytext = text.get(0.0, END)
        n = mytext.count(letter)
        ent_command_7.delete(0, END)
        messagebox.showinfo("", "Количество букв { " + str(letter) + " } в тексте: " + str(n))
    else:
        messagebox.showerror("Ошибка", "Вы не указали букву...")

# Заменить на
def command_3():
    if ent_command_9.get() != '':
        if ent_command_11.get() != '':
            old = ent_command_9.get()
            new = ent_command_11.get()
            mytext = text.get(0.0, END)
            mytext = mytext.replace(old, new)
            a = mytext.split('\n')
            del a[-1]
            a = '\n'.join(a)
            text.delete(0.0, END)
            text.insert(0.0, a)
            ent_command_9.delete(0, END)
            ent_command_11.delete(0, END)
        else:
            messagebox.showerror("Ошибка", "Вы не указали то, на что желаете изменить")
    else:
        messagebox.showerror("Ошибка", "Вы не указали то, что желаете изменить")


# Закраска
def Loadfile():
    filename = filedialog.Open(root, filetypes = [("*.txt files", ".txt")]).show()
    if filename == "":
        return
    text.delete("1.0", "end")
    text.insert("1.0", open(filename, "rt").read())


# Cохранениe
def Savefile():
    filename = filedialog.SaveAs(root, filetypes = [("*.txt files", ".txt")]).show()
    if filename == "":
        return
    if not filename.endswith(".txt"):
        filename += ".txt"
    open(filename, "wt").write(text.get("1.0", "end"))

def Newfile():
    NEW_MESSAGEBOX = messagebox.askyesno(title="Новый",
                                         message="Вы уверены, что хотите создать новый файл? "
                                                  "Все несохраненные данные будут потеряны.")
    if NEW_MESSAGEBOX == True:
        text.delete("1.0", "end")

# Шрифт и цвета и т.д
font = ('Bahnschrift SemiBold SemiConden', 13, 'bold')  # Шрифт
font_g = ('Bahnschrift SemiBold SemiConden', 15, 'bold')
colors = 'w'
# Темные цвета
bg_b = '#46211A'  # Цвет фона
bg_btn_off_b = '#693D3D'  # Цвет кнопок
bg_frm_b = '#A43820'  # Цвет областей
font_color_b = 'white'  # Цвет надписи кнопок
font_color_l_b = 'white'  # Цвет Лейбл
bg_btn_on_b = '#46211A'  # Цвет кнопок нажатая
ent_b = 'white'  # Цвет маленького текста

# Светлые цвета
bg_w = '#d8d8d8'  # Цвет фона
bg_btn_off_w = '#B27373'  # Цвет кнопок
bg_frm_w = 'white'  # Цвет областей
font_color_w = 'black'  # Цвет надписи кнопок
font_color_l_w = 'black'  # Цвет Лейбл
bg_btn_on_w = '#693D3D'  # Цвет кнопок нажатая
ent_w = '#A9A9A9'  # Цвет маленького текста

# Настройка окна
root = Tk()
root.title('Eword')
root.geometry('1200x700')
root.minsize(1200, 700)
root['bg'] = bg_w
root.iconbitmap('icon.ico')

mainmenu = Menu(root)
root.config(menu=mainmenu)


def topic(color):
    global bg_w, bg_frm_w, bg_btn_on_w, bg_btn_off_w, font_color_w, font_color_l_w, ent_w
    global bg_b, bg_frm_b, bg_btn_on_b, bg_btn_off_b, font_color_b, font_color_l_b, ent_b
    global colors
    if color == 'w':
        colors = 'w'
        root['bg'] = bg_w
        frm_translator.config(bg=bg_frm_w)
        btn_translator_eng.config(bg=bg_btn_off_w, fg=font_color_w, activebackground=bg_btn_on_w,
                                  activeforeground=font_color_w)
        btn_translator_rus.config(bg=bg_btn_off_w, fg=font_color_w, activebackground=bg_btn_on_w,
                                  activeforeground=font_color_w)
        frm_command.config(bg=bg_frm_w)
        btn_command_1.config(bg=bg_btn_off_w, fg=font_color_w, activebackground=bg_btn_on_w,
                             activeforeground=font_color_w)
        btn_command_2.config(bg=bg_btn_off_w, fg=font_color_w, activebackground=bg_btn_on_w,
                             activeforeground=font_color_w)
        btn_command_3.config(bg=bg_btn_off_w, fg=font_color_w, activebackground=bg_btn_on_w,
                             activeforeground=font_color_w)
        btn_command_4.config(bg=bg_btn_off_w, fg=font_color_w, activebackground=bg_btn_on_w,
                             activeforeground=font_color_w)
        btn_command_5.config(bg=bg_btn_off_w, fg=font_color_w, activebackground=bg_btn_on_w,
                             activeforeground=font_color_w)
        btn_command_6.config(bg=bg_btn_off_w, fg=font_color_w, activebackground=bg_btn_on_w,
                             activeforeground=font_color_w)
        btn_command_8.config(bg=bg_btn_off_w, fg=font_color_w, activebackground=bg_btn_on_w,
                             activeforeground=font_color_w)
        btn_command_10.config(bg=bg_btn_off_w, fg=font_color_w, activebackground=bg_btn_on_w,
                              activeforeground=font_color_w)
        ent_command_7.config(bg=ent_w)
        ent_command_9.config(bg=ent_w)
        ent_command_11.config(bg=ent_w)
        frm_game.config(bg=bg_frm_w)
        lbl_game.config(bg=bg_frm_w, fg=font_color_l_w)
        btn_game_1.config(bg=bg_btn_off_w, fg=font_color_w, activebackground=bg_btn_on_w,
                          activeforeground=font_color_w)
        btn_game_2.config(bg=bg_btn_off_w, fg=font_color_w, activebackground=bg_btn_on_w,
                          activeforeground=font_color_w)
        btn_game_3.config(bg=bg_btn_off_w, fg=font_color_w, activebackground=bg_btn_on_w,
                          activeforeground=font_color_w)
        btn_game_4.config(bg=bg_btn_off_w, fg=font_color_w, activebackground=bg_btn_on_w,
                          activeforeground=font_color_w)
        btn_game_5.config(bg=bg_btn_off_w, fg=font_color_w, activebackground=bg_btn_on_w,
                          activeforeground=font_color_w)
        btn_game_6.config(bg=bg_btn_off_w, fg=font_color_w, activebackground=bg_btn_on_w,
                          activeforeground=font_color_w)
        btn_game_7.config(bg=bg_btn_off_w, fg=font_color_w, activebackground=bg_btn_on_w,
                          activeforeground=font_color_w)
    else:
        colors = 'b'
        root['bg'] = bg_b
        frm_translator.config(bg=bg_frm_b)
        btn_translator_eng.config(bg=bg_btn_off_b, fg=font_color_b, activebackground=bg_btn_on_b,
                                  activeforeground=font_color_b)
        btn_translator_rus.config(bg=bg_btn_off_b, fg=font_color_b, activebackground=bg_btn_on_b,
                                  activeforeground=font_color_b)
        frm_command.config(bg=bg_frm_b)
        btn_command_1.config(bg=bg_btn_off_b, fg=font_color_b, activebackground=bg_btn_on_b,
                             activeforeground=font_color_b)
        btn_command_2.config(bg=bg_btn_off_b, fg=font_color_b, activebackground=bg_btn_on_b,
                             activeforeground=font_color_b)
        btn_command_3.config(bg=bg_btn_off_b, fg=font_color_b, activebackground=bg_btn_on_b,
                             activeforeground=font_color_b)
        btn_command_4.config(bg=bg_btn_off_b, fg=font_color_b, activebackground=bg_btn_on_b,
                             activeforeground=font_color_b)
        btn_command_5.config(bg=bg_btn_off_b, fg=font_color_b, activebackground=bg_btn_on_b,
                             activeforeground=font_color_b)
        btn_command_6.config(bg=bg_btn_off_b, fg=font_color_b, activebackground=bg_btn_on_b,
                             activeforeground=font_color_b)
        btn_command_8.config(bg=bg_btn_off_b, fg=font_color_b, activebackground=bg_btn_on_b,
                             activeforeground=font_color_b)
        btn_command_10.config(bg=bg_btn_off_b, fg=font_color_b, activebackground=bg_btn_on_b,
                              activeforeground=font_color_b)
        ent_command_7.config(bg=ent_b)
        ent_command_9.config(bg=ent_b)
        ent_command_11.config(bg=ent_b)
        frm_game.config(bg=bg_frm_b)
        lbl_game.config(bg=bg_frm_b, fg=font_color_l_b)
        btn_game_1.config(bg=bg_btn_off_b, fg=font_color_b, activebackground=bg_btn_on_b,
                          activeforeground=font_color_b)
        btn_game_2.config(bg=bg_btn_off_b, fg=font_color_b, activebackground=bg_btn_on_b,
                          activeforeground=font_color_b)
        btn_game_3.config(bg=bg_btn_off_b, fg=font_color_b, activebackground=bg_btn_on_b,
                          activeforeground=font_color_b)
        btn_game_4.config(bg=bg_btn_off_b, fg=font_color_b, activebackground=bg_btn_on_b,
                          activeforeground=font_color_b)
        btn_game_5.config(bg=bg_btn_off_b, fg=font_color_b, activebackground=bg_btn_on_b,
                          activeforeground=font_color_b)
        btn_game_6.config(bg=bg_btn_off_b, fg=font_color_b, activebackground=bg_btn_on_b,
                          activeforeground=font_color_b)
        btn_game_7.config(bg=bg_btn_off_b, fg=font_color_b, activebackground=bg_btn_on_b,
                          activeforeground=font_color_b)


def eword_exit():
    EXIT_MESSAGEBOX = messagebox.askyesno(title = "Выйти",
                                          message = "Вы уверены, что хотите выйти из программы? "
                                                    "Все несохраненные данные будут потеряны.")
    if EXIT_MESSAGEBOX == True:
        root.destroy()


def help_message():
    MESSAGE_1 = messagebox.showinfo(title="Помощь",
                                    message="При возникновении ошибок в работе программы можете обратиться на почту: eword@gmail.com")


def helproot_function():
    helproot = Toplevel()
    helproot.geometry('400x400')
    helproot.resizable(False, False)
    helproot.title("О программе")
    if colors == 'w':
        helproot['bg'] = bg_w




        #helpmenu_title = Label(helproot, text="EWord", font="Arial, 40", bg="#46211A", fg="blue")
        #helpmenu_title.place(x=110, y=50)

        helpmenu_text = Label(helproot,
                               text="\nЭто универсальный редактор строк "
                               "\nс интересными текстовыми мини-играми\n "
                               "такими как: 3х литровая банка,"
                               "\n Игра в Города, Текстовый квест,\n Кликер.",
                          font=font, bg=bg_w, fg="blue")
        helpmenu_text.place(relx=0.5, rely=0.65, anchor=CENTER)

        lab = Label(helproot, image=image_bro)
        lab.place(relx=0.3, rely=0.005, relwidth=0.4)

        helpmenu_info = Label(helproot,
                          text="Имя программы: Eword (Editor word).\nРазработчики: PyBro."
                          "\nЦель программы: Удобство работы с текстом.",
                          fg=font_color_l_w, bg=bg_w, font=font, justify = LEFT)
        helpmenu_info.place(relx=0.5, rely=0.9, anchor=CENTER)
    else:
        helproot['bg'] = bg_b

        # helpmenu_title = Label(helproot, text="EWord", font="Arial, 40", bg="#46211A", fg="blue")
        # helpmenu_title.place(x=110, y=50)

        helpmenu_text = Label(helproot,
                              text="\nЭто универсальный редактор строк "
                                   "\nс интересными текстовыми мини-играми\n "
                                   "такими как: 3х литровая банка,"
                                   "\n Игра в Города, Текстовый квест,\n Кликер.",
                              font=font, bg=bg_b, fg="blue")
        helpmenu_text.place(relx=0.5, rely=0.65, anchor=CENTER)

        lab = Label(helproot, image=image_bro)
        lab.place(relx=0.3, rely=0.005, relwidth=0.4)

        helpmenu_info = Label(helproot,
                              text="Имя программы: Eword.\nРазработчики: PyBro."
                                   "\nЦель программы: Удобство работы с текстом.",
                              fg=font_color_l_b, bg=bg_b, font=font, justify = LEFT)
        helpmenu_info.place(relx=0.5, rely=0.9, anchor=CENTER)

    helproot.mainloop()


def miniroot():
    def counter():

        if miniroot_entry.get() != '':
            letter = miniroot_entry.get()
            mytext = text.get(0.0, END)
            n = mytext.count(letter)
            miniroot_entry.delete(0, END)
            messagebox.showinfo("", "Количество букв { " + str(letter) + " } в тексте: " + str(n))
        else:
            messagebox.showerror("Ошибка", "Вы не указали букву...")
        miniroot.destroy()

    miniroot = Toplevel()
    miniroot.geometry("300x300")
    miniroot.resizable(False, False)
    miniroot.title("Сколько раз встречается")
    miniroot_entry = Entry(miniroot, width=30, bg=ent_w, font=font, relief=FLAT, justify=CENTER)
    if colors == 'w':
        miniroot['bg'] = bg_frm_w


        miniroot_entry.place(relx=0.5, rely=0.25, anchor=CENTER)

        miniroot_button = Button(miniroot, text="Продолжить", width=18, height=2, bg=bg_btn_off_w, fg=font_color_l_w,
                                 activebackground=bg_btn_on_w, font=font, relief=FLAT,  activeforeground=font_color_w,
                                 command = counter)
        miniroot_button.place(relx=0.5, rely=0.6, anchor=CENTER)

    else:
        miniroot['bg'] = bg_frm_b

        miniroot_entry = Entry(miniroot, width=30, bg=ent_b, font=font, relief=FLAT, justify=CENTER)
        miniroot_entry.place(relx=0.5, rely=0.25, anchor=CENTER)

        miniroot_button = Button(miniroot, text="Продолжить", width=18, height=2, bg=bg_btn_off_b, fg=font_color_l_b,
                                 activebackground=bg_btn_on_b, font=font, relief=FLAT,  activeforeground=font_color_b,
                                 command = counter)
        miniroot_button.place(relx=0.5, rely=0.6, anchor=CENTER)
    miniroot.mainloop()


def miniroot_2():
    def rep():
        if miniroot1_entry_2.get() != '':
            if miniroot2_entry_2.get() != '':
                old = miniroot1_entry_2.get()
                new = miniroot2_entry_2.get()
                mytext = text.get(0.0, END)
                mytext = mytext.replace(old, new)
                a = mytext.split('\n')
                del a[-1]
                a = '\n'.join(a)
                text.delete(0.0, END)
                text.insert(0.0, a)

            else:
                messagebox.showerror("Ошибка", "Вы не указали то, на что желаете изменить")
        else:
            messagebox.showerror("Ошибка", "Вы не указали то, что желаете изменить")
        miniroot_2.destroy()
    miniroot_2 = Toplevel()
    miniroot_2.geometry("300x300")
    miniroot_2.resizable(False, False)
    miniroot_2.title("Заменить на:")
    if colors == 'w':
        miniroot_2['bg'] = bg_frm_w

        miniroot1_entry_2 = Entry(miniroot_2, width=30, font=font, bg=ent_w, relief=FLAT, justify=CENTER)
        miniroot1_entry_2.place(relx = 0.5, rely = 0.23, anchor = CENTER)

        miniroot_label_2 = Label(miniroot_2, text="Заменить на:", bg=bg_frm_w, fg=font_color_l_w, font=font)
        miniroot_label_2.place(relx = 0.5, rely = 0.32, anchor = CENTER)

        miniroot2_entry_2 = Entry(miniroot_2, width=30, font=font, bg=ent_w, relief=FLAT, justify=CENTER)
        miniroot2_entry_2.place(relx = 0.5, rely = 0.4, anchor = CENTER)

        miniroot_button_2 = Button(miniroot_2, text="Продолжить", width=18, height=2, bg=bg_btn_off_w, fg=font_color_w,
                                   activebackground=bg_btn_on_w, font=font, relief=FLAT,  activeforeground=font_color_w,
                                   command = rep)
        miniroot_button_2.place(relx = 0.5, rely = 0.7, anchor = CENTER)
    else:
        miniroot_2['bg'] = bg_frm_b

        miniroot1_entry_2 = Entry(miniroot_2, width=30, font=font, bg=ent_b, relief=FLAT, justify=CENTER)
        miniroot1_entry_2.place(relx = 0.5, rely = 0.23, anchor = CENTER)

        miniroot_label_2 = Label(miniroot_2, text="Заменить на:", bg=bg_frm_b, fg=font_color_l_b, font=font)
        miniroot_label_2.place(relx = 0.5, rely = 0.32, anchor = CENTER)

        miniroot2_entry_2 = Entry(miniroot_2, width=30, font=font, bg=ent_b, relief=FLAT, justify=CENTER)
        miniroot2_entry_2.place(relx = 0.5, rely = 0.4, anchor = CENTER)

        miniroot_button_2 = Button(miniroot_2, text="Продолжить", width=18, height=2, bg=bg_btn_off_b, fg=font_color_b,
                                   activebackground=bg_btn_on_b, font=font, relief=FLAT,  activeforeground=font_color_b,
                                   command = rep)
        miniroot_button_2.place(relx = 0.5, rely = 0.7, anchor = CENTER)
    miniroot_2.mainloop()



filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Новый", command=Newfile)
filemenu.add_command(label="Открыть...", command=Loadfile)
filemenu.add_command(label="Сохранить...", command=Savefile)
filemenu.add_command(label="Выход", command=eword_exit)

helpmenu = Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="О программе", command=helproot_function)
helpmenu.add_command(label="Помощь", command=help_message)

gamemenu = Menu(mainmenu, tearoff=0)
gamemenu.add_command(label="Города", command=game_1)
gamemenu.add_command(label="3-х литровая банка", command=game_2)
gamemenu.add_command(label="Виселица", command=game_3)
gamemenu.add_command(label="Придумай рифму за 15 секунд", command=game_4)
gamemenu.add_command(label="Текстовый квест", command=game_5)
gamemenu.add_command(label="Кликер", command=game_6)
gamemenu.add_command(label="Угадай аббревиатуру", command=game_7)

redmenu = Menu(mainmenu, tearoff=0)
redmenu.add_command(label="Транслит на русский", command=lambda x=0:translit(x))
redmenu.add_command(label="Транслит на английский", command=lambda x=1:translit(x))
redmenu.add_command(label="Регистр (Выше)", command = lambda a=1:command_1(a))
redmenu.add_command(label="Регистр (Ниже)", command = lambda a=2:command_1(a))
redmenu.add_command(label="Смена регистра", command = lambda a=3:command_1(a))
redmenu.add_command(label="Кол-во символов", command = symbol)
redmenu.add_command(label="С заглавной", command = lambda a=5:command_1(a))
redmenu.add_command(label="С заглавной (Всё)", command = lambda a=6:command_1(a))
redmenu.add_command(label="Сколько раз встречается:", command=miniroot)
redmenu.add_command(label="Заменить на:", command=miniroot_2)

setmenu = Menu(mainmenu, tearoff=0)
setmenu.add_command(label="Темная тема", command=lambda color='b': topic(color))
setmenu.add_command(label="Светлая тема", command=lambda color='w': topic(color))


mainmenu.add_cascade(label="Файл", menu=filemenu)
mainmenu.add_cascade(label="Игры", menu=gamemenu)
mainmenu.add_cascade(label="Редактор", menu=redmenu)
mainmenu.add_cascade(label="Тема", menu=setmenu)
mainmenu.add_cascade(label="Справка", menu=helpmenu)

# Поле для текста
frm_text = Frame(root, width=800, height=400, bg=bg_frm_w, relief=FLAT)
frm_text.place(x=20, y=20, relwidth=0.64,  relheight=0.65)

# Текст
text = Text(frm_text, width=95, height=29, bg='white', font=font, relief=FLAT)
text.place(x=0, y=0, relwidth=0.988, relheight=0.999)
text.delete(0.0, END)
# Полоса прокрутки
scrollbar = Scrollbar(frm_text, orient="vertical", command=text.yview)
text.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")


# Поле транслит
frm_translator = Frame(root, width=750, height=60, bg=bg_frm_w, relief=FLAT)
frm_translator.place(x=20, y=60, relwidth=0.64, relheight=0.08, rely=0.7, anchor='sw')

# Виджеты
# Кнопка 'Транслит на Анг'
btn_translator_eng = Button(frm_translator, text='Транслит на английский', font=font,
                            width=30, height=1, relief=FLAT, bg=bg_btn_off_w, fg=font_color_w,
                            activebackground=bg_btn_on_w, activeforeground=font_color_w,
                            command=lambda x=1: translit(x))
btn_translator_eng.place(x=-100, y=12, relx=0.2, relheight=0.6, relwidth=0.35)

# Кнопка 'Транслит на Рус'
btn_translator_rus = Button(frm_translator, text='Транслит на русский', font=font,
                            width=30, height=1, relief=FLAT, bg=bg_btn_off_w, fg=font_color_w,
                            activebackground=bg_btn_on_w, activeforeground=font_color_w,
                            command=lambda x=0: translit(x))
btn_translator_rus.place(x=-55, y=12, relx=0.6, relheight=0.6, relwidth=0.35)

# Поле для команд строк
frm_command = Frame(root, width=100, height=100, bg=bg_frm_w, relief=FLAT)
frm_command.place(x=20, y=75, relwidth=0.97, relheight=0.17, rely=0.7)

# Виджеты
btn_command_1 = Button(frm_command, text='Регистр (Выше)', font=font,
                       width=25, height=1, relief=FLAT, bg=bg_btn_off_w, fg=font_color_w,
                       activebackground=bg_btn_on_w, activeforeground=font_color_w, command=lambda a = 1: command_1(a))
btn_command_2 = Button(frm_command, text='Регистр (Ниже)', font=font,
                       width=25, height=1, relief=FLAT, bg=bg_btn_off_w, fg=font_color_w,
                       activebackground=bg_btn_on_w, activeforeground=font_color_w, command=lambda a = 2: command_1(a))
btn_command_3 = Button(frm_command, text='Смена регистра', font=font,
                       width=25, height=1, relief=FLAT, bg=bg_btn_off_w, fg=font_color_w,
                       activebackground=bg_btn_on_w, activeforeground=font_color_w, command=lambda a = 3: command_1(a))
btn_command_4 = Button(frm_command, text='Количество символов', font=font,
                       width=25, height=1, relief=FLAT, bg=bg_btn_off_w, fg=font_color_w,
                       activebackground=bg_btn_on_w, activeforeground=font_color_w, command=symbol)
btn_command_5 = Button(frm_command, text='С заглавной', font=font,
                       width=25, height=1, relief=FLAT, bg=bg_btn_off_w, fg=font_color_w,
                       activebackground=bg_btn_on_w, activeforeground=font_color_w, command=lambda a = 5: command_1(a))
btn_command_6 = Button(frm_command, text='С заглавной (Всё)', font=font,
                       width=25, height=1, relief=FLAT, bg=bg_btn_off_w, fg=font_color_w,
                       activebackground=bg_btn_on_w, activeforeground=font_color_w, command=lambda a = 6: command_1(a))
ent_command_7 = Entry(frm_command, font=font, width=10, relief=FLAT, bg=ent_w, justify=CENTER)
btn_command_8 = Button(frm_command, text='Сколько раз встречается', font=font,
                       width=25, height=1, relief=FLAT, bg=bg_btn_off_w, fg=font_color_w,
                       activebackground=bg_btn_on_w, activeforeground=font_color_w, command=command_2)
ent_command_9 = Entry(frm_command, font=font, width=7, relief=FLAT, bg=ent_w, justify=CENTER)
btn_command_10 = Button(frm_command, text='Заменить на:', font=font,
                        width=15, height=1, relief=FLAT, bg=bg_btn_off_w, fg=font_color_w,
                        activebackground=bg_btn_on_w, activeforeground=font_color_w, command=command_3)
ent_command_11 = Entry(frm_command, font=font, width=7, relief=FLAT, bg=ent_w, justify=CENTER)

btn_command_1.place(x=20, y=10, relwidth=0.2, relheight=0.3, rely=0.05)
btn_command_2.place(x=20, y=40, relwidth=0.2, relheight=0.3, rely=0.25)
btn_command_3.place(x=-70, y=10, relwidth=0.2, relx=0.3, relheight=0.3, rely=0.05)
btn_command_4.place(x=-70, y=40, relwidth=0.2, relx=0.3, relheight=0.3, rely=0.25)
btn_command_5.place(x=-160, y=10, relwidth=0.2, relx=0.6, relheight=0.3, rely=0.05)
btn_command_6.place(x=-160, y=40, relwidth=0.2, relx=0.6, relheight=0.3, rely=0.25)
ent_command_7.place(x=-45, y=40, relwidth=0.05, relx=0.79, relheight=0.3,  anchor='se', rely=0.11)
btn_command_8.place(x=20, y=39, relwidth=0.2, relx=0.96, relheight=0.3, anchor='se', rely=0.11)
ent_command_9.place(x=-45, y=76, relwidth=0.05,  relx=0.79, relheight=0.3, rely=0.27, anchor='se')
btn_command_10.place(x=-15, y=76, relwidth=0.13,  relx=0.92, relheight=0.3, anchor='se', rely=0.27)
ent_command_11.place(x=15, y=76, relwidth=0.05, relx=0.965, relheight=0.3, anchor='se', rely=0.27)

# Поле для игр
frm_game = Frame(root, width=380, height=545, bg=bg_frm_w, relief=FLAT)
frm_game.place(x=5, y=20, relheight=0.751, relx=0.669, relwidth=0.311)

# Виджеты
lbl_game = Label(frm_game, text='Текстовые игры', font=font_g , bg=bg_frm_w, fg=font_color_l_w)
lbl_game.place(x=23, y=-40, relwidth=0.8, relheight=0.3, relx=0.05)

btn_game_1 = Button(frm_game, text="Города", font=font_g,
                    width=35, height=2, relief=FLAT, bg=bg_btn_off_w, fg=font_color_w,
                    activebackground=bg_btn_on_w, activeforeground=font_color_w, command=game_1)

btn_game_2 = Button(frm_game, text="3-х литровая банка", font=font_g,
                    width=35, height=2, relief=FLAT, bg=bg_btn_off_w, fg=font_color_w,
                    activebackground=bg_btn_on_w, activeforeground=font_color_w, command=game_2)

btn_game_3 = Button(frm_game, text="Виселица", font=font_g,
                    width=35, height=2, relief=FLAT, bg=bg_btn_off_w, fg=font_color_w,
                    activebackground=bg_btn_on_w, activeforeground=font_color_w, command=game_3)

btn_game_4 = Button(frm_game, text="Придумай рифму за 15 секунд", font=font_g,
                    width=35, height=2, relief=FLAT, bg=bg_btn_off_w, fg=font_color_w,
                    activebackground=bg_btn_on_w, activeforeground=font_color_w, command=game_4)

btn_game_5 = Button(frm_game, text="Текстовый квест", font=font_g,
                    width=35, height=2, relief=FLAT, bg=bg_btn_off_w, fg=font_color_w,
                    activebackground=bg_btn_on_w, activeforeground=font_color_w, command=game_5)

btn_game_6 = Button(frm_game, text="Кликер", font=font_g,
                    width=35, height=2, relief=FLAT, bg=bg_btn_off_w, fg=font_color_w,
                    activebackground=bg_btn_on_w, activeforeground=font_color_w, command=game_6)

btn_game_7 = Button(frm_game, text="Угадай аббревиатуру", font=font_g,
                    width=35, height=2, relief=FLAT, bg=bg_btn_off_w, fg=font_color_w,
                    activebackground=bg_btn_on_w, activeforeground=font_color_w, command=game_7)
i = PhotoImage(file="fon.png")  #ФОН
image_bro = PhotoImage(file="pybro.png")  #ФОН
im = PhotoImage(file='tenoru.png')

btn_game_1.place(x=25, y=-35, relwidth=0.887, relheight=0.09, rely=0.2)
btn_game_2.place(x=25, y=-22, relwidth=0.887, relheight=0.09, rely=0.3)
btn_game_3.place(x=25, y=-9, relwidth=0.887, relheight=0.09, rely=0.4)
btn_game_4.place(x=25, y=4, relwidth=0.887, relheight=0.09, rely=0.5)
btn_game_5.place(x=25, y=17, relwidth=0.887, relheight=0.09, rely=0.6)
btn_game_6.place(x=25, y=30, relwidth=0.887, relheight=0.09, rely=0.7)
btn_game_7.place(x=25, y=43, relwidth=0.887, relheight=0.09, rely=0.8)

root.mainloop()
