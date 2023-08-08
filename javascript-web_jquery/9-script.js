// Update the text color of the <header> element to red using jQuery
// adds a click butoon that turns to red.
// updates the text color of HTML tag HEADER to red when the user
// clicks on the tag DIV#red_header
const url = https://stefanbohacek.com/hellosalut/?lang=fr

$.get("https://stefanbohacek.com/hellosalut/?lang=fr", function(data) {
    $('#hello').text(data.hello);
  });
