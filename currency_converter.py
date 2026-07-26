import tkinter as tk
from tkinter import messagebox as mb, ttk
import requests

CURRENCIES = {
    "EUR": "Евро",
    "USD": "Американский доллар",
    "RUB": "Российский рубль",
    "GBP": "Фунт стерлингов",
    "JPY": "Японская иена",
}


def update_currency_names(event=None):

    label_name_base1.config(text=CURRENCIES.get(cb_base1.get(), ""))
    label_name_base2.config(text=CURRENCIES.get(cb_base2.get(), ""))
    label_name_target.config(text=CURRENCIES.get(cb_target.get(), ""))


def fetch_exchange_rate(base_code, target_code):

    url = f"https://open.er-api.com/v6/latest/{base_code}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data.get("result") == "success":
            rates = data.get("rates", {})
            return rates.get(target_code)
    return None


# --- СОЗДАНИЕ ОКНА ---
window = tk.Tk()
window.title("Курсы обмена валют")
window.geometry("300x420")

# 1 Базовая валюта №1
tk.Label(window, text="Базовая валюта", font=("Arial", 10)).pack(pady=(15, 5))
cb_base1 = ttk.Combobox(
    window, values=list(CURRENCIES.keys()), state="readonly"
)
cb_base1.pack()
cb_base1.set("EUR")
cb_base1.bind("<<ComboboxSelected>>", update_currency_names)

label_name_base1 = tk.Label(window, text=CURRENCIES["EUR"], fg="gray")
label_name_base1.pack(pady=(2, 10))

# 2. Базовая валюта №2
tk.Label(window, text="Вторая базовая валюта", font=("Arial", 10)).pack(pady=5)
cb_base2 = ttk.Combobox(
    window, values=list(CURRENCIES.keys()), state="readonly"
)
cb_base2.pack()
cb_base2.set("USD")
cb_base2.bind("<<ComboboxSelected>>", update_currency_names)

label_name_base2 = tk.Label(window, text=CURRENCIES["USD"], fg="gray")
label_name_base2.pack(pady=(2, 10))

# 3. Целевая валюта
tk.Label(window, text="Целевая валюта", font=("Arial", 10)).pack(pady=5)
cb_target = ttk.Combobox(
    window, values=list(CURRENCIES.keys()), state="readonly"
)
cb_target.pack()
cb_target.set("RUB")
cb_target.bind("<<ComboboxSelected>>", update_currency_names)

label_name_target = tk.Label(window, text=CURRENCIES["RUB"], fg="gray")
label_name_target.pack(pady=(2, 15))

# Кнопка запроса
btn_get_rate = tk.Button(
    window, text="Получить курс обмена", font=("Arial", 10)
)
btn_get_rate.pack(pady=10)


window.mainloop()