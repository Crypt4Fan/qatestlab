from qalabtest.pages import EmailPage, LoginPage


def test_login_and_send_email(test_setup):
    login_page = LoginPage(test_setup)
    login_page.\
        go().\
        set_email().\
        click_password_button().\
        set_password().\
        submit()

    email_page = EmailPage(test_setup)
    assert email_page.current_user == test_setup.email
    email_page.\
        click_write_email_button().\
        fill_to_field(test_setup.email).\
        fill_subject_field('Test email').\
        fill_body('Test message').\
        click_send_email_button()
