
$(document).ready(function(){
    $('#id_name').on('blur', function(){
        var username = $(this).val();

        $.ajax({
                url: '/check_username/',
                data: {'username': username},
                type: 'GET',
                dataType: 'json',
                headers: {'X-CSRFToken': '{{ csrf_token }}'},  // Include CSRF token
            success: function(data){
                if(data.is_taken){
                    alert('This username is already taken. Please choose another one.');
                    // You can also update the UI to show an error message
                }
            }
        });
    });
});
