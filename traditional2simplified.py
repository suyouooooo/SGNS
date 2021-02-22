import sys
import logging
from opencc import OpenCC
import os
base_dir = os.path.dirname((os.path.abspath(__file__)))
file_dir = os.path.join(base_dir, "file_dir")


def tra2simp(input_file, output_file):
    """
    Convert traditional Chinese characters into simplified Chinese characters in zhwiki.txt
    :param input_file: zhwiki.txt
    :param output_file: zhwiki.simplified.txt
    :return: null
    """
    zhwiki_trditional = []
    with open(input_file, 'r', encoding='utf-8') as input_file:
        for line in input_file:
            line = line.replace('\n', '')
            zhwiki_trditional.append(line)
    logging.info('read zhwiki_traditional file finished!')

    cc = OpenCC('t2s')
    zhwiki_simplified = []
    logging.info('convert traditional to simplified start...')
    for line in zhwiki_trditional:
        zhwiki_simplified.append(cc.convert(line))
    logging.info('convert traditional to simplified finished!')

    with open(output_file, 'w', encoding='utf-8') as output_file:
        for line in zhwiki_simplified:
            output_file.writelines(line + '\n')
    logging.info('write simplified file finished!')

if __name__ == '__main__':
    try:
        if len(sys.argv) == 1:
            tra2simp(os.path.join(file_dir, 'zhwiki.txt'), os.path.join(file_dir, 'zhwiki_simplified.txt'))
        elif len(sys.argv) == 2:
            tra2simp(sys.argv[1], os.path.join(file_dir, 'zhwiki_simplified.txt'))
        elif len(sys.argv) == 3:
            tra2simp(sys.argv[1], sys.argv[2])
    except Exception as err:
        logging.error(err)

