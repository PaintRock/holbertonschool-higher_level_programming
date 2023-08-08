// Update the text color of the <header> element to red using jQuery
// adds a click butoon that turns to red.
// updates the text color of HTML tag HEADER to red when the user
// clicks on the tag DIV#red_header
$.get('http://swapi.co/api/films?format=json', function (data) {
  for (film of data['results']) {
    $('#list_movies').append('<li>' + film['title'] + '</li>');
  }
});

