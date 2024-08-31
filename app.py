import time
import requests
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Secret key for session management

# TMDB API Configuration
TMDB_API_KEY = '888ad08f9ddebe86bcf570efc4e7949c'
TMDB_BASE_URL = 'https://api.themoviedb.org/3'

# Initialize session storage for favorites
def init_favorites():
    if 'favorites' not in session:
        session['favorites'] = []

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Search movies
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if query:
        response = requests.get(f'{TMDB_BASE_URL}/search/movie', params={'api_key': TMDB_API_KEY, 'query': query})
        movies = response.json().get('results', [])
        return render_template('search_results.html', movies=movies, query=query)
    return redirect(url_for('index'))

# Movie details route
@app.route('/movie/<int:movie_id>')
def movie_details(movie_id):
    response = requests.get(f'{TMDB_BASE_URL}/movie/{movie_id}', params={'api_key': TMDB_API_KEY, 'append_to_response': 'videos,credits'})
    movie = response.json()
    return render_template('movie_details.html', movie=movie)

# Add movie to favorites
@app.route('/add_favorite/<int:movie_id>', methods=['POST'])
def add_favorite(movie_id):
    init_favorites()
    movie_title = request.form.get('movie_title')
    if movie_id not in [fav['id'] for fav in session['favorites']]:
        session['favorites'].append({'id': movie_id, 'title': movie_title})
        session.modified = True  # Mark session as modified
    return redirect(url_for('favorites'))

# View favorites
@app.route('/favorites')
def favorites():
    init_favorites()
    return render_template('favorites.html', favorites=session['favorites'])

# Remove movie from favorites
@app.route('/remove_favorite/<int:movie_id>', methods=['POST'])
def remove_favorite(movie_id):
    init_favorites()
    session['favorites'] = [fav for fav in session['favorites'] if fav['id'] != movie_id]
    session.modified = True  # Mark session as modified
    return redirect(url_for('favorites'))

# Movies by Genre
@app.route('/movies/<string:genre_name>')
def movies_by_genre(genre_name):
    genre_map = {
        'action': 28,
        'comedy': 35,
        'horror': 27,
        'romantic': 10749,
        'drama': 18,
        'sci-fi': 878,
        'fantasy': 14,
    }
    
    genre_id = genre_map.get(genre_name.lower())
    if genre_id:
        movies = []
        max_retries = 3
        for page in range(1, 6):  # Fetch up to 5 pages of results
            for attempt in range(max_retries):
                try:
                    response = requests.get(f'{TMDB_BASE_URL}/discover/movie', 
                                            params={'api_key': TMDB_API_KEY, 'with_genres': genre_id, 'page': page})
                    response.raise_for_status()  # Raise an error for bad status codes
                    movies.extend(response.json().get('results', []))
                    break  # If successful, break out of retry loop
                except requests.exceptions.ConnectionError as e:
                    if attempt < max_retries - 1:
                        time.sleep(2)  # Wait before retrying
                    else:
                        print(f"Failed to retrieve page {page} for genre {genre_name}: {e}")
                        return redirect(url_for('index'))

        return render_template('genre_movies.html', movies=movies, genre_name=genre_name.capitalize())

    return redirect(url_for('index'))
@app.route('/language/<string:language_code>')
def movies_by_language(language_code):
    language_map = {
        'hindi': 'hi',
        'telugu': 'te',
    }
    
    language = language_map.get(language_code.lower())
    if language:
        movies = []
        max_retries = 3
        for page in range(1, 6):  # Fetch up to 5 pages of results
            for attempt in range(max_retries):
                try:
                    response = requests.get(f'{TMDB_BASE_URL}/discover/movie', 
                                            params={'api_key': TMDB_API_KEY, 'with_original_language': language, 'page': page})
                    response.raise_for_status()  # Raise an error for bad status codes
                    movies.extend(response.json().get('results', []))
                    break  # If successful, break out of retry loop
                except requests.exceptions.ConnectionError as e:
                    if attempt < max_retries - 1:
                        time.sleep(2)  # Wait before retrying
                    else:
                        print(f"Failed to retrieve page {page} for language {language_code}: {e}")
                        return redirect(url_for('index'))

        return render_template('language_movies.html', movies=movies, language_code=language_code.capitalize())

    return redirect(url_for('index'))

# All Movies
@app.route('/movies')
def all_movies():
    movies = []
    for page in range(1, 51):  # 50 pages with 20 results each = 1000 movies
        response = requests.get(f'{TMDB_BASE_URL}/discover/movie', 
                                params={'api_key': TMDB_API_KEY, 'page': page})
        movies.extend(response.json().get('results', []))

    return render_template('movie_list.html', movies=movies)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)




