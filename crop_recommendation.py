# Crop Recommendation System

print("Crop Recommendation System\n")

# Input
soil = input("Enter soil type (loamy, sandy, clay, silt, peat, chalk): ").lower()

# Rainfall input
while True:
    try:
        rainfall = float(input("Enter rainfall (mm): "))
        break
    except ValueError:
        print("Enter a number")

# Temperature input
while True:
    try:
        temperature = float(input("Enter temperature (°C): "))
        break
    except ValueError:
        print("Enter a number")

# Functions for each soil

def loamy_soil(rainfall, temperature):
    if rainfall > 500 and 20 <= temperature <= 35:
        return ["Rice", "Sugarcane", "Maize"]
    else:
        return ["Wheat", "Vegetables"]

def sandy_soil(rainfall, temperature):
    if rainfall < 400 and temperature >= 25:
        return ["Groundnut", "Millet", "Cotton"]
    else:
        return ["Watermelon", "Peanut"]

def clay_soil(rainfall, temperature):
    if 400 <= rainfall <= 800 and 18 <= temperature <= 30:
        return ["Wheat", "Barley", "Soybean"]
    else:
        return ["Rice", "Broccoli"]

def silt_soil(rainfall, temperature):
    if rainfall >= 500:
        return ["Rice", "Wheat", "Sugarcane"]
    else:
        return ["Maize", "Vegetables"]

def peat_soil(rainfall, temperature):
    if temperature < 25:
        return ["Potato", "Carrot", "Onion"]
    else:
        return ["Lettuce", "Cabbage"]

def chalk_soil(rainfall, temperature):
    if rainfall < 600:
        return ["Barley", "Spinach", "Beetroot"]
    else:
        return ["Wheat", "Clover"]

# Main logic

if soil == "loamy":
    crops = loamy_soil(rainfall, temperature)

elif soil == "sandy":
    crops = sandy_soil(rainfall, temperature)

elif soil == "clay":
    crops = clay_soil(rainfall, temperature)

elif soil == "silt":
    crops = silt_soil(rainfall, temperature)

elif soil == "peat":
    crops = peat_soil(rainfall, temperature)

elif soil == "chalk":
    crops = chalk_soil(rainfall, temperature)

else:
    print("Invalid soil type")
    exit()

# Output

print("\nRecommended crops:")

for crop in crops:
    print("-", crop)
