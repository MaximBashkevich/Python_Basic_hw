violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
my_song = []
count_songs = int(input('Сколько песен выбрать? '))
for i in range(count_songs):
    print('Название ' + str(i +1) + '-й песни: ', end = '')
    song = input()
    my_song.append(song)

sum_time = 0
for i_my_song in my_song:
    for index_song in violator_songs:
        if index_song[0] == i_my_song:
            sum_time += index_song[1]

print('Общее время звучания песен: ' + str(round(sum_time, 2)) + ' минут')


