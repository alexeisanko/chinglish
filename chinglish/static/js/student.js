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
    });
    window.currentCalendar = {calendar: calendar};
    currentCalendar.calendar.render();
});


function GetEvent(id_event) {
    $.ajax({
        type: 'GET',
        url: `get_select_lesson/${id_event}`,
        dataType: 'json',
        success: function (data) {
            console.log(data)


            // Заполнение информации о домашней работе
            $('.lesson-created').css('display', 'block')
            let url_file
            $('.link-homework-file').remove()
            for (let file of data.homework) {
                $(`<a href="/load_homework/${file.id}/" class="link-homework-file">${file.file}</a>`).appendTo($('.lesson-created'))
            }

            OpenModal('modal-lesson_management')
            $('.type_lesson').text(data.info_lesson.title)
            $('.date_lesson').text(data.info_lesson.start.slice(0, 10))
            $('.time_lesson').text(data.info_lesson.start.slice(11, 16))
            $('.teacher_name').text(data.info_lesson.teacher)
            $('.homework_text').text(data.info_lesson.homework_text)
        },
        error: function (data) {
            alert('Проблемы на сервере, попробуйте позже')
        }
    })
}
