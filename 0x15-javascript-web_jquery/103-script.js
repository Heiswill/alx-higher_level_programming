$('document').ready(function () {
    $("#btn_translate").click(translate);
    $("#language_code").keypress(function(e) {
        if (e.which === 13) {
            translate();
        }
    });

    function translate() {
        const languageCode = $("#language_code").val();
        $.getJSON(`https://fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function(data) {
            $("#hello").text(data.hello);
        });
    }
});
