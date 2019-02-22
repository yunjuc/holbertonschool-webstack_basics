$(document).ready(() => {
  $('#update_header').click(() => {
    $('header').empty();
    $('header').append('New Header!!!');
  });
});
