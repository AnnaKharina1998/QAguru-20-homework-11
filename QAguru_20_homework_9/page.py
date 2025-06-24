from selene import browser, command, have, be

from QAguru_20_homework_9.moodel import User
from QAguru_20_homework_9.resourses import resource_path


class RegistrationPage:
    def register_user(self, user: User):
        browser.execute_script('document.querySelector("#fixedban").remove()')
        browser.open("https://demoqa.com/automation-practice-form")
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        browser.element('#userEmail').type(user.email)
        browser.element(f"//label[contains(text(),'{user.gender.value}')]").click()
        browser.element('#userNumber').type(user.mobile)
        day, month_year = user.birthday.split(sep=' ')
        month, year = month_year.split(sep=',')
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__year-select").type(f"{year}").click()
        browser.element(".react-datepicker__month-select").type(f"{month}").click()
        browser.element(f".react-datepicker__day--0{day}").click()
        browser.element('#subjectsInput').type(user.subject[:2]).press_enter()
        browser.element(f"//label[contains(text(),'{user.hobby.value}')]").click()
        browser.element('#uploadPicture').send_keys(resource_path(user.picture_name))
        browser.element('#currentAddress').perform(command.js.scroll_into_view).type(user.adress)
        browser.element("//div[@id='stateCity-wrapper']/descendant::input[1]").type(user.state.value).press_enter()
        browser.element("//div[@id='stateCity-wrapper']/descendant::input[2]").type(user.city).press_enter()
        browser.element('#submit').perform(command.js.scroll_into_view).click()

    def should_have_filled(self, user: User):
        browser.element('.table-responsive').all('td').even.should(
            have.exact_texts(f'{user.first_name} {user.last_name}', user.email, user.gender.value, user.mobile, user.birthday, user.subject,
                             user.hobby.value, user.picture_name, user.adress, f'{user.state.value} {user.city}'))
