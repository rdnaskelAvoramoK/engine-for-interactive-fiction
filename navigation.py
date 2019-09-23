from PIL import Image

#указываем расположение файла карты в файловой системе
map_image = Image.open('map.jpg')

coordinates = {'зеленая': [1, 11], 'желтая': [2, 12], 'красная': [3, 13], 'коворкинг': [4, 21], 'ресепшн': [5, 22], 'коричневая': [6, 23], 'макдональдс': [7, 31], 'коридор': [8, 32], 'уборная': [9, 33]}

actions = {'Вперед':'W', 'Назад':'S', 'Влево':'A', 'Вправо':'D', 'Телепорт': 'T', 'Лифт': 'L', 'Показать карту': 'M', 'Выход': 'E'}

#инициализируем обработчик исключений
try:
    direction_request = int(input('\nВведи цифру локации, откуда хочешь начать: \n\n' + 
        "\n".join([" \n".join(str(index)) + " - " + loc for index, loc in enumerate(coordinates.keys(), 1)]) + 
        "\n ------------------ \n" + "\n"))
    while direction_request > len(list(coordinates.keys())) or direction_request < 0:
            direction_request = int(input(("\nВведено неправильное число. Попробуй еще раз.\n ------------------ \n\n")))
except ValueError:
    while True:
        direction_request = input("\nНеверные данные. Давай еще разок. \n ------------------ \n\n")
        if direction_request.isdigit():
            if int(direction_request) > len(list(coordinates.keys())) or int(direction_request) < 0:
                continue
            else:
                direction_request = int(direction_request)
                break
        else:
            continue
            
#сравниваем введенное пользователем значение с координатой в словаре coordinates и присваиваем координату карты
direction_request = str([i[1] for i in list(coordinates.values()) if i[0] == direction_request][0])

while True:
    available_actions = {}
    print("\nТы находишься в локации: {}".format([key for key, value in coordinates.items() if str(value[1]) == direction_request][0].title()) + "\n")
    if int(direction_request[1]) < 3 and int(direction_request) != 31:
        available_actions[list(actions.keys())[3]] = list(actions.values())[3].lower()
    if int(direction_request[1]) > 1 and int(direction_request) != 32:
        available_actions[list(actions.keys())[2]] = list(actions.values())[2].lower()
    if int(direction_request[0]) < 3 and int(direction_request) != 21:
        available_actions[list(actions.keys())[1]] = list(actions.values())[1].lower()
    if int(direction_request[0]) > 1 and int(direction_request) != 31:
        available_actions[list(actions.keys())[0]] = list(actions.values())[0].lower()
    if int(direction_request) == 31 or int(direction_request) == 32:
        available_actions[list(actions.keys())[5]] = list(actions.values())[5].lower()
    available_actions[list(actions.keys())[4]] = list(actions.values())[4].lower()
    available_actions[list(actions.keys())[6]] = list(actions.values())[6].lower()
    available_actions[list(actions.keys())[7]] = list(actions.values())[7].lower()


    move_request = input("\nДоступны следующие действия: \n\n" + "\n".join([v.title() + " - " + k for k, v in available_actions.items()]) + " \n ------------------ \n\n")
    
    while (move_request.lower() == list(actions.values())[1].lower() and int(direction_request) == 21) or (move_request.lower() == list(actions.values())[0].lower() and int(direction_request) == 31):
        move_request = input("\nТам стена, движение заблокировано. Выбери направление из доступных: \n------------------ \n\n")

    while (move_request.lower() not in available_actions.values()):
        move_request = input("\nНедопустимое действие. Повтори запрос: \n ------------------ \n\n")
        
    if move_request.lower() == list(actions.values())[0].lower():
        direction_request = str(int(direction_request) - 10)
    elif move_request.lower() == list(actions.values())[1].lower():
        direction_request = str(int(direction_request) + 10)
    elif move_request.lower() == list(actions.values())[2].lower():
        direction_request = str(int(direction_request) - 1)
    elif move_request.lower() == list(actions.values())[3].lower():
        direction_request = str(int(direction_request) + 1)
    elif move_request.lower() == list(actions.values())[4].lower():
        direction_request = int(input('\nТы открыл Телепорт! Введи цифру чтобы перейти в локацию: \n\n' + "\n".join([" \n".join(str(index)) + " - " + loc for index, loc in enumerate(coordinates.keys(), 1)]) + "\n\n"))
        direction_request = str([i[1] for i in list(coordinates.values()) if i[0] == direction_request][0])
    elif move_request.lower() == list(actions.values())[5].lower():
        print("\nТы зашел в лифт")
        if int(direction_request) == 31:
            question = input("\nПодняться на 2 этаж в локацию {}? Введите Y или N".format(list(coordinates.keys())[7].title()) + "\n ------------------ \n")
            if question.lower() == "y":
                direction_request = str(int(direction_request) + 1)
                continue
            else:
                continue
        elif int(direction_request) == 32:
            question = input("\nСпуститься на 1 этаж в локацию {}? Введите Y или N".format(list(coordinates.keys())[6].title()) + "\n ------------------ \n")
            if question.lower() == "y":
                direction_request = str(int(direction_request) - 1)
                continue
            else:
                continue
    elif move_request.lower() == list(actions.values())[6].lower():
        map_image.show()
    elif move_request.lower() == list(actions.values())[7].lower():
        break
    else:
        move_request = input("\nНе понимаю что делать. Введи правильную команду. ------------------ \n\n")