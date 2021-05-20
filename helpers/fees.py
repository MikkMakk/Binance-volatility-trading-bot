# from binance.client import Client
# from binance.exceptions import BinanceAPIException
# # Load helper modules
# from helpers.parameters import (
#     parse_args, load_config
# )
# # Load creds modules
# from helpers.handle_creds import (
#     load_correct_creds
# )
#
# # Load arguments then parse settings
# args = parse_args()
# DEFAULT_CREDS_FILE = 'creds.yml'
#
# creds_file = args.creds if args.creds else DEFAULT_CREDS_FILE
# parsed_creds = load_config(creds_file)
#
# # Load creds for correct environment
# access_key, secret_key = load_correct_creds(parsed_creds)

def get_fee_usdt():
    # Authenticate with the client, Ensure API key is good before continuing
#    client = Client(access_key, secret_key)
#    api_ready, msg = test_api_key(client, BinanceAPIException)
#    if api_ready is not True:
#        exit(msg)
    fee_usdt = client.get_all_tickers(BNBUSDT)
    return fee_usdt
