import json

import click

from .. import ripple, tools

PATH_HELP = "BIP-32 path to key, e.g. m/44'/144'/0'/0/0"


@click.group(name="ripple")
def cli():
    """Ripple commands."""


@cli.command()
@click.option("-n", "--address", required=True, help=PATH_HELP)
@click.option("-d", "--show-display", is_flag=True)
@click.pass_obj
def get_address(connect, address, show_display):
    """Get Ripple address"""
    client = connect()
    address_n = tools.parse_path(address)
    return ripple.get_address(client, address_n, show_display)


@cli.command()
@click.option("-n", "--address", required=True, help=PATH_HELP)
@click.option(
    "-f", "--file", type=click.File("r"), default="-", help="Transaction in JSON format"
)
@click.pass_obj
def sign_tx(connect, address, file):
    """Sign Ripple transaction"""
    client = connect()
    address_n = tools.parse_path(address)
    msg = ripple.create_sign_tx_msg(json.load(file))

    result = ripple.sign_tx(client, address_n, msg)
    click.echo("Signature:")
    click.echo(result.signature.hex())
    click.echo()
    click.echo("Serialized tx including the signature:")
    click.echo(result.serialized_tx.hex())
