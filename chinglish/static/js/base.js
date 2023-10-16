$(document).ready(function () {
    $('.mask-phone').mask("+7 (999) 999-99-99")

    $('.modal__close').click(function () {
        $('.modal').css('display', 'none');
        DeleteErrors(true)
    });
})

async function SendAjaxForm(ajax_form, url, method, next_func, data_type = 'json') {
    $.ajax({
        type: method,
        url: url,
        dataType: data_type,
        data: ajax_form.serialize(),
        success: function (data) {
            let full_data = {status: true, data: data}
            next_func(ajax_form, full_data)
        },
        error: function (data) {
            let full_data = {status: false, data: data}
            next_func(ajax_form, full_data)
        }
    })
    return false
}

function CleanOption(input_fields) {
    for (let field of input_fields) {
        field.options.length = 0;
    }
}

function DeleteErrors(close_modal = false) {
    $(':input').removeClass('input--error')
    $('.error-message').text("").removeClass('span--error')
    $('.modal').removeClass('modal__dialog--error')
    if (close_modal) {
        $('.modal').removeClass('modal--visible')
    }
}

function ShowErrorsForm($form, errors, is_modal= false) {
    let field
    let message
    for (let error in errors) {
        field = $form.find($(`[name='${error}']`))
        field.addClass('input--error')
        message = field.next()
        message.text(errors[error]).addClass('span--error')
    }
    if (is_modal) {
        $form.parent('div').parent('div').addClass('modal__dialog--error')
    }
}
