# this is the "test/book_suggestions_test.py" file...

from app.book_suggestions import search_books, display_book_details, suggest_random_book


# Function to search for books
def search_books(query):
    params = {'q': query, 'key': API_KEY}
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return data


# Function to display book details
def display_book_details(book):
    volume_info = book.get('volumeInfo', {})
    title = volume_info.get('title', 'No Title')
    authors = volume_info.get('authors', ['Unknown Author'])
    description = volume_info.get('description', 'No description available')
    print(f"Title: {title}")
    print(f"Authors: {', '.join(authors)}")
    print(f"Description: {description}")
    print("=" * 20)


# Function to suggest a random book
def suggest_random_book(books_data):
    if 'items' in books_data:
        random_book = random.choice(books_data['items'])
        display_book_details(random_book)
    else:
        print("Sorry, no books found for your query.")


