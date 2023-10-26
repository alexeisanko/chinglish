$(document).ready(function () {


    $('.change_homework_file').click(function () {
        OpenModal('change_homework_file')
        $('.data').css('display', 'none');
    });

    $('.change_visitors').click(function () {
        OpenModal('change_visitors')
        $('.data').css('display', 'none');
    });

    $('.create_update_lesson').click(function () {
        OpenModal('create_update_lesson')
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
