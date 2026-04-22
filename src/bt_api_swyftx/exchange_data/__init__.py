from __future__ import annotations

import re

from bt_api_base.containers.exchanges.exchange_data import ExchangeData

_FALLBACK_REST_PATHS = {
    "get_server_time": "GET /api/v1/time",
    "get_tick": "GET /api/v1/markets/{symbol}/ticker",
    "get_ticker": "GET /api/v1/markets/{symbol}/ticker",
    "get_all_tickers": "GET /api/v1/markets/ticker",
    "get_depth": "GET /api/v1/markets/{symbol}/orderbook",
    "get_kline": "GET /api/v1/markets/{symbol}/candles",
    "get_exchange_info": "GET /api/v1/markets",
    "get_account": "GET /api/v1/user/account",
    "get_balance": "GET /api/v1/user/balance",
    "make_order": "POST /api/v1/orders",
    "cancel_order": "DELETE /api/v1/orders/{order_id}",
    "query_order": "GET /api/v1/orders/{order_id}",
    "get_open_orders": "GET /api/v1/orders",
}


class SwyftxExchangeData(ExchangeData):
    def __init__(self) -> None:
        super().__init__()
        self.exchange_name = "SWYFTX___SPOT"
        self.rest_url = "https://api.swyftx.com.au"
        self.wss_url = ""
        self.rest_paths = dict(_FALLBACK_REST_PATHS)
        self.wss_paths = {}
        self.kline_periods = {
            "1m": "60",
            "5m": "300",
            "15m": "900",
            "30m": "1800",
            "1h": "3600",
            "4h": "14400",
            "1d": "86400",
            "1w": "604800",
        }
        self.legal_currency = ["AUD", "USD", "BTC", "ETH", "USDT"]

    @staticmethod
    def get_symbol(symbol):
        s = symbol.strip()
        s = re.sub(r"[/_]", "-", s)
        return s.upper()

    @staticmethod
    def get_reverse_symbol(symbol):
        s = symbol.strip()
        s = re.sub(r"[/_]", "-", s)
        return s.upper()

    def get_period(self, period: str) -> str:
        return self.kline_periods.get(period, period)

    def get_reverse_period(self, period: str) -> str:
        for k, v in self.kline_periods.items():
            if v == period:
                return k
        return period

    def get_rest_path(self, key: str, **kwargs) -> str:
        path = self.rest_paths.get(key, "")
        if not path:
            raise ValueError(f"[{self.exchange_name}] REST path not found: {key}")
        if kwargs:
            path = path.format(**kwargs)
        return str(path)


class SwyftxExchangeDataSpot(SwyftxExchangeData):
    def __init__(self) -> None:
        super().__init__()
        self.asset_type = "SPOT"
