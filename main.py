# use yt-dlp youtube video and music download :
from yt_dlp import YoutubeDL
from sys import path
from os import getcwd, chdir
import yt_dlp
print(" Old cwd = " + getcwd())#取得當前系統環境位置
chdir(path[0])#將當前環境位置設為當前"檔案位置"
print(" New cwd = " + getcwd())

def check_url(url):
	if 'playlist' in url:#為播放清單時
		return 'playlist',url
	elif 'list' in url:#為播放清單的其中一部影片時
		url = url.split('&list')[0]
		return 'video',url
	else:#為單一影片時
		return 'video',url

def download(url_type,url):
	download_model='music' if (input("輸入1下載音樂，輸入任意為下載影片:")=='1') else 'video'
	print("=============執行================")
	if (url_type=='playlist'):
		yt_playlist(url,download_model)
	else:
		yt_video(url,download_model)

def yt_video(url,download_model):
	ydl_opts = {'quiet': True}
	video_info = YoutubeDL(ydl_opts).extract_info(url=url, download=False)
	try:
		
		print("  標題:",video_info.get('title'))
		print("  網址:",url)
		print("  長度:",video_info.get('duration'),"sec")
		print("==========開始下載===============")
		#download youtube video or music:
		if download_model=='music':
			file_name = (f"{video_info.get('title')}.mp3").replace('/','-').replace('\\','-')#設定檔案名
			file_path = file_name;
			
			ydl_opts = {
				#'format': 'bestvideo',#設定最佳影片檔(不含聲音)
				'format' : 'bestaudio',#設定最佳聲音檔(不含影片)
				#'format' : 'best',#最佳包含聲音的影片檔(為預設可不用打)
				'outtmpl': f'{file_path}',#設定輸出路徑及檔名
				'quiet': True#安靜模式
			}
		else:
			file_name = (f"{video_info.get('title')}.mp4").replace('/','-').replace('\\','-')#設定檔案名
			file_path = file_name;
			
			ydl_opts = {
				#'format': 'bestvideo',#設定最佳影片檔(不含聲音)
				#'format' : 'bestaudio',#設定最佳聲音檔(不含影片)
				#'format' : 'best',#最佳包含聲音的影片檔(為預設可不用打)
				'outtmpl': f'{file_path}',#設定輸出路徑及檔名
				'quiet': True#安靜模式
			}
			
		with YoutubeDL(ydl_opts) as ydl:
			try:
				ydl.download(url)
				print(f"  影片:{video_info.get('title')}\n  已下載\n==========================")
			except:
				print("  下載失敗")
				input("  按enter退出")
				exit(0)
		print("  下載完成");
	except:
		print("  下載失敗")
		input("  按enter退出")
		exit(0)

def yt_playlist(url,download_model):
	#get infomation
	try:
		ydl_opts = {'extract_flat': True,'quiet': True}
		
		with YoutubeDL(ydl_opts) as ydl:
			playlist_info = ydl.extract_info(url, download=False)
			
		playlist_count=playlist_info.get('playlist_count')#播放清單影片數量
		print("  播放清單影片數量=",playlist_count);
		for i in range(playlist_count):
			video_info=playlist_info.get('entries')[i]
			print(f"影片{i+1}:")
			print("  標題:",video_info.get('title'))
			print("  網址:",video_info.get('url'))
			print("  長度:",video_info.get('duration'),'sec')
		print('==========開始下載===============')
		
		#download youtube playlist video or music:
		for i in range(playlist_count):
			video_info=playlist_info.get('entries')[i]
			if download_model=='music':
				file_name = (f"{video_info.get('title')}.mp3").replace('/','-').replace('\\','-')#設定檔案名
				file_path = file_name;
				ydl_opts = {
					#'format': 'bestvideo',#設定最佳影片檔(不含聲音)
					'format' : 'bestaudio',#設定最佳聲音檔(不含影片)
					#'format' : 'best',#最佳包含聲音的影片檔(為預設可不用打)
					'outtmpl': f'{file_path}',#設定輸出路徑及檔名
					'quiet': True#安靜模式
				}
			else:
				file_name = (f"{video_info.get('title')}.mp4").replace('/','-').replace('\\','-')#設定檔案名
				file_path = file_name;
				ydl_opts = {
					#'format': 'bestvideo',#設定最佳影片檔(不含聲音)
					#'format' : 'bestaudio',#設定最佳聲音檔(不含影片)
					#'format' : 'best',#最佳包含聲音的影片檔(為預設可不用打)
					'outtmpl': f'{file_path}',#設定輸出路徑及檔名
					'quiet': True#安靜模式
				}
				
			with YoutubeDL(ydl_opts) as ydl:
				try:
					ydl.download(video_info.get('url'))
					print(f"  影片:{video_info.get('title')}\n  已下載\n==========================")
				except:
					print("  跳過無法下載項目\n==========================")
		print("  下載完成")
	except:
		print("  下載失敗")
		input("  按enter退出")
		exit(0)
		

if __name__ == '__main__':
	url=input('輸入網址:')
	#url='https://youtu.be/vbaYdfIUg_A'
	#url='https://youtube.com/playlist?list=PLJvnvm6opLtj8gNPtra2EDL-zJ4a5xBlJ'
	while url!='':
		url_type,url=check_url(url)
		download(url_type,url)
		url=input('輸入網址:')
