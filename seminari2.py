import os
import sys
import subprocess
import requests
from videoprops import get_audio_properties
from videoprops import get_video_properties
class semi():
	def exercici1(self):
		subprocess.call(['ffplay', '-flags2', '+export_mvs', 'BBB.mp4', '-vf', "codecview=mv=pf+bf+bb"])

	def exercici2(self):
		print("diga'm en quin minut vols tallar el vídeo")
		n = int(input())
		m = str(n+1)
		n = str(n)
		start = str("00:0"+n+":00.0")
		end = str("00:0"+m+":00.0")
		#Fem el video d'un minut
		subprocess.call(['ffmpeg', '-ss', start, '-i', 'BBB.mp4', '-c', 'copy', '-t', "00:01:00.0", 'tall.mp4'])
		#exportem l'àudio com mp3
		subprocess.call(['ffmpeg', '-i', 'tall.mp4', '-map', "0:a", 'tall_mp3-audio.mp3'])
		#exportem l'àudio AAC amb menor bitrate
		subprocess.call(['ffmpeg', '-i', 'tall.mp4', '-vn', '-acodec', 'copy', 'tall_aac-audio.aac'])
		#creem el contenidor
		subprocess.call(['ffmpeg', '-i', 'tall.mp4', '-i', 'tall_mp3-audio.mp3', '-i', 'tall_aac-audio.aac', '-map', '0:v', '-map', '1:a', '-map', '2:a', 'paquet.mp4'])

	def exercici3(self):
		video_props = get_video_properties('paquet.mp4')
		audio_props = get_audio_properties('paquet.mp4')
		#cal instal·lar l'asuntu a: https://github.com/mvasilkov/python-get-video-propertie"
		tipus_broadcast = {
			"DVB": {
				"video": ["mpeg2","h264"],
				"audio": ["aac", "ac3", "mp3", "mp2", "mp1"]
			},
			"ATSC": {
				"video": ["mpeg2","h264"],
				"audio": ["aac"]
			},
			"ISDB": {
				"video": ["mpeg2","h264"],
				"audio": ["ac3"]
			},
			"DTMB": {
				"video": ["mpeg2","h264","avs","avs+"],
				"audio": ["dra", "aac", "ac3", "mp1", "mp2", "mp3"]
			}	
		}           
		resultat = []
		for key in tipus_broadcast.keys():
			for i in tipus_broadcast[key]["video"]:
				if video_props['codec_name'] == i:
					for j in tipus_broadcast[key]["audio"]:
						if audio_props['codec_name'] == j:
							resultat.append(key)
		if resultat:
			print(resultat)
		else:
			print("Error!")
		
		#pijada:
		print(f''' 
			Resolution: {video_props['width']}×{video_props['height']}
		''')

	def exercici4(self):
	#he intentat descarregar-los des del meu propi github però no se perquè no va
	#a més, ho he comprovat amb altres estudiants, que ho fan de manera molt similar i els hi funciona	
		'''
		response = requests.get('https://github.com/maxmmelo/Seminari2/blob/main/Dune_subtitlesNOU.srt')
		print(response.content)
		with open("dunesubtitles.srt", 'wb') as f:
		f.write(response.content)
		'''
		subprocess.call(['ffmpeg', '-i', 'BBB.mp4', '-f', 'srt', '-i', 'Dune_subtitlesNOU.srt', '-map', "0:0", '-map', "0:1", '-map', "1:0", "-c:v", 'copy', "-c:a", 'copy', "-c:s", "mov_text", 'BBBprovs.mp4'])	

