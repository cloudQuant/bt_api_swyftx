"""Tests for SwyftxExchangeData container."""

from __future__ import annotations

from bt_api_swyftx.exchange_data import SwyftxExchangeData


class TestSwyftxExchangeData:
    """Tests for SwyftxExchangeData."""

    def test_init(self):
        """Test initialization."""
        exchange = SwyftxExchangeData()

        assert exchange.exchange_name == "SWYFTX___SPOT"
