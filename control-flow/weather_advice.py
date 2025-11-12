# This script provides clothing advice based on the weather condition input by the user.

# Example usage:
# If the user inputs "sunny", the output will be:
# Wear a t-shirt and sunglasses.
# If the user inputs "rainy", the output will be:
# Don't forget your umbrella and a raincoat.
# If the user inputs "cold", the output will be:
# Make sure to wear a warm coat and a scarf.
# If the user inputs anything else, the output will be:
# Sorry, I don't have recommendations for this weather. 


weather_condition = input("What's the weather like today? (sunny/rainy/cold):")

if (weather_condition == "sunny"):
    advice = "Wear a t-shirt and sunglasses."
elif (weather_condition == "rainy"):
    advice = "Don't forget your umbrella and a raincoat."
elif (weather_condition == "cold"):
    advice = "Make sure to wear a warm coat and a scarf."
else:
    advice = "Sorry, I don't have recommendations for this weather."

print(advice)

