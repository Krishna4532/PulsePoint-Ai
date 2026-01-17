import whisper
import os
from brain import get_viral_segment
from editor import create_vertical_clip

# --- CONFIGURATION ---
# Use the AIza... key you found in Google AI Studio
API_KEY = "AIzaSyAfFkNHlVWcEeMC64Pi8QMWG-heBnCDsxE" 
INPUT_VIDEO = "test_video.mp4"
OUTPUT_VIDEO = "pulse_clip.mp4"

def start_pulsepoint():
    print("🚀 PulsePoint AI is starting...")

    # Check if the input video actually exists
    if not os.path.exists(INPUT_VIDEO):
        print(f"❌ Error: {INPUT_VIDEO} not found in this folder!")
        return

    # Step 1: Transcribe (The Ears)
    print("👂 Step 1: Transcribing video with Whisper...")
    # Using 'base' for a balance of speed and accuracy
    model = whisper.load_model("base")
    result = model.transcribe(INPUT_VIDEO)
    
    # Step 2: Analyze (The Brain)
    print("🧠 Step 2: Sending transcript to Gemini...")
    try:
        clip_info = get_viral_segment(result['segments'], API_KEY)
        print(f"✅ AI Highlight Found: '{clip_info['headline']}'")
        print(f"⏱️  Segment: {clip_info['start']}s to {clip_info['end']}s")
    except Exception as e:
        print(f"❌ Brain Error: {e}")
        return
    
    # Step 3: Edit (The Hands)
    print("🎬 Step 3: Cropping to vertical and saving...")
    try:
        create_vertical_clip(
            INPUT_VIDEO, 
            clip_info['start'], 
            clip_info['end'], 
            OUTPUT_VIDEO
        )
        print(f"✨ SUCCESS! Final clip saved as: {OUTPUT_VIDEO}")
    except Exception as e:
        print(f"❌ Editor Error: {e}")

if __name__ == "__main__":
    start_pulsepoint()