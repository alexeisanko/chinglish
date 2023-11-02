$(document).ready(function () {


    $('#modal-account_data, #modal-user_data').on("submit", "form", function (event) {
        event.preventDefault();
        DeleteErrors()
        let $form = $(this);
        SendAjaxForm($form, $(this).attr('action'), $(this).attr('method'), ResponseFormUpdateUserInfo).then()
        return false
    })

})

function ResponseFormUpdateUserInfo($form, response) {
    console.log(response)
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
