from tkinter import *
import random

# создание окна
igra = Tk()
igra.title("'Камень-ножницы-бумага'")
igra.geometry('625x750')
igra.configure(bg="#32292F")
igra.resizable(False,False)

# переменная кол-ва ходов
movesleft = 5

# функция для новой игры
def new_game():
    global player_wins
    global computer_wins
    global score
    global movesleft

    player_wins = 0
    computer_wins = 0
    score = 0
    movesleft = 5

    player_wins_label.config(text=f"Победы игрока: {player_wins}")
    computer_wins_label.config(text=f"Победы компьютера: {computer_wins}")
    score_label.config(text=f"Очки: {score}")
    moves_label.config(text=f"Вы еще можете сделать следующее кол-во ходов: {movesleft}")
    winnername_label.config(text=" ")
    result.config(text="Нажмите кнопку 'Играть',\n чтобы начать игру.")
    update_images(0, 0)

# создание текста с правилами игры
text = Label(igra, text="Выберите функцию из списка:\n Камень бьет ножницы,\n ножницы бьют бумагу,\n бумага бьет камень.", font=("Press Start 2P", 12), bg="#32292F", fg="#99E1F9")
text.pack(side=TOP, pady=20)

# создание метки для результата игры
result = Label(igra, text="Нажмите кнопку 'Играть',\n чтобы начать игру.", font=("Press Start 2P", 9), bg="#32292F", fg="#99E1F9")
result.pack(side=TOP, pady=20)

# игровой процесс
def play(user_choice):
    global player_wins
    global computer_wins
    global score
    global movesleft

    if movesleft > 0:
        update_images(0, 0)
        if user_choice == 0:
            result.config(text="Выберите функцию и нажмите кнопку 'Играть'.")
        else:
            computer_choice = random.randint(1, 3)

            update_images(user_choice, computer_choice)

            if user_choice == computer_choice:
                result.config(text="Ничья!")
            elif (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 3) or (user_choice == 3 and computer_choice == 1):
                result.config(text="Поздравляем, вы победили!")
                player_wins += 1
                score += 1
            else:
                result.config(text="Вы проиграли. Попробуйте еще раз.")
                computer_wins += 1
                if score > 0:
                    score -= 1

            player_wins_label.config(text=f"Победы игрока: {player_wins}")
            computer_wins_label.config(text=f"Победы компьютера: {computer_wins}")
            score_label.config(text=f"Очки: {score}")
            movesleft -= 1
            moves_label.config(text=f"Вы еще можете сделать следующее кол-во ходов: {movesleft}")

            if movesleft == 0:
                if player_wins > computer_wins:
                    winnername_label.config(text="Вы победили!")
                elif player_wins < computer_wins:
                    winnername_label.config(text="Вы проиграли.")
                else:
                    winnername_label.config(text="Ничья.")
    else:
        result.config(text="Ходы закончились. Нажмите кнопку 'Новая игра'.")


# выбираемые варианты
rad1 = Radiobutton(igra, text='Камень', value=1, font=("Press Start 2P", 9), bg="#32292F", fg="#99E1F9")
rad2 = Radiobutton(igra, text='Ножницы', value=2, font=("Press Start 2P", 9), bg="#32292F", fg="#99E1F9")
rad3 = Radiobutton(igra, text='Бумага', value=3, font=("Press Start 2P", 9), bg="#32292F", fg="#99E1F9")
btn = Button(igra, text="Играть", command=lambda: play(var.get()), font=("Press Start 2P", 12), bg="#70ABAF", fg="#F0F7F4", relief=RAISED)
new_game_btn = Button(igra, text="Новая игра", command=new_game, font=("Press Start 2P", 12), bg="#70ABAF", fg="#F0F7F4", relief=RAISED)

rad1.place(relx=0.2, rely=0.7, anchor='center')
rad2.place(relx=0.5, rely=0.7, anchor='center')
rad3.place(relx=0.8, rely=0.7, anchor='center')
btn.place(relx=0.5, rely=0.9, anchor='center')
new_game_btn.place(relx=0.5, rely=0.95, anchor='center')

# создание переменной для выбора пользователя
var = IntVar()

# привязка переменной к кнопкам
rad1.config(variable=var)
rad2.config(variable=var)
rad3.config(variable=var)

# создание изображений
player_empty_img = PhotoImage(file="./empty.png")
player_rock_img = PhotoImage(file="./rock.png")
player_scissors_img = PhotoImage(file="./scissors.png")
player_paper_img = PhotoImage(file="./paper.png")

computer_empty_img = PhotoImage(file="./empty.png")
computer_rock_img = PhotoImage(file="./rock.png")
computer_scissors_img = PhotoImage(file="./scissors.png")
computer_paper_img = PhotoImage(file="./paper.png")

# создание меток для изображений
player_label = Label(igra, image=player_rock_img, text="Игрок", compound="top", font=("Press Start 2P", 9), bg="#32292F", fg="#99E1F9")
computer_label = Label(igra, image=computer_rock_img, text="Компьютер", compound="top", font=("Press Start 2P", 9), bg="#32292F", fg="#99E1F9")

# создание меток игровой механики
moves_label = Label(igra, text=("Вы еще можете сделать \n следующее кол-во ходов: ", movesleft, "."), compound="top", font=("Press Start 2P", 9), bg="#32292F", fg="#99E1F9")
winnername_label = Label(igra, text=" ", compound="top", font=("Press Start 2P", 9), bg="#32292F", fg="#99E1F9")

# размещение меток на экране
player_label.place(relx=0.3, rely=0.5, anchor='center')
computer_label.place(relx=0.7, rely=0.5, anchor='center')
moves_label.place(relx=0.5, rely=0.35, anchor='center')
winnername_label.place(relx=0.5, rely=0.85, anchor='center')

# создание системы подсчета побед и очков
player_wins = 0
computer_wins = 0
score = 0

player_wins_label = Label(igra, text=f"Победы игрока: {player_wins}", font=("Press Start 2P", 6), bg="#32292F", fg="#99E1F9")
player_wins_label.place(relx=0.3, rely=0.58, anchor='center')

computer_wins_label = Label(igra, text=f"Победы компьютера: {computer_wins}", font=("Press Start 2P", 6), bg="#32292F", fg="#99E1F9")
computer_wins_label.place(relx=0.7, rely=0.58, anchor='center')

score_label = Label(igra, text=f"Очки: {score}", font=("Press Start 2P", 9), bg="#32292F", fg="#99E1F9")
score_label.place(relx=0.5, rely=0.80, anchor='center')

# функция для обновления изображений
def update_images(user_choice, computer_choice):
    if user_choice == 0:
        player_label.config(image=player_empty_img)
    elif user_choice == 1:
        player_label.config(image=player_rock_img)
    elif user_choice == 2:
        player_label.config(image=player_scissors_img)
    elif user_choice == 3:
        player_label.config(image=player_paper_img)

    if computer_choice == 0:
        computer_label.config(image=computer_empty_img)
    elif computer_choice == 1:
        computer_label.config(image=computer_rock_img)
    elif computer_choice == 2:
        computer_label.config(image=computer_scissors_img)
    elif computer_choice == 3:
        computer_label.config(image=computer_paper_img)

# вызов функции update_images для установки изображений по умолчанию
update_images(0, 0)

# функция для новой игры
def new_game():
    global player_wins
    global computer_wins
    global score
    global movesleft

    player_wins = 0
    computer_wins = 0
    score = 0
    movesleft = 5

    player_wins_label.config(text=f"Победы игрока: {player_wins}")
    computer_wins_label.config(text=f"Победы компьютера: {computer_wins}")
    score_label.config(text=f"Очки: {score}")
    moves_label.config(text=f"Вы еще можете сделать \n следующее кол-во ходов: {movesleft}")
    winnername_label.config(text=" ")
    result.config(text="Нажмите кнопку 'Играть',\n чтобы начать игру.")
    update_images(0, 0)

# запуск окна
igra.mainloop()