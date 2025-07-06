# Try the Live API

Explore the [Live API](https://ai.google.dev/gemini-api/docs/live).

The Live API enables low-latency bidirectional voice and video interactions with Gemini, letting you talk to Gemini live while also streaming video input or sharing your screen.

You can try the Live API in [Google AI Studio](https://aistudio.google.com/app/live). To use the Live API in Google AI Studio, select **Stream**.

## 1. Text to text

Chat with Gemini live.

Ensure the `GEMINI_API_KEY` environment variable is set to the api-key
you obtained from Google AI Studio.

```
export GEMINI_API_KEY=<your_key>
```

Install dependencies:

```
pip install -U google-genai 
```

Run the script:

```
python text-to-text.py
```

Now you can start chatting.

## 2. Audio to audio

Talk to Gemini live. 

You need to install pyaudio, e.g.

```
brew install portaudio
pip install pyaudio
```

Then run:

```
python audio-to-audio.py
```

Now you can start talking.

**Important**: Use headphones! This script uses the system default audio
input and output, which often won't include echo cancellation. So to prevent
the model from interrupting itself it is important that you use headphones. 


The script is configured to use the new Gemini 2.5 [native audio generation](https://ai.google.dev/gemini-api/docs/live#native-audio-output) models, which directly generates audio output, providing a more natural sounding audio, more expressive voices, more awareness of additional context, e.g., tone, and more proactive responses.

## 3. Audio and video to audio

Share your screen or camera and talk to Gemini.

Install dependencies:

```
pip install -U google-genai opencv-python pyaudio pillow mss
```

Then run:

```
python video-to-audio.py --mode screen
# or
python video-to-audio.py --mode camera
```

Now you can start talking and e.g. asking questions about your screen.



