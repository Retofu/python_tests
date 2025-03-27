from pages.base_page import BasePage
from pages.locators import titles_locators as t_locs

class WhatsNewPage(BasePage):
    page_url = '/what-is-new.html'

    def check_page_header_title(self, text):
        header_title = self.find(t_locs.header_title_loc)
        assert header_title.text == text