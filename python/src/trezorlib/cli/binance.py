import json

import click

from .. import binance, tools

PATH_HELP = "BIP-32 path to key, e.g. m/44'/714'/0'/0/0"


@click.group(name="binance")
def cli():
    """Binance Chain commands."""


@cli.command()
@click.option("-n", "--address", required=True, help=PATH_HELP)
@click.option("-d", "--show-display", is_flag=True)
@click.pass_obj
def get_address(connect, address, show_display):
    """Get Binance address for specified path."""
    client = connect()
    address_n = tools.parse_path(address)

    return binance.get_address(client, address_n, show_display)


@cli.command()
@click.option("-n", "--address", required=True, help=PATH_HELP)
@click.option("-d", "--show-display", is_flag=True)
@click.pass_obj
def get_public_key(connect, address, show_display):
    """Get Binance public key."""
    client = connect()
    address_n = tools.parse_path(address)

    return binance.get_public_key(client, address_n, show_display).hex()


@cli.command(help="Sign Binance transaction")
@click.option("-n", "--address", required=True, help=PATH_HELP)
@click.option(
    "-f",
    "--file",
    type=click.File("r"),
    required=True,
    help="Transaction in JSON format",
)
@click.pass_obj
def sign_tx(connect, address, file):
    client = connect()
    address_n = tools.parse_path(address)

    return binance.sign_tx(client, address_n, json.load(file))
