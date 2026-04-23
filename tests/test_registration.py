from data import ErrorMessages, UserData
from helpers import build_user_credentials


class TestRegistration:
    def test_user_can_register(self, desk_page):
        credentials = build_user_credentials()
        desk_page.register_user(credentials["email"], credentials["password"])

        assert desk_page.is_authorized() is True

    def test_user_profile_has_default_name(self, desk_page):
        credentials = build_user_credentials()
        desk_page.register_user(credentials["email"], credentials["password"])
        desk_page.open_profile()

        assert desk_page.get_profile_name() == UserData.DEFAULT_USER_NAME

    def test_user_cannot_register_with_invalid_email(self, desk_page):
        initial_colors, error_colors = desk_page.submit_invalid_registration("invalid-email")

        assert desk_page.get_registration_error_text() == ErrorMessages.REGISTRATION_ERROR
        assert desk_page.are_registration_fields_highlighted(initial_colors, error_colors) is True

    def test_user_cannot_register_existing_account(self, desk_page):
        credentials = build_user_credentials()
        desk_page.register_user(credentials["email"], credentials["password"])
        desk_page.logout()
        initial_colors, error_colors = desk_page.submit_existing_user_registration(
            credentials["email"],
            credentials["password"],
        )

        assert desk_page.get_registration_error_text() == ErrorMessages.REGISTRATION_ERROR
        assert desk_page.are_registration_fields_highlighted(initial_colors, error_colors) is True