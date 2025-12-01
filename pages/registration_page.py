import os
from selene import browser, by, have, be, command


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        # закрываем баннер если он есть
        if browser.element('#close-fixedban').matching(be.visible):
            browser.element('#close-fixedban').click()
        # убираем рекламные iframe
        browser.driver.execute_script("""
            let ads = document.querySelectorAll('iframe, #fixedban');
            ads.forEach(el => el.remove());
        """)
        return self

    # ---------- Часть I: mid-level шаги ----------
    def fill_first_name(self, value):
        browser.element('#firstName').type(value)
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)
        return self

    def fill_email(self, value):
        browser.element('#userEmail').type(value)
        return self

    def select_gender(self, gender_text):
        el = browser.element('#genterWrapper').element(by.text(gender_text))
        el.perform(command.js.scroll_into_view)
        el.perform(command.js.click)
        return self

    def fill_phone(self, value):
        browser.element('#userNumber').type(value)
        return self

    def fill_birth_date(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').type(year).press_enter()
        browser.element('.react-datepicker__month-select').type(month).press_enter()
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    def fill_subject(self, subject):
        browser.element('#subjectsInput').type(subject).press_enter()
        return self

    def choose_hobby(self, hobby_text):
        browser.element('#hobbiesWrapper').element(by.text(hobby_text)).click()
        return self

    def upload_picture(self, filename):
        file_path = os.path.abspath(f'tests/{filename}')
        browser.element('#uploadPicture').set_value(file_path)
        return self

    def fill_address(self, value):
        browser.element('#currentAddress').type(value)
        return self

    def select_state(self, state):
        browser.element('#react-select-3-input').type(state).press_enter()
        return self

    def select_city(self, city):
        browser.element('#react-select-4-input').type(city).press_enter()
        return self

    def submit(self):
        browser.element('#submit').click()
        return self

    # ---------- Проверка для mid-level ----------
    def should_have_registered(self, *expected_values):
        browser.element('.modal-title').should(have.text('Thanks for submitting the form'))
        browser.all('.table-responsive tbody tr td:nth-child(2)').should(
            have.exact_texts(*expected_values)
        )
        return self

    # ---------- Часть II: high-level шаги ----------
    def register(self, user):
        self.fill_first_name(user.first_name) \
            .fill_last_name(user.last_name) \
            .fill_email(user.email) \
            .select_gender(user.gender) \
            .fill_phone(user.phone) \
            .fill_birth_date(user.birth_year, user.birth_month, user.birth_day)

        for subject in user.subjects:
            self.fill_subject(subject)

        for hobby in user.hobbies:
            self.choose_hobby(hobby)

        self.upload_picture(user.picture) \
            .fill_address(user.address) \
            .select_state(user.state) \
            .select_city(user.city) \
            .submit()
        return self

    # ---------- Проверка для high-level ----------
    def should_have_registered_user(self, user):
        browser.element('.modal-title').should(have.text('Thanks for submitting the form'))

        expected_values = [
            f'{user.first_name} {user.last_name}',
            user.email,
            user.gender,
            user.phone,
            f'{user.birth_day} {user.birth_month},{user.birth_year}',
            ', '.join(user.subjects),
            ', '.join(user.hobbies),
            user.picture,
            user.address,
            f'{user.state} {user.city}'
        ]

        browser.all('.table-responsive tbody tr td:nth-child(2)').should(
            have.exact_texts(*expected_values)
        )
        return self
