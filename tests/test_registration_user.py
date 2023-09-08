from pages.registration_page import RegistrationPage
import allure

first_name = 'Ivan'
last_name = 'Ivanov'
email = 'qwerty@mail.ru'
phone = "8800555353"
current_address = 'CUrrent aDDress 12a Here'
state = "NCR"
city = "Delhi"


def test_registration_students_form_positive(setup_browser):
    with allure.step("Открытие страницы регистрации"):
        registration_page = RegistrationPage()
    with allure.step("Заполнение имени"):
        registration_page.fill_first_name(first_name)
    with allure.step("Заполнение фамилии"):
        registration_page.fill_last_name(last_name)
    with allure.step("Заполнение email"):
        registration_page.fill_email(email)
    with allure.step("Выбор пола"):
        registration_page.choose_gender()
    with allure.step("Заполнение мобильного телефона"):
        registration_page.fill_user_phonenumber(phone)
    with allure.step("Выбор даты рождения"):
        registration_page.choose_birth_date('2000', '5', '1')
    with allure.step("Выбор предметов"):
        registration_page.type_subject('Math')
    with allure.step("Выбор хобби"):
        registration_page.choose_hobbie('2')
        registration_page.choose_hobbie('3')
    with allure.step("Загрузка изображения"):
        registration_page.choose_picture('test.png')
    with allure.step("Заполнения адреса проживания"):
        registration_page.type_current_adress(current_address)
    with allure.step("Выбор Штата и города"):
        registration_page.choose_state(state)
        registration_page.is_enabled('[id="react-select-4-input"]')
        registration_page.choose_city(city)
    with allure.step("Нажатие кнопки подтвердить"):
        registration_page.press_submit()

    with allure.step("Проверка итоговой таблицы"):
        registration_page.should_have_registered(full_name=f"{first_name} {last_name}",
                                                 email=email, gender='Male', mobile=phone,
                                                 date_of_birth='01 June,2000',
                                                 subjects='Maths', hobbies="Reading, Music",
                                                 picture="test.png", address=current_address,
                                                 state_and_city=f"{state} {city}")
