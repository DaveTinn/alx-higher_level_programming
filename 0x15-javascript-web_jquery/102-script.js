$('document').ready(function () {
  const api_url = 'https://www.fourtonfish.com/hellosalut/hello/'
  $('INPUT#btn_translate').click(function () {
    $.get(api_url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
      $('DIV#hello').html(data.hello);
    });
  });
});
