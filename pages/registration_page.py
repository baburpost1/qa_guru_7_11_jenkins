from selene import browser, be, have, command
import os
from tests.conftest import RESOURCE_PATH
from tests.conftest import setup_browser

class RegistrationPage():
    def __init__(self):
        self.open()

    browser = setup_browser
    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        return self

    def fill_first_name(self, value):
        browser.element('[id="firstName"]').should(be.blank).type(value)

    def fill_last_name(self, value):
        browser.element('[id="lastName"]').should(be.blank).type(value)

    def fill_email(self, value):
        browser.element('[id="userEmail"]').should(be.blank).type(value)

    def choose_gender(self):
        browser.element('[for="gender-radio-1"]').click()

    def fill_user_phonenumber(self, value):
        browser.element('[id="userNumber"]').should(be.blank).type(value)

    def choose_birth_date(self, year, month, day):
        browser.element('[id="dateOfBirthInput"]').click()
        browser.element(f'[class="react-datepicker__month-select"]>option[value="{month}"]').click()
        browser.element(f'[class="react-datepicker__year-select"]>option[value="{year}"]').click()
        browser.element(f'.react-datepicker__day--00{day}').click()

    def type_subject(self, value):
        browser.element('[id="subjectsInput"]').click().type(value).press_enter()

    def choose_hobbie(self, value):
        browser.element(f'[for="hobbies-checkbox-{value}"]').click()

    def choose_picture(self, file_name):
        browser.element('[id="uploadPicture"]').send_keys(os.path.join(RESOURCE_PATH, file_name))

    def type_current_adress(self, value):
        browser.element('[id="currentAddress"]').type(value)

    def is_enabled(self, element):
        if browser.element(element).should(be.enabled):
            return True
        else:
            raise ValueError

    def choose_state(self, value):
        browser.element('[id="react-select-3-input"]').type(value).press_enter()

    def choose_city(self, value):
        browser.element('[id="react-select-4-input"]').type(value).press_enter()

    def press_submit(self):
        browser.element('[id="submit"]').click()

    def should_have_registered(self, full_name, email, gender, mobile, date_of_birth, subjects, hobbies, picture,
                               address, state_and_city):
        browser.element('[class="table-responsive"]>table>tbody').should(have.exact_text(
            f"""Student Name {full_name}
Student Email {email}
Gender {gender}
Mobile {mobile}
Date of Birth {date_of_birth}
Subjects {subjects}
Hobbies {hobbies}
Picture {picture}
Address {address}
State and City {state_and_city}"""
        ))
