$(document).ready(() => {
  $.get('https://swapi.co/api/people/5/?format=json').then((res) => {
    $('#character').append(res.name);
  });
});
