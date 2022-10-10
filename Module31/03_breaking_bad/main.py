import requests
import json


request_deaths = requests.get('https://www.breakingbadapi.com/api/deaths')
data_death = json.loads(request_deaths.text)

with open('breakingbad_deaths.json', 'w') as file:
    json.dump(data_death, file, indent=4)

request_episodes = requests.get('https://www.breakingbadapi.com/api/episodes')
data_episodes = json.loads(request_episodes.text)
# with open('breakingbad_episodes.json', 'w') as file:
#     json.dump(data2, file, indent=4)

with open('breakingbad_deaths.json', 'r') as file:
    deaths = json.load(file)
    max_deaths = {'death': []}
    max_count_death = 0
    # ищу серию и эпизод с максимальным количеством смертей
    for death in deaths:
        if death["number_of_deaths"] > max_count_death:
            max_count_death = death["number_of_deaths"]
            max_deaths['season'] = death['season']
            max_deaths['episode'] = death['episode']
            max_deaths['number_of_deaths'] = death['number_of_deaths']
    # заношу всех убитых из найденной серии в словарь
    for death in deaths:
        if death['season'] == max_deaths['season'] and death['episode'] == max_deaths['episode']:
            max_deaths['death'].append(death['death'])
    for episode in data_episodes:
        if int(episode['season']) == max_deaths['season'] and int(episode['episode']) == max_deaths['episode']:
            max_deaths['episode_id'] = episode['episode_id']

print(f'1. ID эпизода: {max_deaths["episode_id"]}\n'
      f'2. Номер сезона: {max_deaths["season"]}\n'
      f'3. Номер эпизода: {max_deaths["episode"]}\n'
      f'4. Общее количество смертей: {max_deaths["number_of_deaths"]}\n'
      f'5. Список погибших: {max_deaths["death"]}')
with open('max_count_deaths.json', 'w') as file:
    json.dump([max_deaths], file, indent=4)
