$(document).ready(function () {

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

    $('#modal-data').on("submit", "form", function (event) {
        event.preventDefault();
        DeleteErrors()
        let $form = $(this);
        SendAjaxForm($form, $(this).attr('action'), $(this).attr('method'), ResponseFormUpdateUserInfo).then()
        return false
    })

})

function ResponseFormUpdateUserInfo($form, response) {
    if (response.status) {
        DeleteErrors()
        location.reload()
    } else {
        let errors = response.data['responseJSON']
        if (Object.keys(errors).length > 0) {
            ShowErrorsForm($form, errors, true)
        } else {
            alert('Ошибка сервера')
        }
    }
}
