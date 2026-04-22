from __future__ import annotations

from typing import TYPE_CHECKING

from bt_api_base.balance_utils import simple_balance_handler as _swyftx_balance_handler

from bt_api_swyftx.exchange_data import SwyftxExchangeDataSpot
from bt_api_swyftx.feeds.live_swyftx.spot import SwyftxRequestDataSpot

if TYPE_CHECKING:
    from bt_api_base.registry import ExchangeRegistry


def register_swyftx(registry: type[ExchangeRegistry]) -> None:
    registry.register_feed("SWYFTX___SPOT", SwyftxRequestDataSpot)
    registry.register_exchange_data("SWYFTX___SPOT", SwyftxExchangeDataSpot)
    registry.register_balance_handler("SWYFTX___SPOT", _swyftx_balance_handler)
