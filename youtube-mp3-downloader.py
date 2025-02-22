from pytube import YouTube
from moviepy.editor import *
import os

def download_youtube_mp3(url, output_path="."):
    """
    YouTube 영상을 MP3로 다운로드하는 함수
    
    Parameters:
        url (str): YouTube 영상 URL
        output_path (str): 저장할 경로 (기본값: 현재 디렉토리)
    
    Returns:
        str: 저장된 MP3 파일 경로
    """
    try:
        # YouTube 객체 생성
        yt = YouTube(url)
        
        # 영상 제목에서 부적절한 문자 제거
        video_title = "".join([c for c in yt.title if c.isalnum() or c.isspace()]).rstrip()
        
        print(f"다운로드 시작: {yt.title}")
        
        # 오디오 스트림 선택 및 다운로드
        audio_stream = yt.streams.filter(only_audio=True).first()
        temp_file = audio_stream.download(output_path=output_path, filename=f"{video_title}.mp4")
        
        # MP4를 MP3로 변환
        mp3_path = os.path.join(output_path, f"{video_title}.mp3")
        video_clip = AudioFileClip(temp_file)
        video_clip.write_audiofile(mp3_path)
        
        # 임시 파일 삭제
        video_clip.close()
        os.remove(temp_file)
        
        print(f"변환 완료: {mp3_path}")
        return mp3_path
        
    except Exception as e:
        print(f"에러 발생: {str(e)}")
        return None

# 사용 예시
if __name__ == "__main__":
    # YouTube 영상 URL
    video_url = "https://www.youtube.com/watch?v=example"
    
    # 다운로드 실행
    output_file = download_youtube_mp3(video_url, "downloads")
    
    if output_file:
        print(f"파일이 성공적으로 저장되었습니다: {output_file}")
    else:
        print("다운로드 실패")
