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