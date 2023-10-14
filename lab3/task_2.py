# TODO Напишите функцию find_common_participants
def find_common_participants(first_str, second_str, delimiter=','):
    return sorted(set(first_str.split(delimiter)) & set(second_str.split(delimiter)))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '|'))
