$(document).ready(function(){
    $('#ml').on('submit', function(event){
        event.preventDefault();
        $.ajax({
            data : $(this).serialize(),
            url : '/questionnaire/',
            type : "POST",
            beforeSend: function(xhr){
                    xhr.setRequestHeader('X-CSRFToken',document.cookie.replace(/csrftoken=/,''))
                },
                
            success : function(json) {
                console.log('success');
                $('#name').text(json.name);
                $('#prediction').text(json.prediction)
                $('#result').modal('show');
            },

            error : function(xhr,errmsg,err) {
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
    });
});