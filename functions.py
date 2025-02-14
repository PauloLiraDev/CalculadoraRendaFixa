import requests

def get_selic_annual():
    response = requests.get("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados/ultimos/1?formato=json")
    data = response.json()
    selic_diaria = float(data[0]["valor"]) / 100
    selic_anual = ((1 + selic_diaria) ** 252 - 1) * 100
    return selic_anual


def calculate_investment(cdi_percentage, selic_rate):
    monthly_rate = (selic_rate / 100) / 12
    return cdi_percentage * monthly_rate


def compost_interest(principal, rate, time):
    return principal * (1 + rate) ** time


def aliquot_ir(months):
    aliquot = 0 
    if months < 6:
        aliquot = 22.5
    elif months < 12:
        aliquot = 20
    elif months < 24:
        aliquot = 17.5
    else:
        aliquot = 15
    return aliquot