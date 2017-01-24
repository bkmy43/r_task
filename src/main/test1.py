import sys
import click
import logging
import os
import random

LOGGER = logging.getLogger(__name__)


@click.command()
@click.option('--input_mode',
              help='input channel to use. You can choose between 3 options: ''stdin'', ''random'' and ''api'' (default: stdin)',
              type=str,
              default='stdin')
@click.option('--sample_size',
              help='how many characters from input should be kept in the random sample (default: 10)',
              type=int,
              default=10)
@click.option('--verbose',
              help='if the script should print debug info (default: False)',
              type=bool,
              default=False)

def main(input_mode, sample_size, verbose):
    """Simple program that does sampling over data stream. You need to specify input channel, then enjoy..."""
    if verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    LOGGER.info('*** Research gate programming assignment: "Random Sampling over Data Streams" by Ilya Vladimirskiy Jan 2017**')
    LOGGER.debug('input_mode = %s', input_mode)
    LOGGER.debug('sample_size = %s', sample_size)
    LOGGER.debug('verbose = %s', verbose)

    sample = [None] * sample_size
    char_count = 0

    for line in sys.stdin:
        LOGGER.debug('input line = %s', line)
        for char in line:
            if char_count < sample_size:
                index = char_count
            else:
                index = random.randint(0, sample_size - 1)

            sample[index] = char
            char_count += 1

    LOGGER.info('Resulting sample: {}'.format(''.join(sample)))

if __name__ == '__main__':
    main()

