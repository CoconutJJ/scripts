from ctypes.wintypes import SIZE
import sys
import math
import heapq


class MarketData():
    def __init__(self, price, quantity):
        self.price = float(price)
        self.quantity = float(quantity)


class TradeRequest():
    def __init__(self, tradeRequestTokens):
        self.qty = int(tradeRequestTokens[0])
        self.riskPerQty = float(tradeRequestTokens[1])


def ParseMarketData(mdLine):
    tokens = mdLine.split()
    return [MarketData(price, size)
            for price, size in zip(tokens[1::2], tokens[::2])]


class Hedger():
    def __init__(self, bids, offers):
        self.bids = bids
        self.offers = offers
        self.remaining_risk = 0
        self.bid_hp = []
        self.offer_hp = []
        for m in self.bids:
            heapq.heappush(self.bid_hp, (m.price, m.quantity))

        for m in self.offers:
            heapq.heappush(self.offer_hp, (-m.price, m.quantity))

    def PassTrade(self, tradeRequest):
        TotalFillPriceCost = 0
        TotalFillPriceCount = 0
        riskPerQty = float(tradeRequest.riskPerQty)
        qty = float(tradeRequest.qty)

        self.remaining_risk += qty * riskPerQty

        units = math.floor(self.remaining_risk / riskPerQty)

        count = 0
        while self.remaining_risk >= riskPerQty:

            rate = price = size = 0

            if qty < 0:
                (price, size) = heapq.heappop(self.bid_hp)
            else:
                (price, size) = heapq.heappop(self.offer_hp)

            if size < units:

                units -= size

                TotalFillPriceCost += abs(price)
                TotalFillPriceCount += size

                self.remaining_risk -= size * riskPerQty
                count += size
            else:
                size -= units
                TotalFillPriceCost += abs(price)
                TotalFillPriceCount += units

                if size > 0:

                    if qty < 0:
                        heapq.heappush(self.bid_hp, (price, size))
                    else:
                        heapq.heappush(self.offer_hp, (price, size))

                self.remaining_risk -= units * riskPerQty
                count += units

        return "%d %f" % (riskPerQty * count,
                          TotalFillPriceCost / TotalFillPriceCount)


linesParsed = 0
hedger = None
for line in sys.stdin:
    if linesParsed == 0:
        offers = ParseMarketData(line)
        linesParsed += 1
    elif linesParsed == 1:
        bids = ParseMarketData(line)
        hedger = Hedger(bids, offers)
        linesParsed += 1
    else:
        if hedger is None:
            raise Exception('no good')
        tradeRequest = TradeRequest(line.split())
        res = hedger.PassTrade(tradeRequest)
        if res is not None:
            print(res)
        linesParsed += 1
