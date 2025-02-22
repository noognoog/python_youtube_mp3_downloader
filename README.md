# python_youtube_mp3_downloader

- Install yt-dlp, ffmpeg-python library before using this code
- Replace "video_url" in the Usage example code block with the actual YouTube video URL

  
```python
!pip install yt-dlp
!pip install ffmpeg-python
```

```python
# Usage example
if __name__ == "__main__":
    # YouTube video URL
    video_url = "https://www.youtube.com/watch?v=Zbo7UY8dxh8"
    
    # Execute download
    output_file = download_youtube_mp3(video_url, "downloads")
    
    if output_file:
        print(f"File successfully saved to: {output_file}")
    else:
        print("Download failed")
```
