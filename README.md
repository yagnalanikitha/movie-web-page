# movie-web-page
The Movie Search Web Application is a user-friendly platform designed to enhance the movie-watching experience. Built with Flask (Python), a lightweight web framework, the app provides core functionality for searching and managing movies. It uses Python for backend development to handle server-side logic and API interactions.
Project Overview
This project is a Movie Search Web Application developed using Flask and integrated with the TMDB (The Movie Database) API. The application allows users to search for movies, view detailed information, and manage a list of favorite movies. It features search functionality, movie details, genre-based movie listings, language-based movie listings, and a comprehensive list of movies.
setup instructions:
Create a Virtual Environment:python -m venv venv
Activate the Virtual Environment:venv\Scripts\activate
Install Required Packages:pip install Flask requests
Run the Flask Application:python app.py
Access the Application:Open web browser and navigate to http://127.0.0.1:5000
API Usage Details
TMDB API Key: Required for accessing the TMDB API.
Base URL: https://api.themoviedb.org/3
Approach to the Project:
1. Setting Up the Environment:
     Initial Setup: Begin by setting up a development environment using a framework Flask
     API Integration: Obtained an API key from TMDb and with the API endpoints that will be used, such as searching for movies and  retrieving movie details
2. Frontend Development:
     1 Search Functionality:
     Search Bar:Implementing a search bar on the homepage.
     frontend framework like HTML  to handle  search suggestions as the user types.
     TMDB_BASE_URL: This would typically be set to the base URL of the TMDb API, which is https://api.themoviedb.org/3. This is the root URL for all API requests to TMDb.
     /search/movie: This is the specific TMDb API endpoint used to search for movies by title.
     2 Favorites Feature:
     Add to Favorites: Implemented a feature allowing users to save movies to their favorites list.
     Ensuring  users can easily add and remove movies from their favorites.
     3 Movie Details Page:
     Detailed View: When a user selects a movie from the search results, redirect them to a detailed view page.
     /movie/{movie_id}:his is the specific TMDb API endpoint used to fetch detailed information about a movie.
     The {movie_id} is a placeholder for the unique identifier of the movie in the TMDb database.
     4 Language Selection Options:
     Created a dropdown menu  that allows users to select a language.
     The language codes are standardized according to ISO 639-1, which TMDb uses to identify languages.
     /discover/movie: This is the specific TMDb API endpoint used for discovering movies based on various criteria, including the original language of the movie.
     5 Genre Selection Options:
     Created a dropdown menu  that allows users to select a genre.
     Each option corresponds to a specific genre ( Action, Comedy, Drama,Horror,Romance,Fantasy).
     Defined a mapping between genre names and their corresponding genre IDs according to TMDb. TMDb provides a set of predefined genre
     action: 28,
     comedy: 35,
     drama: 18,
     horror: 27,
     romance: 10749
     6 Responsive Design:
     Designed the interface with mobile users in mind first and progressively enhance it for larger screens Using CSS.
     Cross-Device Compatibility: Tested the application on various devices and screen sizes to guarantee a consistent and accessible user experience.
3  Backend Development:
     1. Setup and Configuration:
        Created a Flask Application:
        Initialized a Flask application instance which will serve as the core of backend and handling routing
     2. API Configuration:
        Defined TMDb API base URL and API key.
        These will be constants will to make requests to the TMDb API.
     3. Define Routes and Views:
        Search Functionality:Implemented a route to handle movie searches. This route should accept a query parameter, make a request to the TMDb and render the search results.
        Movie Details:Created a route to fetch and display detailed information about a specific movie.
        Genre-Based Movies:Implement a route to fetch movies based on selected genres.
        Language-Based Movies:Added a route to fetch movies by language.
     4. Error Handling and Retries:
        Implement Error Handling:Used try and except blocks to handle potential errors during API requests, such as connection errors and ensure the application remains robust.
     5. Template Rendering:
        Create HTML Templates:Developed HTML templates for displaying search results, movie details, genre-based movies, and language-based movies.
        Ensure these templates are well-designed and user-friendly.
     6. Testing and Debugging:
       Test Routes:Thoroughly test all routes to ensure they correctly handle API requests and display the expected results.
4 Conclusion:
     The approach focuses on building a robust and user-friendly movie search application with essential features like search, movie details, and favorites management


















