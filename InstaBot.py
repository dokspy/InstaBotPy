from instapy import InstaPy


# функция проверки сообщения для отправки True or False
def checking_logic(log):
    log = log.lower()
    if log == "yes":
        return True
    elif log == "no":
        return False
    else:
        print("Error type")


# функция собирает хештеги в список
def save_tags_list():
    n = int(input("Ведите к-ло хештегов: "))
    hashtags = []
    for i in range(n):
        hashtags.append(str(input(f"Введите хештег #{i + 1}: ")))
    return hashtags


username = input("Введите логин от аккаунта: ")
password = input("Введите пароль от аккаунта: ")

# Включить или выключить видимость браузера и работы в нем кода
vanish_browser = input(
    "Хочеш видеть как все происходит в браузере то пиши Yes(нагрузка на процесор больше), а если нет то пиши No: ")
vanish_browser = checking_logic(vanish_browser)

# собирает хештеги которые нужно лайкать
print('Введите хештеги которые нужно лайкать!')
tags = save_tags_list()

# собирает хештеги которорые нужно игнорировать
print('Ведите хештеги которые нужно игнорировать!')
dont_tags = save_tags_list()

# к-ло лайков которые вообщем нужно поставить
x = int(input("Ведите количество лайков которою нужно поставить: "))

# вкл или выкл подписку(True or False)
value = input("Введите Yes или No, чтоб включить(Yes) функцию подписки от к-ло лайков, или выключить(No)!: ")
value = checking_logic(value)

# вкл выкл ограничение по к-ло подписчиков
bounds_on_off = input()
bounds_on_off = checking_logic(bounds_on_off)

# максимальное к-ло подписчиков пользователь на которых подписываемя или лайкаем(чтоб не попасть на блогеров)
followers_max = int(input())

# Включить или выключить ограничение действий на день
quota_supervisor = input()
quota_supervisor = checking_logic(quota_supervisor)

# максимальная квота лайков которые можно поставить за час
likes_hourly = int(input())
# максимальная квота к-ло лайков которые можно поставить за день
likes_daily = int(input())

session = InstaPy(username=username, password=password, headless_browser=vanish_browser)
session.login()
session.like_by_tags(tags, amount=x)
session.dont_like(dont_tags)

if value:
    # к-ло процентов для подписки от к-ло лайков
    number = int(input("Введите к-ло процентов для подписки от к-ло лайков: "))
    session.set_do_follow(value, percentage=number)

session.set_relationship_bounds(enabled=bounds_on_off, max_followers=followers_max)
session.set_quota_supervisor(enabled=quota_supervisor, peak_likes_hourly=likes_hourly, peak_likes_daily=likes_daily)
session.end()
