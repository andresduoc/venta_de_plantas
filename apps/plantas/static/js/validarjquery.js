$(document).ready(function() {
    $('#formulariotarjeta').submit(function(event) {
        event.preventDefault();
        
        var nombre = $('#nombre').val();
        var correo = $('#correo').val();
        var numero = $('#numero').val();
        var numeros = $('#numeros').val();

        // nombre
        if (nombre.trim() === '') {
            $('#errorNombre').text('Debe ingresar un nombre');
            return;
        } else {
            $('#errorNombre').text('');
        }

        // correo
        var correoRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!correo.match(correoRegex)) {
            $('#errorCorreo').text('Ingrese un correo electrónico válido');
            return;
        } else {
            $('#errorCorreo').text('');
        }

        //  num celular
        if (numero.length <= 6) {
            $('#errornumero').text('La contraseña debe tener más de 6 caracteres');
            return;
        } else {
            $('#errornumero').text('');
        }

        // tarjeta
        var numerosRegex = /^\d{16}$/;
        if (!numeros.match(numerosRegex)) {
            $('#errorNumeros').text('Ingrese exactamente 16 números');
            return;
        } else {
            $('#errorNumeros').text('');
        }

        // enviar if correcto
        alert('Formulario enviado con éxito');
    });
});