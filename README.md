🚀 PulsePoint AI
Transform long-form content into viral vertical clips in seconds.

💡 The Vision
Content creators spend hours manually finding highlights and cropping videos for TikTok/Shorts. PulsePoint AI automates this entire pipeline using a multi-model AI approach.

🛠️ How it Works
The Ears (OpenAI Whisper): Transcribes the audio with high precision.

The Brain (Google Gemini 1.5 Flash): Analyzes the transcript to identify high-impact, viral moments and generates a catchy headline.

The Hands (MoviePy): Automatically crops the video to a 9:16 aspect ratio, cuts the selected segment, and renders the final clip.

🛡️ Robust Architecture (The "Safe" System)
We built PulsePoint with Fault Tolerance in mind. If the AI API reaches a rate limit or encounters a network error, our custom "Emergency Fallback" logic ensures the video processing continues by selecting a high-probability highlight based on the video duration.

📦 Tech Stack
Language: Python

AI Models: Google Gemini, OpenAI Whisper

Video Processing: MoviePy (v2.0)# PulsePoint-Ai
