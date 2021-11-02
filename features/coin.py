import requests

DRACO_URL = "https://api.mir4global.com/wallet/prices/draco/lastest"
DOLAR_URL = "https://economia.awesomeapi.com.br/all/USD-BRL"


def getDolarCotationInBrl() -> float:
    response = requests.get(DOLAR_URL).json()
    dolar_high = response["USD"]["high"]
    return float(dolar_high).__round__(2)


def getDracoPriceInUSD() -> float:
    response = requests.post(DRACO_URL).json()
    draco_rate = response["Data"]["USDDracoRate"]
    return float(draco_rate).__round__(2)


def convertDracoToBRL() -> float:
    draco_price = getDracoPriceInUSD()
    dolar_price = getDolarCotationInBrl()
    return float(draco_price * dolar_price).__round__(2)