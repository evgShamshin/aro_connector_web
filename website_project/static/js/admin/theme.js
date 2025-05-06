'use strict';
{
    // 1. Всегда по умолчанию ставим светлую тему
    const defaultTheme = "light";

    // 2. Устанавливаем тему (если не "dark" — ставим "light")
    function setTheme(mode) {
        const theme = (mode === "dark") ? "dark" : "light";
        document.documentElement.dataset.theme = theme;
        localStorage.setItem("djangoTheme", theme);  // Сохраняем выбор
        updateThemeButton(theme);
    }

    // 3. Переключатель тем (просто light ↔ dark)
    function cycleTheme() {
        const currentTheme = localStorage.getItem("djangoTheme") || defaultTheme;
        setTheme(currentTheme === "light" ? "dark" : "light");
    }

    // 4. Обновляем иконку кнопки
    function updateThemeButton(theme) {
        const buttons = document.querySelectorAll(".theme-toggle");
        buttons.forEach(btn => {
            btn.textContent = theme === "light" ? "ᴀʀᴏ" : "ᴀʀᴏ";
        });
    }

    // 5. Инициализация темы при загрузке
    function initTheme() {
        const savedTheme = localStorage.getItem("djangoTheme");
        setTheme(savedTheme || defaultTheme);  // Если нет сохранённой — ставим светлую
    }

    // 6. Вешаем обработчик на кнопку
    window.addEventListener("DOMContentLoaded", () => {
        const buttons = document.querySelectorAll(".theme-toggle");
        buttons.forEach(btn => {
            btn.addEventListener("click", cycleTheme);
        });
        initTheme();
    });
}
