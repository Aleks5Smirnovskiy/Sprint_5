from data import DEFAULT_USER_NAME


class TestRegistration:
    def test_user_can_register(self, desk_page, user_credentials):
        desk_page.register_user(user_credentials["email"], user_credentials["password"])

        assert desk_page.is_authorized() is True

        desk_page.open_profile()

        assert desk_page.get_profile_name() == DEFAULT_USER_NAME

    def test_user_cannot_register_with_invalid_email(self, desk_page):
        initial_colors, error_colors = desk_page.submit_invalid_registration("invalid-email")

        assert desk_page.get_email_error_text() == "Ошибка"

        assert desk_page.are_registration_fields_highlighted(initial_colors, error_colors) is True

    def test_user_cannot_register_existing_account(self, desk_page, user_credentials):
        desk_page.register_user(user_credentials["email"], user_credentials["password"])
        desk_page.logout()
        initial_colors, error_colors = desk_page.submit_existing_user_registration(
            user_credentials["email"],
            user_credentials["password"],
        )

        assert desk_page.get_email_error_text() == "Ошибка"

        assert desk_page.are_registration_fields_highlighted(initial_colors, error_colors) is True