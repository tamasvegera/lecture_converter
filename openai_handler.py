import openai
openai.api_key = "xxx"

def whisper(audio_file):
    audio_file = open(audio_file, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)

    return transcript.text


def chatgpt_convert(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Te egy egyetemi előadó vagy egy pszichológia képzésen"},
            {"role": "user", "content": 'A következő szöveg egy előadás hangfelvételének AI-al készült leirata. Fogalmazd át könnyen olvashatóvá, miközben minden információt és tényt megtartasz. Te vagy az előadó, fogalmazz érdekes stílusban: ' + text},

        ]
    )
    result = response.choices[0]["message"]["content"]
    #print("Usage: ", response.usage.total_tokens)
    return result

