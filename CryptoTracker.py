import tkinter as tk
import requests

# Список монет
CRYPTO_IDS = "bitcoin,ethereum,solana,binancecoin,ripple"


def update_prices():
    # Запрашиваем цены сразу для всех монет
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={CRYPTO_IDS}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()

    # Обновляем текст в метках
    labels_dict['bitcoin'].config(text=f"${data['bitcoin']['usd']:.2f}")
    labels_dict['ethereum'].config(text=f"${data['ethereum']['usd']:.2f}")
    labels_dict['solana'].config(text=f"${data['solana']['usd']:.2f}")
    labels_dict['binancecoin'].config(text=f"${data['binancecoin']['usd']:.2f}")
    labels_dict['ripple'].config(text=f"${data['ripple']['usd']:.4f}")


root = tk.Tk()
root.title("Мониторинг криптовалют")
root.geometry("360x320")

# Шапка
tk.Label(root, text="Курсы криптовалют (USD)", font=("Arial", 14, "bold")).pack(pady=10)

# Фрейм для сетки монет
frame = tk.Frame(root)
frame.pack(pady=10)

# Красивые названия монет
coins = [
    ("Bitcoin (BTC)", "bitcoin"),
    ("Ethereum (ETH)", "ethereum"),
    ("Solana (SOL)", "solana"),
    ("Binance Coin (BNB)", "binancecoin"),
    ("Ripple (XRP)", "ripple")
]

labels_dict = {}

# Выводим монеты строками
for i, (name, coin_id) in enumerate(coins):
    tk.Label(frame, text=name, font=("Arial", 11), anchor="w", width=18).grid(row=i, column=0, padx=5, pady=3)
    val_label = tk.Label(frame, text="---", font=("Arial", 11, "bold"), width=12)
    val_label.grid(row=i, column=1, padx=5, pady=3)
    labels_dict[coin_id] = val_label

# Кнопка для обновления
btn_update = tk.Button(root, text="Обновить курсы", font=("Arial", 10), command=update_prices)
btn_update.pack(pady=15)

root.mainloop()