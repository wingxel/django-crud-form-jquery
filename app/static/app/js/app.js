"use strict";

function myAjax(data, url, method, csrf_token, nextUrl="/") {
    $.ajax({
        type: method,
        url: url,
        data: data,
        processData: false,
        contentType: false,
        beforeSend: function (request) {
            request.setRequestHeader("X-CSRFToken", csrf_token);
        },
        success: function (xhr) {
            location.assign(nextUrl);
        },
        error: function (xhr) {
            alert(`Error ${xhr.status} - ${xhr.statusText}`);
        }
    });
}

$(function () {

    let csrf = $("input[name=csrfmiddlewaretoken]").val();

    $("#add_form").submit(function (submitEvent) {
        let username = $("#username").val();
        let email = $("#email").val();
        let data = new FormData();
        data.append("username", username);
        data.append("email", email);

        myAjax(data, "/add/", "POST", csrf, "/?a=create");

        submitEvent.preventDefault();
    });

    $("#delete_form").submit(function (submitEvent) {
        let id = $("#id").val();
        let data = new FormData();
        data.append("id", id);

        myAjax(data, "/delete/", "POST", csrf, "/?a=delete");

        submitEvent.preventDefault();
    });

    $("#update_form").submit(function (submitEvent) {
        let id = $("#update_id").val();
        let newUsername = $("#update_uname").val();
        let newEmail = $("#update_email").val();

        if (newUsername.length === 0 && newEmail.length == 0) {
            alert("Provide at least one value to update");
        } else {
            let data = new FormData();
            data.append("id", id);
            data.append("username", newUsername);
            data.append("email", newEmail);

            myAjax(data, "/update/", "POST", csrf, "/?a=update");
        }

        submitEvent.preventDefault();
    });

    $("#create").click(function (clickEvent) { 
        $("#crt").show();
        $("#del, #upd").hide();
        clickEvent.preventDefault();
    });

    $("#update").click(function (clickEvent) { 
        $("#upd").show();
        $("#crt, #del").hide();
        clickEvent.preventDefault();
    });

    $("#delete").click(function (clickEvent) { 
        $("#del").show();
        $("#crt, #upd").hide();
        clickEvent.preventDefault();
    });

    if (window.location.href.indexOf("?q=") > -1) {
        $("#create, #update, #delete").hide();
    }

    if (window.location.href.indexOf("?a=update") > -1) {
        $("#update").trigger("click");
    } else if (window.location.href.indexOf("?a=delete") > -1) {
        $("#delete").trigger("click");
    }

    $("#navbarSupportedContent").on("show.bs.collapse", () =>
        $("a.nav-link").click(() => $("#navbarSupportedContent").collapse("hide"))
    );

});