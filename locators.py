from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Вход и регистрация']")
    POST_LISTING_BUTTON = (By.XPATH, "//button[normalize-space()='Разместить объявление']")
    AVATAR_BUTTON = (By.CSS_SELECTOR, "button.circleSmall")
    LOGOUT_BUTTON = (By.XPATH, "//button[normalize-space()='Выйти']")
    UNAUTHORIZED_POST_TITLE = (
        By.XPATH,
        "//h1[normalize-space()='Чтобы разместить объявление, авторизуйтесь']",
    )


class AuthPopupLocators:
    LOGIN_TITLE = (By.XPATH, "//h1[normalize-space()='Войти']")
    REGISTRATION_TITLE = (By.XPATH, "//h1[normalize-space()='Зарегистрироваться']")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    REPEAT_PASSWORD_INPUT = (By.NAME, "submitPassword")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[normalize-space()='Войти']")
    OPEN_REGISTRATION_BUTTON = (By.XPATH, "//button[normalize-space()='Нет аккаунта']")
    REGISTER_SUBMIT_BUTTON = (By.XPATH, "//button[normalize-space()='Создать аккаунт']")
    ERROR_MODAL_TITLE = (
        By.XPATH,
        "//div[contains(@class,'popUp_titleRow')]//h1",
    )


class CreateListingPageLocators:
    PAGE_TITLE = (By.XPATH, "//h1[normalize-space()='Новое объявление']")
    TITLE_INPUT = (By.NAME, "name")
    CATEGORY_ARROW_BUTTON = (By.XPATH, "//input[@name='category']/following-sibling::button")
    CITY_ARROW_BUTTON = (By.XPATH, "//input[@name='city']/following-sibling::button")
    USED_CONDITION_INPUT = (By.CSS_SELECTOR, "input[name='condition'][value='Б/У']")
    NEW_CONDITION_INPUT = (By.CSS_SELECTOR, "input[name='condition'][value='Новый']")
    DESCRIPTION_TEXTAREA = (By.NAME, "description")
    PRICE_INPUT = (By.NAME, "price")
    PUBLISH_BUTTON = (By.XPATH, "//button[normalize-space()='Опубликовать']")


class ProfilePageLocators:
    PAGE_TITLE = (By.XPATH, "//h1[normalize-space()='Мой профиль']")
    NAME_INPUT = (By.XPATH, "//input[@placeholder='Имя']")
    MY_LISTINGS_TITLE = (By.XPATH, "//h1[normalize-space()='Мои объявления']")


class DynamicLocators:
    @staticmethod
    def dropdown_option(option_text):
        return (By.XPATH, f"//button[normalize-space()='{option_text}']")

    @staticmethod
    def listing_title_in_profile(listing_title):
        return (
            By.XPATH,
            f"//h1[normalize-space()='Мои объявления']/following::*[normalize-space()='{listing_title}'][1]",
        )