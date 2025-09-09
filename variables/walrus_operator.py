# x = 3
# print(x)

print(x := 3)  # walrus operator
print(x)

# t = (1,)
# print(type(t))

yearly_salaries = [
    1000,
    2000,
    3000,
    4000,
    5000,
]

# V1
# yearly_salaries_statistics = {
#     "count": len(yearly_salaries),
#     "summa": sum(yearly_salaries),
#     "average": sum(yearly_salaries) / len(yearly_salaries),
# }

# v2
# count_of_salaries = len(yearly_salaries)
# sum_of_salaries = sum(yearly_salaries)

# yearly_salaries_statistics = {
#     "count": count_of_salaries,
#     "summa": sum_of_salaries,
#     "average": sum_of_salaries / count_of_salaries,
# }

# V3
yearly_salaries_statistics = {
    "count": (count_of_salaries := len(yearly_salaries)),
    "summa": (sum_of_salaries := sum(yearly_salaries)),
    "average": sum_of_salaries / count_of_salaries,
}