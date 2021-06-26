$(function () {
    $('#leader-board').on('show.bs.modal', function (e) {
        var button = $(e.relatedTarget);
        var id = button.data('id');
        var url = button.data('url');
        var modal = $(this);
        var request = $.ajax({
            url: url,
            type: "GET",
            dataType: "html"
        });
        request.done(function (data) {
            modal.find('.loader').removeClass('d-flex').addClass('d-none');
            modal.find('.modal-body').append(data);
        });
        request.fail(function (jqXHR, textStatus) {
            console.log("Request Failed: "+textStatus);
        });
    });

    $('#leader-board').on('hide.bs.modal', function (e) {
        var modal = $(this);
        modal.find('.contest-details').remove();
        modal.find('.loader').removeClass('d-none').addClass('d-flex');
    });

    $('.join-contest').on('submit', function (e) {
        e.preventDefault();
        $('#checkout').modal('show');
        var frmData = $(this).serialize();
        var url = $(this).attr('action');
        var modal = $('#checkout');
        var request = $.ajax({
            type: "POST",
            url: url,
            data: frmData,
            dataType: "html"
        });
        request.done(function (data) {
            modal.find('.loader').removeClass('d-flex').addClass('d-none');
            modal.find('.modal-body').append(data);
        });
        request.fail(function (jqXHR, textStatus) {
            console.log("Request Failed: "+textStatus);
        });
    });

    $('#checkout').on('shown.bs.modal', function (e) {
       var fees = parseInt($('input[name="fees"]').val());
       var balance = parseInt($('input[name="balance"]').val());
       var paytm = $('.paytm-check');
       var wallet = $('.wallet-check');
       $('#wallet').change(function () {
           if($(this).prop("checked")){
               paytm.find('.amountToPay').removeClass('d-inline').addClass('d-none');
               wallet.find('.amountToPay').addClass('d-inline').removeClass('d-none');
               if (balance < fees){
                   console.log( 'enabled');
                   $('input#paytm').attr('disabled', false);
                   paytm.find('.amountToPay').text('₹ '+ (fees - balance));
                   paytm.find('.amountToPay').removeClass('d-none').addClass('.d-inline');
               } else {
                   console.log( 'disabled');
                   $('input#paytm').prop('checked', false);
                   $('input#paytm').attr('disabled', true);
               }
           } else{
               console.log( 'enabled');
               wallet.find('.amountToPay').removeClass('d-inline').addClass('d-none');
               paytm.find('.amountToPay').text('₹ '+ fees);
               paytm.find('.amountToPay').removeClass('d-none').addClass('.d-inline');
               $('input#paytm').attr('disabled', false );
               $('input#paytm').prop('checked', true);
           }
       });

    });

    $('#checkout, #wrong-time, #time-changed').on('hide.bs.modal', function (e) {
       location.reload();
    });
});
$('.navbar-toggler').click(function () {
   $(this).toggleClass('open');
});

$(function () {
    var st = srvTime();
    var srvtym = new Date(st);
    var time = new Date();
    console.log(srvtym+' === '+time);
    if (Math.abs(srvtym.getTime() - time.getTime()) > 60000){
        if(!($('#time-changed').hasClass('show'))){
            $('#wrong-time').modal('show');
        }
    }
});
function getTime()  {
    var d = new Date();
    return d.getTime();
}

function checkTime()  {
    if (Math.abs(getTime() - oldtime) > 60000)  {  // Changed by more than 2 seconds?
        if(!($('#wrong-time').hasClass('show'))) {
            $('#time-changed').modal('show');
        }
    }
    oldtime = getTime();
}

var oldtime = getTime();
setInterval(checkTime, 1000);  // Check every second that the time is not off