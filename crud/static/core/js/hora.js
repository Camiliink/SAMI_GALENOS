document.addEventListener('DOMContentLoaded', function () {
    const horaSelect = document.getElementById('hora');
    const minutosSelect = document.getElementById('minutos');
    const dateInput = document.getElementById('date');

    // Función para cargar las opciones de horas y minutos
    function cargarHorasYMinutos() {
        const selectedDate = new Date(dateInput.value);
        
        // Limpiar las opciones previas
        horaSelect.innerHTML = '';
        minutosSelect.innerHTML = '';

        // Crear opciones de hora (por ejemplo, de 9 a 18 horas)
        for (let i = 9; i <= 18; i++) {
            const horaOption = document.createElement('option');
            horaOption.value = i;
            horaOption.textContent = i < 10 ? `0${i}:00` : `${i}:00`; // Formateo 09:00, 10:00, etc.
            horaSelect.appendChild(horaOption);
        }

        // Crear opciones de minutos (cada 15 minutos)
        const minutosArray = ['00', '15', '30', '45'];
        minutosArray.forEach(function (minuto) {
            const minutosOption = document.createElement('option');
            minutosOption.value = minuto;
            minutosOption.textContent = minuto;
            minutosSelect.appendChild(minutosOption);
        });
    }

    // Llamar a la función al cargar la página
    if (dateInput.value) {
        cargarHorasYMinutos();
    }

    // Actualizar horas y minutos cada vez que el usuario cambia la fecha
    dateInput.addEventListener('change', cargarHorasYMinutos);
});
