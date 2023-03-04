import openai_handler
import audio_processing
import os
import split_text
import re
import epub_conv
import doc_conv
import pdf_conv

title = "Előadás neve - 1. előadás"
audio_file = "lecture/Előadás neve - 1. előadás.m4a"

if not os.path.exists("lecture"):
    os.makedirs("lecture")
if not os.path.exists("lecture_chunks"):
    os.makedirs("lecture_chunks")

print("Splitting audio...")
audio_processing.split_audio_file(audio_file, "lecture_chunks")

audio_files = [f for f in os.listdir("lecture_chunks") if f.endswith(".mp3")]
regex_pattern = re.compile(r'_\d+')
audio_files = sorted(audio_files, key=lambda x: int(re.search(regex_pattern, x).group(0)[1:]))

# GET the literal text from the audio
print("Processing audio...")
lecture_text = ""
# Loop through the audio files and process each one with whisper()
for file in audio_files:
    print(file)
    lecture_text += openai_handler.whisper("lecture_chunks/" + file)
    os.remove("lecture_chunks/" + file)

with open('lecture/lecture_text.txt', 'w') as f:
    f.write(lecture_text)


basic_text_filename = "Basic text - " + title
epub_conv.create_epub(basic_text_filename, lecture_text, "lecture")
doc_conv.convert_to_doc(basic_text_filename + ".doc", lecture_text, "lecture")
pdf_conv.convert_to_pdf(basic_text_filename + ".pdf", lecture_text, "lecture")

# GET the converted text
text_chunks = split_text.split_text(lecture_text)

print("Converting text...")
converted_text = ""
cnt = 1
for text_chunk in text_chunks:
    print("Converting ", cnt, "/", len(text_chunks))
    converted_text += openai_handler.chatgpt_convert(text_chunk)
    cnt += 1

with open('lecture/converted_text.txt', 'w') as f:
    f.write(converted_text)

converted_text_filename = "Converted text - " + title
epub_conv.create_epub(converted_text_filename, converted_text, "lecture")
doc_conv.convert_to_doc(converted_text_filename + ".doc", converted_text, "lecture")
pdf_conv.convert_to_pdf(converted_text_filename + ".pdf", converted_text, "lecture")
