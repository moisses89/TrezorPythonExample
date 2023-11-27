from trezorlib.client import get_default_client
from trezorlib.ethereum import get_address
from trezorlib import tools

def get_ethereum_address():
    try:
        client = get_default_client()


        # Get Ethereum address using the client
        address_n = tools.parse_path("m/44'/60'/0'/0/0")
        address = get_address(client=client, n=address_n)

        # Print the Ethereum address retrieved from the Trezor
        print(f"Ethereum Address: {address}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_ethereum_address()
