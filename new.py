import pandas as pd
import numpy as np
import random
# Number of vehicles

# Vehicle categories and corresponding characteristics

# Generate vehicle brands and models
vehicle_types = {
    "Sports Car": {"engine_range": (3.0, 8.0), "hp_range": (300, 1500), "torque_range": (300, 1200), "time_range": (2.0, 4.5),"index":0}
}

# Generate random vehicle types
vehicle_types_list = np.random.choice(list(vehicle_types.keys()), size=570)
brands = ['Porsche' ,'Lamborghini', 'Ferrari', 'Audi' ,'McLaren', 'BMW' ,'Mercedes-Benz',
 'Chevrolet', 'Ford' ,'Nissan' ,'Aston Martin', 'Bugatti' ,'Dodge', 'Jaguar',
 'Koenigsegg', 'Lexus' ,'Lotus' ,'Maserati', 'Alfa Romeo', 'Ariel', 'Bentley',
 'Mercedes-AMG' ,'Pagani', 'Polestar', 'Rimac' ,'Acura' ,'Mazda', 'Rolls-Royce',
 'Tesla' ,'Toyota', 'W Motors', 'Shelby', 'TVR' ,'Subaru', 'Pininfarina' ,'Kia',
 'Alpine' ,'Ultima']

models = [
["488 GTB",
"911 Turbo S",
"Huracan Evo",
"720S",
"Corvette Z06",
"Mustang Shelby GT500",
"GT-R Nismo",
"Vantage",
"R8 V10 Plus",
"GT R",
"Challenger SRT Hellcat",
"F-Type SVR",
"NSX",
"M4",
"Supra"]]



# Data storage
data = {
    "Car Brand": [],
    "Car Model": [],
    "Year": [],
    "Engine Size (L)": [],
    "Horsepower (hp)": [],
    "Torque (lb-ft)": [],
    "0-60 mph Time (s)": []
}

# Generate the dataset
for vehicle_type in vehicle_types_list:
    brand = np.random.choice(brands)
    model = np.random.choice(models[vehicle_types[vehicle_type]['index']])
    
    specs = vehicle_types[vehicle_type]
    
    engine_size = round(np.random.uniform(*specs["engine_range"]), 2)
    horsepower = int(np.random.uniform(*specs["hp_range"]))
    torque = int(np.random.uniform(*specs["torque_range"]))
    time_0_60 = round(np.random.uniform(*specs["time_range"]), 2)
    
    data["Car Brand"].append(brand)
    data["Car Model"].append(model)
    data["Year"].append(random.randrange(2016,2024))
    data["Engine Size (L)"].append(engine_size)
    data["Horsepower (hp)"].append(horsepower)
    data["Torque (lb-ft)"].append(torque)
    data["0-60 mph Time (s)"].append(time_0_60)

# Convert to DataFrame
df = pd.DataFrame(data)

df.to_csv("data.csv")