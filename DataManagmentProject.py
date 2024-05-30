import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path_to_folder = '/Users/jackmoskowitz/Desktop/ISI Project/'
file_name = 'Water_Consumption_in_the_City_of_New_York.csv'
file_name2='Electric_Consumption_And_Cost__2010_-_Feb_2022_ copy.csv'
water_consumption = pd.read_csv(path_to_folder + file_name)
energy_consumption= pd.read_csv(path_to_folder+file_name2)

water_consumption = water_consumption[water_consumption['Year'] >= 2010]

print("Descending values of individual water consumption throughout the years: ")
print(water_consumption.sort_values(by='Per Capita(Gallons per person per day)', ascending=False))

average_per_capita = water_consumption['Per Capita(Gallons per person per day)'].mean()
average_city_consumption = water_consumption['NYC Consumption(Million gallons per day)'].mean()

print("Average gallons per person per day: ", round(average_per_capita, 2))
print("Average gallons consumed by New York City (Millions): ", round(average_city_consumption, 2))

max = water_consumption['Per Capita(Gallons per person per day)'].max()
print("Max gallons consumed in the 21st century per person:", max)

average_energy_use= energy_consumption['Consumption (KW)'].mean()
print("Average energy consumption througout the years: ", average_energy_use)

max_energy_use= energy_consumption['Consumption (KW)'].max()
print("The max energy consumed is: ",max_energy_use)

min_energy_use=energy_consumption['Consumption (KW)'].min()
print("The least amount of energy consumed is: ",min_energy_use)


energy_consumption['Service End Date'] = pd.to_datetime(energy_consumption['Service End Date'])
energy_consumption['Year'] = energy_consumption['Service End Date'].dt.year
merged_data = pd.merge(water_consumption, energy_consumption, on='Year')


grouped_analysis = merged_data.groupby('Year').agg({'Per Capita(Gallons per person per day)': 'mean', 'Consumption (KW)': 'mean'})
print("Grouped and aggregated data by Year: ")
print(grouped_analysis)

grouped_analysis.plot(kind='bar', y=['Per Capita(Gallons per person per day)', 'Consumption (KW)'],color=(['blue','orange']) )

plt.title('Water and Energy Consumption in New York City')
plt.xlabel('Year')
plt.ylabel('Consumption')

plt.show()