$(document).ready(function() {
    $('#song').select2({
        placeholder: 'Select a song',
        allowClear: true,
        ajax: {
            url: '/get_songs',
            dataType: 'json',
            delay: 250,
            data: function (params) {
                return {
                    q: params.term // search term
                };
            },
            processResults: function (data) {
                return {
                    results: data
                };
            },
            cache: true
        },
        minimumInputLength: 1
    });
});