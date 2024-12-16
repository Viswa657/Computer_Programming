import os
import webbrowser
import plotly.express as px
import pandas as pd
from fpdf import FPDF
import Formula as calculations
import suggestions as advice

# Save Plotly charts to PNG files 
def export_chart(fig, filename):
    output_folder = "charts"
    os.makedirs(output_folder, exist_ok=True)
    file_path = os.path.join(output_folder, filename)
    fig.write_image(file_path, format='png')  # Save as PNG
    return file_path

# Generate Pie Chart and Bar Chart
def generate_monthly_charts(month, data):
    labels = ["Energy", "Waste", "Travel"]
    values = data
    colors = ['#ff9999', '#66b3ff', '#99ff99']

    # Pie Chart
    fig_pie = px.pie(
        names=labels,
        values=values,
        title=f"{month} Emissions Breakdown",
        color=labels,
        color_discrete_map=dict(zip(labels, colors)),
        hole=0.3
    )
    pie_chart_path = export_chart(fig_pie, f"{month}_breakdown_pie.png")

    # Bar Chart
    df = pd.DataFrame({'Category': labels, 'Emissions': values})
    fig_bar = px.bar(
        df,
        x="Category",
        y="Emissions",
        color="Category",
        title=f"{month} Emissions by Category",
        color_discrete_sequence=colors,
        text="Emissions"
    )
    fig_bar.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    fig_bar.update_layout(yaxis_title="Emissions (metric tons)", xaxis_title="Category")
    bar_chart_path = export_chart(fig_bar, f"{month}_breakdown_bar.png")

    return pie_chart_path, bar_chart_path

# Generate PDF Report
def generate_pdf_report(data_entries, months):
    report = FPDF()
    report.set_auto_page_break(auto=True, margin=15)
    report.add_page()
    report.set_font("Arial", "B", 16)
    report.cell(200, 10, txt="Monthly Carbon Emissions Report", ln=True, align="C")
    report.set_font("Arial", size=12)
    report.ln(10)

    for month, data in zip(months, data_entries):
        report.set_font("Arial", "B", 12)
        report.cell(200, 10, txt=f"{month} Overview:", ln=True, align="L")
        report.set_font("Arial", size=12)
        report.cell(200, 10, txt=f"Total Emissions: {sum(data):.2f} metric tons CO2", ln=True)
        report.multi_cell(0, 10, txt=f"Energy Advice:\n{advice.energy_suggestion(data[0])}")
        report.multi_cell(0, 10, txt=f"Waste Advice:\n{advice.waste_suggestion(data[1])}")
        report.multi_cell(0, 10, txt=f"Travel Advice:\n{advice.travel_suggestion(data[2])}")
        report.ln(5)

        # Add charts as images
        pie_chart_path, bar_chart_path = generate_monthly_charts(month, data)
        if os.path.exists(pie_chart_path):
            report.image(pie_chart_path, x=10, w=180)
            report.ln(10)
        if os.path.exists(bar_chart_path):
            report.image(bar_chart_path, x=10, w=180)
            report.ln(10)

    report.output("carbon_emissions_report.pdf")

# Main Function
def main():
    months = input("Enter the months for analysis, separated by commas (e.g., Jan, Feb, Mar): ").split(",")
    months = [month.strip() for month in months]

    data_entries = []

    for month in months:
        print(f"\nData for {month}:")
        try:
            elec_bill = float(input("Monthly electricity bill: "))
            gas_bill = float(input("Monthly natural gas bill: "))
            fuel_cost = float(input("Monthly fuel bill: "))
            waste = float(input("Waste generated per month (kg): "))
            recycle_rate = float(input("Recycling rate (%): "))
            travel_distance = float(input("Annual travel distance (km): "))
            fuel_efficiency = float(input("Average fuel efficiency (km/L): "))

            energy = calculations.sum_energy_usage(elec_bill, gas_bill, fuel_cost)
            waste_emissions = calculations.sum_waste(waste, recycle_rate)
            travel_emissions = calculations.sum_business_travel(travel_distance, fuel_efficiency)

            data_entries.append((energy, waste_emissions, travel_emissions))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            return

    # Generate PDF Report
    generate_pdf_report(data_entries, months)
    print("\nReport generated as 'carbon_emissions_report.pdf'.")
    webbrowser.open("carbon_emissions_report.pdf")

if __name__ == "__main__":
    main()
