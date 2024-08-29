__author__ = 'Yocheved'

from flask import Flask

print('__name__ = ',__name__)
print(f'__name__ = {__name__}')

# create Flask server
# Flask() - is a constructor of Flask
app = Flask(__name__)

def main():
    user_name = input('Enter your name, please: ')
    print(f'Dear {user_name}, hello from {__author__}, \
          here is your Flask server:')
    app.run()

if (__name__ == '__main__'):
    main()


