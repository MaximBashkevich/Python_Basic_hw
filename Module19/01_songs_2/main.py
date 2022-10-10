violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

nums_lst = ['первой', 'второй', 'третьей', 'четвертой', 'пятой', 'шестой', 'седьмой', 'восьмой']
sum_time = 0
songs_count = int(input('Сколько песен выбрать: '))

for i_song in range(songs_count):
  song = input('Название {} песни: '.format(nums_lst[i_song]))
  if song in violator_songs:
    sum_time += violator_songs[song]

print('Общее время звучания песен:', sum_time)
