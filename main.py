plank = list(range(1, 10))

wins_line = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)] # прописываем спсок вариаций для победы
def draw_plank ():
    print("--------------") #ДЕЛАЕМ ВЕРХНЮЮ ГРАНИЦУ
    for i in range(3):
        print('|', plank[0 + i * 3], '|', plank[1 + i * 3], '|', plank[2 + i *3], '|') #ФОРМИРУЕМ БОКОВЫЕ ГРАНИЦЫ
    print("--------------")

def take_input (player_symbol): #ПРОПИСЫВАЕМ АЛГОРИТМ ДЛЯ ДЕЙСТВИИЙ ИГРОКА 
    while True:
        value = input('where put :' + player_symbol + '?')
        if not (value in '123456789'):
            print('error input.try again')
            continue
        value = int(value)
        if str(plank[value - 1]) in 'XO':
            print('this cell is already occupied')
            continue
        plank[value - 1] = player_symbol
        break

def check_win():
    for i in wins_line:
        if (plank[i[0] - 1]) == (plank[i[1] - 1]) == (plank[i[2] - 1]):
            return plank[i[1] - 1] # ВОЗВРАЩАЕМ ЗНАК ПОБЕДИТЕЛЯ
    else:
        return False


def main():
    step = 0
    while True:
        draw_plank()
        if step % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        if step > 3:
            winner = check_win()
            if winner:
                draw_plank()
                print(winner,'U WON')
                break



        step+= -1
        if step > 8:
            draw_plank()
            print('STANDOFF!!!')
            break

main()