document.addEventListener('DOMContentLoaded', function () {
    $('#start-time').attr('value', "")
    $('#end-time').attr('value', "")
    let calendarEl = document.getElementById('calendar');
    GetRecordingCalendar(calendarEl)
});


function GetRecordingCalendar(calendarEl) {
    let start_recording = new Date()
    start_recording.setDate(start_recording.getDate() + 1)
    let finish_recording = new Date()
    finish_recording.setDate(finish_recording.getDate() + 60)
    let calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        initialDate: start_recording.toISOString().slice(0, 10),
        headerToolbar: {
            left: 'today',
            center: 'title',
            right: 'prev,next'
        },
        events: [
            {
                start: start_recording.toISOString().slice(0, 10),
                end: finish_recording.toISOString().slice(0, 10),
                overlap: false,
                display: 'inverse-background',
            },
        ],
        eventColor: '#2c3e50',
        dateClick: function (info) {
            if (Date.parse(info.dateStr) >= Date.parse(start_recording.toISOString().slice(0, 10)) && Date.parse(info.dateStr) < Date.parse(finish_recording.toISOString().slice(0, 10))) {
                FreeTime(info.dateStr, calendarEl)
            }
        },
    });
    calendar.render();
}

