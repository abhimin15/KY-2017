
//CONTACT FORM VALIDATION
$(document).ready(function() {

    "use strict";

    $(".form_submit").click(function() {

        "use strict";

        
        var emaild = $("#email").val();
        var testEmail = /^[A-Z0-9._%+-]+@([A-Z0-9-]+\.)+[A-Z]{2,4}$/i;
        if (emaild) {
            if (testEmail.test(emaild)) {
                $(".field_wrap .form_email").addClass("color_email");
            } else {
                $(".field_wrap .form_email").removeClass("color_email");
                
            }
        }
    });
});
