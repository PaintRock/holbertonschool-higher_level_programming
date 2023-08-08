// Update the text color of the <header> element to red using jQuery
$.get("https://swapi-api.hbtn.io/api/films/?format=json", function(data) {
    data.results.forEach(function(movie) {
      $('#list_movies').append('<li>' + movie.title + '</li>');
    });
  });
  