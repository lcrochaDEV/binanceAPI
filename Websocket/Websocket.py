import asyncio
from binance import AsyncClient, BinanceSocketManager

class WebsocketUsage:

    @classmethod
    async def __websocket(self, args=None, kwargs=None):

        client = await AsyncClient.create(tld='us')
        bm = BinanceSocketManager(client)
        # start any sockets here, i.e a trade socket
        ts = bm.trade_socket('BNBBTC')
        # then start receiving messages
        async with ts as tscm:
            while True:
                res = await tscm.recv()
                print(res)

        await client.close_connection()

    @classmethod
    def WebsocketUserge(self, *args, **kwargs):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(WebsocketUsage.__websocket())
