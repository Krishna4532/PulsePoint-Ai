import os
from moviepy import VideoFileClip, TextClip, CompositeVideoClip, ColorClip

def create_vertical_clip(input_path, start_time, end_time, output_path, headline="VIRAL MOMENT"):
    print(f"🎬 Loading video: {input_path}")
    
    # 1. Load the video
    video = VideoFileClip(input_path)
    
    # Safety Check for Duration
    actual_duration = video.duration
    if end_time is None or end_time > actual_duration:
        end_time = actual_duration
    
    # 2. Cut the segment
    clip = video.subclipped(start_time, end_time)
    
    # 3. Crop to Vertical (9:16)
    w, h = clip.size
    target_width = h * (9/16)
    x1 = (w - target_width) / 2
    x2 = x1 + target_width
    final_clip = clip.cropped(x1=x1, y1=0, x2=x2, y2=h)
    
    # 4. Add Headline Text Overlay
    # Note: MoviePy 2.0 uses .with_position() and .with_duration()
    try:
        txt_clip = TextClip(
            text=headline.upper(),
            font_size=50,
            color='white',
            font='Arial-Bold', # Basic font usually available on Windows
            stroke_color='black',
            stroke_width=2,
            method='label'
        ).with_duration(final_clip.duration).with_position(('center', 100))
        
        # Merge Video and Text
        final_output = CompositeVideoClip([final_clip, txt_clip])
    except Exception as e:
        print(f"⚠️ Text Overlay failed (likely missing ImageMagick): {e}")
        print("💡 Proceeding with just the video crop.")
        final_output = final_clip

    # 5. Render/Write File
    print(f"⏳ Rendering final vertical video...")
    final_output.write_videofile(
        output_path, 
        codec="libx264", 
        audio_codec="aac",
        fps=24,
        temp_audiofile="temp-audio.m4a",
        remove_temp=True
    )
    
    # Cleanup
    video.close()
    final_output.close()
    print(f"✨ SUCCESS: {output_path} is ready for submission!")