document.addEventListener("DOMContentLoaded", () => {
    const calendario = document.querySelector("#calendar");
    const dateField = document.querySelector("#date"); // Campo de fecha del formulario
    const prevButton = calendario.querySelector(".prev");
    const nextButton = calendario.querySelector(".next");
    const dateDisplay = calendario.querySelector(".date");
    const daysContainer = calendario.querySelector(".days");
    const todayButton = calendario.querySelector(".today-btn");

    let currentDate = new Date();

    // Función para mostrar el mes y los días
    function renderCalendar() {
        const month = currentDate.getMonth(); // Obtén el mes actual
        const year = currentDate.getFullYear(); // Obtén el año actual
        const firstDayOfMonth = new Date(year, month, 1);
        const lastDayOfMonth = new Date(year, month + 1, 0);
        const lastDayOfPreviousMonth = new Date(year, month, 0); // Último día del mes anterior
        const totalDays = lastDayOfMonth.getDate(); // Total de días en el mes
        const firstDayOfWeek = firstDayOfMonth.getDay(); // Día de la semana en que comienza el mes

        // Actualiza el display de la fecha
        dateDisplay.textContent = `${String(firstDayOfMonth.getMonth() + 1).padStart(2, '0')}/${String(firstDayOfMonth.getDate()).padStart(2, '0')}/${year}`;
        daysContainer.innerHTML = "";

        // Mostrar los días del mes anterior (si es necesario para completar la primera semana)
        for (let i = firstDayOfWeek - 1; i >= 0; i--) {
            const emptyCell = document.createElement("div");
            emptyCell.classList.add("day", "prev-month-day");
            emptyCell.textContent = lastDayOfPreviousMonth.getDate() - i;
            daysContainer.appendChild(emptyCell);
        }

        // Mostrar los días del mes actual
        for (let day = 1; day <= totalDays; day++) {
            const dayCell = document.createElement("div");
            dayCell.textContent = day;
            dayCell.classList.add("day");
            dayCell.addEventListener("click", () => {
                // Al hacer clic, actualizamos el campo de fecha
                const selectedDate = new Date(year, month, day);
                const formattedDate = `${selectedDate.getFullYear()}-${String(selectedDate.getMonth() + 1).padStart(2, '0')}-${String(selectedDate.getDate()).padStart(2, '0')}`; // Formato yyyy-mm-dd
                console.log("Fecha seleccionada: ", formattedDate); // Verificar que la fecha se está actualizando
                dateField.value = formattedDate; // Mostrar la fecha en formato yyyy-mm-dd
            });
            daysContainer.appendChild(dayCell);
        }

        // Rellenar con días del mes siguiente si la última semana no se llena completamente
        const remainingCells = 42 - (daysContainer.children.length); // Hay 42 celdas en total (6 semanas x 7 días)
        for (let i = 1; i <= remainingCells; i++) {
            const emptyCell = document.createElement("div");
            emptyCell.classList.add("day", "next-month-day");
            emptyCell.textContent = i;
            daysContainer.appendChild(emptyCell);
        }

        // Aplicar clases para crear el grid visual
        daysContainer.style.gridTemplateColumns = "repeat(7, 1fr)"; // Crear 7 columnas (uno por día de la semana)
    }

    // Función para manejar los cambios de mes
    prevButton.addEventListener("click", () => {
        currentDate.setMonth(currentDate.getMonth() - 1);
        renderCalendar();
    });

    nextButton.addEventListener("click", () => {
        currentDate.setMonth(currentDate.getMonth() + 1);
        renderCalendar();
    });

    // Función para mostrar el calendario del día de hoy
    todayButton.addEventListener("click", () => {
        currentDate = new Date();
        renderCalendar();
    });

    // Inicializar el calendario
    renderCalendar();
});
