$(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (resp, status) {
    if (status === 'success') {
      $('#sf_wind_speed').text(resp.query.results.channel.wind.speed);
    }
  });
});
