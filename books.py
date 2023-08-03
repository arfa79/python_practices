from flask import Flask, jsonify, request

app = Flask(__name__)

# Let's create a list to store our books
books = ['cat' 'dog' 'fish']
# Route to get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({'books': books})

# Route to get a specific book by its index
@app.route('/books/<int:index>', methods=['GET'])
def get_book(index):
    if index < len(books):
        return jsonify({'book': books[index]})
    else:
        return jsonify({'error': 'Book not found'})

# Route to add a new book
@app.route('/books', methods=['POST'])
def add_book():
    book = request.get_json()
    books.append(book)
    return jsonify({'message': 'Book added successfully'})

# Route to update a book
@app.route('/books/<int:index>', methods=['PUT'])
def update_book(index):
    if index < len(books):
        book = request.get_json()
        books[index] = book
        return jsonify({'message': 'Book updated successfully'})
    else:
        return jsonify({'error': 'Book not found'})

# Route to delete a book
@app.route('/books/<int:index>', methods=['DELETE'])
def delete_book(index):
    if index < len(books):
        del books[index]
        return jsonify({'message': 'Book deleted successfully'})
    else:
        return jsonify({'error': 'Book not found'})
if __name__ == '__main__':
    app.run(debug=True)