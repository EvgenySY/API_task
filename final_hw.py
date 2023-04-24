import requests


base_url = 'https://swapi.dev/api'
people_url = '/people'
dart_number = '/4'
dart_url = base_url+people_url+dart_number
print("Ссылка на информацию о Дарт Вейдере: " + dart_url + "\n")
result_get = requests.get(dart_url)
check_get = result_get.json()
films = check_get.get('films')
print("Ссылки на фильмы с участием Дарт Вейдера: \n" + str(films) + "\n")

for k in films:
    result_get_1 = requests.get(k)
    check_get_1 = result_get_1.json()
    characters = check_get_1.get('characters')
    print("Ссылки на информацию о всех героях из фильма " + str(k) + ": \n" + str(characters))
    print("Имена героев из фильма " + str(k))
    for i in characters:
        result_get_2 = requests.get(i)
        check_get_2 = result_get_2.json()
        name = check_get_2.get('name')
        print(name)
        fl = open("names.txt", "a", encoding='utf-8')
        fl.write(name)
        fl.write("\n")
        fl.close()
    print("\n")

with open('names.txt', 'r') as f:
    lst = set(f.readlines())
with open('names.txt', 'w') as f:
    f.write(''.join(lst))
