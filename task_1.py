numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
spisok = numbers[0:4] + numbers[5:]
sum_ = sum(spisok)
len_ = len(numbers)
SAr = sum_/len_
numbers[4] = SAr
# TODO заменить значение пропущенного элемента средним арифметическим
print("Измененный список:", numbers)