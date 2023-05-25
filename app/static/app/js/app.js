"use strict";

$(function () { 
    $("#form").submit(function (submitEvent) { 
        let username = $("#username").val();
        let email = $("#email").val();
        let csrf = $("input[name=csrfmiddlewaretoken]").val();
        let data = new FormData();
        data.append("username", username);
        data.append("email", email);

        $.ajax({
            type: "POST",
            url: "/add/",
            data: data,
            processData: false,
            contentType: false,
            beforeSend: function(request) {
                request.setRequestHeader("X-CSRFToken", csrf);
            },
            success: function (xhr) {
                alert(`${xhr}`);
            },
            error: function (xhr) { 
                alert(`${xhr.status} - ${xhr.statusText}`);
            }
        });

        submitEvent.preventDefault();
    });
 });