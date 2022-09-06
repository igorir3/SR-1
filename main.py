import json
import os
import time
from pick import pick
from rich import print
import rich
import random
import math

Day = 1
Month = 9 
Year = 2029

def start():
    os.system('cls||clear')
    title_start =   ("         Меню        ")
    options_start = ['Создание персонажей', 'Создание професий', 'Создание xронических заболеваний', 'Выход']
    input1, index1 = pick(options_start,title=title_start, indicator='=>')
    if input1 == 'Создание персонажей':
        create_character()
    elif input1 == 'Создание професий':
        add_prof()
    elif input1 == 'Выход':
        raise SystemExit
    elif input1 == 'Создание xронических заболеваний':
        add_chronical()

def loading():
    os.system('cls||clear')
    percent1 = 0
    while percent1 < 100:
        percent1 = percent1 + random.randint(1, 20)
        if percent1 >= 100:
            percent1 = 100
            print(f"Starting...    {percent1}%")
        else:
            print(f"Starting...    {percent1}%", end="\r")
        time.sleep(0.3)
        
    print(f"Loading", end="\r")
    time.sleep(0.3)
    print(f"Loading.", end="\r")
    time.sleep(0.3)
    print(f"Loading..", end="\r")
    time.sleep(0.3)
    print(f"Loading...")
    time.sleep(0.3)

    percent1 = 0
    while percent1 < 100:
        percent1 = percent1 + random.randint(1, 20)
        if percent1 >= 100:
            percent1 = 100
            print(f"Initialisation...    {percent1}%")
        else:
            print(f"Initialisation...    {percent1}%", end="\r")
        time.sleep(0.3)

    print(f"Loading Data", end="\r")
    time.sleep(0.3)
    print(f"Loading Data.", end="\r")
    time.sleep(0.3)
    print(f"Loading Data..", end="\r")
    time.sleep(0.3)
    print(f"Loading Data...")
    time.sleep(0.6)
    print("[bold red] FILE NOT FOUND \n File C:\\User\\Data\\SR-1 Data\\Alpha Protocol.db    KEY Not Exist \n ERROR 0x80070002 [/bold red]", end="\r")
    time.sleep(0.3)
    print("[bold red]DATA ERROR[/bold red]")
    time.sleep(0.3)
    print("Repeat request")
    time.sleep(0.2)
    print(f"Loading Data", end="\r")
    time.sleep(0.3)
    print(f"Loading Data.")
    time.sleep(0.4)
    print("[bold red]ERROR 0x80070002[/bold red]")
    time.sleep(0.3)
    print("[bold red] Data Corrupted [/bold red]")
    time.sleep(0.2)
    print("Launching the emergency protocol", end="\r")
    time.sleep(0.3)
    t = 0
    while t <= 2:
        print("Launching the emergency protocol.", end="\r")
        time.sleep(0.3)
        print("Launching the emergency protocol..", end="\r")
        time.sleep(0.3)
        print("Launching the emergency protocol...", end="\r")
        time.sleep(0.3)
        t = t + 1
    print("Launching the emergency protocol.", end="\r")
    time.sleep(0.3)
    print("Launching the emergency protocol..", end="\r")
    time.sleep(0.3)
    print("Launching the emergency protocol...")
    time.sleep(0.3)
    print("Searching recoverable data", end="\r")
    time.sleep(0.3)
    while t <= 3:
        print("Searching recoverable data.", end="\r")
        time.sleep(0.3)
        print("Searching recoverable data..", end="\r")
        time.sleep(0.3)
        print("Searching recoverable data...", end="\r")
        time.sleep(0.3)
        t = t + 1
    print("Searching recoverable data.", end="\r")
    time.sleep(0.3)
    print("Searching recoverable data..", end="\r")
    time.sleep(0.3)
    print("Searching recoverable data...")
    time.sleep(0.3)
    print("[bold green3]Process successful[/bold green3]")
    print("Summary recoverable data", end="\r")
    time.sleep(0.3)
    while t <= 5:
        print("Summary recoverable data.", end="\r")
        time.sleep(0.3)
        print("Summary recoverable data..", end="\r")
        time.sleep(0.3)
        print("Summary recoverable data...", end="\r")
        time.sleep(0.3)
        t = t + 1
    print(f"Summary recoverable data... {random.randint(60, 90)}%")
    time.sleep(0.3)
    print("Summary recoverable data.", end="\r")
    time.sleep(0.3)
    print("Summary recoverable data..", end="\r")
    time.sleep(0.3)
    print("Summary recoverable data...")
    time.sleep(0.3)
    percent1 = 0
    while percent1 < 100:
        percent1 = percent1 + random.randint(1, 20)
        if percent1 >= 100:
            percent1 = 100
            print(f"Close protocol starting...   {percent1}%")
        else:
            print(f"Close protocol starting...   {percent1}%", end="\r")
        time.sleep(3)
    start()

def create_character():
    os.system('cls||clear')
    print(' ')
    print                 ("   ---Основные данные---")
    print(' ')
    NNN        = str(input("Фио          : "))
    Sex        = str(input("Пол (М/Ж)    : "))
    DateOfBorn = str(input("Дата Рождения: "))
    DateOfBorn = DateOfBorn.split(sep='.')
    DateOfBorn = list(map(int, DateOfBorn))
    DayOfBorn = DateOfBorn[0]
    MonthOfBorn = DateOfBorn[1]
    YearOfBorn = DateOfBorn[2]
    age = Year - YearOfBorn
    if Month > MonthOfBorn:
        age = age + 1
    elif Month == MonthOfBorn and Day > DayOfBorn:
        age = age + 1
    os.system('cls||clear')
    print(' ')
    print("---Основные Характеристики---")
    print(' ')
    print(" 1. Сила \n 2. Интеллект \n 3. Ловкость \n 4. Воля \n 5. Телосложение \n 6. Харизма \n \n Писать все значения через пробел в том порядке, что записан выше!")
    print(' ')
    while True:
        input2 = str(input(">>> "))
        Str_characteristic = input2.split()
        if len(Str_characteristic) != 6:
              print(f"[bold red]Ты должен написать 6 цифр через пробелы, а ты написал {len(Str_characteristic)}[/bold red]")
              print(" ")
        else:
            characteristic = list(map(int, Str_characteristic))
            sum_characteristic = characteristic[0] + characteristic[1] + characteristic[2] + characteristic[3] + characteristic[4] + characteristic[5]
            if  characteristic[0] > 5 or characteristic[1] > 5 or characteristic[2] > 5 or characteristic[3] > 5 or characteristic[4] > 5 or characteristic[5] > 5:
                print("[bold red]Основные характеристики не должны превышать 5 очков[/bold red]")
                print(" ")
            elif  characteristic[0] < 1 or characteristic[1] < 1 or characteristic[2] < 1 or characteristic[3] < 1 or characteristic[4] < 1 or characteristic[5] < 1:
                print("[bold red]Основные характеристики должны быть более 0[/bold red]")
                print(" ")
            elif sum_characteristic != 14 :
                print(f"[bold red]Сумма статов должна быть равна 14! А у вас {sum_characteristic}[/bold red]")
                print(" ")
            else:
                os.system('cls||clear')
                break
    print(' ')
    print("           ---Второстепенные Характеристики---")
    print(' ')
    print("1. Атлетика                    11. Запугивание         ")
    print("2. Бдительность                12. Обман               ")
    print("3. Ближний бой К-Р             13. Лидерство           ")
    print("4. Ближний бой У-Д             14. Природа             ")
    print("5. Внимание                    15. Механика/электроника")
    print("6. Вождение/пилотирование      16. Религия             ")
    print("7. Выживание                   17. Скрытность          ")
    print("8. Дальний бой лёгкое оружие   18. Убеждение/торг      ")
    print("9. Дальний бой среднее оружие  19. Ловкость рук        ")
    print("10. Дальний бой тяжёлое оружие 20. Химия               ")
    print(' ')
    print('Выберете [bold green3]3[/bold green3] приоритетных характеристики. Введите их номера')
    while True:
        input3 = str(input(">>> "))
        Str_Star_characteristics = input3.split()
        if len(Str_Star_characteristics) != 3:
              print(f"[bold red]Ты должен написать 3 цифры через пробелы, а ты написал {len(Str_Star_characteristics)}[/bold red]")
              print(" ")
        elif int(Str_Star_characteristics[0]) > 20 or int(Str_Star_characteristics[0]) < 1 or int(Str_Star_characteristics[1]) > 20 or int(Str_Star_characteristics[1]) < 1 or int(Str_Star_characteristics[2]) > 20 or int(Str_Star_characteristics[2]) < 1:
            print("[bold red]Номер характеристики смотри по списку![/bold red]")
        else:
            break
    Star_characteristics = list(map(int, Str_Star_characteristics))
    Star_characteristics[0] = Star_characteristics[0] - 1
    Star_characteristics[1] = Star_characteristics[1] - 1
    Star_characteristics[2] = Star_characteristics[2] - 1
    Second_characteristics = []
    Settings_characteristics = [0, 3, 2, 0, 3, 2, 1, 2, 2, 0, 3, 5, 5, 3, 1, 3, 2, 5, 2, 1]
    Fst_Second_characteristics = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Second_characteristics.append(Fst_Second_characteristics)
    Second_characteristics.append(Settings_characteristics)
    Second_characteristics.append(Star_characteristics)
    os.system('cls||clear')
    print(' ')
    print("           ---Второстепенные Характеристики---")
    print(' ')
    print("1. Атлетика                    11. Запугивание         ")
    print("2. Бдительность                12. Обман               ")
    print("3. Ближний бой К-Р             13. Лидерство           ")
    print("4. Ближний бой У-Д             14. Природа             ")
    print("5. Внимание                    15. Механика/электроника")
    print("6. Вождение/пилотирование      16. Религия             ")
    print("7. Выживание                   17. Скрытность          ")
    print("8. Дальний бой лёгкое оружие   18. Убеждение/торг      ")
    print("9. Дальний бой среднее оружие  19. Ловкость рук        ")
    print("10. Дальний бой тяжёлое оружие 20. Химия               ")
    print(' ')
    print("Выберите характеристику которую хотите изменить и число на которое меняете, через пробел.")
    input4 = 'FUCK'
    while input4 != 'save':
        input4 = str(input(">>> "))
        if input4 != 'save':
            Str_input4 = input4.split()
            if len(Str_input4) == 2:
                input4 = list(map(int, Str_input4))
                input4[0] = input4[0] - 1
                if input4[1] > 0:
                    if input4[1] <= 10:
                        if Second_characteristics[2][0] == input4[0] or Second_characteristics[2][1] == input4[0] or Second_characteristics[2][2] == input4[0]:
                            Backup_Second_characteristics = Second_characteristics[0][input4[0]]
                            Second_characteristics[0][input4[0]] = input4[1]
                            Sum_Second_characteristics = sum(Second_characteristics[0])
                            if Sum_Second_characteristics > 20 :
                                print("[bold red]Вы используете слишком много очков характеристик![/bold red]")
                                print(f"[bold red]Максимум 20, а у вас {Sum_Second_characteristics}[/bold red]")
                                print(" ")
                                Second_characteristics[0][input4[0]] = Backup_Second_characteristics
                            elif Sum_Second_characteristics < 20 :
                                Points_Sum_Second_characteristics = 20 - Sum_Second_characteristics
                                print("[bold green3]Готово![/bold green3]")
                                print(f"У вас осталось [bold green3]{Points_Sum_Second_characteristics}[/bold green3] очков характеристик")
                                print(" ")
                            else:
                                os.system('cls||clear')
                                break
                        elif characteristic[Second_characteristics[1][input4[0]]] * 2 >= input4[1]:
                            Backup_Second_characteristics = Second_characteristics[0][input4[0]]
                            Second_characteristics[0][input4[0]] = input4[1]
                            Sum_Second_characteristics = sum(Second_characteristics[0])
                            if Sum_Second_characteristics > 20 :
                                print("[bold red]Вы используете слишком много очков характеристик![/bold red]")
                                print(f"[bold red]Максимум 20, а у вас {Sum_Second_characteristics}[/bold red]")
                                print(" ")
                                Second_characteristics[0][input4[0]] = Backup_Second_characteristics
                            elif Sum_Second_characteristics < 20 :
                                Points_Sum_Second_characteristics = 20 - Sum_Second_characteristics
                                print("[bold green3]Готово![/bold green3]")
                                print(f"У вас осталось [bold green3]{Points_Sum_Second_characteristics}[/bold green3] очков характеристик")
                                print(" ")
                            else:
                                os.system('cls||clear')
                                break
                        else:
                            print(f"[bold red]Вы не можете ввести в Доп.Хар. №{input4[0]+1} число {input4[1]} т. к. сюда можно ввести максимум {characteristic[Second_characteristics[1][input4[0]]] * 2}[/bold red]")
                            print(" ")
                    else:
                        print("[bold red]Число очков должно быть меньше или равно 10[/bold red]")
                        print(" ")
                else:
                    print("[bold red]Число очков должно быть более 0[/bold red]")
                    print(" ")
            else:
                print("[bold red]Надо ввести 2 числа!!![/bold red]")
                print(" ")

    os.system('cls||clear')
    
    Len_Prof = 0
    Len_Chronical = 0
    if age >= 15 and age <= 25:
        Len_Prof = 1
        Len_Chronical = 0
    elif age >= 26 and age <= 35:
        Len_Prof = 2
        Len_Chronical = 1
    elif age > 36:
        Len_Prof = 3
        Len_Chronical = 2
    else:
        Len_Prof = 0
        Len_Chronical = 0
    input_prof = []
    if Len_Prof > 0:    
        list_of_prof = os.listdir("profs\\")
        title_prof =   (f"  Вам доступно {Len_Prof}, \n  выберите профессию. Для выделения профессии используйте кнопку Пробел.")
        options_prof = os.listdir("profs\\")
        
        Prof = []

        if Len_Prof > 1:
            prof_added_characteristics = [0, 0, 0, 0, 0, 0]   
            prof_added_Second_characteristics = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            while True:
                list_input_prof = pick(options_prof,title=title_prof, indicator='=>', multiselect=True)
                if len(list_input_prof) == Len_Prof:
                    break
                else:
                    title_prof = f"Вы можете выбрать только {Len_Prof}"
            for i in range(len(list_input_prof)):
                input_prof.append(list_input_prof[i][0])
            for a in range(len(input_prof)):
                with open("profs\\" + input_prof[a], "r") as read_file:
                    prof_dict = json.load(read_file)
                Prof.append(prof_dict.get("Name"))
                prof_main_added_characteristics = prof_dict.get("added_characteristics")
                pre_prof_added_characteristics = prof_main_added_characteristics[0]
                pre_prof_added_Second_characteristics = prof_main_added_characteristics[1] 
                prof_added_characteristics = list(map(sum, zip(pre_prof_added_characteristics, prof_added_characteristics)))
                prof_added_Second_characteristics = list(map(sum, zip(pre_prof_added_Second_characteristics, prof_added_Second_characteristics)))
        else:
            while True:
                list_input_prof = pick(options_prof,title=title_prof, indicator='=>', multiselect=True)
                if len(list_input_prof) == Len_Prof:
                    break
                else:
                    title_prof = f"Вы можете выбрать только {Len_Prof}"
            with open("profs\\" + list_input_prof[0][0], "r") as read_file:
                prof_dict = json.load(read_file)
            Prof.append(prof_dict.get("Name"))
            prof_main_added_characteristics = prof_dict.get("added_characteristics")
            prof_added_characteristics = prof_main_added_characteristics[0]
            prof_added_Second_characteristics = prof_main_added_characteristics[1]

    
    chron = []

    if Len_Chronical > 0:    
        list_of_chron = os.listdir("chronical\\")
        title_chron =   (f"  Вам доступно {Len_Chronical}, \n  выберите хроническое заболевание(я). Для выделения профессии используйте кнопку Пробел.")
        options_chron = os.listdir("chronical\\")
        if Len_Chronical > 1:
            chron_added_characteristics = [0, 0, 0, 0, 0, 0]   
            chron_added_Second_characteristics = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            chron_added_main_characteristics = [0, 0, 0, 0, 0]
            while True:
                list_input_chron = pick(options_chron,title=title_chron, indicator='=>', multiselect=True)
                if len(list_input_chron) == Len_Chronical:
                    break
                else:
                    title_chron = f"Вы можете выбрать только {Len_Chronical}"
            for i in range(len(list_input_chron)):
                input_chron.append(list_input_chron[i][0])
            for a in range(len(input_chron)):
                with open("chronical\\" + input_chron[a], "r") as read_file:
                    chron_dict = json.load(read_file)
                chron.append(chron_dict.get("Name"))
                chron_main_added_characteristics = chron_dict.get("added_characteristics")
                pre_chron_added_characteristics = chron_main_added_characteristics[0]
                pre_chron_added_Second_characteristics = chron_main_added_characteristics[1]
                pre_chron_added_main_characteristics = chron_main_added_characteristics[2]

                chron_added_characteristics = list(map(sum, zip(pre_chron_added_characteristics, chron_added_characteristics)))
                chron_added_Second_characteristics = list(map(sum, zip(pre_chron_added_Second_characteristics, chron_added_Second_characteristics)))
                chron_added_main_characteristics = list(map(sum, zip(pre_chron_added_main_characteristics, chron_added_main_characteristics)))

        else:
            while True:
                list_input_chron = pick(options_chron,title=title_chron, indicator='=>', multiselect=True)
                if len(list_input_chron) == Len_Chronical:
                    break
                else:
                    title_chron = f"Вы можете выбрать только {Len_Chronical}"
            with open("chronical\\" + list_input_chron[0][0], "r") as read_file:
                chron_dict = json.load(read_file)
            chron.append(chron_dict.get("Name"))
            chron_main_added_characteristics = chron_dict.get("added_characteristics")

            chron_added_characteristics = chron_main_added_characteristics[0]
            chron_added_Second_characteristics = chron_main_added_characteristics[1]
            chron_added_main_characteristics = chron_main_added_characteristics[2]
    
    nameofjson = 'persons\\json\\' + NNN + '.json'
    nameoftxt = 'persons\\' + NNN + '.txt'
    
    Star_characteristics = Second_characteristics[2] 
    Settings_of_Second_characteristics = Second_characteristics[1]
    Second_characteristics = Second_characteristics[0]
    if age >= 26: 
        prof_added_characteristics = list(map(sum, zip(prof_added_characteristics, chron_added_characteristics)))
        prof_added_Second_characteristics = list(map(sum, zip(prof_added_Second_characteristics, chron_added_Second_characteristics)))
    
    characteristic = list(map(sum, zip(characteristic, prof_added_characteristics)))
    Second_characteristics = list(map(sum, zip(Second_characteristics, prof_added_Second_characteristics)))
    main_characteristics = []
    main_characteristics.append(characteristic)
    main_characteristics.append(Second_characteristics)
    if age >= 26:
        chron_added_main_characteristics[0] = chron_added_main_characteristics[0] / 100
        chron_added_main_characteristics[1] = chron_added_main_characteristics[1] / 100
        chron_added_main_characteristics[2] = chron_added_main_characteristics[2] / 100
        chron_added_main_characteristics[4] = chron_added_main_characteristics[4] / 100
    if age >= 26:
        Health = 10 * characteristic[4] * chron_added_main_characteristics[0]
        Damage_resistance = Second_characteristics[0] + Second_characteristics[6] * chron_added_main_characteristics[1]
        Speed = 5 * chron_added_main_characteristics[2]
        Steps = Speed * 3 
        Steps = Steps + chron_added_main_characteristics[3]
        Fatigue_threshold = characteristic[2] + characteristic[3] * chron_added_main_characteristics[4]

    Health = 10 * characteristic[4]
    Damage_resistance = Second_characteristics[0] + Second_characteristics[6]
    Speed = 5
    Steps = Speed * 3 
    Steps = Steps
    Fatigue_threshold = characteristic[2] + characteristic[3]

    Star_characteristics.sort()
    OutputJson = dict(NNN=NNN, Sex=Sex, age=age, Chronical=chron, Prof=Prof, Fatigue_threshold=Fatigue_threshold, Steps=Steps, Speed=Speed, Damage_resistance=Damage_resistance, Health=Health, characteristic=main_characteristics, Star_characteristics=Star_characteristics) 
    chron_added_main_characteristics = [1, 1, 1, 0, 1]
    with open(nameofjson,"w") as write_file: 
        json.dump(OutputJson, write_file, ensure_ascii=False)
    stars_table_data = ["□", "□", "□", "□", "□", "□", "□", "□", "□", "□", "□", "□", "□", "□", "□", "□", "□", "□", "□", "□"]
    for t in range(len(Star_characteristics)):
        stars_table_data[Star_characteristics[t]] = "☑"

    if DayOfBorn < 10:
        StrDayOfBorn = '0' + str(DayOfBorn)
    if MonthOfBorn < 10:
        StrMonthOfBorn = '0' + str(MonthOfBorn)

    str_chron_added_main_characteristics = []
    l = 0
    while l <= 4:
        if l != 3:
            strrrrr = str(chron_added_main_characteristics[l] * 100)
            if chron_added_main_characteristics[l] * 100 == 100:
                str_chron_added_main_characteristics.append("     ")
            elif chron_added_main_characteristics[l] * 100 < 100:
                str_chron_added_main_characteristics.append("(" +" " + strrrrr + "%" + ")")
            elif chron_added_main_characteristics[l] * 100 >= 101:
                str_chron_added_main_characteristics.append("(" + strrrrr + "%" + ")")
            else:
                str_chron_added_main_characteristics.append(strrrrr)
        strrr = str(chron_added_main_characteristics[3])
        if chron_added_main_characteristics[3] == 0:
            str_chron_added_main_characteristics.append("     ")
        elif chron_added_main_characteristics[3] < 10 and chron_added_main_characteristics[3] > 0:
            str_chron_added_main_characteristics.append("(" + "+" + strrr + " " + " " + ")")
        elif chron_added_main_characteristics[3] > 9:
            str_chron_added_main_characteristics.append("(" + "+" + strrr + " " + ")")
        elif chron_added_main_characteristics[3] < -9:
            str_chron_added_main_characteristics.append("(" + strrr + " " + ")")

        l = l + 1

    txt_file = open(nameoftxt, "w+", encoding="utf-8")
    txt_file.write(f"ФИО           : {NNN}\n")
    txt_file.write(f"Пол           : {Sex}\n")
    txt_file.write(f"Возраст       : {age}\n")
    txt_file.write(f"Дата Рождения : {StrDayOfBorn}.{StrMonthOfBorn}.{YearOfBorn}\n")
    txt_file.write(f"\n")
    txt_file.write(f"Профессии: ")
    for z in range(len(Prof)):
        txt_file.write(f"{Prof[z]} ")
    txt_file.write(f"\n")
    txt_file.write(f"\n")
    txt_file.write(f"Порог усталости : {Fatigue_threshold} {str_chron_added_main_characteristics[4]}\n")
    txt_file.write(f"Шаги            : {Steps} {str_chron_added_main_characteristics[3]}\n")
    txt_file.write(f"\n")
#    txt_file.write(f"Здоровье             : {Health} {str_chron_added_main_characteristics[0]}\n")
#    txt_file.write(f"Устойчивость к урону : {Damage_resistance} {str_chron_added_main_characteristics[1]}\n")
    txt_file.write(f"Скорость             : {Speed} {str_chron_added_main_characteristics[2]}\n")
    txt_file.write(f"\n")
    txt_file.write(f"Основные Характеристики\n")
    txt_file.write(f"\n")
    str_prof_added_characteristics = []
    for k in range(len(prof_added_characteristics)):
        strrr = str(prof_added_characteristics[k])
        if prof_added_characteristics[k] == 0:
            str_prof_added_characteristics.append("     ")
        elif prof_added_characteristics[k] < 10 and prof_added_characteristics[k] > 0:
            str_prof_added_characteristics.append("(" + "+" + strrr + " " + ")")
        elif prof_added_characteristics[k] > 9:
            str_prof_added_characteristics.append("(" + "+" + strrr + ")")
        elif prof_added_characteristics[k] < -9:
            str_prof_added_characteristics.append("(" + strrr + ")")
        else:
            str_prof_added_characteristics.append(strrr)
    txt_file.write(f"Сила         : {main_characteristics[0][0]} {str_prof_added_characteristics[0]} Интеллект : {main_characteristics[0][1]} {str_prof_added_characteristics[1]}\n")
    txt_file.write(f"Ловкость     : {main_characteristics[0][2]} {str_prof_added_characteristics[2]} Воля      : {main_characteristics[0][3]} {str_prof_added_characteristics[3]}\n")
    txt_file.write(f"Телосложение : {main_characteristics[0][4]} {str_prof_added_characteristics[4]} Харизма   : {main_characteristics[0][5]} {str_prof_added_characteristics[5]}\n")

    str_main_characteristics = []
    for g in range(len(main_characteristics[1])):
        strrr = str(main_characteristics[1][g])
        if main_characteristics[1][g] < 10:
            str_main_characteristics.append(strrr + " ")
        else:
            str_main_characteristics.append(strrr)
    str_prof_added_Second_characteristics = []
    for u in range(len(prof_added_Second_characteristics)):
        strrr = str(prof_added_Second_characteristics[u])
        if prof_added_Second_characteristics[u] == 0:
            str_prof_added_Second_characteristics.append("     ")
        elif prof_added_Second_characteristics[u] < 10 and prof_added_Second_characteristics[u] > 0:
            str_prof_added_Second_characteristics.append("(" + "+" + strrr + " " + ")")
        elif prof_added_Second_characteristics[u] > 9:
            str_prof_added_Second_characteristics.append("(" + "+" + strrr + ")")
        elif prof_added_Second_characteristics[u] < -9:
            str_prof_added_Second_characteristics.append("(" + strrr + ")")
        else:
            str_prof_added_Second_characteristics.append(strrr)


    txt_file.write(f"\n")
    txt_file.write(f"Второстепенные Характеристики\n")
    txt_file.write(f"\n")
    txt_file.write(f"{stars_table_data[0]} Атлетика                    : {str_main_characteristics[0]} {str_prof_added_Second_characteristics[0]}   {stars_table_data[10]} Запугивание          : {str_main_characteristics[10]} {str_prof_added_Second_characteristics[10]}\n")
    txt_file.write(f"{stars_table_data[1]} Бдительность                : {str_main_characteristics[1]} {str_prof_added_Second_characteristics[1]}   {stars_table_data[11]} Обман                : {str_main_characteristics[11]} {str_prof_added_Second_characteristics[11]}\n")
    txt_file.write(f"{stars_table_data[2]} Ближний бой К-Р             : {str_main_characteristics[2]} {str_prof_added_Second_characteristics[2]}   {stars_table_data[12]} Лидерство            : {str_main_characteristics[12]} {str_prof_added_Second_characteristics[12]}\n")
    txt_file.write(f"{stars_table_data[3]} Ближний бой У-Д             : {str_main_characteristics[3]} {str_prof_added_Second_characteristics[3]}   {stars_table_data[13]} Природа              : {str_main_characteristics[13]} {str_prof_added_Second_characteristics[13]}\n")
    txt_file.write(f"{stars_table_data[4]} Внимание                    : {str_main_characteristics[4]} {str_prof_added_Second_characteristics[4]}   {stars_table_data[14]} Механика/электроника : {str_main_characteristics[14]} {str_prof_added_Second_characteristics[14]}\n")
    txt_file.write(f"{stars_table_data[5]} Вождение/пилотирование      : {str_main_characteristics[5]} {str_prof_added_Second_characteristics[5]}   {stars_table_data[15]} Религия              : {str_main_characteristics[15]} {str_prof_added_Second_characteristics[15]}\n")
    txt_file.write(f"{stars_table_data[6]} Выживание                   : {str_main_characteristics[6]} {str_prof_added_Second_characteristics[6]}   {stars_table_data[16]} Скрытность           : {str_main_characteristics[16]} {str_prof_added_Second_characteristics[16]}\n")
    txt_file.write(f"{stars_table_data[7]} Дальний бой лёгкое оружие   : {str_main_characteristics[7]} {str_prof_added_Second_characteristics[7]}   {stars_table_data[17]} Убеждение/торг       : {str_main_characteristics[17]} {str_prof_added_Second_characteristics[17]}\n")
    txt_file.write(f"{stars_table_data[8]} Дальний бой среднее оружие  : {str_main_characteristics[8]} {str_prof_added_Second_characteristics[8]}   {stars_table_data[18]} Ловкость рук         : {str_main_characteristics[18]} {str_prof_added_Second_characteristics[18]}\n")
    txt_file.write(f"{stars_table_data[9]} Дальний бой тяжёлое оружие  : {str_main_characteristics[9]} {str_prof_added_Second_characteristics[9]}   {stars_table_data[19]} Химия                : {str_main_characteristics[19]} {str_prof_added_Second_characteristics[19]}\n")
    txt_file.close()

    print(f"ФИО           : {NNN}")
    print(f"Пол           : {Sex}")
    print(f"Возраст       : {age}")
    print(f"Дата Рождения : {StrDayOfBorn}.{StrMonthOfBorn}.{YearOfBorn}")
    print(f"")
    print(f"Профессии: ")
    for z in range(len(Prof)):
        print(f"{Prof[z]}", end=" ")
    print(f" ")
    print(f"Порог усталости : {Fatigue_threshold} {str_chron_added_main_characteristics[4]}")
    print(f"Шаги            : {Steps} {str_chron_added_main_characteristics[3]}")
    print(f" ")
#    print(f"Здоровье             : {Health} {str_chron_added_main_characteristics[0]}")
#    print(f"Устойчивость к урону : {Damage_resistance} {str_chron_added_main_characteristics[1]}")
    print(f"Скорость             : {Speed} {str_chron_added_main_characteristics[2]}")
    print(f" ")
    print(f"Основные Характеристики")
    print(f" ")
    print(f"Сила         : {main_characteristics[0][0]} {str_prof_added_characteristics[0]} Интеллект : {main_characteristics[0][1]} {str_prof_added_characteristics[1]}\n")
    print(f"Ловкость     : {main_characteristics[0][2]} {str_prof_added_characteristics[2]} Воля      : {main_characteristics[0][3]} {str_prof_added_characteristics[3]}\n")
    print(f"Телосложение : {main_characteristics[0][4]} {str_prof_added_characteristics[4]} Харизма   : {main_characteristics[0][5]} {str_prof_added_characteristics[5]}\n")
    print(f" ")
    print(f"Второстепенные Характеристики ")
    print(f" ")
    print(f"{stars_table_data[0]} Атлетика                    : {str_main_characteristics[0]} {str_prof_added_Second_characteristics[0]}   {stars_table_data[10]} Запугивание          : {str_main_characteristics[10]} {str_prof_added_Second_characteristics[10]}")
    print(f"{stars_table_data[1]} Бдительность                : {str_main_characteristics[1]} {str_prof_added_Second_characteristics[1]}   {stars_table_data[11]} Обман                : {str_main_characteristics[11]} {str_prof_added_Second_characteristics[11]}")
    print(f"{stars_table_data[2]} Ближний бой К-Р             : {str_main_characteristics[2]} {str_prof_added_Second_characteristics[2]}   {stars_table_data[12]} Лидерство            : {str_main_characteristics[12]} {str_prof_added_Second_characteristics[12]}")
    print(f"{stars_table_data[3]} Ближний бой У-Д             : {str_main_characteristics[3]} {str_prof_added_Second_characteristics[3]}   {stars_table_data[13]} Природа              : {str_main_characteristics[13]} {str_prof_added_Second_characteristics[13]}")
    print(f"{stars_table_data[4]} Внимание                    : {str_main_characteristics[4]} {str_prof_added_Second_characteristics[4]}   {stars_table_data[14]} Механика/электроника : {str_main_characteristics[14]} {str_prof_added_Second_characteristics[14]}")
    print(f"{stars_table_data[5]} Вождение/пилотирование      : {str_main_characteristics[5]} {str_prof_added_Second_characteristics[5]}   {stars_table_data[15]} Религия              : {str_main_characteristics[15]} {str_prof_added_Second_characteristics[15]}")
    print(f"{stars_table_data[6]} Выживание                   : {str_main_characteristics[6]} {str_prof_added_Second_characteristics[6]}   {stars_table_data[16]} Скрытность           : {str_main_characteristics[16]} {str_prof_added_Second_characteristics[16]}")
    print(f"{stars_table_data[7]} Дальний бой лёгкое оружие   : {str_main_characteristics[7]} {str_prof_added_Second_characteristics[7]}   {stars_table_data[17]} Убеждение/торг       : {str_main_characteristics[17]} {str_prof_added_Second_characteristics[17]}")
    print(f"{stars_table_data[8]} Дальний бой среднее оружие  : {str_main_characteristics[8]} {str_prof_added_Second_characteristics[8]}   {stars_table_data[18]} Ловкость рук         : {str_main_characteristics[18]} {str_prof_added_Second_characteristics[18]}")
    print(f"{stars_table_data[9]} Дальний бой тяжёлое оружие  : {str_main_characteristics[9]} {str_prof_added_Second_characteristics[9]}   {stars_table_data[19]} Химия                : {str_main_characteristics[19]} {str_prof_added_Second_characteristics[19]}")
    dskfo = input("Нажмите Enter для выхода")



    start()

def add_prof():
    os.system('cls||clear')
    while True:
        added_characteristics = []
        main_characteristics = [0, 0, 0, 0, 0, 0]
        second_characteristics = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        added_characteristics.append(main_characteristics)
        added_characteristics.append(second_characteristics)
        added_characteristics[0] = list(map(int, added_characteristics[0]))
        added_characteristics[1] = list(map(int, added_characteristics[1]))
        title_add_prof =   ("  Меню создания персонажей")
        options_add_prof = ['Создать Профу', 'Вернуться']
        maininput, index2 = pick(options_add_prof,title=title_add_prof, indicator='=>')
        if maininput == 'Создать Профу':
            Name = input("Название професии: ")
            print('введите три числа:')
            print(" ")
            print('1. [bright_white]0/1 Основные/второстепенные характеристики')
            print('2. [bright_white]Номер характеристики по списку ниже')
            print('3. [bright_white]То сколько очков к характеристики добавляет профа или добавте "[bold green3]-[/bold green3]" для отнимания')
            print("[bright_white]Напишите [bold green3]save[/bold green3] для сохранения данных об профе")
            print(" ")
            print("                ---Основные Характеристики---          ")
            print("1.[bright_white] Сила")
            print("2.[bright_white] Интеллект")
            print("3.[bright_white] Ловкость")
            print("4.[bright_white] Воля")
            print("5.[bright_white] Телосложение")
            print("6.[bright_white] Харизма")
            print(" ")
            print("             ---Второстепенные Характеристики---       ")
            print("1. Атлетика                    11. Запугивание         ")
            print("2. Бдительность                12. Обман               ")
            print("3. Ближний бой К-Р             13. Лидерство           ")
            print("4. Ближний бой У-Д             14. Природа             ")
            print("5. Внимание                    15. Механика/электроника")
            print("6. Вождение/пилотирование      16. Религия             ")
            print("7. Выживание                   17. Скрытность          ")
            print("8. Дальний бой лёгкое оружие   18. Убеждение/торг      ")
            print("9. Дальний бой среднее оружие  19. Ловкость рук        ")
            print("10. Дальний бой тяжёлое оружие 20. Химия               ")
            print(" ")
            while True:
                input1 = input('>>> ')
                if input1 == 'save':
                    os.system('cls||clear')
                    break
                input1 = input1.split()
                input1 = list(map(int, input1))
                input1[1] = input1[1] - 1
                added_characteristics[input1[0]][input1[1]] = input1[2]
                nameofjson = "profs\\" + Name + '.json'
                OutputJson = dict(Name=Name, added_characteristics=added_characteristics)
                with open(nameofjson,"w") as write_file: 
                    json.dump(OutputJson, write_file, ensure_ascii=False)
                

        elif maininput == 'Вернуться':
            start()

def add_chronical():
    os.system('cls||clear')
    while True:
        added_characteristics = []
        main_characteristics = [0, 0, 0, 0, 0, 0]
        second_characteristics = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        first_characteristics = [100.0, 100.0, 100.0, 100.0, 100.0]
        added_characteristics.append(main_characteristics)
        added_characteristics.append(second_characteristics)
        added_characteristics.append(first_characteristics)
        added_characteristics[0] = list(map(int, added_characteristics[0]))
        added_characteristics[1] = list(map(int, added_characteristics[1]))
        added_characteristics[2] = list(map(int, added_characteristics[2]))
        title_add_chron =   ("  Меню создания хронических заболеваний")
        options_add_chron = ['Создать хроническую болезень', 'Вернуться']
        maininput, index2 = pick(options_add_chron,title=title_add_chron, indicator='=>')
        if maininput == 'Создать хроническую болезень':
            Name = input("Название хронической болезни: ")
            print('введите три числа:')
            print(" ")
            print('1. [bright_white]0/1/2 Основные/второстепенные/главные характеристики')
            print('2. [bright_white]Номер характеристики по списку ниже')
            print('3. [bright_white]То сколько очков к характеристики добавляет болезнь или добавте "[bold green3]-[/bold green3]" для отнимания в случае главных характеристик пишите процентное соотношение')
            print("[bright_white]Напишите [bold green3]save[/bold green3] для сохранения данных об профе")
            print(" ")
            print("                ---Основные Характеристики---          ")
            print("1.[bright_white] Сила")
            print("2.[bright_white] Интеллект")
            print("3.[bright_white] Ловкость")
            print("4.[bright_white] Воля")
            print("5.[bright_white] Телосложение")
            print("6.[bright_white] Харизма")
            print(" ")
            print("             ---Второстепенные Характеристики---       ")
            print("1. Атлетика                    11. Запугивание         ")
            print("2. Бдительность                12. Обман               ")
            print("3. Ближний бой К-Р             13. Лидерство           ")
            print("4. Ближний бой У-Д             14. Природа             ")
            print("5. Внимание                    15. Механика/электроника")
            print("6. Вождение/пилотирование      16. Религия             ")
            print("7. Выживание                   17. Скрытность          ")
            print("8. Дальний бой лёгкое оружие   18. Убеждение/торг      ")
            print("9. Дальний бой среднее оружие  19. Ловкость рук        ")
            print("10. Дальний бой тяжёлое оружие 20. Химия               ")
            print(" ")
            print("1. [bold red][0x80070002][/bold red]")
            print("2. [bold red][0x80070002][/bold red]")
            print("3. Скорость")
            print("4. Шаги (Писать количество)")
            print("5. Порог усталости")
            while True:
                input1 = input('>>> ')
                if input1 == 'save':
                    os.system('cls||clear')
                    break
                input1 = input1.split()
                input1 = list(map(int, input1))
                if input1[0] != 2:
                    input1[1] = input1[1] - 1
                    added_characteristics[input1[0]][input1[1]] = input1[2]
                    nameofjson = "chronical\\" + Name + '.json'
                    OutputJson = dict(Name=Name, added_characteristics=added_characteristics)
                    with open(nameofjson,"w") as write_file: 
                        json.dump(OutputJson, write_file, ensure_ascii=False)
                elif input1[1] == 3 or input1[1] == 4 or input1[1] == 5:
                    input1[1] = input1[1] - 1
                    added_characteristics[input1[0]][input1[1]] = input1[2]
                    nameofjson = "chronical\\" + Name + '.json'
                    OutputJson = dict(Name=Name, added_characteristics=added_characteristics)
                    with open(nameofjson,"w") as write_file: 
                        json.dump(OutputJson, write_file, ensure_ascii=False)
                else:
                    t = 1
                    while t <= 500:
                        print("[bold red]Данныe удалены![/bold red]")
                        secsec = t / 10
                        sec = math.exp(secsec * -1)
                        time.sleep(sec)
                        t = t + 1 
                    Errrr = input("           ОШ  бКа )№    )а?   ;№ПЫВ *(ФА*%!__________     _________===      ")
                    loading()
                    

        elif maininput == 'Вернуться':
            start()
loading()