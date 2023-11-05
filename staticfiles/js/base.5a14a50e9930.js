const menuButton = document.getElementById('menuButton');
        const menuPanel = document.getElementById('menuPanel');
        const contentDiv = document.getElementById('contentDiv');
        const closeButton = document.getElementById('closeButton');
    
        menuButton.addEventListener('click', () => {
            menuPanel.style.transform = 'translateX(0)';
        });

        closeButton.addEventListener('click', () => {
            menuPanel.style.transform = 'translateX(-100%)';
        });

        // Desplegar menú de usuario
        const userLink = document.querySelector('.userLink');
        const userDropdown = document.querySelector('.userDropdown');
        
        userLink.addEventListener('click', () => {
            userDropdown.classList.toggle('hidden');
        });

        // Cerrar el menú si se hace clic fuera del menú
        window.addEventListener('click', (event) => {
            if (!menuPanel.contains(event.target) && !menuButton.contains(event.target)) {
                menuPanel.style.transform = 'translateX(-100%)';
            }
        });

        

        //alertas
        document.getElementById('custom-alert-button').addEventListener('click', function() {
            const signinURL = this.getAttribute('data-signin-url');
        
            Swal.fire({
                title: '¿Cancelar?',
                text: '¿Estás seguro de que quieres cancelar agregar un recurso?',
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
        
        