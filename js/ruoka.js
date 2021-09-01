(function() {
    if ('content' in document.createElement('template')) {

        var main_content = document.querySelector("main-content");
        document.getElementById("p1").innerHTML = "New text!";
        var template = document.querySelector('#restaurant-template');
    
        // Clone the new row and insert it into the table
        var clone = template.content.cloneNode(true);
        var td = clone.querySelectorAll("menu-name");
        td[0].textContent = "1235646565";
    
        main_content.appendChild(clone);
    } else {
      // Find another way to add the rows to the table because
      // the HTML template element is not supported.
    }
})();