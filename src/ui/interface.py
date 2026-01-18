import tkinter as tk

class MonitorUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Accident Detection Monitor")

        self.label = tk.Label(self.root, text="System Idle", font=("Arial", 16))
        self.label.pack(pady=10)

        self.button = tk.Button(
            self.root,
            text="Deactivate Buzzer",
            command=self.deactivate_buzzer,
            font=("Arial", 14)
        )
        self.button.pack(pady=10)

        self.communicator = None

    def update_status(self, message):
        self.label.config(text=message)

    def deactivate_buzzer(self):
        if self.communicator:
            self.communicator.deactivate_buzzer()
        self.update_status("Buzzer Deactivated")

    def run(self):
        self.root.mainloop()
