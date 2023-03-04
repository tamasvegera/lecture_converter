
def split_text(text):
    # Split the text into sentences
    sentences = text.split('.')

    # Initialize variables
    num_sentences = len(sentences)
    sentence_count = 0
    words_count = 0
    chunks = []
    current_chunk = ""

    # Loop through each sentence and add it to a chunk until the chunk has at least 300 words
    for sentence in sentences:
        sentence = sentence + '.'
        sentence_count += 1
        words_count += len(sentence.split())
        current_chunk += sentence

        # If the chunk has at least 300 words or it's the last sentence, add the chunk to the list of chunks
        if words_count >= 300 or sentence_count == num_sentences:
            chunks.append(current_chunk)
            current_chunk = ""
            words_count = 0

    return chunks
