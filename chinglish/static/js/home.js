$('.rewievs__slider').owlCarousel({
    loop: true,
    margin: 20,
    nav: true,
    dots: false,
    responsive: {
        0: {
            items: 1,
            dots: true,
            nav: false
        },
        600: {
            items: 1,
            dots: true,
            nav: false
        },
        1000: {
            items: 2
        }
    }
});
$('.cert').owlCarousel({
    loop: true,
    margin: 20,
    nav: true,
    dots: false,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 2
        },
        1000: {
            items: 3

        }
    }
})

$(document).ready(function () {
    let input_type_lesson = document.getElementById('id_type_lesson')
    let input_teacher = document.getElementById('id_teacher')
    let input_date = document.getElementById('id_date')
    let input_time = document.getElementById('id_time')
    CleanOption([input_type_lesson, input_teacher, input_date, input_time])
    input_type_lesson.options.length = 0;
    input_type_lesson.options[0] = new Option("Выберите вид занятия", null);
    let i = 1
    for (let lesson in available_type_lesson) {
        input_type_lesson.options[i] = new Option(available_type_lesson[lesson].name, lesson);
        i += 1
    }

    $('#id_type_lesson').on('change', function () {
        CleanOption([input_teacher, input_date, input_time])
        input_teacher.options[0] = new Option("Выберите преподавателя", null);
        let i = 1
        let available_teachers = available_type_lesson[$('#id_type_lesson').val()]['teachers']
        for (let teacher of available_teachers) {
            input_teacher.options[i] = new Option(teacher[1], teacher[0]);
            i += 1
        }
    })

    $('#id_teacher').on('change', function () {
        CleanOption([input_date, input_time])
        input_date.options[0] = new Option("Выберите дату", null);
        let i = 1
        let available_date = free_time_teachers[$('#id_teacher').val()]['free_time_record']
        for (let date in available_date) {
            input_date.options[i] = new Option(date, date);
            i += 1
        }
    })

    $('#id_date').on('change', function () {
        CleanOption([input_time])
        input_time.options[0] = new Option("Выберите время", null);
        let i = 1
        let available_time = free_time_teachers[$('#id_teacher').val()]['free_time_record'][$('#id_date').val()]
        for (let time of available_time) {
            input_time.options[i] = new Option(time[1], time[0]);
            i += 1
        }
    })

    $('.form-lesson').submit(function (event) {
        event.preventDefault();
        DeleteErrors()
        let $form = $(this);
        SendAjaxForm($form, $(this).attr('action'), $(this).attr('method'), ResponseFormTrialLesson).then()
        return false
    })
})

function ResponseFormTrialLesson($form, response) {
    if (response.status) {
        DeleteErrors()
        alert('Поздравляю с записью, скоро мы с вами свяжемся.')
        location.reload()
    } else {
        let errors = response.data['responseJSON']
        if (Object.keys(errors).length > 0) {
            ShowErrorsForm($form, errors)
        } else {
            alert('Ошибка сервера')
        }
    }
}
