$(function () {
  $('#btn_translate').click(function () {
    const language_code = $('#language_code').val();
    $.get('https://www.fourtonfish.com/hellosalut/?'+$.param({ lang: language_code }), function (data, textStatus) {
      if (textStatus === 'success') {
        $('#hello').text(data.hello);
      } else {
        $('#hello').text('Invalid language code');
      }
    });
  });
});
