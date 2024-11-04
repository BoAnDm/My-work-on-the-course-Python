# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, sign = ","):
    participant = list(set(first_group.split(sign)).intersection(set(second_group.split(sign))))
    participant.sort()
    return participant

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, "|"))