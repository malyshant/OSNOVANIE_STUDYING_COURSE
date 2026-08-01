import tkinter as tk
import requests


# Функция для получения цены Bitcoin с CoinGecko
def get_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()

    # Достаем цену биткоина из словаря
    price = data['bitcoin']['usd']
    price_label.config(text=f"Bitcoin: ${price}")


# Создаем главное окно
root = tk.Tk()
root.title("Курс Криптовалют v1")
root.geometry("300x200")

# Заголовок
title = tk.Label(root, text="Крипто-трекер", font=("Arial", 14))
title.pack(pady=10)

# Метка для вывода курса
price_label = tk.Label(root, text="Нажмите кнопку для загрузки", font=("Arial", 11))
price_label.pack(pady=10)

# Кнопка обновления
btn_update = tk.Button(root, text="Запросить курс BTC", command=get_bitcoin_price)
btn_update.pack(pady=10)

# Запуск приложения
root.mainloop()