import sys
import os
from pytube import YouTube
from pyfiglet import Figlet
from colorama import Fore, Style

preview = Figlet(font='slant')

print(Fore.WHITE + preview.renderText('YOUTUBE DOWNLOADER'))

# print(Fore.WHITE + 'Made by @intosins')
print(Fore.BLUE + 'Discord: ' + Fore.WHITE + '@intosins')

print('')

output_path = os.path.expanduser('~/downloads')

def validate_youtube_link(url):
    try:
        YouTube(url)
        return True
    except Exception:
        return False

def download_youtube_video(url, quality, output_path):
    try:
        youtube = YouTube(url)

        if quality == 'high':
            stream = youtube.streams.get_highest_resolution()
        elif quality == 'low':
            stream = youtube.streams.get_lowest_resolution()
        print(Fore.CYAN + f'Downloading: {youtube.title}')

        print(Fore.CYAN + f'Total size: {stream.filesize // (1024 * 1024)} MB')

        stream.download(output_path)

        print(Fore.CYAN + f'Download completed: {youtube.title}')
    except Exception as e:
        print(Fore.RED + f'Error: {str(e)}')


print(Fore.CYAN + "Type 'exit' if you want to exit")

print('')

print(Fore.CYAN + 'Output Path: ' + output_path)

print('')

while True:
    Input = input(Fore.WHITE + 'Enter the YouTube video URL: ')

    if Input.lower() == 'exit':
        sys.exit(0)

    if validate_youtube_link(Input):
        print(Fore.CYAN + "Type 'return' if you want to return")

        print('')
        
        while True:
            Input2 = input(Fore.WHITE + 'Enter video quality (high or low): ')

            if Input2.lower() == 'exit':
                sys.exit(0)

            if Input2.lower() == 'return':
                break

            if Input2.lower() == 'high' or Input2.lower() == 'low':
                Quality = Input2.lower()
                download_youtube_video(Input, Quality, output_path)
                break
            else:
                print(Fore.RED + 'Invalid video quality. Please provide valid quality (high or low).')
    else:
        print(Fore.RED + 'Invalid YouTube video URL. Please provide a valid link.')