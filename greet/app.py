from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return 'welcome'

@app.route('/welcome/<page>')
def welcome_page(page):
    if page == 'home':
        return 'welcome home'
    elif page == 'back':
        return 'welcome back'