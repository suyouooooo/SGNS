import logging
import sys
from gensim.corpora import WikiCorpus
import os
base_dir = os.path.dirname((os.path.abspath(__file__)))
file_dir = os.path.join(base_dir, "file_dir")


def parse_corpus(input_file, output_file):
    """
    change zhwiki.xml.bz2 to zhwiki.txt
    :param input_file: zhwiki.xml.bz2
    :param output_file: zhwiki.txt
    :return: null
    """
    logging.info('xml2txt start...')
    with open(output_file, 'w', encoding='utf-8') as output_file:
        wiki_corpus = WikiCorpus(input_file, lemmatize=False, dictionary={})
        for text in wiki_corpus.get_texts():
            output_file.write(' '.join(text) + '\n')
    logging.info('xml2txt end...')

if __name__ == '__main__':
    try:
        if len(sys.argv) == 1:
            parse_corpus(os.path.join(file_dir, 'zhwiki-20191120-pages-articles-multistream.xml.bz2'),
                         os.path.join(file_dir, 'zhwiki.txt'))
        elif len(sys.argv) == 2:
            parse_corpus(sys.argv[1], os.path.join(file_dir, 'zhwiki.txt'))
        elif len(sys.argv) == 3:
            parse_corpus(sys.argv[1], sys.argv[2])
    except Exception as err:
        logging.error(err)
