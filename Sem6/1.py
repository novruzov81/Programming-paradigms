# используется парадигма ООП

import time

class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.pause_time = None
        self.paused_duration = 0.0

    def start(self):
        if not self.start_time:
            self.start_time = time.time()
            print("Секундомер запущен.")

    def pause(self):
        if self.start_time and not self.pause_time:
            self.pause_time = time.time()
            print("Секундомер приостановлен.")

    def resume(self):
        if self.start_time and self.pause_time:
            self.paused_duration += time.time() - self.pause_time
            self.pause_time = None
            print("Секундомер возобновлен.")

    def stop(self):
        if self.start_time:
            total_duration = time.time() - self.start_time - self.paused_duration
            self.start_time = None
            self.pause_time = None
            print("Секундомер остановлен.")
            return total_duration

stopwatch = Stopwatch()

while True:
    print("Меню секундомера:")
    print("1. Запустить")
    print("2. Приостановить")
    print("3. Возобновить")
    print("4. Остановить")
    print("5. Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        stopwatch.start()
    elif choice == "2":
        stopwatch.pause()
    elif choice == "3":
        stopwatch.resume()
    elif choice == "4":
        duration = stopwatch.stop()
        print("Прошло {:.2f} секунд.".format(duration))
    elif choice == "5":
        break
    else:
        print("Неверный выбор. Попробуйте снова.")

