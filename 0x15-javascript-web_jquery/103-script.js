$('document').ready(function () {
  $('INPUT#btn_translate').click(translate);
  $('INPUT#language_code').focus(function () {
    $(this).keydown(function (lan) {
      if (lan.keyCode === 13) {
        translate();
      }
    });
  });
});

function translate () {
  const api_url = 'https://www.fourtonfish.com/hellosalut/hello/';
  $.get(api_url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
    $('DIV#hello').html(data.hello);
  });
}
