import asyncio
import logging
import lighter

logging.basicConfig(level=logging.DEBUG)

# The API_KEY_PRIVATE_KEY provided belongs to a dummy account registered on Testnet.
# It was generated using the setup_system.py script, and serves as an example.
BASE_URL = "https://mainnet.zklighter.elliot.ai"
API_KEY_PRIVATE_KEY = "654ae8cf9e14f270661e0231ea07b38e50e88c1d40228a938cb735a4804b9dedf09fc8c32ad0851b"
ACCOUNT_INDEX = 259397
API_KEY_INDEX = 5


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
        market_index=0,
        client_order_index=0,
        base_amount=1,  # 0.000001 ETH
        avg_execution_price=5000,  # $5000
        is_ask=False, # Buy
    )
    print("Create Order Tx:", tx)
    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
