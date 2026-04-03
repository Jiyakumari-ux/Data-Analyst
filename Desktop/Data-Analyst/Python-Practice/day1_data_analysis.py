# Day 1 - Basic Data Analysis using Python

# Sample data
names = ["Aman", "Riya", "Jiya", "Rahul"]
ages = [23, 28, 21, 30]
cities = ["Delhi", "Mumbai", "Bhopal", "Delhi"]

# Total people
print("Total People:", len(names))

# Average age
avg_age = sum(ages) / len(ages)
print("Average Age:", avg_age)

# People from Delhi
print("\nPeople from Delhi:")
for i in range(len(names)):
    if cities[i] == "Delhi":
        print(names[i])

# Find oldest person
max_age = max(ages)
index = ages.index(max_age)
print("\nOldest Person:", names[index])
# Count people in each city
city_count = {}

for city in cities:
    if city in city_count:
        city_count[city] += 1
    else:
        city_count[city] = 1

print("\nCity-wise Count:")
for city, count in city_count.items():
    print(city, ":", count)