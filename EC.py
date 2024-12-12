import tkinter as tk
from tkinter import messagebox, filedialog
import matplotlib.pyplot as plt
import json
import os
import random

def calculate_footprint(data):
    try:
        electricity = float(data.get("electricity", 0))
        gas = float(data.get("gas", 0))
        fuel = float(data.get("fuel", 0))
        waste = float(data.get("waste", 0))
        recycling = float(data.get("recycling", 0)) / 100
        travel_km = float(data.get("travel_km", 0))
        fuel_efficiency = float(data.get("fuel_efficiency", 0))

        carbon = {
            "electricity": electricity * 12 * 0.0005,
            "gas": gas * 12 * 0.0053,
            "fuel": fuel * 12 * 2.32,
            "waste": waste * 12 * (0.57 - recycling),
            "travel": travel_km * (1 / fuel_efficiency) * 2.31,
        }
        carbon["total"] = sum(carbon.values())
        return carbon

    except Exception as e:
        messagebox.showerror("Error", f"Calculation error: {e}")
        return None

def save_data(data, filepath):
    try:
        with open(filepath, "w") as f:
            json.dump(data, f, indent=4)
        messagebox.showinfo("Success", f"Data saved to {filepath}")
    except Exception as e:
        messagebox.showerror("Error", f"Could not save data: {e}")

def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load data: {e}")
        return None

def plot_bar_graph(data):
    try:
        labels = list(data.keys())[:-1]  # Exclude 'total'
        values = list(data.values())[:-1]

        plt.figure(figsize=(10, 6))
        plt.bar(labels, values, color="skyblue")
        plt.title("Carbon Footprint by Category")
        plt.ylabel("kg CO2")
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", f"Could not plot bar graph: {e}")

def plot_pie_chart(data):
    try:
        labels = list(data.keys())[:-1]  # Exclude 'total'
        values = list(data.values())[:-1]

        # Replace negative values with their absolute values for plotting purposes
        adjusted_values = [abs(value) for value in values]

        plt.figure(figsize=(8, 8))
        plt.pie(adjusted_values, labels=labels, autopct="%1.1f%%", startangle=140)
        plt.title("Carbon Footprint Distribution")
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", f"Could not plot pie chart: {e}")

def get_random_suggestion():
    suggestions = [
        "Switch to energy-efficient light bulbs",
        "Install solar panels",
        "Use public transport instead of personal vehicles",
        "Carpool to work",
        "Reduce meat consumption",
        "Recycle and compost waste",
        "Plant trees in your community",
        "Unplug devices when not in use",
        "Use a programmable thermostat",
        "Upgrade to energy-efficient appliances",
        "Use cold water for laundry",
        "Insulate your home to save energy",
        "Reduce air travel when possible",
        "Opt for reusable bags and containers",
        "Avoid single-use plastics",
        "Drive a fuel-efficient or electric car",
        "Practice water conservation",
        "Buy locally-produced goods",
        "Reduce food waste",
        "Educate others about climate change",
        "Invest in renewable energy",
        "Switch to a green energy provider",
        "Work remotely to reduce commuting",
        "Use ceiling fans instead of air conditioning",
        "Reduce paper usage",
        "Harvest rainwater",
        "Advocate for environmental policies",
        "Turn off lights when not in use",
        "Conduct a home energy audit",
        "Switch to an electric lawn mower"
    ]
    return random.choice(suggestions)

def main():
    def calculate_and_display():
        data = {
            "electricity": electricity_var.get(),
            "gas": gas_var.get(),
            "fuel": fuel_var.get(),
            "waste": waste_var.get(),
            "recycling": recycling_var.get(),
            "travel_km": travel_km_var.get(),
            "fuel_efficiency": fuel_efficiency_var.get(),
        }

        carbon = calculate_footprint(data)
        if carbon:
            suggestion = ""
            if carbon['total'] > 40000:
                suggestion = get_random_suggestion()
                result_text.set(f"Total Carbon Footprint: {carbon['total']:.2f} kg CO2\nSuggestion: {suggestion}")
            else:
                result_text.set(f"Total Carbon Footprint: {carbon['total']:.2f} kg CO2")
            return carbon, suggestion
        return None, ""

    def display_bar_graph():
        carbon, _ = calculate_and_display()
        if carbon:
            plot_bar_graph(carbon)

    def display_pie_chart():
        carbon, _ = calculate_and_display()
        if carbon:
            plot_pie_chart(carbon)

    def save():
        filepath = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if filepath:
            data = {
                "electricity": electricity_var.get(),
                "gas": gas_var.get(),
                "fuel": fuel_var.get(),
                "waste": waste_var.get(),
                "recycling": recycling_var.get(),
                "travel_km": travel_km_var.get(),
                "fuel_efficiency": fuel_efficiency_var.get(),
            }
            carbon, suggestion = calculate_and_display()
            if carbon:
                data["carbon_footprint"] = carbon
                if suggestion:
                    data["suggestion"] = suggestion
                save_data(data, filepath)

    def load():
        filepath = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if filepath:
            data = load_data(filepath)
            if data:
                electricity_var.set(data.get("electricity", "0"))
                gas_var.set(data.get("gas", "0"))
                fuel_var.set(data.get("fuel", "0"))
                waste_var.set(data.get("waste", "0"))
                recycling_var.set(data.get("recycling", "0"))
                travel_km_var.set(data.get("travel_km", "0"))
                fuel_efficiency_var.set(data.get("fuel_efficiency", "0"))

    # GUI setup
    root = tk.Tk()
    root.title("Carbon Footprint Calculator")

    # Variables
    electricity_var = tk.StringVar(value="0")
    gas_var = tk.StringVar(value="0")
    fuel_var = tk.StringVar(value="0")
    waste_var = tk.StringVar(value="0")
    recycling_var = tk.StringVar(value="0")
    travel_km_var = tk.StringVar(value="0")
    fuel_efficiency_var = tk.StringVar(value="0")
    result_text = tk.StringVar(value="")

    # Input Fields
    inputs = [
        ("Average monthly electricity bill (euros):", electricity_var),
        ("Average monthly natural gas bill (euros):", gas_var),
        ("Average monthly fuel bill (euros):", fuel_var),
        ("Monthly waste generated (kg):", waste_var),
        ("Recycled/composted waste (%):", recycling_var),
        ("Yearly business travel (km):", travel_km_var),
        ("Fuel efficiency (L/100km):", fuel_efficiency_var),
    ]

    for i, (label_text, var) in enumerate(inputs):
        tk.Label(root, text=label_text).grid(row=i, column=0, sticky="w", padx=10, pady=5)
        tk.Entry(root, textvariable=var).grid(row=i, column=1, padx=10, pady=5)

    # Buttons
    tk.Button(root, text="Calculate", command=calculate_and_display).grid(row=len(inputs), column=0, padx=10, pady=10)
    tk.Button(root, text="Bar Graph", command=display_bar_graph).grid(row=len(inputs), column=1, padx=10, pady=10)
    tk.Button(root, text="Pie Chart", command=display_pie_chart).grid(row=len(inputs) + 1, column=0, padx=10, pady=10)
    tk.Button(root, text="Save Data", command=save).grid(row=len(inputs) + 1, column=1, padx=10, pady=10)
    tk.Button(root, text="Load Data", command=load).grid(row=len(inputs) + 2, column=0, columnspan=2, padx=10, pady=10)

    # Result Display
    tk.Label(root, textvariable=result_text, fg="blue").grid(row=len(inputs) + 3, column=0, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
