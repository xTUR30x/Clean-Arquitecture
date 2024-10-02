from user_authetication import *
from user_registration import *

if __name__ == '__main__':
    username = 'jhon-doe'
    password = 'Password123'

    user_registration = UserRegistration()
    user_authentication = UserAuthentication()

    if user_registration.register_user(username, password):
        print('User Register succesfully')
    else:
        print('User Register failed')

    if user_authentication.authenticate_user(username, password):
        print('User Logged succesfully')
    else:
        print('User Logged failed')
        

