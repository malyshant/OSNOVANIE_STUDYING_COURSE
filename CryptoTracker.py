import tkinter as tk
import requests
from datetime import datetime

# Настройки API
CRYPTO_IDS = "bitcoin,ethereum,solana,binancecoin,ripple"
API_URL = f"https://api.coingecko.com/api/v3/simple/price?ids={CRYPTO_IDS}&vs_currencies=usd"


def update_prices():
    status_label.config(text="Загрузка данных...", fg="gray")
    root.update()

    try:
        # Указываем timeout, чтобы программа не зависала при плохом интернете
        response = requests.get(API_URL, timeout=5)
        response.raise_for_status()  # Проверка статуса ответа (200 OK)
        data = response.json()

        # Обновляем значения в виджетах
        for coin_id, label in labels_dict.items():
            if coin_id in data:
                price = data[coin_id]['usd']
                # Форматируем вывод с запятыми в тысячах
                label.config(text=f"${price:,.2f}")

        # Фиксируем время последнего успешного обновления
        current_time = datetime.now().strftime("%H:%M:%S")
        status_label.config(text=f"Успешно обновлено в {current_time}", fg="green")

    except requests.exceptions.RequestException:
        # Если нет интернета или ошибка сервера
        status_label.config(text="Ошибка подключения к API!", fg="red")


# Главное окно
root = tk.Tk()
root.title("Crypto Tracker v1.0")
root.geometry("380x360")
root.resizable(False, False)

# Заголовок
tk.Label(root, text="Курсы криптовалют к USD", font=("Arial", 14, "bold")).pack(pady=12)

# Таблица монет
frame = tk.Frame(root, relief="groove", bd=1)
frame.pack(pady=5, padx=15, fill="x")

coins = [
    ("Bitcoin (BTC)", "bitcoin"),
    ("Ethereum (ETH)", "ethereum"),
    ("Solana (SOL)", "solana"),
    ("Binance Coin (BNB)", "binancecoin"),
    ("Ripple (XRP)", "ripple")
]

labels_dict = {}

for i, (name, coin_id) in enumerate(coins):
    tk.Label(frame, text=name, font=("Arial", 10), anchor="w").grid(row=i, column=0, padx=15, pady=6, sticky="w")
    val_label = tk.Label(frame, text="$0.00", font=("Arial", 10, "bold"))
    val_label.grid(row=i, column=1, padx=15, pady=6, sticky="e")
    labels_dict[coin_id] = val_label

# Кнопка запроса
btn_update = tk.Button(root, text="Обновить курсы", font=("Arial", 10, "bold"), bg="#e1e1e1", command=update_prices)
btn_update.pack(pady=12)

# Метка статуса
status_label = tk.Label(root, text="Нажмите кнопку для загрузки", font=("Arial", 9), fg="gray")
status_label.pack()

# Автоматически загружаем курсы при запуске
update_prices()

root.mainloop()