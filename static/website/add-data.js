const ckie = getCookie('csrftoken');

const add_data = (event) => {
    event.preventDefault();
    const data = new FormData(event.target)
    $.ajax({
        url:`/api/v1/c-data/`,
        type: 'post',
        headers: {'X-CSRFToken': ckie},
        data: data,
        processData: false,
        contentType: false,
        beforeSend: () => {

        },
        success: () => {
            window.location.reload();
        },
        error: () => {

        },
        complete: () => {

        }
    })
}