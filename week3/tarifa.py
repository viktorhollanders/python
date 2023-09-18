mb_per_month = int(input())
n = int(input())

data_saved = mb_per_month

for i in range(n):
    used_data = int(input())
    data_saved += mb_per_month - used_data

print(data_saved)
