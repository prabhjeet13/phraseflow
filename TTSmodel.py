# import torch
# from transformers import AutoModelForCausalLM, AutoTokenizer
# import torchaudio
import os
from gtts import gTTS
# import pyttsx3
# from googletrans import Translator
# Dictionary to map languages to model names
# language_model_map = {
#     'en': 'facebook/tts_transformer-en',
#     'es': 'facebook/tts_transformer-es-css10',
#     'fr': 'facebook/tts_transformer-fr',
#     # Add more languages and corresponding models here
# }

# # Cache for loaded models and tokenizers
# language_model_cache = {}

# # Function to load model and tokenizer based on selected language (Lazy Loading)
# def load_model(language: str):
#     if language not in language_model_cache:
#         model_name = language_model_map.get(language)
        
#         if model_name is None:
#             raise ValueError(f"Language model for '{language}' not available.")
        
#         # Load model and tokenizer
#         model = AutoModelForCausalLM.from_pretrained(model_name)
#         tokenizer = AutoTokenizer.from_pretrained(model_name)
        
#         language_model_cache[language] = (model, tokenizer)
    
#     return language_model_cache[language]

# Function to convert text to speech
# def text_to_speech(text: str, language: str, output_filename: str):
#     # Load model and tokenizer for the selected language
#     model, tokenizer = load_model(language)

#     # Tokenize input text
#     input_ids = tokenizer(text, return_tensors="pt").input_ids

#     # Generate audio from input text
#     with torch.no_grad():
#         audio = model.generate(input_ids)

#     # Save audio to file
#     torchaudio.save(output_filename, audio.squeeze(0), 22050)  # Adjust sample rate as needed
#     return output_filename

def text_to_speech(text: str, language: str,output_filename: str = 'output_audio.wav'):
    
     tts = gTTS(text=text, lang=language, slow=False)
     tts.save(output_filename)
     return output_filename
    
    # engine = pyttsx3.init(driverName='sapi5')
    # engine = pyttsx3.init(driverName='espeak')
    # Set the properties for the voice based on language
    # voices = engine.getProperty('voices')
    # available_voices = {voice.id: voice.name for voice in voices}
    # print("Available voices:", available_voices)
    # Change the voice based on the selected language


    # translator = Translator()

    # Translate the text to the target language (French)
    # translated_text = translator.translate(text, dest=language).text
    # print(f"Translated text: {translated_text}")

    # Initialize TTS engine

    # Define voice mapping
    # voices = {
        #     'en': 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0',  # English (US)
        #     # 'en_US': 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0',  # American English
        #     # 'en_GB': 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-GB_HELENA_11.0',  # British English
        #     'fr': 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_FR-FR_HORTENSE_11.0',  # French
        #     'es': 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_ES-ES_HELENA_11.0',  # Spanish
        #     'de': 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_DE-DE_HEDDA_11.0',    # German
        #     'it': 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_IT-IT_CHIARA_11.0',  # Italian
        #     # 'zh': 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_ZH-CN_HUIHUI_11.0',  # Chinese
        #     # 'ja': 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_JA-JP_MISAKI_11.0',  # Japanese
        #     # 'ko': 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_KO-KR_HYUNJUNG_11.0', # Korean
        #     # 'ru': 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_RU-RU_ALISA_11.0',   # Russian
        #     # 'ar': 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_AR-SA_HAIDER_11.0',   # Arabic
        #     # 'hi': 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_HI-IN_AJAY_11.0',     # Hindi
        #     'pt': 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_PT-BR_HENRIQUE_11.0', # Portuguese
        # }

    # Set the voice based on the selected language
    # if language in voices:
    #     engine.setProperty('voice', voices[language])
    # else:
    #     print(f"No voice found for language: {language}. Using default voice.")
    
    # Save speech to a file
    # engine.save_to_file(translated_text, output_filename)
    # engine.runAndWait()
    
    # return output_filename









    # print('voices:')



    # voices = {
    #     'en': 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\SAPI\\Voices\\Tokens\\Microsoft Zira Desktop',  # English
    #     'fr': 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\SAPI\\Voices\\Tokens\\Microsoft Henri Desktop'  # French
    # }

    # # Set the voice based on the selected language
    # if language in voices:
    #     engine.setProperty('voice', voices[language])
    # else:
    #     print(f"No voice found for language: {language}. Using default voice.")
    
    # # Save speech to a file
    # engine.save_to_file(text, output_filename)
    # engine.runAndWait()
    
    # return output_filename
    # voice_found = False
    # for voice in voices:
    #     # Check if the voice supports the output language
    #     if language in voice.languages:
    #         engine.setProperty('voice', voice.id)
    #         voice_found = True
    #         break

    # if not voice_found:
    #     print(f"No voice found for language: {language}. Using default voice.")
    #     engine.setProperty('voice', voices[0].id)  # Default to the first voice


    # # Save speech to a file
    # engine.save_to_file(text, output_filename)
    # engine.runAndWait()
    
    # return output_filename


