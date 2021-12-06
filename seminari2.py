import os
import sys
import subprocess
import requests

#ffmpeg -ss 00:01:30.0 -i BBB.mp4 -c copy -t 00:00:10.0 proba.mp4
#subprocess.call(['ffmpeg', '-ss', "00:01:30.0", '-i', 'BBB.mp4', '-c', 'copy', '-t', "00:00:10.0", 'proba.mp4'])

#ffplay -flags2 +export_mvs proba.mp4 -vf codecview=mv=pf+bf+bb
print("Exercici 1")
#subprocess.call(['ffplay', '-flags2', '+export_mvs', 'proba.mp4', '-vf', "codecview=mv=pf+bf+bb"])

print("Exercici 2")
print("diga'm en quin minut vols tallar el vídeo")
'''
n = int(input())
m = str(n+1)
n = str(n)
start = str("00:0"+n+":00.0")
end = str("00:0"+m+":00.0")
subprocess.call(['ffmpeg', '-ss', start, '-i', 'BBB.mp4', '-c', 'copy', '-t', "00:01:00.0", 'tall.mp4'])
subprocess.call(['ffmpeg', '-i', 'tall.mp4', '-map', "0:a", 'tall_mp3-audio.mp3'])
subprocess.call(['ffmpeg', '-i', 'tall.mp4', '-vn', '-acodec', 'copy', 'tall_aac-audio.aac'])
#ffmpeg -i input-video.avi -vn -acodec copy output-audio.aac
#ffmpeg -i input.mp4 -map 0:a output.mp3
'''

print("exercici 4")

#he intentat descarregar-los des de la web però no se perquè no ho aconsegueixo.
#url = 'https://www.opensubtitles.com/es/subtitles/dune-2021-1080p-hdrip-x264-ac3-evo-es?download=1'
#response = requests.get(url, allow_redirects=True)
#open("dunesubtitles.srt", 'wb').write(response.content)
#subprocess.call(['ffplay', '-i', 'BBB.mp4', '-ss', start, '-vf', 'subtitles=Dune 2021 1080p HDRip X264 AC3-EVO.srt', '-t', end])
#subprocess.call(['ffplay', '-i', 'BBB.mp4', '-vf', 'subtitles=Dune_subtitles.srt'])


subprocess.call(['ffmpeg', '-i', 'BBB.mp4', '-f', 'srt', '-i', 'Dune_subtitlesNOU.srt', '-map', "0:0", '-map', "0:1", '-map', "1:0", "-c:v", 'copy', "-c:a", 'copy', "-c:s", "mov_text", 'BBBsubs.mp4'])



