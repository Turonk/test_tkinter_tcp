import tkinter as tk
import threading
import socket
import time

class ToggleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Toggle Buttons TCP")

        self.is_button1_active = True
        self.running = False
        self.thread = None
        
        # Лейбл с текстом
        self.label = tk.Label(root, text="Тестовая программа", font=("Arial", 14))
        self.label.pack()
        
        # Создание больших кнопок
        self.button1 = tk.Button(root, text="Button 1", font=("Arial", 24), command=self.toggle_buttons)
        self.button1.pack(expand=True, fill='both')
        
        self.button2 = tk.Button(root, text="Button 2", font=("Arial", 24), command=self.toggle_buttons, state='disabled')
        self.button2.pack(expand=True, fill='both')
        
        # Кнопка для старта и остановки передачи данных
        self.start_stop_button = tk.Button(root, text="Start Sending Data", font=("Arial", 14), command=self.start_stop_thread)
        self.start_stop_button.pack()

    def toggle_buttons(self):
        # Переключение активности кнопок
        if self.is_button1_active:
            self.button1.config(state='disabled')
            self.button2.config(state='normal')
        else:
            self.button1.config(state='normal')
            self.button2.config(state='disabled')

        self.is_button1_active = not self.is_button1_active

    def send_tcp_packet(self):
        MESSAGE = "1234567890"  # Пакет из 10 символов
        SERVER_IP = "127.0.0.1" # Задайте IP адрес сервера
        SERVER_PORT = 12345     # Задайте порт сервера

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((SERVER_IP, SERVER_PORT))
                s.sendall(MESSAGE.encode('utf-8'))
                print(f"Sent packet: {MESSAGE}")
        except Exception as e:
            print(f"Error sending packet: {e}")

    def start_stop_thread(self):
        if self.running:
            self.running = False
            self.start_stop_button.config(text="Start Sending Data")  # Обновление текста кнопки
        else:
            self.running = True
            self.start_stop_button.config(text="Stop Sending Data")
            self.thread = threading.Thread(target=self.send_data_continuously)
            self.thread.start()

    def send_data_continuously(self):
        while self.running:
            self.send_tcp_packet()
            time.sleep(1)  # Пауза в 1 секунду между посылками

if __name__ == "__main__":
    root = tk.Tk()
    app = ToggleApp(root)
    root.mainloop()