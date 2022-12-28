"""from ton.sypinc import TonlibClient

client = TonlibClient()
TonlibClient.enable_unaudited_binaries()
client.init_tonlib()

wallet = client.create_wallet()
print('Wallet address:', wallet.address)
print('Seed:', wallet.export())"""

from pyTONPublicAPI import pyTONPublicAPI
client = pyTONPublicAPI(
    address='EQCz7yI0FdoCH0BT2Hp7m8pUTsfuGEWl3e70tMdmrNpOqmzu')
print(client.get_address_balance())
print(client.get_transactions())
