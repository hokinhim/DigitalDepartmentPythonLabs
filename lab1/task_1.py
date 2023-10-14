numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
total_sum = sum(num for num in numbers if num is not None)
total_count = sum(1 for num in numbers if num is not None) + 1
average = total_sum / total_count if total_count else 0
numbers = [average if num is None else num for num in numbers]

print("Измененный список:", numbers)
