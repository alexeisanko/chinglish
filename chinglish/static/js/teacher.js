$(document).ready(function () {

    $('.modal__close').click(function () {
        $('.modal-data').css('display', 'none');
        $('.modal-user-data').css('display', 'none');
        $('#modal-user_img').css('display', 'none');
        $('.data').css('display', 'none');
        DeleteErrors(true)
    });
    $('.data-btn').click(function () {
        $('.data').css('display', 'block');
    });
    $('.btn-change-data').click(function () {
        $('#modal-data').css('display', 'block');
        $('#modal-user_data').css('display', 'none');
        $('#modal-user_img').css('display', 'none');
        $('.data').css('display', 'none');
    });
    $('.btn-change-user-data').click(function () {
        $('#modal-user_data').css('display', 'block');
        $('#modal-data').css('display', 'none');
        $('#modal-user_img').css('display', 'none');
        $('.data').css('display', 'none');
    });
        $('.data__img').click(function () {
        $('#modal-user_img').css('display', 'block');
        $('#modal-data').css('display', 'none');
        $('#modal-user_data').css('display', 'none');
        $('.data').css('display', 'none');
    });

})
