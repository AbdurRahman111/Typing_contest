    // open profile on hover
    $( document ).ready(function() {
        $(".dropdown").mouseenter(function(){
            $(".dropdown-menu").addClass('show');
        });
        $(".dropdown-menu").mouseleave(function(){
            $(".dropdown-menu").removeClass('show');
        }); 
    });