import tkinter as tk

class MonitorUI:

    def __init__(self, communicator=None):
        self.communicator = communicator

        self.root = tk.Tk()
        self.root.title("Accident Detection Monitor")
        self.root.geometry("400x200")

        # Status label (green = idle)
        self.label = tk.Label(
            self.root,
            text="System Idle",
            font=("Arial", 16),
            fg="green"
        )
        self.label.pack(pady=20)

        self.button = tk.Button(
            self.root,
            text="Deactivate Buzzer",
            command=self.deactivate_buzzer,
            font=("Arial", 14)
        )
        self.button.pack(pady=10)

    def update_status(self, message, alert=False):
        self.label.config(text=message, fg="red" if alert else "green")

    def deactivate_buzzer(self):

        if self.communicator:
            self.communicator.deactivate_buzzer()
        self.update_status("Buzzer Deactivated", alert=False)

    def run(self):

        self.root.mainloop()

if __name__ == "__main__":
    # For testing without real communicator
    ui = MonitorUI()
    ui.update_status("Vehicle Accident Detected!", alert=True)
    ui.run()
