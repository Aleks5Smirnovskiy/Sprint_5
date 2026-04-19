class TestCreateListing:
    def test_guest_cannot_open_listing_creation(self, desk_page):
        desk_page.click_post_listing_as_guest()

        assert (
            desk_page.get_unauthorized_listing_text()
            == "Чтобы разместить объявление, авторизуйтесь"
        )

    def test_authorized_user_can_create_listing(
        self,
        desk_page,
        registered_user,
        listing_payload,
    ):
        desk_page.create_listing(listing_payload)
        desk_page.open_profile()

        assert desk_page.profile_has_listing(listing_payload["title"]) is True