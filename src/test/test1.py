import sys
import click
import logging
import os

LOGGER = logging.getLogger(__name__)


@click.command()
@click.option('--input_mode',
              help='input channel to use. You can choose between 3 options: ''stdin'', ''random'' and ''api'' (default: random)',
              type=str,
              default='random')
@click.option('--verbose',
              help='if the script should print debug info (default: False)',
              type=bool,
              default=False)
def cli(input_mode, verbose):
    """Simple program that does sampling over data stream. You need to specify input channel, then enjoy..."""
    if verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)


    LOGGER.debug('input_mode = %s', input_mode)
    LOGGER.debug('verbose = %s', verbose)


if __name__ == '__main__':
    # logging.basicConfig(level=logging.DEBUG)
    cli()

