current_row = [1, 2, 1]
next_row = [1]
for i in range(len(current_row) - 1):
    neighbor_sum = current_row[i] + current_row[i + 1]
    next_row.append(neighbor_sum)


next_row.append(1)

print(next_row)  # 