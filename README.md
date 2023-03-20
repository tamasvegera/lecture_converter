# lecture_converter
Converts audio recordings of lectures into readable book-like documents in doc, pdf, and epub formats.

# Intro
The Lecture Converter tool utilizes OpenAI to convert audio recordings into easily readable documents, catering to those who prefer reading over listening to learn. This tool is not limited to simple speech recognition software as it also transforms the transcription into captivating and easily understandable content. 
Currently, it has been tested only with Hungarian lectures on MacOS, but it is expected to work with any other language.

# How to use it
- clone the repo
- install packages from requirements.txt
- insert your OpenAI API key into openai_handler.py (you can get your key at https://platform.openai.com/account/api-keys)
- set the audio file and title in lecture_converter.py
- start lecture_converter.py

The results will be stored in the ./lecture folder in doc, pdf, and epub formats. 
The processing time for a two-hour-long course is approximately five minutes, and the cost is less than one dollar in OpenAI fees.

# Required changes for non-Hungarian languages:
- modify the "system" and "user" prompts in openai_handler.py
- "system" content should be similar to: "You are a university professor teaching a psychology course"
- "user" content should be similar to: "The following text is an AI transcript of a lecture recording. Make it easy to read while retaining all the information and facts. Write in an interesting style as if you were the speaker:"

# GUI
GUI is not ready yet, but it will look like this:

<img width="460" alt="lecture_converter_gui_" src="https://user-images.githubusercontent.com/44163159/226462828-768a094b-bd70-42bf-b5a1-0d2999b802c0.png">


# License
Free for personal and educational purposes.
