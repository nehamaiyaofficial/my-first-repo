cdnvjfdvnkdjfvndkfkdnvd// ================================
// FRONTEND REPOSITORY - BEGINNER LEVEL
// ================================

// Branch: html-pages
// File: index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Travel Planner - Find Your Dream Destination</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>🌍 Travel Planner</h1>
        <nav>
            <a href="index.html">Home</a>
            <a href="search.html">Search</a>
            <a href="login.html">Login</a>
        </nav>
    </header>

    <main>
        <section class="hero">
            <h2>Find Your Next Adventure!</h2>
            <p>Discover amazing places around the world</p>
            
            <div class="search-box">
                <input type="text" id="destination" placeholder="Where do you want to go?">
                <button onclick="searchDestination()">Search</button>
            </div>
        </section>

        <section class="popular-places">
            <h3>Popular Destinations</h3>
            <div class="places-grid">
                <div class="place-card">
                    <img src="https://via.placeholder.com/200x150/4285f4/ffffff?text=Paris" alt="Paris">
                    <h4>Paris, France</h4>
                    <p>$500 per person</p>
                    <button class="book-btn">View Details</button>
                </div>
                
                <div class="place-card">
                    <img src="https://via.placeholder.com/200x150/34a853/ffffff?text=Tokyo" alt="Tokyo">
                    <h4>Tokyo, Japan</h4>
                    <p>$800 per person</p>
                    <button class="book-btn">View Details</button>
                </div>
                
                <div class="place-card">
                    <img src="https://via.placeholder.com/200x150/ea4335/ffffff?text=London" alt="London">
                    <h4>London, UK</h4>
                    <p>$600 per person</p>
                    <button class="book-btn">View Details</button>
                </div>
            </div>
        </section>
    </main>

    <footer>
        <p>&copy; 2024 Travel Planner. Made by Sarah (Frontend Developer)</p>
    </footer>

    <script src="main.js"></script>
</body>
</html>

// File: search.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Search Destinations - Travel Planner</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>🌍 Travel Planner</h1>
        <nav>
            <a href="index.html">Home</a>
            <a href="search.html">Search</a>
            <a href="login.html">Login</a>
        </nav>
    </header>

    <main>
        <h2>Search for Your Perfect Trip</h2>
        
        <form class="search-form">
            <div class="form-group">
                <label for="where">Where do you want to go?</label>
                <input type="text" id="where" name="where" placeholder="Enter city or country">
            </div>
            
            <div class="form-group">
                <label for="when">When do you want to travel?</label>
                <input type="date" id="when" name="when">
            </div>
            
            <div class="form-group">
                <label for="budget">What's your budget?</label>
                <select id="budget" name="budget">
                    <option value="">Choose budget</option>
                    <option value="low">Under $500</option>
                    <option value="medium">$500 - $1000</option>
                    <option value="high">Over $1000</option>
                </select>
            </div>
            
            <button type="button" onclick="doSearch()">Find Trips</button>
        </form>

        <div id="search-results">
            <!-- Results will appear here -->
        </div>
    </main>

    <script src="search.js"></script>
</body>
</html>

// File: login.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - Travel Planner</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>🌍 Travel Planner</h1>
        <nav>
            <a href="index.html">Home</a>
            <a href="search.html">Search</a>
            <a href="login.html">Login</a>
        </nav>
    </header>

    <main>
        <div class="login-container">
            <h2>Login to Your Account</h2>
            
            <form class="login-form">
                <div class="form-group">
                    <label for="email">Email:</label>
                    <input type="email" id="email" required>
                </div>
                
                <div class="form-group">
                    <label for="password">Password:</label>
                    <input type="password" id="password" required>
                </div>
                
                <button type="button" onclick="loginUser()">Login</button>
            </form>
            
            <p>Don't have an account? <a href="#" onclick="showSignup()">Sign up here</a></p>
        </div>
    </main>

    <script>
        function loginUser() {
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            
            if (email && password) {
                alert('Login successful! (This is just a demo)');
            } else {
                alert('Please fill in all fields');
            }
        }
        
        function showSignup() {
            alert('Signup feature coming soon!');
        }
    </script>
</body>
</html>

// ================================
// Branch: css-styling
// File: style.css
/* Basic CSS for beginners */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
}

/* Header */
header {
    background-color: #2196F3;
    color: white;
    padding: 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

header h1 {
    font-size: 1.5rem;
}

nav a {
    color: white;
    text-decoration: none;
    margin: 0 10px;
    padding: 5px 10px;
    border-radius: 3px;
}

nav a:hover {
    background-color: rgba(255, 255, 255, 0.2);
}

/* Main content */
main {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

/* Hero section */
.hero {
    text-align: center;
    padding: 40px 20px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border-radius: 10px;
    margin-bottom: 40px;
}

.hero h2 {
    font-size: 2.5rem;
    margin-bottom: 10px;
}

.hero p {
    font-size: 1.2rem;
    margin-bottom: 30px;
}

/* Search box */
.search-box {
    display: flex;
    justify-content: center;
    gap: 10px;
    max-width: 500px;
    margin: 0 auto;
}

.search-box input {
    flex: 1;
    padding: 12px;
    border: none;
    border-radius: 25px;
    font-size: 16px;
}

.search-box button {
    padding: 12px 24px;
    background-color: #ff6b6b;
    color: white;
    border: none;
    border-radius: 25px;
    cursor: pointer;
    font-size: 16px;
}

.search-box button:hover {
    background-color: #ff5252;
}

/* Popular places */
.popular-places h3 {
    text-align: center;
    font-size: 2rem;
    margin-bottom: 30px;
    color: #333;
}

.places-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
}

.place-card {
    background: white;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    overflow: hidden;
    transition: transform 0.3s ease;
}

.place-card:hover {
    transform: translateY(-5px);
}

.place-card img {
    width: 100%;
    height: 150px;
    object-fit: cover;
}

.place-card h4 {
    padding: 15px;
    font-size: 1.3rem;
    color: #333;
}

.place-card p {
    padding: 0 15px;
    color: #666;
    font-size: 1.1rem;
}

.book-btn {
    width: 100%;
    padding: 15px;
    background-color: #4CAF50;
    color: white;
    border: none;
    cursor: pointer;
    font-size: 16px;
}

.book-btn:hover {
    background-color: #45a049;
}

/* Forms */
.search-form, .login-form {
    background: white;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    max-width: 500px;
    margin: 0 auto;
}

.form-group {
    margin-bottom: 20px;
}

.form-group label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
}

.form-group input,
.form-group select {
    width: 100%;
    padding: 10px;
    border: 2px solid #ddd;
    border-radius: 5px;
    font-size: 16px;
}

.form-group input:focus,
.form-group select:focus {
    border-color: #2196F3;
    outline: none;
}

.search-form button,
.login-form button {
    width: 100%;
    padding: 12px;
    background-color: #2196F3;
    color: white;
    border: none;
    border-radius: 5px;
    font-size: 16px;
    cursor: pointer;
}

.search-form button:hover,
.login-form button:hover {
    background-color: #1976D2;
}

/* Login container */
.login-container {
    max-width: 400px;
    margin: 50px auto;
}

.login-container h2 {
    text-align: center;
    margin-bottom: 30px;
    color: #333;
}

.login-container p {
    text-align: center;
    margin-top: 20px;
}

.login-container a {
    color: #2196F3;
    text-decoration: none;
}

.login-container a:hover {
    text-decoration: underline;
}

/* Footer */
footer {
    background-color: #333;
    color: white;
    text-align: center;
    padding: 20px;
    margin-top: 50px;
}

/* Search results */
#search-results {
    margin-top: 30px;
}

.result-item {
    background: white;
    padding: 20px;
    margin-bottom: 15px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

// File: colors.css
/* Simple color scheme for beginners */
:root {
    --primary-blue: #2196F3;
    --secondary-purple: #667eea;
    --accent-red: #ff6b6b;
    --success-green: #4CAF50;
    --text-dark: #333;
    --text-light: #666;
    --background-light: #f5f5f5;
    --white: #ffffff;
}

/* You can use these colors like this: */
/* background-color: var(--primary-blue); */

// ================================
// Branch: javascript-basics
// File: main.js
// Simple JavaScript for beginners

// Function to search for destinations
function searchDestination() {
    const destination = document.getElementById('destination').value;
    
    if (destination === '') {
        alert('Please enter a destination!');
        return;
    }
    
    // Simple search - in real app, this would call the backend
    alert('Searching for trips to ' + destination + '...');
    
    // Redirect to search page (simple way)
    window.location.href = 'search.html';
}

// Function to show place details
function showPlaceDetails(placeName) {
    alert('Showing details for ' + placeName + '\n\nThis feature is coming soon!');
}

// Make buttons work when page loads
document.addEventListener('DOMContentLoaded', function() {
    console.log('Travel Planner website loaded!');
    
    // Add click events to all "View Details" buttons
    const bookButtons = document.querySelectorAll('.book-btn');
    bookButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            const placeCard = button.closest('.place-card');
            const placeName = placeCard.querySelector('h4').textContent;
            showPlaceDetails(placeName);
        });
    });
});

// Simple function to change page title
function updatePageTitle(newTitle) {
    document.title = newTitle + ' - Travel Planner';
}

// Function to show welcome message
function showWelcomeMessage() {
    const hour = new Date().getHours();
    let greeting;
    
    if (hour < 12) {
        greeting = 'Good morning';
    } else if (hour < 18) {
        greeting = 'Good afternoon';
    } else {
        greeting = 'Good evening';
    }
    
    console.log(greeting + '! Welcome to Travel Planner!');
}

// Call welcome message when page loads
showWelcomeMessage();

// File: search.js
// JavaScript for search page

function doSearch() {
    const where = document.getElementById('where').value;
    const when = document.getElementById('when').value;
    const budget = document.getElementById('budget').value;
    
    // Check if user filled in the form
    if (!where) {
        alert('Please enter where you want to go!');
        return;
    }
    
    // Simple search results (fake data for beginners)
    const results = [
        {
            name: where + ' Adventure Tour',
            price: '$' + (Math.floor(Math.random() * 1000) + 200),
            description: 'Amazing trip to ' + where + ' with great activities!'
        },
        {
            name: where + ' Cultural Experience',
            price: '$' + (Math.floor(Math.random() * 800) + 300),
            description: 'Explore the culture and history of ' + where
        },
        {
            name: where + ' Relaxation Package', 
            price: '$' + (Math.floor(Math.random() * 1200) + 400),
            description: 'Relax and unwind in beautiful ' + where
        }
    ];
    
    displayResults(results);
}

function displayResults(results) {
    const resultsDiv = document.getElementById('search-results');
    
    if (results.length === 0) {
        resultsDiv.innerHTML = '<p>No trips found. Try searching for something else!</p>';
        return;
    }
    
    let html = '<h3>We found ' + results.length + ' trips for you:</h3>';
    
    results.forEach(function(result) {
        html += `
            <div class="result-item">
                <h4>${result.name}</h4>
                <p>${result.description}</p>
                <p><strong>Price: ${result.price}</strong></p>
                <button onclick="bookTrip('${result.name}')">Book This Trip</button>
            </div>
        `;
    });
    
    resultsDiv.innerHTML = html;
}

function bookTrip(tripName) {
    alert('Booking trip: ' + tripName + '\n\nThis will connect to the booking system soon!');
}

// Clear results when page loads
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('search-results').innerHTML = '';
});

// ================================
// Branch: responsive-mobile
// File: mobile.css
/* Simple mobile styles for beginners */

/* Mobile phones (up to 768px) */
@media screen and (max-width: 768px) {
    
    /* Make header work on mobile */
    header {
        flex-direction: column;
        text-align: center;
        padding: 15px;
    }
    
    header h1 {
        margin-bottom: 10px;
    }
    
    nav {
        display: flex;
        justify-content: center;
        gap: 10px;
    }
    
    /* Make main content fit on mobile */
    main {
        padding: 10px;
    }
    
    /* Make hero section work on mobile */
    .hero {
        padding: 20px 15px;
    }
    
    .hero h2 {
        font-size: 1.8rem;
    }
    
    .hero p {
        font-size: 1rem;
    }
    
    /* Make search box work on mobile */
    .search-box {
        flex-direction: column;
        width: 100%;
    }
    
    .search-box input,
    .search-box button {
        width: 100%;
        margin-bottom: 10px;
    }
    
    /* Make place cards work on mobile */
    .places-grid {
        grid-template-columns: 1fr;
        gap: 15px;
    }
    
    /* Make forms work on mobile */
    .search-form,
    .login-form {
        padding: 20px 15px;
        margin: 10px;
    }
    
    /* Make buttons bigger for mobile */
    .book-btn,
    .search-form button,
    .login-form button {
        padding: 15px;
        font-size: 18px;
    }
}

/* Small mobile phones (up to 480px) */
@media screen and (max-width: 480px) {
    
    .hero h2 {
        font-size: 1.5rem;
    }
    
    .popular-places h3 {
        font-size: 1.5rem;
    }
    
    .place-card h4 {
        font-size: 1.1rem;
    }
    
    /* Make navigation easier on small screens */
    nav a {
        padding: 8px 12px;
        font-size: 14px;
    }
}

/* Tablets (769px to 1024px) */
@media screen and (min-width: 769px) and (max-width: 1024px) {
    
    .places-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 20px;
    }
    
    .search-box {
        max-width: 600px;
    }
}

/* Simple package.json for beginners */
{
  "name": "travel-planner-frontend",
  "version": "1.0.0",
  "description": "Simple travel planner website - Frontend by Sarah",
  "main": "index.html",
  "scripts": {
    "start": "echo 'Open index.html in your browser!'",
    "test": "echo 'No tests yet - learning step by step!'"
  },
  "keywords": ["travel", "planner", "beginner", "html", "css", "javascript"],
  "author": "Sarah (Frontend Developer - Beginner)",
  "license": "MIT"
}
