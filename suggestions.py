def energy_suggestion(usage):
    if usage < 5:
        return "Great efficiency! Maintain low usage with renewable energy."
    elif usage < 10:
        return "Moderate usage. Use energy-efficient appliances."
    return "High usage. Prioritize insulation and renewables."

def waste_suggestion(waste):
    if waste < 2:
        return "Minimal waste. Continue composting and recycling!"
    elif waste < 5:
        return "Moderate waste. Reduce single-use items."
    return "High waste. Focus on reducing disposables."

def travel_suggestion(travel):
    if travel < 2:
        return "Minimal emissions. Well done!"
    elif travel < 5:
        return "Moderate emissions. Consider carpooling."
    return "High emissions. Use fuel-efficient or electric vehicles."
