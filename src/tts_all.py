import pyttsx3, pyaudio, torch
from huggingface_hub import snapshot_download
from transformers import AutoModel, AutoTokenizer, pipeline
import sounddevice as sd
import numpy as np

class transAutoTTS():
    def __init__(self, model_dir, local_files_only=True):
        self.model = AutoModel.from_pretrained(model_dir, local_files_only=local_files_only)
        self.tokenizer = AutoTokenizer.from_pretrained(model_dir, local_files_only=local_files_only)
    def say(self, text:str):
        inputs= self.tokenizer(text, return_tensore="pt")
        with torch.no_grad:
            outputs=self.model(**inputs)
            audio = outputs.audio[0].cpu().numpy()
            sr = self.model.config.samplerate
        sd.play(audio, sr)
        sd.wait()

class transPiplineTTS():
    def __init__(self, model_dir, local_files_only=True):
        self.pipe = pipeline("text-to-audio", model=model_dir,local_files_only=local_files_only)
    def say(self, text:str):
        outputs=self.pipe(text)
        audio= outputs["audio"]
        sr= outputs["sampling_rate"]
        if audio.dtype != np.float32:
            audio = audio.astype(np.float32)
        sd.play(audio, sr)
        sd.wait()

class pyttsx3TTS():
    def __init__(self, voice_id:int=0): 
        self.engine = pyttsx3.init()
        self.engine.startLoop(False)
        self.voices = self.engine.getProperty("voices")
        self.voice_id = voice_id
    def settings(self, set:str, data):
        self.engine.setProperty(set, data)
    def say(self, text:str):
        self.settings('voice', self.voices[self.voice_id].id)
        self.engine.say(text)
        self.engine.runAndWait()
        self.engine.stop()
       
def download_TTSmodel(repo_id, local_dir):
    model_path = snapshot_download(
        repo_id=repo_id,
        local_dir=local_dir,
        local_dir_use_symlinks=False,
    )