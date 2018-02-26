$(document).ready(function(){
        let fadeInTime = 500
        // create sidebar and attach to menu open
        $('.ui.sidebar')
          .sidebar('attach events', '.toc.item')
        ;
        $('.beer-image').hide();
        $('.beer-image').fadeIn(fadeInTime);
});
