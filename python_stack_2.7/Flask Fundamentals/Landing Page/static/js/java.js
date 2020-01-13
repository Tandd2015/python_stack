$(document).ready(function(){

    alert("Hello!!! for the first time");

    $(document).on('click', '#1', function(){
        $('#2').html('<div><h5>' + 'Saying HELLO the Fourth time for fun' +'</h5></div>');
        alert('HELLO again again again!!! attached to the thrid time');

    });

});