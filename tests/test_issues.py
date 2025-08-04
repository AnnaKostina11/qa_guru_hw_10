import allure
from allure_commons.types import Severity
from selene import have
from selene.support import by
from selene.support.shared import browser


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "AnnaKostina11")
@allure.feature("Проверка названия Issue")
@allure.story("Selene без шагов")
@allure.link("https://github.com", name="Testing")
def test_issue_name_selene():
    browser.open('https://github.com')
    browser.element('.Button-label').click()
    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').type('AnnaKostina11/qa_guru_hw_1').press_enter()
    browser.element(by.link_text('AnnaKostina11/qa_guru_hw_1')).click()
    browser.element('#issues-tab').click()
    browser.element('[data-testid=issue-pr-title-link]').should(have.exact_text('issue title 11'))



@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "AnnaKostina11")
@allure.feature("Проверка названия Issue")
@allure.story("С динамическими шагами")
@allure.link("https://github.com", name="Testing")
def test_issue_name_dynamic_steps():
    with allure.step("Открываем главную страницу"):
        browser.open('https://github.com')

    with allure.step("Ищем репозитория"):
        browser.element('.Button-label').click()
        browser.element('.header-search-button').click()
        browser.element('#query-builder-test').type('AnnaKostina11/qa_guru_hw_1').press_enter()

    with allure.step("Переходим по ссылке репозитория"):
        browser.element(by.link_text('AnnaKostina11/qa_guru_hw_1')).click()

    with allure.step("Открываем таб Issues"):
        browser.element('#issues-tab').click()

    with allure.step("Проверяем наличие Issue с названием issue title 11"):
        browser.element('[data-testid=issue-pr-title-link]').should(have.exact_text('issue title 11'))



@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "AnnaKostina11")
@allure.feature("Проверка названия Issue")
@allure.story("Шаги с декоратором")
@allure.link("https://github.com", name="Testing")
def test_issue_name_decorator_steps():
    open_main_page()
    search_for_repository("AnnaKostina11/qa_guru_hw_1")
    go_to_repository("AnnaKostina11/qa_guru_hw_1")
    open_issue_tab()
    issue_with_name("issue title 11")


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Ищем репозитория {repo}")
def search_for_repository(repo):
    browser.element('.Button-label').click()
    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').type(repo).press_enter()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    browser.element('#issues-tab').click()


@allure.step("Проверяем наличие Issue с названием {name}")
def issue_with_name(name):
    browser.element('[data-testid=issue-pr-title-link]').should(have.exact_text(name))