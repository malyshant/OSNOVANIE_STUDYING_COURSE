import tkinter as tk
from tkinter import ttk

# Словарь  валют
CURRENCIES = {
    "EUR": "Евро",
    "USD": "Доллар США",
    "RUB": "Российский рубль",
    "GBP": "Фунт UK",
    "JPY": "Японская иена",
}

# --- Главное окно ---
window = tk.Tk()
window.title("Курсы обмена валют")
window.geometry("300x420")

# 1. базовая валюта №1
tk.Label(window, text="Базовая валюта", font=("Arial", 10)).pack(pady=(15, 5))
cb_base1 = ttk.Combobox(
    window, values=list(CURRENCIES.keys()), state="readonly"
)
cb_base1.pack()
cb_base1.set("EUR")

label_name_base1 = tk.Label(window, text=CURRENCIES["EUR"], fg="gray")
label_name_base1.pack(pady=(2, 10))

# 2. Вторая базовая валюта
tk.Label(window, text="Вторая базовая валюта", font=("Arial", 10)).pack(pady=5)
cb_base2 = ttk.Combobox(
    window, values=list(CURRENCIES.keys()), state="readonly"
)
cb_base2.pack()
cb_base2.set("USD")

label_name_base2 = tk.Label(window, text=CURRENCIES["USD"], fg="gray")
label_name_base2.pack(pady=(2, 10))

# 3. Целевая валюта
tk.Label(window, text="Целевая валюта", font=("Arial", 10)).pack(pady=5)
cb_target = ttk.Combobox(
    window, values=list(CURRENCIES.keys()), state="readonly"
)
cb_target.pack()
cb_target.set("RUB")

label_name_target = tk.Label(window, text=CURRENCIES["RUB"], fg="gray")
label_name_target.pack(pady=(2, 15))

# Кнопка запроса
btn_get_rate = tk.Button(
    window, text="Получить курс обмена", font=("Arial", 10)
)
btn_get_rate.pack(pady=10)

window.mainloop()