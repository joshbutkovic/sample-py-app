from . import utils


def welcome_user():
    print('Welcome To The CLI')


def request_task():
    if utils.is_welcomed():
        print(utils.show_options())
