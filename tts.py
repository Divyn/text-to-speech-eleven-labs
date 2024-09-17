
# !pip install elevenlabs

# !pip install mpv

from elevenlabs import Voice, VoiceSettings, play,stream,save
from elevenlabs.client import ElevenLabs

client = ElevenLabs(api_key="hhhhh", )
audio = client.generate(
    text="அகர முதல எழுத்தெல்லாம் ஆதி பகவன் முதற்றே உலகு",
    voice=Voice(
         voice_id="zcAOhNBS3c14rBihAFp1",
    optimize_streaming_latency="0",
    output_format="mp3_22050_32",

    voice_settings=VoiceSettings(
        stability=0.1,
        similarity_boost=0.3,
        style=0.2,
    ),
         stream=True
    )
)


save(audio, "my-file.mp3")
