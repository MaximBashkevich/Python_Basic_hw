import re


def check_auto_number(auto_numbers: str) -> None:
    car = re.findall(r"[АВЕКМНОРСТУХавекмнорсту]\d{3}[АВЕКМНОРСТУХавекмнорсту]{2}\d{2,3}", auto_numbers)
    taxi = re.findall(r"[АВЕКМНОРСТУХавекмнорсту]{2}\d{5,6}", auto_numbers)
    print(f'Список номеров частных автомобилей: {car}\nСписок номеров такси: {taxi}')


auto_numbers = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'
check_auto_number(auto_numbers)
