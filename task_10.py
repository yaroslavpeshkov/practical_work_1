import local_ru as r

flight_number = input(r.FLIGHT_NUMBER)
airline_ru = input(r.AIRLINE_RU)
airline_eng = input(r.AIRLINE_ENG)
destination_ru = input(r.DESTINATION_RU)
destination_eng = input(r.DESTINATION_ENG)
print(r.BOARDING, flight_number, airline_ru, r.TO, destination_ru)
print('This is the final boarding call for', airline_eng, 'flight', flight_number, 'to', destination_eng)
