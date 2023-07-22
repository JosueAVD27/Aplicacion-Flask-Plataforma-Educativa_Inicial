//Formato de correo electronico
var expr = /^[a-zA-Z0-9_\.\-]+@[a-zA-Z0-9\-]+\.[a-zA-Z0-9\-\.]+$/;

//Crea la funcion
$(document).ready(function () {
    $("#UEnviar").click(function () {
        //crea Variables y obtiene los campos del formulario de validaciones 
        var nombreUser = $("#UnombreUser").val();
        var nombre = $("#Unombre").val();
        var apellido = $("#Uapellido").val();
        var cedula = $("#Ucedula").val();
        var email = $("#Ucorreo").val();
        var contrasenia = $("#Ucontrasenia").val();
        var rol = $("#Urol").val();
        var materia = $("#Umateria").val();
        var curso = $("#Ucurso").val();
        var foto = $("#Ufoto").val();


        //Validacion de nombre
        if (nombreUser == "") {
            $("#mensaje9").fadeIn();        //Muestra el campo de validacion
            return false;
        } else {
            $("#mensaje9").fadeOut();        //Oculta el campo de validacion
            //Validacion de apellido
            if (rol == 'Administrador') {
                $("#mensaje2").fadeOut();
                $("#mensaje3").fadeOut();
                $("#Uapellido").prop("disabled", false);
                $("#Ucedula").prop("disabled", false);
                $("#Umateria").prop("disabled", false);
            } else {

                if (nombre == "") {
                    $("#mensaje1").fadeIn();        //Muestra el campo de validacion
                    return false;
                } else {
                    $("#mensaje1").fadeOut();        //Oculta el campo de validacion
                }

                if (apellido == "") {
                    $("#mensaje2").fadeIn();        //Muestra el campo de validacion
                    return false;
                } else {
                    $("#mensaje2").fadeOut();        //Oculta el campo de validacion
                }

                if (cedula > 1000000000 && cedula < 9999999999) {
                    $("#mensaje3").fadeOut();        //Oculta el campo de validacion
                } else {
                    $("#mensaje3").fadeIn();        //Muestra el campo de validacion
                    return false;
                }

                if (email == "" || !expr.test(email)) {
                    $("#mensaje4").fadeIn();        //Muestra el campo de validacion
                    return false;
                } else {
                    $("#mensaje4").fadeOut();        //Oculta el campo de validacion
                }

                if (materia == "") {
                    $("#mensaje7").fadeIn();        //Muestra el campo de validacion
                    return false;
                } else {
                    $("#mensaje7").fadeOut();        //Oculta el campo de validacion
                }

                if (curso == "") {
                    $("#mensaje8").fadeIn();        //Muestra el campo de validacion
                    return false;
                } else {
                    $("#mensaje8").fadeOut();        //Oculta el campo de validacion
                }

            }

            if (email == "" || !expr.test(email)) {
                $("#mensaje4").fadeIn();        //Muestra el campo de validacion
                return false;
            } else {
                $("#mensaje4").fadeOut();        //Oculta el campo de validacion
            }

            //Validacion de contraseña
            if (rol == 'Estudiante') {
                $("#mensaje5").fadeOut();
                $("#Ucontrasenia").prop("disabled", false);
                $("#Umateria").prop("disabled", false);

                if (foto == "") {
                    $("#mensaje10").fadeIn();        //Muestra el campo de validacion
                    return false;
                } else {
                    $("#mensaje10").fadeOut();        //Oculta el campo de validacion
                }
            } else {
                if (contrasenia == "") {
                    $("#mensaje5").fadeIn();        //Muestra el campo de validacion
                    return false;
                } else {
                    $("#mensaje5").fadeOut();        //Oculta el campo de validacion
                }
            }
        }
    })
})

$(function () {
    $("#Urol").change(function () {
        if ($(this).val() == "Estudiante") {
            $("#Ucontrasenia").prop("disabled", true);
        } else {
            $("#Ucontrasenia").prop("disabled", false);
        }
    });
});


$(function () {
    $("#Urol").change(function () {
        if ($(this).val() == "Administrador") {
            $("#Unombre").prop("disabled", true);
            $("#Uapellido").prop("disabled", true);
            $("#Ucedula").prop("disabled", true);
            $("#Umateria").prop("disabled", true);
            $("#Ucurso").prop("disabled", true);
            $("#Ufoto").prop("disabled", true);

        } else if ($(this).val() == "Estudiante") {
            $("#Unombre").prop("disabled", false);
            $("#Uapellido").prop("disabled", false);
            $("#Ucedula").prop("disabled", false);
            $("#Ucorreo").prop("disabled", false);
            $("#Umateria").prop("disabled", false);
            $("#Ucurso").prop("disabled", false);
            $("#Ucontrasenia").prop("disabled", true);
            $("#Ufoto").prop("disabled", false);

        } else {
            $("#Unombre").prop("disabled", false);
            $("#Uapellido").prop("disabled", false);
            $("#Ucedula").prop("disabled", false);
            $("#Ucorreo").prop("disabled", false);
            $("#Umateria").prop("disabled", false);
            $("#Ucurso").prop("disabled", false);
        }
    });
});