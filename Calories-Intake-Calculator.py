# Приветствие
username = input('\nКак тебя зовут? Пожалуйста, впиши: ').strip().title()
print(f'\nПривет, {username}, приятно познакомиться!\n\nМы рады помочь тебе вычислить твой Индекс Массы Тела, сделать рекомендацию относительно количества калорий, \nкоторое ты должен потреблять каждый день, и даже составить тебе индивидуальный план питания.\n\nЗа дело!\n')

# Пол
sex = input('Укажи свой пол, используя буквы М и Ж: ').replace(' ', '').upper()
while sex == '' or sex != 'М' and sex != 'Ж':
    sex = input('\nВероятно, ты опечатался. Пожалуйста, укажи свой пол, используя буквы М и Ж (используй русскую раскладку клавиатуры): ').replace(
        ' ', '').upper()
if sex == 'М':
    male, female = 1, 0
else:
    male, female = 0, 1

# Возраст
while True:
    try:
        age = float(
            input('\n\nВведи, пожалуйста, свой возраст: ').replace(',', '.'))
        if age > 122 or age <= 3:
            raise ValueError
        break
    except:
        print('\nВероятно, ты ошибся. Давай попробуем ещё раз. Используй только цифры и точку или запятую в качестве разделителя.'*male +
              '\nВероятно, ты ошиблась. Давай попробуем ещё раз. Используй только цифры и точку или запятую в качестве разделителя.'*female)

# Вес
while True:
    try:
        weight = float(
            input('\n\nВведи, пожалуйста, свой вес в кг: ').replace(',', '.'))
        if weight >= 400 or weight <= 10:
            raise ValueError
        break
    except:
        print('\nВероятно, ты ошибся. Давай попробуем ещё раз. Используй только цифры и точку или запятую в качестве разделителя.'*male +
              '\nВероятно, ты ошиблась. Давай попробуем ещё раз. Используй только цифры и точку или запятую в качестве разделителя.'*female)

# Рост
while True:
    try:
        height = float(
            input('\n\nВведи, пожалуйста, свой рост в см: ').replace(',', '.'))
        if height >= 260 or height <= 50:
            raise ValueError
        break
    except:
        print('\nВероятно, ты ошибся. Давай попробуем ещё раз. Используй только цифры и точку или запятую в качестве разделителя.'*male +
              '\nВероятно, ты ошиблась. Давай попробуем ещё раз. Используй только цифры и точку или запятую в качестве разделителя.'*female)

# Рассчёт индекса массы тела (BMI):
bmi = round(float(weight / height**2 * 10000), 2)

print(
    f'\n\nСпасибо за информацию, {username}. При росте {height} см и весе {weight} кг твой ИМТ (Индекс Массы Тела) составляет {bmi}.')

if bmi <= 16:
    print('Это значит, у тебя значительный дефицит массы тела, тебе следует набрать вес. Мы сможем тебе в этом помочь!')
if bmi > 16 and bmi <= 18.5:
    print('Это значит, у тебя дефицит массы тела, тебе следовало бы набрать вес. Мы сможем тебе в этом помочь!')
if bmi > 18.5 and bmi <= 25:
    print('Это значит, что твой вес в пределах нормы. Продолжай в том же духе!')
if bmi > 25 and bmi <= 30:
    print('Это значит, что твой вес чуть выше нормы, в идеале его надо чуть снизить. Мы сможем тебе в этом помочь!')
if bmi > 30 and bmi <= 35:
    print('Это значит, что у тебя ожирение первой степени, необходимо ограничить потребляемые калории. Мы сможем тебе в этом помочь!')
if bmi > 35 and bmi <= 40:
    print('Это значит, что у тебя ожирение второй степени, необходимо ограничить потребляемые калории. Мы сможем тебе в этом помочь!')
if bmi > 40:
    print('Это значит, что у тебя ожирение третьей степени, необходимо ограничить потребляемые калории. Мы сможем тебе в этом помочь!')

# activity_dummy - это коэффициент активности, на который будет умножаться кол-во калорий.
activity = input("\nПо шкале от 1 до 9 оцени уровень своей физической активности, где 1 - это полностью лежачий образ жизни,\
    \n5 значит, что у тебя как минимум 3 тренировки в неделю по 1 часу, а 9 - что ты профессиональный спортсмен\
    \nили твоя нагрузка соизмерима с нагрузкой профессионального спортсмена: ").replace(' ', '')
while activity.isdigit() == False or int(activity) < 1 or int(activity) > 9:
    activity = input(
        '\nВероятно, это опечатка. Пожалуйста, укажи уровень своей физической активности, используя только цифры: ').replace(' ', '')
activity_dummy = float(activity)/10+1

# lose_or_gain - это коэффициент похудения, на который будет умножаться кол-во калорий.
lose_or_gain = 1
need_lose = input(
    '\nТы хочешь сбросить вес? Вставь ДА (или "+"), или же пропускай вопрос, нажав "Enter": ').replace(' ', '').lower()
while need_lose not in (['да', '+', '']):
    need_lose = input(
        '\nВероятно, это опечатка. Давай попробуем ещё раз: ').replace(' ', '').lower()
if need_lose == "да" or need_lose == "+":
    lose_or_gain = 0.9
if lose_or_gain == 1:
    need_gain = input(
        '\nТы хочешь набрать вес? Вставь ДА (или "+"), или же пропускай вопрос: ').replace(' ', '').lower()
    while need_gain not in (['да', '+', '']):
        need_gain = input(
            '\nВероятно, это опечатка. Давай попробуем ещё раз: ').replace(' ', '').lower()
    if need_gain == "да" or need_gain == "+":
        lose_or_gain = 1.1

# Для расчета кол-ва калорий мы используем формулу Харриса-Бенедикта, она разная для мужчин и для женщин.
# Минимальное количество калорий для человека - 1200.
cal = round(max(((88.362+(13.397*weight)+(4.799*height)-(5.677*age))*male +
                 (447.593+(9.247*weight)+(3.098*height)-(4.33*age))*female)*activity_dummy*lose_or_gain, 1200), 1)

# Необходимое кол-во БЖУ из расчета 1200 ккал в день:
multiplier = cal/1200
belki = round(multiplier*90)
zhiry = round(multiplier*26.7)
uglevody = round(multiplier*150)

# Посчитаем также необходимый объем воды. Рассчитывается по формуле 35 мл на каждый кг веса.
# Если человек худеет, то 40 мл на каждый кг идеального веса:
if lose_or_gain == 0.9:
    voda = max(1200, 40*min((height-100), weight-1))
else:
    voda = max(1200, 35*weight)
voda = round(float(voda), -2)/1000

print(f'\n{username}, спасибо за информацию! Мы посчитали для тебя оптимальное количество калорий в день: {cal}\nПриблизительное суточное количество белков - {belki} гр, жиров - {zhiry} гр, углеводов - {uglevody} гр.\
    \nТакже мы посчитали, что тебе следует выпивать {voda} л воды в день.\
    \n\nПри изменении веса рекомендуется пересчитывать данные показатели (желательно - несколько раз в месяц). \n\nТеперь давай составим тебе рацион питания.')

# Возможность пользователя самому ввести необходимое кол-во калорий
while True:
    try:
        cal_input = input(
            'Если ты лучше знаешь свою суточную норму калорий, можешь вписать число сюда,\nи мы рассчитаем тебе рацион на его основе (введи только цифры от 1200 до 10 000 или пропусти вопрос): ').replace(',', '.').replace(' ', '')
        if cal_input == '':
            break
        cal_input = int(cal_input)
        if cal_input > 10000 or cal_input < 1200:
            raise ValueError
        cal = cal_input
        multiplier = cal/1200
        belki = round(multiplier*90)
        zhiry = round(multiplier*26.7)
        uglevody = round(multiplier*150)
        print(f'\nТы ввёл свою суточную норму калорий: {cal}\nПриблизительное суточное количество белков для тебя - {belki} гр, жиров - {zhiry} гр, углеводов - {uglevody} гр.\
        \n\nПри изменении веса рекомендуется пересчитывать данный показатель (желательно - несколько раз в месяц). \n\nТеперь давай составим тебе рацион питания.'*male+f'\nТы ввела свою суточную норму калорий: {cal}\
        \nПриблизительное суточное количество белков для тебя - {belki} гр, жиров - {zhiry} гр, углеводов - {uglevody} гр.\
        \n\nПри изменении веса рекомендуется пересчитывать данный показатель (желательно - несколько раз в месяц). \n\nТеперь давай составим тебе рацион питания.'*female)
        break
    except:
        print('\nВероятно, ты ошибся. Давай попробуем ещё раз. Используй только цифры.'*male +
              '\nВероятно, ты ошиблась. Давай попробуем ещё раз. Используй только цифры.'*female)

# Пищевые ограничения пользователя
red_meat = input('\nЕсли ты НЕ употребляешь в пищу что-то из следующих продуктов, пожалуйста, вставь минус (-).\nЕсли употребляешь - можешь пропустить вопрос.\n\nКрасное мясо: ')
bird_meat = input('Мясо птицы: ').replace(' ', '')
eggs = input('Яйца: ').replace(' ', '')
dairy = input('Молочные продукты: ').replace(' ', '')
fish = input('Рыбу, морепродукты: ').replace(' ', '')
gluten = input('Глютен: ').replace(' ', '')
honey = input('Мёд: ').replace(' ', '')

# Функции просчета количества граммов и калорий для пользователя с учетом его потребностей:


def gr_quant(a):
    a = int(round(a['gr_1200']*multiplier, -1))
    return(a)


def cal_quant(a):
    a = int(round(a['gr_1200']*multiplier, -1))*a['cal']/100
    return(a)


def day_cal(a):
    print(f'\nОбщее количество калорий за день: {a}\n\n----------------')


def menu_output(a):
    print(f'{a["meal"]}\n{gr_quant(a)} грамм, {cal_quant(a)} ккал')


# Выведение результатов на экран
print('\nМы рады представить тебе твоё примерное меню на неделю с учётом твоих пищевых особенностей. Держи:')
cal_day1, cal_day2, cal_day3, cal_day4, cal_day5, cal_day6, cal_day7 = 0, 0, 0, 0, 0, 0, 0

# Day 1
zavtrak1 = {'meal': 'Яичница-глазунья с болгарским перцем и петрушкой',
            'cal': 150, 'gr_1200': 190}
veg_zavtrak1 = {
    'meal': 'Веганская яичница с болгарским перцем и петрушкой', 'cal': 120, 'gr_1200': 240}
perekus1 = {'meal': 'Запеканка с вишнёвым соусом', 'cal': 250, 'gr_1200': 90}
veg_gluten_perekus1 = {
    'meal': 'Веганская запеканка из тофу с вишнёвым соусом', 'cal': 140, 'gr_1200': 170}
obed1 = {'meal': 'Палтус, запечёный с бэби-картофелем',
         'cal': 180, 'gr_1200': 220}
veg_obed1 = {'meal': 'Лобио с бэби-картофелем', 'cal': 180, 'gr_1200': 240}
uzhin1 = {'meal': 'Тосты с печёночным паштетом и сыром',
          'cal': 180, 'gr_1200': 150}
veg_uzhin1 = {'meal': 'Тосты с паштетом из жареных баклажанов и орехов',
              'cal': 180, 'gr_1200': 150}
veg_gluten_uzhin1 = {
    'meal': 'Безглютеновые тосты с паштетом из жареных баклажанов и орехов', 'cal': 180, 'gr_1200': 150}

print('\n\n День 1. \n\n Завтрак:')
if eggs == '-':
    menu_output(veg_zavtrak1)
    cal_day1 += cal_quant(veg_zavtrak1)
else:
    menu_output(zavtrak1)
    cal_day1 += cal_quant(zavtrak1)

print('\n Перекус:')
if eggs or dairy or gluten == '-':
    menu_output(veg_gluten_perekus1)
    cal_day1 += cal_quant(veg_gluten_perekus1)
else:
    menu_output(perekus1)
    cal_day1 += cal_quant(perekus1)

print('\n Обед:')
if fish == '-':
    menu_output(veg_obed1)
    cal_day1 += cal_quant(veg_obed1)
else:
    menu_output(obed1)
    cal_day1 += cal_quant(obed1)

print('\n Ужин:')
if (red_meat and bird_meat) == '-' and gluten != '-':
    menu_output(veg_uzhin1)
    cal_day1 += cal_quant(veg_uzhin1)
elif gluten == '-':
    menu_output(veg_gluten_uzhin1)
    cal_day1 += cal_quant(veg_gluten_uzhin1)
else:
    menu_output(uzhin1)
    cal_day1 += cal_quant(uzhin1)

day_cal(cal_day1)

# Day 2
zavtrak2 = {'meal': 'Злаковый хлеб с листом салата, творожным сыром и сёмгой',
            'cal': 200, 'gr_1200': 150}
veg_zavtrak2 = {
    'meal': 'Злаковый хлеб с хумусом и вялеными томатами', 'cal': 200, 'gr_1200': 150}
gluten_zavtrak2 = {
    'meal': 'Безглютеновый хлеб с хумусом и вялеными томатами', 'cal': 200, 'gr_1200': 150}
perekus2 = {'meal': 'Сушеные манго, горький шоколад',
            'cal': 400, 'gr_1200': 57}
veg_gluten_perekus2 = {
    'meal': 'Сушеные манго, кэроб', 'cal': 250, 'gr_1200': 70}
obed2 = {'meal': 'Курица, фаршированная сулугуни, с салатом из свеклы',
         'cal': 150, 'gr_1200': 250}
veg_gluten_obed2 = {
    'meal': 'Кабачковые котлеты с нутом и тофу, обжаренные в масле', 'cal': 180, 'gr_1200': 223}
uzhin2 = {'meal': 'Овощи на гриле', 'cal': 150, 'gr_1200': 210}

print('\n День 2. \n\n Завтрак:')
if fish or dairy == '-' and gluten != '-':
    menu_output(veg_zavtrak2)
    cal_day2 += cal_quant(veg_zavtrak2)
elif gluten == '-':
    menu_output(gluten_zavtrak2)
    cal_day2 += cal_quant(gluten_zavtrak2)
else:
    menu_output(zavtrak2)
    cal_day2 += cal_quant(zavtrak2)

print('\n Перекус:')
if dairy or gluten == '-':
    menu_output(veg_gluten_perekus2)
    cal_day2 += cal_quant(veg_gluten_perekus2)
else:
    menu_output(perekus2)
    cal_day2 += cal_quant(perekus2)

print('\n Обед:')
if dairy or bird_meat or gluten == '-':
    menu_output(veg_gluten_obed2)
    cal_day2 += cal_quant(veg_gluten_obed2)
else:
    menu_output(obed2)
    cal_day2 += cal_quant(obed2)

print('\n Ужин:')
menu_output(uzhin2)
cal_day2 += cal_quant(uzhin2)

day_cal(cal_day2)

# Day 3
zavtrak3 = {'meal': 'Кукурузная каша на миндальном молоке',
            'cal': 135, 'gr_1200': 210}
perekus3 = {'meal': 'Банан, йогурт, горсть орешков',
            'cal': 100, 'gr_1200': 220}
veg_perekus3 = {
    'meal': 'Банан, растительный йогурт, горсть орешков', 'cal': 100, 'gr_1200': 220}
gluten_perekus3 = {
    'meal': 'Банан, растительный безгютеновый йогурт, горсть орешков', 'cal': 100, 'gr_1200': 220}
obed3 = {'meal': 'Чечевичный суп-пюре c жареными семенами кунжута и оливковым маслом',
         'cal': 130, 'gr_1200': 300}
uzhin3 = {'meal': 'Хек печёный, на листе салата романо с помидорами черри',
          'cal': 120, 'gr_1200': 250}
veg_uzhin3 = {'meal': 'Фалафель с кукурузным салатом',
              'cal': 150, 'gr_1200': 200}

print('\n День 3. \n\n Завтрак:')
menu_output(zavtrak3)
cal_day3 += cal_quant(zavtrak3)

print('\n Перекус:')
if dairy == '-' and gluten != '-':
    menu_output(veg_perekus3)
    cal_day3 += cal_quant(veg_perekus3)
elif gluten == '-':
    menu_output(gluten_perekus3)
    cal_day3 += cal_quant(gluten_perekus3)
else:
    menu_output(perekus3)
    cal_day3 += cal_quant(perekus3)

print('\n Обед:')
menu_output(obed3)
cal_day3 += cal_quant(obed3)

print('\n Ужин:')
if fish == '-':
    menu_output(veg_uzhin3)
    cal_day3 += cal_quant(veg_uzhin3)
else:
    menu_output(uzhin3)
    cal_day3 += cal_quant(uzhin3)

day_cal(cal_day3)

# Day 4
zavtrak4 = {'meal': 'Сырники с клубникой', 'cal': 200, 'gr_1200': 170}
veg_zavtrak4 = {'meal': 'Веганские сырники с клубникой',
                'cal': 150, 'gr_1200': 250}
perekus4 = {'meal': 'Протеиновый батончик', 'cal': 250, 'gr_1200': 100}
veg_perekus4 = {'meal': 'Батончик с растительным протеином',
                'cal': 250, 'gr_1200': 110}
gluten_perekus4 = {
    'meal': 'Батончик с растительным протеином без глютена', 'cal': 250, 'gr_1200': 110}
obed4 = {
    'meal': 'Фаршированные перцы (рис+говяжий фарш)', 'cal': 120, 'gr_1200': 280}
veg_obed4 = {
    'meal': 'Фаршированные перцы (рис+овощи)', 'cal': 70, 'gr_1200': 430}
uzhin4 = {'meal': 'Запеканка овощная', 'cal': 80, 'gr_1200': 310}

print('\n День 4. \n\n Завтрак:')
if eggs or dairy == '-':
    menu_output(veg_zavtrak4)
    cal_day4 += cal_quant(veg_zavtrak4)
else:
    menu_output(zavtrak4)
    cal_day4 += cal_quant(zavtrak4)

print('\n Перекус:')
if (red_meat and bird_meat and eggs == "-") and gluten != '-':
    menu_output(veg_perekus4)
    cal_day4 += cal_quant(veg_perekus4)
elif gluten == '-':
    menu_output(gluten_perekus4)
    cal_day4 += cal_quant(gluten_perekus4)
else:
    menu_output(perekus4)
    cal_day4 += cal_quant(perekus4)

print('\n Обед:')
if red_meat == '-':
    menu_output(veg_obed4)
    cal_day4 += cal_quant(veg_obed4)
else:
    menu_output(obed4)
    cal_day4 += cal_quant(obed4)

print('\n Ужин:')
menu_output(uzhin4)
cal_day4 += cal_quant(uzhin4)

day_cal(cal_day4)

# Day 5
zavtrak5 = {'meal': 'Омлет из тофу с помидорами черри',
            'cal': 120, 'gr_1200': 230}
perekus5 = {'meal': 'Бутерброды с арахисовой пастой',
            'cal': 500, 'gr_1200': 90}
gluten_perekus5 = {
    'meal': 'Безглютеновые бутерброды с арахисовой пастой', 'cal': 500, 'gr_1200': 90}
obed5 = {'meal': 'Тыквенно-картофельный суп на кокосовом молоке с гренками и семечками',
         'cal': 100, 'gr_1200': 250}
uzhin5 = {'meal': 'Филе из индейки со шпинатом', 'cal': 100, 'gr_1200': 230}
veg_uzhin5 = {'meal': 'Грибы с красной фасолью и шпинатом с маслом ореха макадамии',
              'cal': 100, 'gr_1200': 230}

print('\n День 5. \n\n Завтрак:')
menu_output(zavtrak5)
cal_day5 += cal_quant(zavtrak5)

print('\n Перекус:')
if gluten == '-':
    menu_output(gluten_perekus5)
    cal_day5 += cal_quant(gluten_perekus5)
else:
    menu_output(perekus5)
    cal_day5 += cal_quant(perekus5)

print('\n Обед:')
menu_output(obed5)
cal_day5 += cal_quant(obed5)

print('\n Ужин:')
if bird_meat == '-':
    menu_output(veg_uzhin5)
    cal_day5 += cal_quant(veg_uzhin5)
else:
    menu_output(uzhin5)
    cal_day5 += cal_quant(uzhin5)

day_cal(cal_day5)

# Day 6
zavtrak6 = {'meal': 'Чиабатта с авокадо и перепелиными яйцами',
            'cal': 210, 'gr_1200': 140}
veg_zavtrak6 = {
    'meal': 'Чиабатта с авокадо, грибами и семенами чиа', 'cal': 210, 'gr_1200': 140}
veg_gluten_zavtrak6 = {
    'meal': 'Безглютеновая чиабатта с авокадо и грибами и семенами чиа', 'cal': 210, 'gr_1200': 140}
perekus6 = {'meal': 'Банановый смузи на молоке из кешью',
            'cal': 100, 'gr_1200': 180}
obed6 = {'meal': 'Паста с креветками и соусом песто',
         'cal': 200, 'gr_1200': 210}
veg_obed6 = {'meal': 'Паста с кедровыми орешками и соусом песто',
             'cal':  200, 'gr_1200': 210}
gluten_obed6 = {
    'meal': 'Безглютеновая паста с кедровыми орешками и соусом песто', 'cal': 200, 'gr_1200': 210}
uzhin6 = {'meal': 'Холодный итальянский салат с макаронами и оливками',
          'cal': 200, 'gr_1200': 150}
gluten_uzhin6 = {
    'meal': 'Холодный итальянский салат с безлютеновыми макаронами и оливками', 'cal': 200, 'gr_1200': 150}

print('\n День 6. \n\n Завтрак:')
if eggs == '-' and gluten != '-':
    menu_output(veg_zavtrak6)
    cal_day6 += cal_quant(veg_zavtrak6)
elif gluten == '-':
    menu_output(veg_gluten_zavtrak6)
    cal_day6 += cal_quant(veg_gluten_zavtrak6)
else:
    menu_output(zavtrak6)
    cal_day6 += cal_quant(zavtrak6)

print('\n Перекус:')
menu_output(perekus6)
cal_day6 += cal_quant(perekus6)

print('\n Обед:')
if fish == '-' and gluten != '-':
    menu_output(veg_obed6)
    cal_day6 += cal_quant(veg_obed6)
elif gluten == '-':
    menu_output(gluten_obed6)
    cal_day6 += cal_quant(gluten_obed6)
else:
    menu_output(obed6)
    cal_day6 += cal_quant(obed6)

print('\n Ужин:')
if gluten == '-':
    menu_output(gluten_uzhin6)
    cal_day6 += cal_quant(gluten_uzhin6)
else:
    menu_output(uzhin6)
    cal_day6 += cal_quant(uzhin6)

day_cal(cal_day6)

# Day 7
zavtrak7 = {'meal': 'Панкейки на рисовой муке с мёдом',
            'cal': 230, 'gr_1200': 130}
veg_nohoney_zavtrak7 = {
    'meal': 'Панкейки веганские на рисовой муке с кленовым сиропом', 'cal': 230, 'gr_1200': 130}
perekus7 = {'meal': 'Морковные чипсы', 'cal': 440, 'gr_1200': 40}
obed7 = {'meal': 'Телятина с гречкой и морковью', 'cal': 150, 'gr_1200': 280}
bird_obed7 = {'meal': 'Куриные котлеты с гречкой и морковью',
              'cal': 150, 'gr_1200': 280}
veg_obed7 = {'meal': 'Соевое мясо с гречкой и морковью',
             'cal': 150, 'gr_1200': 280}
uzhin7 = {'meal': 'Салат с тунцом', 'cal': 120, 'gr_1200': 245}
veg_uzhin7 = {'meal': 'Салат из морских водорослей с кунжутом',
              'cal': 120, 'gr_1200': 245}

print('\n День 7. \n\n Завтрак:')
if eggs or dairy or honey == '-':
    menu_output(veg_nohoney_zavtrak7)
    cal_day7 += cal_quant(veg_nohoney_zavtrak7)
else:
    menu_output(zavtrak7)
    cal_day7 += cal_quant(zavtrak7)

print('\n Перекус:')
menu_output(perekus7)
cal_day7 += cal_quant(perekus7)

print('\n Обед:')
if red_meat == '-' and bird_meat != '-':
    menu_output(bird_obed7)
    cal_day7 += cal_quant(bird_obed7)
elif bird_meat == '-':
    menu_output(veg_obed7)
    cal_day7 += cal_quant(veg_obed7)
else:
    menu_output(obed7)
    cal_day7 += cal_quant(obed7)

print('\n Ужин:')
if fish == '-':
    menu_output(veg_uzhin7)
    cal_day7 += cal_quant(veg_uzhin7)
else:
    menu_output(uzhin7)
    cal_day7 += cal_quant(uzhin7)

day_cal(cal_day7)

print(
    f'\n\n{username}, надеемся, тебе понравилось твоё меню!\n\n')
