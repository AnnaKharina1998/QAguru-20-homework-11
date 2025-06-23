from QAguru_20_homework_9.moodel import Gender, Hobby, State, User
from QAguru_20_homework_9.page import RegistrationPage


def test_correct_filling():
    registration_page = RegistrationPage()
    # тестовые данные
    user = User(first_name='Vasya',
                last_name='Pupkin',
                email='some_email@mail.ru',
                gender=Gender.MALE,
                mobile='1234567890',
                birthday='01 January,2000',
                subject='Chemistry',
                hobby=Hobby.MUSIC,
                picture_name='my_cat_better_than_my_face.jpg',
                adress='Some street, 9 house',
                state=State.NCR,
                city='Delhi')
    # заполнение данных
    registration_page.register_user(user)

    # проверка
    registration_page.should_have_filled(user)
