import tkinter as tk
from tkinter import messagebox
from .get_weather import get_sunshine_percentage_in


def calculate_savings():
    try:
        panel_size_kw = float(panel_size_entry.get())
        electricity_rate_cents = float(electricity_rate_entry.get())
        
        # Calculate potential energy generated (kWh)
        energy_generated_today = panel_size_kw * SUNLIGHT_HOURS * SUN_PERCENTAGE_TODAY * PANEL_EFFICIENCY
         
        # Calculate savings (in cents)
        savings_today = energy_generated_today * electricity_rate_cents
        
        # Display the results
        result_message.config(text=(
            f"Energy Produced Today: {energy_generated_today:.2f} kWh\n"
            f"Estimated Savings: {savings_today:.2f} cents"
        ))
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

def init_window():

    # Initialize the main window
    window = tk.Tk()
    window.title("Solar Panel Cost and Benefit Calculator")
    window.geometry("400x400")
    window.config(bg="#f5f5f5")

    # Static values
    SUNLIGHT_HOURS = 4  # Approximate sunlight hours in peak conditions
    SUN_PERCENTAGE_TODAY = 0.8  # 80% sunshine today
    PANEL_EFFICIENCY = 0.15  # 15% panel efficiency

    # Header Label
    header_label = tk.Label(window, text="Solar Panel Cost and Benefit Calculator", font=("Arial", 14, "bold"), fg="#333", bg="#f5f5f5")
    header_label.pack(pady=15)

    # Input: Panel Size (kW)
    tk.Label(window, text="Panel Size (kW):", font=("Arial", 11), bg="#f5f5f5").pack(pady=(10, 5))
    panel_size_entry = tk.Entry(window, font=("Arial", 11), width=20)
    panel_size_entry.pack()

    # Input: Electricity Rate (cents per kWh)
    tk.Label(window, text="Electricity Rate (cents per kWh):", font=("Arial", 11), bg="#f5f5f5").pack(pady=(10, 5))
    electricity_rate_entry = tk.Entry(window, font=("Arial", 11), width=20)
    electricity_rate_entry.pack()

    # Calculate function


    # Calculate button
    calculate_button = tk.Button(window, text="Calculate", command=calculate_savings, font=("Arial", 10), bg="#4CAF50", fg="white")
    calculate_button.pack(pady=20)

    # Result message
    result_message = tk.Label(window, text="", font=("Arial", 12), fg="#333", bg="#f5f5f5")
    result_message.pack(pady=10)

    # Close button
    def close_window():
        window.destroy()

    close_button = tk.Button(window, text="Close", command=close_window, font=("Arial", 10), bg="lightcoral", fg="white")
    close_button.pack(pady=20)

    # Run the application
    window.mainloop()


if __name__ == "__main__":
    init_window()