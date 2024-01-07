const popularMoviesURL =
  "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=9edfed69bb5a893712fa46ffe01e882c";

const moviePosterBaseURL = "https://image.tmdb.org/t/p/w1280";
const searchMoviesURL =
  'https://api.themoviedb.org/3/search/movie?api_key=9edfed69bb5a893712fa46ffe01e882c&query="';

const mainContainer = document.getElementById("main");
const searchForm = document.getElementById("form");
const searchInput = document.getElementById("search");

getMovies(popularMoviesURL);

async function getMovies(url) {
  const response = await fetch(url);
  const movieData = await response.json();

  showMovies(movieData.results);
}

function showMovies(movies) {
  mainContainer.innerHTML = "";

  movies.forEach((movie) => {
    const { title, poster_path, vote_average, overview } = movie;

    const movieElement = document.createElement("div");
    movieElement.classList.add("movie");

    movieElement.innerHTML = `
    <div class="a">
      <img src="${moviePosterBaseURL + poster_path}" alt="${title}">
      <div class="movie-info">
        <h3>${title}</h3>
        <span class="${getClassByRate(vote_average)}">${vote_average}</span>
      </div>
      <div class="overview">
        <h3>Overview</h3>
        ${overview}
      </div></div>
    `;

    mainContainer.appendChild(movieElement);
  });
}

function getClassByRate(vote) {
  if (vote >= 8) {
    return "green";
  } else if (vote >= 5) {
    return "orange";
  } else {
    return "red";
  }
}

searchForm.addEventListener("submit", (event) => {
  event.preventDefault();

  const searchTerm = searchInput.value;

  if (searchTerm && searchTerm !== "") {
    getMovies(searchMoviesURL + searchTerm);

    searchInput.value = "";
  } else {
    window.location.reload();
  }
});
