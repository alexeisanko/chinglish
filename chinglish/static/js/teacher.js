$(document).ready(function () {
    $('.multi-field-wrapper').each(function() {
        var $wrapper = $('.multi-fields', this);
        $(".add-field", $(this)).click(function(e) {
            $('.multi-field:first-child', $wrapper).clone(true).appendTo($wrapper).find('input').val('').focus();
        });
        $('.multi-field .remove-field', $wrapper).click(function() {
            if ($('.multi-field', $wrapper).length > 1)
                $(this).parent('.multi-field').remove();
        });
    });
})

document.addEventListener('DOMContentLoaded', function () {
    let calendarEl = document.getElementById('calendar');
    RenderCalendar(calendarEl, lessons_json)
});


function RenderCalendar(calendarEl, events) {
    let calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        initialDate: new Date().toISOString().slice(0, 10),
        headerToolbar: {
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek,timeGridDay'
        },
        events: events,
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
    calendar.render();
}

function MakeNewEvent(date) {
    OpenModal('modal-lesson_management')
    $('#id_date').val(date)
    $('.date_lesson').text(date)
    CleanOption([input_type_lesson, input_time])
    input_type_lesson.options[0] = new Option("Выберите Вид занятия", null);
    let i = 1
    for (let type_lesson of type_lessons_json) {
        input_type_lesson.options[i] = new Option(type_lesson.type, type_lesson.id);
        i += 1
    }

}

function GetEvent(id_event) {
    $.ajax({
        type: 'GET',
        url: '/api/get_select_event/',
        dataType: 'json',
        data: {
            'id_event': id_event,
        },
        success: function (data) {
            let $modal = $('.modal__change-event')
            $modal.addClass('modal--visible');
            $modal.find($('.name_client')).text(data['client'])
            $modal.find($('.car_client')).text(data['car'])
            $modal.find($('.type_service')).text(data['service'])
            $modal.find($("[name='start_time_plan']")).val(data['start_plan'].slice(0, 16))
            $modal.find($("[name='end_time_plan']")).val(data['end_plan'].slice(0, 16))
            if (data['start_fact']) {
                $modal.find($("[name='start_time_fact']")).val(data['start_fact'].slice(0, 16))
            }
            if (data['end_fact']) {
                $modal.find($("[name='end_time_fact']")).val(data['end_fact'].slice(0, 16))
            }
            $modal.find($("[name='status']")).val(data['status_service'])
            $modal.find($("[name='worker']")).val(data['worker'])
            $modal.find($("[name='event_id']")).val(id_event)
            $modal.attr('data', id_event)
        },
    })
}

function GetWorkingConditions(date) {
    $.ajax({
        type: 'GET',
        url: '/api/get_working_conditions/',
        dataType: 'json',
        data: {
            'date': date.slice(0, 10),
        },
        success: function (data) {
            let $modal = $('.modal__change_work')
            $modal.addClass('modal--visible');
            $modal.find($('.modal__title')).text(`Условия работы ${date.slice(0, 10)}`)
            if (data) {
                console.log(data)
                $modal.find($("[name='open_time']")).val(data['open'])
                $modal.find($("[name='close_time']")).val(data['close'])
                $modal.find($("[name='discount']")).val(data['discount'])
            } else {
                $modal.find($("[name='open_time']")).val(none)
                $modal.find($("[name='close_time']")).val(none)
                $modal.find($("[name='discount']")).val(none)
            }
        },
    })
}



