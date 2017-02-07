import sys
import click
import logging
import random
from memory_profiler import memory_usage

__author__ = "Ilya Vladimirskiy"
__email__ = "bkmy43@googlemail.com"

LOGGER = logging.getLogger(__name__)


@click.command()
@click.option('--input_mode',
              help='input channel to use. You can choose between 3 options: ''stdin'', \
                   ''random'' and ''api'' (default: stdin)',
              type=str,
              default='stdin')
@click.option('--sample_size',
              help='how many characters from input should be kept in the random sample (default: 10)',
              type=int,
              default=10)
@click.option('--skip_newline_characters',
              help='if set to true, the script will ignore "\n" characters in the input, assuming they \
                    are not part of the input data (default: True)',
              type=bool,
              default=True)
@click.option('--verbose',
              help='if the script should print debug info (default: False)',
              type=bool,
              default=False)

def main(input_mode, sample_size, skip_newline_characters, verbose):
    """Simple program that does sampling over data stream. You need to specify input channel, size of the sample and
    two system parameters: if it should ignore \n characters and if you want debug information to be displayed.
    Please contact me using bkmy43@googlemail.com if you need any assistance or support with this software"""
    if verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    LOGGER.info('*** Research gate programming assignment: "Random Sampling over Data Streams" ' +
                'by Ilya Vladimirskiy Jan 2017 ***')
    LOGGER.debug('input_mode = %s', input_mode)
    LOGGER.debug('sample_size = %s', sample_size)
    LOGGER.debug('verbose = %s', verbose)

    if input_mode == 'stdin':
        source = sys.stdin
    else:
        LOGGER.error('Input mode %s is not implemented yet... exiting', input_mode)
        return False

    memory_used = memory_usage( random_sampling(sample_size, skip_newline_characters, source) )
    LOGGER.info('Memory used: {}'.format(memory_used))

def random_sampling(sample_size, skip_newline_characters, source):
    sample = [None] * sample_size
    char_count = 0

    for line in source:
        LOGGER.debug('input line = %s', line)
        for char in line:
            if char == '\n' and skip_newline_characters:
                continue
            elif char_count < sample_size:
                index = char_count
            else:
                index = random.randint(0, sample_size - 1)

            sample[index] = char
            char_count += 1

    if char_count < sample_size:
        LOGGER.error('Not enoupth data in input stream to do sampling ' +
                     '({} characters too few)... exiting'.format(sample_size - char_count))
        return False
    else:
        LOGGER.info('Resulting sample: {}'.format(''.join(sample)))
        return True

if __name__ == '__main__':
    main()
