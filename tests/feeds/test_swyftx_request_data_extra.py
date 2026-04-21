from __future__ import annotations

from unittest.mock import MagicMock

from bt_api_swyftx.feeds.live_swyftx.request_base import SwyftxRequestData


def test_swyftx_disconnect_closes_http_client() -> None:
    request_data = SwyftxRequestData(None)
    request_data._http_client.close = MagicMock()

    request_data.disconnect()

    request_data._http_client.close.assert_called_once_with()


def test_swyftx_falls_back_to_api_key_when_public_key_is_empty() -> None:
    request_data = SwyftxRequestData(None, public_key="", api_key="public-key")

    assert request_data.api_key == "public-key"
