$(window).load(function(){
    $('.loader').fadeOut("slow");
});

$(function(){

	//add item
	$('#add_cart').click(function(e){
        var pid = $(this).attr('data-pid');
        var quantity = $('#qty').val();
        var csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            type: 'post',
            url: '/add_cart',
            data:{
                pid: pid,
                quantity: quantity,
                csrfmiddlewaretoken: csrfmiddlewaretoken,
            },
            success: function(){
                location.reload();
             }
        });      
    });
    //remove item
    $('.rem-item').click(function(event){
        var pid = $(event.currentTarget).attr('data-pid');
        var csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();
        $.get('/remove_item', {'pid':pid, 'csrfmiddlewaretoken':csrfmiddlewaretoken}, function(){
            location.reload();
        });   
    });
    //change quantity
    $('.chng-qty').click(function(event){
        var pid = 0
        pid = $(event.currentTarget).attr('data-pid');
        var id = "#prod"+pid;
        var qty = $(id).val();
        $.get('/change', {'pid':pid, 'qty':qty}, function(){
            location.reload();
        });
    });
    //not logged in
    $('#no-cart').click(function(){
        $('#not-logged').fadeTo(2000,500);
        $('#not-logged').fadeOut();
    });
});