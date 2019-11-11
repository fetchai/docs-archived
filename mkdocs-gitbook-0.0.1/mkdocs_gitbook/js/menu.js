
$("#summary").children().children().not(".head").toggle();
$("#summary").on("click", ".header", function(event){
    console.log('clicked');
    $(this).children().not(".head").toggle();
    //$(this).find('*').hide();
    // $(this).next('li').next('li').toggle(200);
    // $(this).next('li').next('li').next('li').toggle(200);
    // $(this).next('li').next('li').next('li').next('ul').toggle(200);
});
