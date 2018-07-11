# -*- encoding:utf-8 -*-  
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home_page():
    return 'data of home page'

@app.route('/books')
def books():
    return 'all book list'

@app.route('/book/<book_id>')
def book(book_id):
    return 'return data of a book: {}'.format(book_id)

@app.route('/students')
def students():
    return 'all student list'

@app.route('/student/<student_id>')
def student(student_id):
    return 'return data of a student: {}'.format(student_id)

if __name__ == '__main__':
    app.run(debug=True)