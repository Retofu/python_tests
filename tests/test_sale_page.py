from elements.headers import Title_Headers as t_headers

def test_header_title(sale_page):
    sale_page.open_page()
    sale_page.check_page_header_title(t_headers.Sale.value)