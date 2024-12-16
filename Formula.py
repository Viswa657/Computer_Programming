# Calculate the total carbon footprint from energy usage
def sum_energy_usage(electricity, gas, fuel):
    """
    electricity: Annual electricity usage in kWh
    gas: Annual gas usage in cubic meters
    fuel: Annual fuel consumption in liters
    """
    # Updated coefficients based on average emission factors
    electricity_emission_factor = 0.000233  # metric tons of CO2 per kWh
    gas_emission_factor = 0.002  # metric tons of CO2 per cubic meter
    fuel_emission_factor = 2.31  # metric tons of CO2 per liter
    
    return (
        (electricity * electricity_emission_factor) +
        (gas * gas_emission_factor) +
        (fuel * fuel_emission_factor)
    )

# Calculate carbon emissions from waste
def sum_waste(waste, recycle):
    """
    waste: Annual waste generated in kilograms
    recycle: Percentage of waste that is recycled
    """
    # Updated coefficients
    waste_emission_factor = 0.5  # metric tons of CO2 per kg for non-recycled waste
    recycled_waste_reduction = 0.85  # 85% reduction for recycled materials
    
    non_recycled_waste = waste * ((100 - recycle) / 100)
    return non_recycled_waste * waste_emission_factor * (1 - recycled_waste_reduction)

# Calculate carbon emissions from business travel
def sum_business_travel(distance, fuel_efficiency):
    """
    distance: Total distance traveled in kilometers
    fuel_efficiency: Vehicle fuel efficiency in kilometers per liter
    """
    # Updated emission factor for gasoline (in metric tons of CO2 per liter)
    fuel_emission_factor = 2.31  # metric tons of CO2 per liter
    
    fuel_used = distance / fuel_efficiency
    return fuel_used * fuel_emission_factor
