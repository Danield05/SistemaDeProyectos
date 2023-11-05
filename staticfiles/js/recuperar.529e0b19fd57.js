document.getElementById('custom-alert-button').addEventListener('click', function() {
    const signinURL = this.getAttribute('data-signin-url');

    Swal.fire({
        title: '¿Cancelar?',
        text: '¿Estás seguro de que quieres cancelar la recuperación de tu contraseña?',
        icon: 'question',
        showCancelButton: true,
        confirmButtonText: 'OK',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            window.location.href = signinURL;
        }
    });
});
