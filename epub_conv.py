from ebooklib import epub

def create_epub(book_title, lecture_text, output_dir):
    if output_dir[-1] != '/':
        output_dir += '/'

    book_content = "<p>" + lecture_text + "</p>"

    book = epub.EpubBook()
    book.set_title(book_title)
    book.set_language("hu")
    book.add_author("A_book_author")

    c1 = epub.EpubHtml(title="chapter_1", file_name="chapter_1.xhtml", lang="en")
    c1.content = book_content

    book.add_item(c1)

    book.toc = (epub.Link("chapter_1.xhtml", "1. előadás", "intro"), )
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    book.spine = ["nav", c1]

    epub.write_epub(output_dir + book_title + '.epub', book, {})
