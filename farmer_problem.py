'''
Farmer Problem:
Mahesh is a farmer and owns 80 acres of land. His land is equally divided into 5 segments. He grows tomatoes in the 1st segment, potatoes in the 2nd segment, cabbage in the 3rd segment, sunflower in the 4th segment and sugarcane in the 5th segment. He is converting his land from chemical-driven farming to chemical-free farming. Mahesh starts with the conversion of vegetables into chemical-free produce. He spends the first 6 months doing the same. He then converts the sunflower land bank into chemical-free farming. This takes him another 4 months. Finally, he converts sugarcane into chemical-free farming over the next 4 months. He gets a yield of the following for tomatoes. 30% of his tomato land gives him 10 tonne yield per acre. The remaining 70% of his tomato land gives him 12 tonnes yield per acre. The selling price of tomato is Rs. 7 per Kg. The yield of potatoes is 10 tonnes per acre. He sells each kg at Rs. 20. The yield of cabbage is 14 tonnes per acre. He sells each kg at Rs. 24. The yield of sunflowers is 0.7 tonnes per acre. He sells each kg at Rs. 200. The yield of sugarcane is 45 tonnes per acre. He sells each tonne at Rs. 4,000. All the crops are sowed at the same time. Mahesh gets the above yield at the above-mentioned rate in one crop cycle across his entire land of 80 acres. What is
a. The overall sales achieved by Mahesh from the 80 acres of land.
b. Sales realisation from chemical-free farming at the end of 11 months?
'''

land = 80  # acres

# 16 acres for each crop
acres_per_crop = land // 5

# Tomatoes
tom_30 = 0.3 * acres_per_crop
tom_70 = 0.7 * acres_per_crop
tomato_30 = 10 * tom_30 * 1000  # tonnes to kg
tomato_70 = 12 * tom_70 * 1000  # tonnes to kg
tomato_sp = 7  # Rs per kg
tomato_cost = (tomato_30 + tomato_70) * tomato_sp

# Potatoes
potato = 10 * acres_per_crop * 1000  # tonnes to kg
potato_sp = 20 # Rs per kg
potato_cost = potato * potato_sp

# Cabbage
cabbage = 14 * acres_per_crop * 1000
cabbage_sp = 24  # Rs per kg
cabbage_cost = cabbage * cabbage_sp

# Sunflower
sunflower = 0.7 * acres_per_crop * 1000
sunflower_sp = 200 # Rs per kg
sunflower_cost = sunflower * sunflower_sp

# Sugarcane
sugarcane = 45 * acres_per_crop  # already in tonnes
sugarcane_sp = 4000  # Rs per tonne
sugarcane_cost = sugarcane * sugarcane_sp

# Total sales
overall_sales = tomato_cost + potato_cost + cabbage_cost + sunflower_cost + sugarcane_cost

print(f"Total sales from 80 acres: Rs. {overall_sales:,.2f}")





'''
6 months for vegetables(tomato, potato, cabbage) + 4 months for sunflower + 4 months for sugarcane
Total - 14 months
but we are asked only for 11 months, so we must consider only vegetables and sunflower
'''

chemical_free_sales = tomato_cost + potato_cost + cabbage_cost + sunflower_cost
print(f"Chemical-Free Sales by end of 11 months: Rs. {chemical_free_sales:,.2f}")