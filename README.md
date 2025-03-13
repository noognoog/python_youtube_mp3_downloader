# 🎵 YouTube MP3 다운로드 & 트리머 🎵

**YouTube 영상을 MP3로 다운로드하고 원하는 구간을 추출하는 파이썬 스크립트**  
`yt-dlp` + `pydub`로 YouTube 음원을 **다운로드** → **트리밍** → **저장** ✂️

---

## 🚀 주요 기능
- **YouTube 영상 MP3 변환** 🎧  
- **시작/종료 시간 지정 트리밍** ⏱️  
  - 앞부분 n초 자르기 ✅
  - 특정 구간 추출하기 (시작~종료) ✅
- **자동 폴더 생성** 📂
- **에러 핸들링** 🛠️ (유효 시간 검증, 오디오 길이 초과 경고)

---

## 📋 필수 조건
- **Python 3.8+** 🐍
- **외부 라이브러리** 📦  



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
