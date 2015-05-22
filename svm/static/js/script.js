$('form').on('submit', function(event){
    event.preventDefault();
    $.ajax({
        data : $(this).serialize(),
        url : $(this).attr('action'),
        type : "POST",
        beforeSend: function(xhr){
                xhr.setRequestHeader('X-CSRFToken',document.cookie.replace(/csrftoken=/,''))
            },
            
        success : function(json) {
            console.log(json);
            console.log("success");
        },

        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText);
        }
    });
});
