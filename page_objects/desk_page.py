from locators import (
    AuthPopupLocators,
    CreateListingPageLocators,
    DynamicLocators,
    MainPageLocators,
    ProfilePageLocators,
)
from page_objects.base_page import BasePage
from data import BASE_URL


class DeskPage(BasePage):
    def get_registration_error_text(self):
        # Попробуем получить текст ошибки, если она появляется в попапе
        try:
            return self.get_text(AuthPopupLocators.ERROR_MODAL_TITLE)
        except Exception:
            return None
    def open_home_page(self):
        self.open(BASE_URL)

    def open_login_popup(self):
        self.open_home_page()
        self.click(MainPageLocators.LOGIN_BUTTON)
        self.wait_visible(AuthPopupLocators.LOGIN_TITLE)

    def open_registration_popup(self):
        self.open_login_popup()
        self.click(AuthPopupLocators.OPEN_REGISTRATION_BUTTON)
        self.wait_visible(AuthPopupLocators.REGISTRATION_TITLE)

    def fill_login_form(self, email, password):
        self.fill(AuthPopupLocators.EMAIL_INPUT, email)
        self.fill(AuthPopupLocators.PASSWORD_INPUT, password)

    def fill_registration_form(self, email, password):
        self.fill(AuthPopupLocators.EMAIL_INPUT, email)
        self.fill(AuthPopupLocators.PASSWORD_INPUT, password)
        self.fill(AuthPopupLocators.REPEAT_PASSWORD_INPUT, password)

    def register_user(self, email, password):
        self.open_registration_popup()
        self.fill_registration_form(email, password)
        self.click(AuthPopupLocators.REGISTER_SUBMIT_BUTTON)
        self.wait_until_authorized()

    def submit_invalid_registration(self, email):
        self.open_registration_popup()
        initial_colors = self.get_registration_border_colors()
        self.fill_registration_form(email, "Password123!")
        self.click(AuthPopupLocators.REGISTER_SUBMIT_BUTTON)
        return initial_colors, self.get_registration_border_colors()

    def submit_existing_user_registration(self, email, password):
        self.open_registration_popup()
        initial_colors = self.get_registration_border_colors()
        self.fill_registration_form(email, password)
        self.click(AuthPopupLocators.REGISTER_SUBMIT_BUTTON)
        return initial_colors, self.get_registration_border_colors()

    def login_user(self, email, password):
        self.open_login_popup()
        self.fill_login_form(email, password)
        self.click(AuthPopupLocators.LOGIN_SUBMIT_BUTTON)
        self.wait_until_authorized()

    def logout(self):
        self.click(MainPageLocators.LOGOUT_BUTTON)
        self.wait_visible(MainPageLocators.LOGIN_BUTTON)

    def click_post_listing_as_guest(self):
        self.open_home_page()
        self.click(MainPageLocators.POST_LISTING_BUTTON)
        self.wait_visible(MainPageLocators.UNAUTHORIZED_POST_TITLE)

    def open_create_listing_page(self):
        self.click(MainPageLocators.POST_LISTING_BUTTON)
        self.wait_visible(CreateListingPageLocators.PAGE_TITLE)

    def select_dropdown_option(self, arrow_locator, option_text):
        self.click(arrow_locator)
        self.click(DynamicLocators.dropdown_option(option_text))

    def select_used_condition(self):
        element = self.wait_present(CreateListingPageLocators.USED_CONDITION_INPUT)
        self.execute_script("arguments[0].click();", element)

    def create_listing(self, listing_data):
        self.open_create_listing_page()
        self.fill(CreateListingPageLocators.TITLE_INPUT, listing_data["title"])
        self.fill(
            CreateListingPageLocators.DESCRIPTION_TEXTAREA,
            listing_data["description"],
        )
        self.fill(CreateListingPageLocators.PRICE_INPUT, listing_data["price"])
        self.select_dropdown_option(
            CreateListingPageLocators.CATEGORY_ARROW_BUTTON,
            listing_data["category"],
        )
        self.select_dropdown_option(
            CreateListingPageLocators.CITY_ARROW_BUTTON,
            listing_data["city"],
        )
        self.select_used_condition()
        current_url = self.get_current_url()
        self.click(CreateListingPageLocators.PUBLISH_BUTTON)
        self.wait_url_changes(current_url)

    def open_profile(self):
        self.click(MainPageLocators.AVATAR_BUTTON)
        self.wait_visible(ProfilePageLocators.PAGE_TITLE)

    def wait_until_authorized(self):
        self.wait_visible(MainPageLocators.AVATAR_BUTTON)
        self.wait_visible(MainPageLocators.LOGOUT_BUTTON)

    def get_profile_name(self):
        return self.get_attribute(ProfilePageLocators.NAME_INPUT, "value")

    def get_unauthorized_listing_text(self):
        return self.get_text(MainPageLocators.UNAUTHORIZED_POST_TITLE)

    def get_registration_border_colors(self):
        return {
            "email": self.get_computed_style(AuthPopupLocators.EMAIL_INPUT, "border-color"),
            "password": self.get_computed_style(AuthPopupLocators.PASSWORD_INPUT, "border-color"),
            "repeat_password": self.get_computed_style(
                AuthPopupLocators.REPEAT_PASSWORD_INPUT,
                "border-color",
            ),
        }

    def are_registration_fields_highlighted(self, initial_colors, error_colors):
        print(f"Initial colors: {initial_colors}")
        print(f"Error colors: {error_colors}")
        # Считаем, что поле подсвечено, если цвет изменился хотя бы у одного поля
        return any(error_colors[field] != initial_colors[field] for field in error_colors)

    def is_authorized(self):
        return self.is_visible(MainPageLocators.AVATAR_BUTTON) and self.is_visible(
            MainPageLocators.LOGOUT_BUTTON
        )

    def is_guest(self):
        return self.is_visible(MainPageLocators.LOGIN_BUTTON)

    def profile_has_listing(self, listing_title):
        self.wait_visible(ProfilePageLocators.MY_LISTINGS_TITLE)
        return self.is_visible(DynamicLocators.listing_title_in_profile(listing_title))