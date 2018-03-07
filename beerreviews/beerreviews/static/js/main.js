$(document).ready(function(){
        let fadeInTime = 500
        // create sidebar and attach to menu open
        $('.ui.sidebar')
          .sidebar('attach events', '.toc.item')
        ;
        $('.beer-image').hide();
        $('.beer-image').fadeIn(fadeInTime);
        show_stars();

});

// Transforms the numerical value of divs to stars on a single beer page
function show_stars(){
  let div = $('.stars-container');
  if (div !=  null){
    div.each(function(index){
      let r = $(this).text()
      $(this).empty();
      for (let i = 0; i < 5; i++){
        if (i < r){
        $(this).append('<i class="fas fa-star"></i>');
        }
        else{
        $(this).append('<i class="far fa-star"></i>');
        }
      }
    });
  }
}
