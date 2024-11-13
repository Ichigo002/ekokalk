import tkinter as tk
from tkinter import messagebox
from .get_weather import get_sunshine_percentage_in

class EkokalkWindow:

    SUNLIGHT_HOURS = 4  # Approximate sunlight hours in peak conditions
    SUN_PERCENTAGE_TODAY = 0.8  # 80% sunshine today
    PANEL_EFFICIENCY = 0.15  # 15% panel efficiency

    panel_size_entry = 0
    electricity_rate_entry = 0
    result_message = 0

    def __init__(self, title, geometry):
            self.window = tk.Tk()
            self.window.title(title)
            self.window.geometry(geometry)
            self.window.config(bg="#f5f5f5")

    def run(self):
        self.window.mainloop()

    def create_widgets(self):
        header_label = tk.Label(self.window, text="Solar Panel Cost and Benefit Calculator", font=("Arial", 14, "bold"), fg="#333", bg="#f5f5f5")
        header_label.pack(pady=15)

        # Input: Panel Size (kW)
        tk.Label(self.window, text="Panel Size (kW):", font=("Arial", 11), bg="#f5f5f5").pack(pady=(10, 5))
        self.panel_size_entry = tk.Entry(self.window, font=("Arial", 11), width=20)
        self.panel_size_entry.pack()

        # Input: Electricity Rate (cents per kWh)
        tk.Label(self.window, text="Electricity Rate (cents per kWh):", font=("Arial", 11), bg="#f5f5f5").pack(pady=(10, 5))
        self.electricity_rate_entry = tk.Entry(self.window, font=("Arial", 11), width=20)
        self.electricity_rate_entry.pack()

        # Calculate function
        self.result_message = tk.Label(self.window, text="", font=("Arial", 12), fg="#333", bg="#f5f5f5")
        self.result_message.pack(pady=10)

        # Calculate button
        calculate_button = tk.Button(self.window, text="Calculate", command=self.calculate_savings, font=("Arial", 10), bg="#4CAF50", fg="white")
        calculate_button.pack(pady=20)


        close_button = tk.Button(self.window, text="Close", command=self.close_window, font=("Arial", 10), bg="lightcoral", fg="white")
        close_button.pack(pady=20)

    def close_window(self):
        self.window.destroy()

    def calculate_savings(self):
            # Static values

        try:
            panel_size_kw = float(self.panel_size_entry.get())
            electricity_rate_cents = float(self.electricity_rate_entry.get())
            
            # Calculate potential energy generated (kWh)
            energy_generated_today = panel_size_kw * self.SUNLIGHT_HOURS * self.SUN_PERCENTAGE_TODAY * self.PANEL_EFFICIENCY
            
            # Calculate savings (in cents)
            savings_today = energy_generated_today * electricity_rate_cents
            

            # Display the results
            self.result_message.config(text=(
                f"Energy Produced Today: {energy_generated_today:.2f} kWh\n"
                f"Estimated Savings: {savings_today:.2f} cents"
            ))
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numerical values.")



