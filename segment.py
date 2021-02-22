import re
import jieba
import sys
import logging
import os
base_dir = os.path.dirname((os.path.abspath(__file__)))
file_dir = os.path.join(base_dir, "file_dir")


def seg_depart(sentence):
    """
    Use jieba for precise word segmentation
    :param sentence: sentence to be segmented
    :return: sentence that have been segmented
    """
    sentence_depart = jieba.cut(sentence.strip())
    segment_res = ' '.join(sentence_depart)
    return segment_res


def textParse_news(sentence):
    """
    Use regular filters to filter out special symbols, punctuation, English, Numbers, etc
    :param sentence: sentence that need to be filtered
    :return: filtered sentence
    """
    r1 = '[0-9’!"#$%&\'()*+,-./:：;；|<=>?@，—。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'
    sentence = re.sub(r1, ' ', sentence)
    sentence = re.sub('\u3000', '', sentence)
    sentence=re.sub('\s+', ' ', sentence)
    return sentence


def zhwiki_segment(input_file, output_file):
    """
    Clean the input_file and do word segmentation to the input_file, the write to the output_file
    :param input_file: zhwiki.simplified.txt
    :param output_file: zhwiki.simplified.segment.txt
    :return: null
    """
    zhwiki_simplified = []
    with open(input_file, 'r', encoding='utf-8') as input_file:
        for line in input_file:
            zhwiki_simplified.append(line)
    logging.info('read zhwiki finished!')

    logging.info('zhwiki segment start...')
    zhwiki_segment = []
    for line in zhwiki_simplified:
        line = textParse_news(line)
        line = seg_depart(line)
        zhwiki_segment.append(line)
    logging.info('zhwiki segment finished!')

    logging.info('write zhwiki segment start...')
    with open(output_file, 'w', encoding='utf-8') as output_file:
        for line in zhwiki_segment:
            output_file.writelines(line + '\n')
    logging.info('write zhwiki segment finished!')

if __name__ == '__main__':
    try:
        if len(sys.argv) == 1:
            zhwiki_segment(os.path.join(file_dir, 'zhwiki_simplified.txt'),
                           os.path.join(file_dir, 'zhwiki_simplified_segment.txt'))
        elif len(sys.argv) == 2:
            zhwiki_segment(sys.argv[1], os.path.join(file_dir, 'zhwiki_simplified_segment.txt'))
        elif len(sys.argv) == 3:
            zhwiki_segment(sys.argv[1], sys.argv[2])
    except Exception as err:
        logging.error(err)
