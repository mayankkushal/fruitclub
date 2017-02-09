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
//blog comment ajax
$(document).on('submit', '#comment-form', function(e){
    e.preventDefault();
    $.ajax({
      type:"POST",
      url:'/blog/add_comment',
      data:{
      comment:$("#id_comment").val(),
      pid:$("#pid").val(),
      csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
      },
      success:function(data){
          $('#id_comment').val('');
          $("#show_comm").append('<li><strong>' + data.user + "</strong> says: " + data.comment + '</li>');
          $("#no-comm").hide();
      },
    });
  });