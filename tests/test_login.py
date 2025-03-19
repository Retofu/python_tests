error_alert = 'The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.'

def test_incorrect_login(login_page):
    login_page.open_page()
    login_page.fill_login_form('invalid_email@example.com', 'wrong_password')
    login_page.check_error_alert(error_alert)