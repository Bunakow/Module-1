my_dict = {'Sara':1985, 'Simon':1999, 'Valera':1977}
print('Словарь:', my_dict)
print('Год рождения Sara: ',my_dict['Sara'])
print('Год рождения Dima:', my_dict.get('Dima', 'Нет такого ключа'))
my_dict.update({'Diana':1998, 'Alex':2001})
removed_year=my_dict.pop('Sara')
print('Значение удалённого элемента \'Sara\':', removed_year)
print('Изменённый словарь:', my_dict)
my_set={1, 2, 3, 4, 5, 1, 2, 3, 4, True, 'Masha', "Masha"}
print('Множество',my_set)
my_set.add(11)
my_set.add('Luna')
my_set.remove(1)
print('Изменённое множество',my_set)






