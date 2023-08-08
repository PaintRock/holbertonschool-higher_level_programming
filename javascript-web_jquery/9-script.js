// Update the text color of the <header> element to red using jQuery
$.get("https://stefanbohacek.com/hellosalut/?lang=fr", function(data) {
    $('#hello').text(data.hello);
  });
