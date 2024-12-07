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
country_for_year = []

for i in range(len(years)):
    if years[i] == year:
        for_every_year.append(expectancy[i])
        country_for_year.append(countries[i])

if len(for_every_year) > 0:
    avg_life = sum(for_every_year) / len(for_every_year)
    max_life = max(for_every_year)
    min_life = min(for_every_year)

    max_index = for_every_year.index(max_life)
    min_index = for_every_year.index(min_life)

    print(f"For the year {year}:")
    print(f"The average life expectancy across all countries was {avg_life:.2f}")
    print(f"The max life expectancy was in {country_for_year[max_index]} with {max_life:.2f}")
    print(f"The min life expectancy was in {country_for_year[min_index]} with {min_life:.2f}")
else:
    print(f"No data available for the year {year}.")


maxi = max(expectancy)
mini = min(expectancy)

max_index = expectancy.index(maxi)
min_index = expectancy.index(mini)

print(f"The overall max life expectancy is: {maxi:.2f} from {countries[max_index]} in {years[max_index]}")
print(f"The overall min life expectancy is: {mini:.2f} from {countries[min_index]} in {years[min_index]}")