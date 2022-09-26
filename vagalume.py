import json
def getlink():
		animeInfo = []
		animeLink = input('Paste catbox link > ')
		with open('vagalume.json', 'r', encoding='utf-8') as json_file:
			json_list = json.loads(json_file.read())
			for i in range(len(json_list)):
				for i2 in range(len(json_list[i]['songs'])):
					try:
						if json_list[i]['songs'][i2]['examples']['mp3'] == animeLink:
							animeInfo.append(json_list[i])
							infoIndex = i2
							
						if json_list[i]['songs'][i2]['examples']['480'] == animeLink:
							animeInfo.append(json_list[i])
							infoIndex = i2
							
						if json_list[i]['songs'][i2]['examples']['720'] == animeLink:
							animeInfo.append(json_list[i])
							infoIndex = i2
							
					except KeyError:
						continue
		if len(animeInfo):
			print('ANIME :', animeInfo[0]['name'])
			print('SONG NAME :', animeInfo[0]['songs'][infoIndex]['name'])
			print('ARTIST :', animeInfo[0]['songs'][infoIndex]['artist'])
			if animeInfo[0]['songs'][infoIndex]['type'] == 1:
				print('TYPE : OPENING')
			elif animeInfo[0]['songs'][infoIndex]['type'] == 2:
				print('TYPE : ENDING')
			elif animeInfo[0]['songs'][infoIndex]['type'] == 3:
				print('TYPE : INSERT')
		else:
					print("ERROR 404: Not Found")
					
while True:
	getlink()
