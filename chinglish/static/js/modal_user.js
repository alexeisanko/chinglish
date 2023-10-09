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

    $('#modal-data').on("submit", "form", function () {
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
                location.reload()
            },
            error: function (data) {
                console.log(data)
                let response = data['responseJSON']
                if (Object.keys(response).length > 0) {
                    let field
                    let message
                    for (let error in response) {
                        field = $form.find($(`[name='${error}']`))
                        field.addClass('input--error')
                        message = field.next()
                        message.text(response[error]).addClass('span--error')
                    }
                    $form.parent('div').parent('div').addClass('modal__dialog--error')
                } else {
                    alert('Ошибка сервера')
                }
            }
        })
        return false
    })

    function DeleteErrors(close_modal = false) {
        $(':input').removeClass('input--error')
        $('.error-message').text("").removeClass('span--error')
        $('.modal').removeClass('modal__dialog--error')
        if (close_modal) {
            $('.modal').removeClass('modal--visible')
        }
    }

    function MessageEvent(event) {
        $('.modal__message').addClass('modal--visible');
        $('.text-message-modal').text(event['msg'])
    }
})
