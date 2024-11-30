with open('life-expectancy.csv') as file:
    lines = file.readlines()

countries = []
years = []
expectancy = []

for line in lines[1:]:
    
    information = line.strip().split(',')
    countries.append(information[0])
    years.append(int(information[2]))
    expectancy.append(float(information[3]))

year = int(input("Enter the year of interest: "))


for_every_year = []

for i in range(len(years)):
    if years[i] == year:
        for_every_year.append(expectancy[i])

if len(for_every_year) > 0:
    avg_life = sum(for_every_year) / len(for_every_year)
    print(f"The average life expectancy in {year} is {avg_life:.2f}")
else:
    print(f"No data available for the year {year}.")

    
maxi = max(expectancy)
mini = min(expectancy)

max_index = expectancy.index(maxi)
min_index = expectancy.index(mini)

print(f"The overall max life expectancy is: {maxi} from {countries[max_index]} in {years[max_index]}")
print(f"The overall min life expectancy is: {mini} from {countries[min_index]} in {years[min_index]}")