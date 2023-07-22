var contador = 0;

//Crea la funcion
$(document).ready(function () {
    $("#AEnviar").click(function () {
        //crea Variables y obtiene los campos del formulario de validaciones 
        var codigo = $("#Acodigo").val();
        var periodo = $("#Aperiodo").val();
        var informacion = $("#Ainformacion").val();
        var estado = $("#Aestado").val();

        //Validacion de nombre
        if (codigo == "") {
            $("#mensaje1").fadeIn(); //Muestra el campo de validacion
            return false;
        } else {
            $("#mensaje1").fadeOut(); //Oculta el campo de validacion

            if (periodo == "") {
                $("#mensaje2").fadeIn(); //Muestra el campo de validacion
                return false;
            } else {
                $("#mensaje2").fadeOut(); //Oculta el campo de validacion

                if (informacion == "") {
                    $("#mensaje3").fadeIn(); //Muestra el campo de validacion
                    return false;
                } else {
                    $("#mensaje3").fadeOut();

                    if (estado == "") {
                        $("#mensaje4").fadeIn(); //Muestra el campo de validacion
                        return false;
                    } else {
                        $("#mensaje4").fadeOut();
                        $("#mensaje5").fadeOut();
                    }
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
    $("#CEnviar").click(function () {
        //crea Variables y obtiene los campos del formulario de validaciones 
        var curso = $("#Acurso").val();
        var tutor = $("#Atutor").val();

        if (curso == "") {
            $("#mensaje10").fadeIn(); //Muestra el campo de validacion
            return false;
        } else {
            $("#mensaje10").fadeOut(); //Oculta el campo de validacion

            if (tutor == "") {
                $("#mensaje11").fadeIn(); //Muestra el campo de validacion
                return false;
            } else {
                $("#mensaje11").fadeOut(); //Oculta el campo de validacion

                $("#Anivel").prop("disabled", false);
                $("#CperiodoA").prop("disabled", false);
            }
        }
    })
})



//Crea la funcion
$(document).ready(function () {
    $("#MEnviar").click(function () {
        //crea Variables y obtiene los campos del formulario de validaciones 
        var nrc = $("#Mnrc").val();
        var nombre = $("#Mnombre").val();
        var docente = $("#Mdocente").val();
        var curso = $("#Mcurso").val();
        var horario = $("#Mhorario").val();

        //Validacion de nombre
        if (nrc == "") {
            $("#mensaje6").fadeIn(); //Muestra el campo de validacion
            return false;
        } else {
            $("#mensaje6").fadeOut(); //Oculta el campo de validacion

            if (nombre == "") {
                $("#mensaje7").fadeIn(); //Muestra el campo de validacion
                return false;
            } else {
                $("#mensaje7").fadeOut(); //Oculta el campo de validacion

                if (docente == "") {
                    $("#mensaje8").fadeIn(); //Muestra el campo de validacion
                    return false;
                } else {
                    $("#mensaje8").fadeOut();

                    if (curso == "") {
                        $("#mensaje12").fadeIn(); //Muestra el campo de validacion
                        return false;
                    } else {
                        $("#mensaje12").fadeOut();

                        if (horario == "") {
                            $("#mensaje13").fadeIn(); //Muestra el campo de validacion
                            return false;
                        } else {
                            $("#mensaje13").fadeOut();

                            $("#MperiodoA").prop("disabled", false);
                        }
                    }
                }
            }
        }
    })
})