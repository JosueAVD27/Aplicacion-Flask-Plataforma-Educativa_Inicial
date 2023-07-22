var contador = 0;

//Crea la funcion
$(document).ready(function () {
    $("#REnviar").click(function () {
        //crea Variables y obtiene los campos del formulario de validaciones 
        var rol = $("#Prol").val();
        var permiso = $("#PpermisoR").val();
        var informacion = $("#PdescripcionR").val();

        //Validacion de nombre
        if (rol == "") {
            $("#mensaje1").fadeIn();        //Muestra el campo de validacion
            return false;
        } else {
            $("#mensaje1").fadeOut();        //Oculta el campo de validacion

            if (permiso == "") {
                $("#mensaje2").fadeIn();        //Muestra el campo de validacion
                return false;
            } else {
                $("#mensaje2").fadeOut();        //Oculta el campo de validacion

                if (informacion == "") {
                    $("#mensaje3").fadeIn();        //Muestra el campo de validacion
                    return false;
                } else {
                    $("#mensaje3").fadeOut();
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
            $("#Uapellido").prop("disabled", true);
            $("#Ucedula").prop("disabled", true);
            $("#Ucorreo").prop("disabled", true);
        } else {
            $("#Uapellido").prop("disabled", false);
            $("#Ucedula").prop("disabled", false);
            $("#Ucorreo").prop("disabled", false);
        }
    });
});

//Crea la funcion
$(document).ready(function () {
    $("#PEnviar").click(function () {
        //crea Variables y obtiene los campos del formulario de validaciones 
        var nombre = $("#Pnombre").val();
        var tipo = $("#Ppermiso").val();
        var descripcion = $("#Pdescripcion").val();

        //Validacion de nombre
        if (nombre == "") {
            $("#mensaje4").fadeIn();        //Muestra el campo de validacion
            return false;
        } else {
            $("#mensaje4").fadeOut();        //Oculta el campo de validacion

            if (tipo == "") {
                $("#mensaje5").fadeIn();        //Muestra el campo de validacion
                return false;
            } else {
                $("#mensaje5").fadeOut();        //Oculta el campo de validacion

                if (descripcion == "") {
                    $("#mensaje6").fadeIn();        //Muestra el campo de validacion
                    return false;
                } else {
                    $("#mensaje6").fadeOut();
                }
            }
        }
    })
})