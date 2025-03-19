header_title = 'Sale'

def test_header_title(sale_page):
    sale_page.open_page()
    sale_page.check_page_header_title(header_title)