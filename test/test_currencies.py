from model.currency import Currency
import fixture.currency_api


def test_currencies(app):
    date = '20/03/2020'
    curr_from_ui = app.currency.get_curr(date)
    curr_from_api = fixture.currency_api.api(date)
    assert sorted(curr_from_ui, key=Currency.id_or_max) == sorted(curr_from_api, key=Currency.id_or_max)
