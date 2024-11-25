document.addEventListener("DOMContentLoaded", () => {
    const horaSelect = document.querySelector("#hora");
    const minutosSelect = document.querySelector("#minutos");

    // Función para generar las opciones de hora y minutos
    function generarOpcionesHora() {
        // Crear las opciones de hora desde las 07:00 hasta las 19:00
        for (let hora = 7; hora <= 19; hora++) {
            // Opciones para cada hora
            const horaOption = document.createElement("option");
            horaOption.value = String(hora).padStart(2, '0'); // Formato 07, 08, ..., 19
            horaOption.textContent = String(hora).padStart(2, '0');
            horaSelect.appendChild(horaOption);
        }

        // Crear las opciones de minutos (solo 00, 15, 30, 45)
        const minutos = ["00", "15", "30", "45"];
        minutos.forEach(minuto => {
            const minutosOption = document.createElement("option");
            minutosOption.value = minuto;
            minutosOption.textContent = minuto;
            minutosSelect.appendChild(minutosOption);
        });

        // Establecer valores por defecto
        horaSelect.value = "07";
        minutosSelect.value = "00";
    }

    // Inicializar la generación de opciones
    generarOpcionesHora();
});
