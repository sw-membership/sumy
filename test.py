# mysumy.py

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


LANGUAGE = "korean"
SENTENCES_COUNT = 10


if __name__ == "__main__":
    # parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
    # 문장을 직접 파이썬 문자열로 넣어주고 싶다면 아래 코드를 사용하세요
    my_sentence = "이것은 요약하고 싶은 문자열입니다."
    parser = PlaintextParser.from_string(my_sentence, Tokenizer(LANGUAGE))
    
    stemmer = Stemmer(LANGUAGE)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        print(sentence)
