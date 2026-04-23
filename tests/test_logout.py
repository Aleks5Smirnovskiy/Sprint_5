class TestLogout:
    def test_user_can_log_out(self, desk_page, registered_user):
        desk_page.logout()

        assert desk_page.is_guest() is True