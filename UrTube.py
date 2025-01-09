import time


class User:
    '''
    Класс User создает объект пользователь с атрибутами:
    nickname - имя пользователя
    password - пароль в хэшированном виде
    age - возраст пользователя

    при просмотре - отображает nickname
    print() - отображает nickname
    '''

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(str(password))
        self.age = int(age)

    def __str__(self):
        return f'{self.nickname}'

    def __repr__(self):
        return f'{self.nickname}'


class Video:
    '''
    Класс Video создает объект видео с атрибутами:
    title - название видео
    duration - продолжительность, сек
    time_now - точка начала просмотра, сек
    adult_mode - возрастной рейтинг (True/False)

    При просмотре отображает название видео
    print() - выводит все атрибуты
    '''

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration  # продожительность
        self.time_now = time_now  # секунда остановки
        self.adult_mode = adult_mode

    def __str__(self):
        return (f'Название: {self.title} \n'
                f'Продолжитльность: {self.duration} \n'
                f'Возростной рейтинг: {self.adult_mode}\n'
                f'Точка просмотра, сек: {self.time_now}')

    def __repr__(self):  # отображате если объект в списке
        return f'{self.title}'


class UrTube:
    '''
    Класс UrTube создает объект UrTube типа "аналог YouTube" с атрибутами:
    users - список объектов класса User
    videos - список объектов класса Video
    current_user - объект класса User или None

    соержит функции:
    log_in(self, nicname, password) - присваивает атрибуту current_user объект класса User
        если nicname и password соответствуют одному из объектов из списка users;

    register(self, nickname, password, age) - создате новый объект класса User и записывает его
        в список  users, если nicname и password НЕ соответствуют ни одному из объектов из списка users

    log_out(self) - присваивает current_user значение None

    add(self, *args) - добавляет оъект класса Video в список videos, если знвчение атрибута title.arg
        не содержит ни один объект в списке videos

    get_video(self, name_video) - возвращает список объектов класса Video из списка videos,
        которые содержат name_video в атрибуте title

    watch_video(self, name_video) - ищет в списке videos объект с атрибутом title = name_video
        воспроизводит счетчик времени с сек time_now по duration в соотвествии с атр. найденого объекта,
        при условии, если:
        - current_user != None
        - user.age > 18 или video.adult_mode == False
        - user.age > 18 и video.adult_mode == True

    print() - выводит все атрибуты
    '''

    def __init__(self):
        self.users = []  # список содержит объекты класса User
        self.videos = []
        self.current_user = None

    def __str__(self):
        return (f'--------------UrTube-----------------\n'
                f'Список пользователй: {self.users} \n'
                f'Список видео: {self.videos} \n'
                f'Текущий пользователь: {self.current_user} \n'
                f'------------------------------------------')

    def log_in(self, nicname, password):
        password = str(password)
        if nicname in self.users.__repr__():  # в списке есть пользователь с таким именем
            for user in self.users:  # проходим по всем пользователям в списке
                if user.__repr__() == nicname:  # находим пользователя с нужным nickname
                    if user.password == hash(password):  # сравниваем пароль пользователя с введенным паролем
                        self.current_user = user  # смена текущего пользователя
                        print(f"Поздравляю, {user} вы вошли")
                    else:
                        print(f'Пользователя с таким \x1B[3m"именем"\x1B[0m или \x1B[3m"паролем"\x1B[0m не существует')
        else:
            print(f'Пользователя с таким \x1B[3m"именем"\x1B[0m или \x1B[3m"паролем"\x1B[0m не существует')

    def register(self, nickname, password, age):
        if nickname not in self.users.__repr__():  # Проверям, есть ли в списке таой пользователь
            user = User(nickname, password, age)  # если нет, то создаем пользователя
            self.users.append(user)  # добавляем объект класса User в список
            self.current_user = user  # назначаем текущего пользователя
            print(f'Добро пожаловать, {nickname}')
        else:
            print(f'Пользователь {nickname} уже существует')

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for video in args:
            if video.title not in my_tube.videos.__repr__():
                self.videos.append(video)

    def get_video(self, name_video):
        video_list = []
        for video in my_tube.videos:
            if name_video.lower() in video.title.lower():
                video_list.append(video)
        return video_list

    def watch_video(self, name_video):
        if my_tube.current_user:  # если пользователь залогинился
            for video in my_tube.videos:  # поиск названия видое
                if name_video == video.title:
                    if video.adult_mode and my_tube.current_user.age < 18:
                        print("Вам нет 18, пожалуйста покиньте страницу")
                        break
                    else:
                        print(f'----------Просмотр фильма {video.title}-----------')
                        print(video)
                        for sec in range(video.time_now, video.duration, 1):
                            print(sec + 1, end=' ', flush=True)  # Выводим число без перехода на новую строку
                            time.sleep(1)  # Задержка на 1 секунду
                            if (sec + 1) % 10 == 0:  # прострочный вывод счета каждые 10 сек
                                print()
                        print("Конец")
                        video.time_now = 0  # сбрасываем счетчик после просмотра
                        break
            else:
                print(f'Видео {name_video} не найдено')
        else:
            print('Войдите в аккаунт, что бы посмотреть видео')


if __name__ == '__main__':
    # print(UrTube.__doc__)
    # print(Video.__doc__)
    # print(User.__doc__)

    my_tube = UrTube()

    video1 = Video('Home video', 20, adult_mode=True)
    video2 = Video('Comedy', 30, time_now=11)
    video3 = Video('Since', 15)
    video4 = Video('Home video', 21, adult_mode=True)  # видео с повторяющимся название
    my_tube.add(video1, video2, video3, video4)  # добавляем видео коллекцию
    print('Поиск по запросу "O": ', my_tube.get_video('O'))

    my_tube.register('Danil', '1234Dd', 34)  # проверка регистрации
    my_tube.register('Alex', 4321, 20)  # проверка регистрации
    my_tube.register('Max', '1111hhh', 16)  # проверка регистрации
    my_tube.log_in('Danil', '1234Dd')  # проверка входа по логину
    my_tube.log_in('Danil', 9999)  # проверка неправильного пароля
    my_tube.log_in('Peres', '1234Dd')  # проверка неправильного логина

    my_tube.log_out()  # проверка разлогирования
    my_tube.watch_video('Home video')  # Войдите в аккаунт, что бы посмотреть видео
    my_tube.log_in('Max', '1111hhh')  # проверка регистрации
    my_tube.watch_video('Home video')  # Вам нет 18, пожалуйста покиньте страницу
    my_tube.watch_video('Comediya')  # Видео Comediya не найдено
    my_tube.watch_video('Comedy')  # проверка просмотра видео сек = 11
    my_tube.log_out()
    my_tube.log_in('Danil', '1234Dd')  # проверка входа по логину
    my_tube.watch_video('Comedy')  # проверка просмотра видео сек = 0
    print(my_tube)
