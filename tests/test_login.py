from data import DEFAULT_USER_NAME


class TestLogin:
    def test_user_can_log_in(self, desk_page, logged_out_registered_user):
        desk_page.login_user(
            logged_out_registered_user["email"],
            logged_out_registered_user["password"],
        )
        desk_page.open_profile()

        assert desk_page.get_profile_name() == DEFAULT_USER_NAME