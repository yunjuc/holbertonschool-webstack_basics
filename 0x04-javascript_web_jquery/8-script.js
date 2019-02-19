$(document).ready(() => {
  $.get('https://swapi.co/api/films/?format=json').then((res) => {
    res.results.forEach((result) => {
      $('#list_movies').append(`<li>${result.title}</li>`);
    });
  });
});
