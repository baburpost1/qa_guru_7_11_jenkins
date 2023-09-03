from pages.registration_page import RegistrationPage

first_name = 'Ivan'
last_name = 'Ivanov'
email = 'qwerty@mail.ru'
phone = "8800555353"
current_address = 'CUrrent aDDress 12a Here'
state = "NCR"
city = "Delhi"


def test_registration_students_form_positive():
    registration_page = RegistrationPage()
    registration_page.fill_first_name(first_name)
    registration_page.fill_last_name(last_name)
    registration_page.fill_email(email)
    registration_page.choose_gender()
    registration_page.fill_user_phonenumber(phone)
    registration_page.choose_birth_date('2000', '5', '1')
    registration_page.type_subject('Math')
    registration_page.choose_hobbie('2')
    registration_page.choose_hobbie('3')
    registration_page.choose_picture('test.png')
    registration_page.type_current_adress(current_address)
    registration_page.choose_state(state)
    registration_page.is_enabled('[id="react-select-4-input"]')
    registration_page.choose_city(city)
    registration_page.press_submit()

    #     Проверка итоговой таблицы
    registration_page.should_have_registered(full_name=f"{first_name} {last_name}",
                                             email=email, gender='Male', mobile=phone,
                                             date_of_birth='01 June,2000',
                                             subjects='Maths', hobbies="Reading, Music",
                                             picture="test.png", address=current_address,
                                             state_and_city=f"{state} {city}")
