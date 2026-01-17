import google.generativeai as genai
import json

def get_viral_segment(transcript_segments, api_key):
    # 1. Basic configuration
    genai.configure(api_key=api_key)
    
    # 2. Use the most direct model string possible
    # We do NOT use RequestOptions here to avoid the 'unexpected keyword' error
    model = genai.GenerativeModel('models/gemini-1.5-flash')
    
    formatted_transcript = ""
    for seg in transcript_segments:
        formatted_transcript += f"[{seg['start']}-{seg['end']}] {seg['text']}\n"

    prompt = f"""
    You are a viral social media editor. Analyze this transcript and find the best 30-60 second clip.
    Return ONLY a JSON object. No extra text.
    Format: {{"start": 0, "end": 30, "headline": "title"}}
    
    Transcript:
    {formatted_transcript}
    """

    print("🧠 Gemini is analyzing the transcript (Direct Mode)...")
    
    try:
        # 3. Simple call - if this fails, we use a hardcoded fallback 
        # so your project NEVER crashes during the hackathon.
        response = model.generate_content(prompt)
        
        # Clean up the AI response
        raw_text = response.text.strip()
        if "```json" in raw_text:
            raw_text = raw_text.split("```json")[1].split("```")[0].strip()
        elif "```" in raw_text:
            raw_text = raw_text.split("```")[1].split("```")[0].strip()
            
        return json.loads(raw_text)
        
    except Exception as e:
        print(f"⚠️ AI Analysis failed: {e}")
        print("💡 Using emergency fallback (first 30 seconds) to keep the project running!")
        return {"start": 0, "end": 30, "headline": "Viral Moment"}