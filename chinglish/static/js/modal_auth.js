$(document).ready(function () {

    $('.header .auth').click(function () {
        OpenModal('modal-auth')
    });
    $('.modal-auth span').click(function () {
        OpenModal('modal-reg');
    });
    $('.modal-reg span').click(function () {
        OpenModal('modal-auth')
    });

    $('.modal-auth, .modal-reg').on("submit", "form", function () {
        DeleteErrors()
        let $form = $(this);
        $.ajax({
            type: $(this).attr('method'),
            url: $(this).attr('action'),
            dataType: 'json',
            data: $form.serialize(),
            success: function (data) {
                console.log(data)
                DeleteErrors()
                location.replace(data.location)


            },
            error: function (data) {
                let response = data['responseJSON']['form']
                let errors_fields = GetErrorsField(response['fields'])
                if (response['errors'].length > 0) {
                    $('.form-error').text(response['errors'][0]).addClass('span--error')
                    $form.parent('div').parent('div').addClass('modal__dialog--error')
                } else if (Object.keys(errors_fields).length > 0) {
                    let field
                    let message
                    for (let error in errors_fields) {
                        field = $form.find($(`[name='${error}']`))
                        field.addClass('input--error')
                        message = field.next()
                        message.text(errors_fields[error]).addClass('span--error')
                    }
                    $form.parent('div').parent('div').addClass('modal__dialog--error')
                } else {
                    alert('Ошибка сервера')
                }
            }
        })
        return false
    })

    function GetErrorsField(fields) {
        let errors = {}
        for (let field in fields) {
            if (fields[field]['errors'].length !== 0) {

                errors[field] = fields[field]['errors'][0]
            }
        }
        return errors
    }

})
