import tkinter as tk
from tkinter import messagebox
from .calculator import estimate_solar_power

class EkokalkWindow:

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

        tk.Label(self.window, text="Nazwa miasta:", font=("Arial", 11), bg="#f5f5f5").pack(pady=(10, 5))
        self.panel_city_name = tk.Entry(self.window, font=("Arial", 11), width=20)
        self.panel_city_name.pack()

        tk.Label(self.window, text="Produkcja twoich paneli (kWh):", font=("Arial", 11), bg="#f5f5f5").pack(pady=(10, 5))
        self.panel_production = tk.Entry(self.window, font=("Arial", 11), width=20)
        self.panel_production.pack()

        tk.Label(self.window, text="Koszt elektrycznosci (zł/kWh):", font=("Arial", 11), bg="#f5f5f5").pack(pady=(10, 5))
        self.electricity_rate_entry = tk.Entry(self.window, font=("Arial", 11), width=20)
        self.electricity_rate_entry.pack()

        self.result_message = tk.Label(self.window, text="", font=("Arial", 12), fg="#333", bg="#f5f5f5")
        self.result_message.pack(pady=10)

        # Calculate button
        calculate_button = tk.Button(self.window, text="Oblicz", command=self.calculate_savings, font=("Arial", 10), bg="#4CAF50", fg="white")
        calculate_button.pack(pady=20)


        close_button = tk.Button(self.window, text="Zamknij", command=self.close_window, font=("Arial", 10), bg="lightcoral", fg="white")
        close_button.pack(pady=20)

    def close_window(self):
        self.window.destroy()

    def calculate_savings(self):
            # Static values

        try:
            city_name = self.panel_city_name.get()
            electricity_rate_cents = float(self.electricity_rate_entry.get())
            panel_production = float(self.panel_production.get())
            
            solar_panel_production_Wh = estimate_solar_power(city_name, panel_production)
            
            # Calculate savings (in cents)
            savings_today = solar_panel_production_Wh * electricity_rate_cents
            

            # Display the results
            self.result_message.config(text=(
                f"Energia wyprodukowana dzisiaj: {solar_panel_production_Wh:.2f} kWh\n"
                f"Szacowane oszczędności: {savings_today:.2f} zł"
            ))
        except ValueError:
            messagebox.showerror("Input Error", "Prosze wprowadzic prawidlowe wartości.")



