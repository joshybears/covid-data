import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
from datetime import datetime


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """

    execution_date = kwargs.get('execution_date').date()
    #execution_date = datetime(year=2020, month=9, day=1)

    date = execution_date.strftime('%m-%d-%Y')
    url = f'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/{date}.csv'
    response = requests.get(url)

    print(*args)
    df = pd.read_csv(io.StringIO(response.text), sep=',')
    df['load_date'] = execution_date.strftime('%Y-%m-%d')
    print(f'date is {execution_date}')
    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    print(output)
    assert output is not None, 'The output is undefined'
