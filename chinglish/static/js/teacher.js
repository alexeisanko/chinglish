$(document).ready(function () {
    $('.multi-field-wrapper').each(function () {
        var $wrapper = $('.multi-fields', this);
        $(".add-field", $(this)).click(function (e) {
            let next_field = $('.multi-field:last-child', $wrapper).clone(true).appendTo($wrapper).find('input').val('').focus();
            $(next_field[0]).attr('name', incrementString($(next_field[0]).attr('name')))
        });
        $('.text-flex .remove-field').click(function () {
            if ($('.multi-field', $wrapper).length > 1)
                $('.multi-field:last-child', $wrapper).remove();
        });
    });

    $('#modal-lesson_management, #modal-lesson_student').on("submit", "form", function (event) {
        console.log(event)
        event.preventDefault();
        DeleteErrors()
        let $form = $(this);
        SendAjaxForm($form, $(this).attr('action'), $(this).attr('method'), UpdateLessonInfo).then()
        return false
    })

    $('#modal-lesson_homework').on("submit", "form", function (event) {
        event.preventDefault();
        DeleteErrors()
        var fd = new FormData();
        let $form = $(this);
        for (let input of Object.values($form[0])) {
            if (input.files) {
                fd.append(input.files[0].name, input.files[0]);
            } else {
                fd.append(input.name, input.value);
            }
        }
        $.ajax({
            type: $(this).attr('method'),
            url: $(this).attr('action'),
            cache: false,
            contentType: false,
            processData: false,
            data: fd,
            success: function (data) {
                let full_data = {status: true, data: data}
                UpdateLessonInfo($form, full_data)
            },
            error: function (data) {
                let full_data = {status: false, data: data}
                UpdateLessonInfo($form, full_data)
            }
        })
        return false
    })

})

document.addEventListener('DOMContentLoaded', function () {
    let calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        initialDate: new Date().toISOString().slice(0, 10),
        headerToolbar: {
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek,timeGridDay'
        },
        events: lessons_json,
        navLinks: true,
        eventClick: function (info) {
            GetEvent(info.event.extendedProps.id_event)
        },
        dateClick: function (info) {
            MakeNewEvent(info.dateStr)

        },
        // navLinkDayClick: function (date) {
        //     GetWorkingConditions(date.toISOString())
        // }
    });
    window.currentCalendar = {calendar: calendar};
    currentCalendar.calendar.render();
});

function MakeNewEvent(date) {
    OpenModal('modal-lesson_management')
    $("#modal-lesson_management form").attr('action', `create_lesson/`)
    $('#id_date').val(date)
    $('.form_id_lesson').val(null)
    $('.form_id_student').val(null)
    $('.date_lesson').text(date)
    $('.link-homework-file').remove()
    $('.lesson-created, .text-flex').css('display', 'none')

    CleanOption([input_type_lesson, input_time])
    input_type_lesson.options[0] = new Option("Выберите Вид занятия", null);
    let i = 1
    for (let type_lesson of type_lessons_json) {
        input_type_lesson.options[i] = new Option(type_lesson.type, type_lesson.id);
        i += 1
    }
    $.ajax({
        type: 'get',
        url: `get_free_times/${date}/`,

        success: function (free_times) {
            input_time.options[0] = new Option("Выберите время", null);
            i = 1
            for (let free_time of free_times['free_time']) {
                input_time.options[i] = new Option(free_time.time, free_time.id);
                i += 1
            }
        },
        error: function (data) {
            console.log(data)
        }
    })

}

function GetEvent(id_event) {
    $.ajax({
        type: 'GET',
        url: `get_select_lesson/${id_event}`,
        dataType: 'json',
        success: function (data) {
            console.log(data)

            // Заполнение информации о студентах
            let $wrapper = $('.multi-fields', '#modal-lesson_student .modal-content form .multi-field-wrapper')
            while ($('.multi-field', $wrapper).length > 1) {
                $('.multi-field:last-child', $wrapper).remove();
            }
            $('.form_id_student').val(null)

            if (data['students'].length > 0) {
                let first_student = $('#modal-lesson_student .modal-content form .multi-field-wrapper .multi-field input')
                first_student.val(`${data['students'][0]['name']} id: ${data['students'][0]['id']}`)
            }
            let next_field
            for (let student of data['students'].slice(1)) {
                next_field = $('.multi-field:last-child', $wrapper).clone(true).appendTo($wrapper).find('input').val(`${student['name']} id: ${student['id']}`)
                $(next_field[0]).attr('name', incrementString($(next_field[0]).attr('name')))
            }


            // Заполнение информации о домашней работе
            $('.lesson-created').css('display', 'block')
            $('.text-flex').css('display', 'flex')
            $wrapper = $('.multi-fields', '#modal-lesson_homework .modal-content form .multi-field-wrapper')
            while ($('.multi-field', $wrapper).length > 1) {
                $('.multi-field:last-child', $wrapper).remove();
            }
            let url_file
            $('.link-homework-file').remove()
            for (let file of data.homework) {
                $(`<a href="/load_homework/${file.id}/" class="link-homework-file">${file.file}</a>`).appendTo($('.lesson-created'))
            }
            $('.form_id_homework').val(null)
                $('#id_homework_text').val(data['info_lesson']['homework_text'])


            OpenModal('modal-lesson_management')
            $('#id_date').val(data.info_lesson.start.slice(0, 10))
            $("#modal-lesson_management form").attr('action', `update_lesson/${id_event}/`)
            $('.form_id_lesson').val(data.info_lesson.id_event)
            $('#modal-lesson_student #id_form-0-lesson').val(data.info_lesson.id_event)
            $('#modal-lesson_homework #id_form-0-lesson').val(data.info_lesson.id_event)
            $('.date_lesson').text(data.info_lesson.start.slice(0, 10))

            CleanOption([input_type_lesson, input_time])
            let i = 0
            for (let type_lesson of type_lessons_json) {
                input_type_lesson.options[i] = new Option(type_lesson.type, type_lesson.id);
                i += 1
                if (data.info_lesson.title == input_type_lesson.options[i]) {
                    input_type_lesson.options[i].selected = true
                }
            }
            $.ajax({
                type: 'get',
                url: `get_free_times/${data.info_lesson.start.slice(0, 10)}/`,

                success: function (free_times) {
                    input_time.options[0] = new Option(data.info_lesson.start.slice(11, 16), data.info_lesson.id_time)
                    input_time.options[0].selected = true
                    i = 1
                    for (let free_time of free_times['free_time']) {
                        input_time.options[i] = new Option(free_time.time, free_time.id);
                        i += 1

                    }
                },
                error: function (data) {
                    console.log(data)
                }
            })
        },
        error: function (data) {
            alert('Проблемы на сервере, попробуйте позже')
        }
    })
}

function UpdateLessonInfo($form, response) {
    if (response.status) {
        DeleteErrors()
        CloseModal()
        if (response.data.info === 'visitors update') {
            alert("Студенты обновлены")
        } else if (response.data.info  === 'homework update') {
            alert("Домашняя работа обновлена")
        } else {
            location.reload()
        }
    } else {
        console.log(response)
        let errors = response.data['responseJSON']
        if (errors) {
            if (Object.keys(errors).length > 0) {
                ShowErrorsForm($form, errors, true)
            } else {
                alert('Ошибка сервера')
            }
        } else {
            alert('Ошибка сервера. Скорее всего вы ввели некорректного ученика.')
        }

    }
}

function incrementString(str) {
    return str.replace(/\d+/, s => (parseInt(s) + 1));
}
