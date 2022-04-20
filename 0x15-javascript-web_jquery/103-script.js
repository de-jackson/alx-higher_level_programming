$(function () {
  $('#btn_translate').click(translate);
  $('#language_code').focus(function () {
    $(this).keyup(function (event) {
      if (event.keyCode === 13) {
        translate();
      }
    });
  });
});

function translate() {
  const language_code = $('#language_code').val();
  $.get('https://www.fourtonfish.com/hellosalut/?'+$.param({ lang: language_code }), function (data) {
    $('#hello').text(data.hello);
  });
}
