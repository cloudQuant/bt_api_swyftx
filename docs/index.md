# SWYFTX Documentation

## English

Welcome to the SWYFTX documentation for bt_api.

### Quick Start

```bash
pip install bt_api_swyftx
```

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "SWYFTX___SPOT": {
        "api_key": "your_key",
        "secret": "your_secret",
    }
})

ticker = api.get_tick("SWYFTX___SPOT", "BTCUSDT")
balance = api.get_balance("SWYFTX___SPOT")
```

## 中文

欢迎使用 bt_api 的 SWYFTX 文档。

### 快速开始

```bash
pip install bt_api_swyftx
```

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "SWYFTX___SPOT": {
        "api_key": "your_key",
        "secret": "your_secret",
    }
})

ticker = api.get_tick("SWYFTX___SPOT", "BTCUSDT")
balance = api.get_balance("SWYFTX___SPOT")
```

## API Reference

See source code in `src/bt_api_swyftx/` for detailed API documentation.
