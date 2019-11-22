
$(document).ready(function() {

    function check() { 
        var navBarMotto = document.getElementById("motto"); 
        var curOverf = navBarMotto.style.overflow; 
        console.log(curOverf);
          
        if ( !curOverf || curOverf === "visible" ) 
            navBarMotto.style.overflow = "hidden"; 
          
        var isOverflowing = navBarMotto.clientWidth < navBarMotto.scrollWidth
            || navBarMotto.clientHeight < navBarMotto.scrollHeight; 
          
        navBarMotto.style.overflow = curOverf; 
        
    } 

    check();

    function openInNewTab(url) {
        var win = window.open(url, '_blank');
        win.focus();
    }   

});
