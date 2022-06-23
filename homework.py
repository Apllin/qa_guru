def open_browser(browser, version):
    pass


def go_to_companyname_homepage():
    pass


def find_registration_button_on_login_page():
    pass


functions = [open_browser, go_to_companyname_homepage, find_registration_button_on_login_page]


def print_function(func):
    for i in func:
        print(f"Name of function: '{i.__name__}'", end='. ')
        if not any(i.__code__.co_varnames):
            print("No arguments")
        else:
            print(f"Arguments of function: {i.__code__.co_varnames}")


print_function(functions)
