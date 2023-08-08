// Update the text color of the <header> element to red using jQuery
  $.get("https://swapi-api.hbtn.io/api/people/5/?format=json", function(data) {
    $('#character').text(data.name);
  });
