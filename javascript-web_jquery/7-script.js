// Update the text color of the <header> element to red using jQuery
// adds a click butoon that turns to red.
// updates the text color of HTML tag HEADER to red when the user
// clicks on the tag DIV#red_header
$.get('http://swapi.co/api/people/5/?format=json', function (data) {
  $('#character').text(data.name);
});

