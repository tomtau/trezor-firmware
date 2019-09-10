import json

import click

from .. import messages, protobuf, tezos, tools

PATH_HELP = "BIP-32 path, e.g. m/44'/1729'/0'"


@click.group(name="tezos")
def cli():
    """Tezos commands."""


@cli.command()
@click.option("-n", "--address", required=True, help=PATH_HELP)
@click.option("-d", "--show-display", is_flag=True)
@click.pass_obj
def get_address(connect, address, show_display):
    """Get Tezos address for specified path."""
    client = connect()
    address_n = tools.parse_path(address)
    return tezos.get_address(client, address_n, show_display)


@cli.command()
@click.option("-n", "--address", required=True, help=PATH_HELP)
@click.option("-d", "--show-display", is_flag=True)
@click.pass_obj
def get_public_key(connect, address, show_display):
    """Get Tezos public key."""
    client = connect()
    address_n = tools.parse_path(address)
    return tezos.get_public_key(client, address_n, show_display)


@cli.command()
@click.option("-n", "--address", required=True, help=PATH_HELP)
@click.option(
    "-f",
    "--file",
    type=click.File("r"),
    default="-",
    help="Transaction in JSON format (byte fields should be hexlified)",
)
@click.pass_obj
def sign_tx(connect, address, file):
    """Sign Tezos transaction."""
    client = connect()
    address_n = tools.parse_path(address)
    msg = protobuf.dict_to_proto(messages.TezosSignTx, json.load(file))
    return tezos.sign_tx(client, address_n, msg)
