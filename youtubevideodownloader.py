from pytube import YouTube
link=input("Enter the video link:")
youtube_1=YouTube(link)
print(youtube_1.title)
print(youtube_1.thumbnail_url)
videos=youtube_1.streams.all()
vid=list(enumerate(videos))
for i in vid:
    print(i)
print()
strm=int(input("Enter the video stream:"))
videos[strm].download()
print("Downloaded successfully")