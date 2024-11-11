from setuptools import setup

setup(
    name='tax_rates_table',
    entry_points={
        'mkdocs.plugins': [
            'tax_rates_table = plugins.tax_rates_table:TaxRatesTablePlugin'
        ]
    }
)
