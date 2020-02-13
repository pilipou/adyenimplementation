import Adyen as Adyen


def getAll():
    adyen = Adyen.Adyen()
    adyen.client.xapikey = 'AQEvhmfxKorNbhNDw0m/n3Q5qf3VeINEAZpaSE5TynSujCHnR3/qRdp+KWCc+aOkGbsQwV1bDb7kfNy1WIxIIkxgBw==-G09SKxVbs058XvVm6f3J5l5fghU2o3L0JvZpW2+O460=-p8zgE4JWse66WdGM'

    request = {
        'merchantAccount': 'PhilippKellerCOM',
        'countryCode': 'DE',
        'amount': {
            'value': 1000,
            'currency': 'EUR'
        },
        'channel': 'Web'
    }
    response = adyen.checkout.payment_methods(request)

    return response
