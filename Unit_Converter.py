import tkinter as tk
from tkinter import ttk

# meters_per_unit: how many meters are in 1 <unit>
METER_PER_UNIT = {
    "meter": 1.0,
    "centimeter": 0.01,
    "millimeter": 0.001,
    "kilometer": 1000.0,
    "inch": 0.0254,
    "feet": 0.3048,
    "yard": 0.9144,
    "mile": 1609.344
}

def length_converter(value, from_unit, to_unit):
    # Convert value -> meters -> target unit
    meters = value * METER_PER_UNIT[from_unit]
    return meters / METER_PER_UNIT[to_unit]

def convert_unit():
    try:
        value = float(entry_value.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()

        if not from_unit or not to_unit:
            label_result.config(text="Please select both units")
            return

        result = length_converter(value, from_unit, to_unit)
        label_result.config(text=f"Result: {result:.4f} {to_unit}")
    except ValueError:
        label_result.config(text="Please enter a valid number")
    except KeyError:
        label_result.config(text="Unknown unit selected")

root = tk.Tk()
root.title("Unit Converter")
root.geometry("420x420")

# Category (kept in case you want to add more types later)
label_category = ttk.Label(root, text="Select Category:")
label_category.pack(pady=5)
combo_category = ttk.Combobox(root, values=["Length"], state="readonly")
combo_category.current(0)
combo_category.pack(pady=10)

# From unit
label_from = ttk.Label(root, text="Convert from:")
label_from.pack(pady=5)
units_list = list(METER_PER_UNIT.keys())
combo_from = ttk.Combobox(root, values=units_list, state="readonly")
combo_from.current(0)
combo_from.pack(pady=10)

# To unit
label_to = ttk.Label(root, text="Convert to:")
label_to.pack(pady=5)
combo_to = ttk.Combobox(root, values=units_list, state="readonly")
combo_to.current(1)
combo_to.pack(pady=10)

# Value entry
label_value = ttk.Label(root, text="Enter Value:")
label_value.pack(pady=5)
entry_value = ttk.Entry(root)
entry_value.pack(pady=10)

# Convert button
button_convert = ttk.Button(root, text="Convert", command=convert_unit)
button_convert.pack(pady=12)

# Result label
label_result = ttk.Label(root, text="Result:", font=("Arial", 16))
label_result.pack(pady=18)

root.mainloop()
