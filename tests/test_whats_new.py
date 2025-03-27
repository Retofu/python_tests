from elements.headers import Title_Headers as t_headers

def test_header_title(whats_new_page):
    whats_new_page.open_page()
    whats_new_page.check_page_header_title(t_headers.Whats_New.value)