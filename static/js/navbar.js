//For navbar, changes from a transparent background to white background on scroll
$(document).ready(function() {
  $(window).scroll(function() {
    if($(this).scrollTop() < $("#main-content").height()){
       $(".navbar").removeClass("bg-light");
    }
    else{
       $(".navbar").addClass("bg-light");
    }
  });
});
