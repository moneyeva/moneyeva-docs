import os
from mkdocs.plugins import BasePlugin


class TaxRatesTablePlugin(BasePlugin):
    def on_page_markdown(self, markdown, **kwargs):
        if "{{ tax_rates_table }}" not in markdown:
            return markdown

        url_path = '/examples/tax-rates'
        folder_path = f"docs{url_path}"
        files = os.listdir(folder_path)
        files.sort()

        table = "| Country | Jurisdiction | Type | Year | View Equation |\n"
        table += "|---------|--------------|------|------|---------------|\n"
        for file in files:
            if file.endswith('.md'):
                if os.path.isfile(os.path.join(folder_path, file)):
                    parts = file[:-3].split('--')
                    if len(parts) != 4:
                        raise ValueError(f"Invalid file name: {file}  File name must be in the format: country--jurisdiction--type--year.md")
                    table += f"| {parts[0]} | {parts[1]} | {parts[2]} | {parts[3]} | [View](./tax-rates/{file}) |\n"

        return markdown.replace("{{ tax_rates_table }}", table)
