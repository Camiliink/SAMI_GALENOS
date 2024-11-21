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

        dateDisplay.textContent = `${firstDayOfMonth.toLocaleString('default', { month: 'long' })} ${year}`;

        // Limpiar los días previos
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
                dateField.value = `${day} ${firstDayOfMonth.toLocaleString('default', { month: 'short' })} ${year}`;
            });
            daysContainer.appendChild(dayCell);
        }
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
