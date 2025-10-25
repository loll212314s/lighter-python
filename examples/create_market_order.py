import asyncio
import logging
import lighter

logging.basicConfig(level=logging.DEBUG)

# The API_KEY_PRIVATE_KEY provided belongs to a dummy account registered on Testnet.
# It was generated using the setup_system.py script, and serves as an example.
BASE_URL = "https://testnet.zklighter.elliot.ai"
API_KEY_PRIVATE_KEY = "cc9c29835382fbd8d958c91cda7afb936e1f1b673ac37e52b43d92dfd07ee694a4f51ec0ca2b2f79"
ACCOUNT_INDEX = 211
API_KEY_INDEX = 2


def trim_exception(e: Exception) -> str:
    return str(e).strip().split("\n")[-1]


async def main():
    client = lighter.SignerClient(
        url=BASE_URL,
        private_key=API_KEY_PRIVATE_KEY,
        account_index=ACCOUNT_INDEX,
        api_key_index=API_KEY_INDEX,
    )

    tx = await client.create_market_order(
        market_index=1,
        client_order_index=0,
        base_amount=0.0001,  # 0.1 ETH
        avg_execution_price=170000,  # $1700 -- worst acceptable price for the order
        is_ask=True,
    )
    print("Create Order Tx:", tx)
    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
