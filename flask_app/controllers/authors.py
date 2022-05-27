from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.author import Author
from flask_app.models.book import Book

@app.route('/')
def index():
    return redirect('/authors')

@app.route('/authors')
def authors():
    return render_template("index.html", all_authors = Author.get_all())

@app.route('/create/author', methods=['POST'])
def create_author():
    data = {
        "name": request.form['name']
    }
    author_id = Author.create(data)
    return redirect('/')

@app.route('/author/<int:id>')
def show_author(id):
    data = {
        "id": id
    }
    return render_template('author.html', author=Author.get_by_id(data), unfavorited_books = Book.unfavorited_books(data))

@app.route('/join/book', methods = ['POST'])
def join_book():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    Author.add_favorite(data)
    return redirect(f"/author/{request.form['author_id']}")


@app.route('/dojos')
def dojo():
    return redirect('index.html')
