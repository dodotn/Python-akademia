import requests
from bs4 import BeautifulSoup
import csv
import sys
from typing import List

def scrape_election_data(url: str, output_file: str) -> None:
    """
    Scrape election data from a given URL and save it to a CSV file.

    Args:
        url (str): The URL of the election data page.
        output_file (str): The name of the output CSV file.

    Returns:
        None
    """
    try:
        # Stažení hlavní stránky
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Najít odkazy na jednotlivé obce
        links = soup.find_all('a', href=True)
        municipality_links = [
            'https://www.volby.cz/pls/ps2017nss/' + link['href']
            for link in links
            if 'ps311' in link['href'] and 'xobec' in link['href']
        ]

        print(f"Nalezeno obcí: {len(municipality_links)}")

        # Hlavička CSV
        header = ['kód obce', 'název obce', 'voliči v seznamu', 'vydané obálky', 'platné hlasy']
        party_names = []
        all_data = []

        for municipality_url in municipality_links:
            print(f"Zpracovávám obec: {municipality_url}")
            try:
                response = requests.get(municipality_url)
                response.raise_for_status()
                municipality_soup = BeautifulSoup(response.text, 'html.parser')

                # Základní data obce
                basic_data_table = municipality_soup.find('table', {'class': 'table'})
                if not basic_data_table:
                    print(f"Základní tabulka nenalezena pro obec: {municipality_url}")
                    continue

                rows = basic_data_table.find_all('tr')
                if len(rows) < 3:
                    print(f"Nedostatečný počet řádků v základní tabulce obce: {municipality_url}")
                    continue

                try:
                    # Zpracování třetího řádku tabulky (s daty obce)
                    data_cells = rows[2].find_all('td')
                    code = municipality_url.split('xobec=')[-1].split('&')[0]  # Extrahujeme kód obce z URL
                    name_tag = municipality_soup.find('td', class_='overflow_name')
                    name = name_tag.text.strip() if name_tag else "Neznámá obec"
                    voters = data_cells[3].text.strip().replace('\xa0', '').replace(' ', '')
                    envelopes = data_cells[4].text.strip().replace('\xa0', '').replace(' ', '')
                    valid_votes = data_cells[6].text.strip().replace('\xa0', '').replace(' ', '')

                    row_data = [code, name, voters, envelopes, valid_votes]
                    print(f"Základní data: {row_data}")
                except IndexError as e:
                    print(f"Chybějící data v základní tabulce obce: {municipality_url}")
                    print(f"Detail chyby: {e}")
                    continue

                # Data stran
                party_table = municipality_soup.find_all('table')[-1]
                if not party_table:
                    print(f"Tabulka s daty stran nenalezena pro obec: {municipality_url}")
                    continue

                party_rows = party_table.find_all('tr')[2:]
                if not party_rows:
                    print(f"Žádná data o stranách pro obec: {municipality_url}")
                    continue

                # Načíst názvy stran (pouze poprvé)
                if not party_names:
                    header_cells = party_table.find_all('tr')[1].find_all('td')
                    party_names = [cell.text.strip() for cell in header_cells if cell.text.strip()]
                    header.extend(party_names)

                # Načíst data pro strany
                party_votes = []
                for party_row in party_rows:
                    party_columns = party_row.find_all('td')
                    if len(party_columns) > 1:
                        votes = party_columns[1].text.strip().replace('\xa0', '').replace(' ', '')
                        party_votes.append(votes)
                    else:
                        print(f"Neplatný řádek ve stranách pro obec: {municipality_url}")
                row_data.extend(party_votes)

                all_data.append(row_data)

            except Exception as e:
                print(f"Chyba při zpracování obce: {municipality_url}")
                print(f"Detail chyby: {e}")
                continue

        # Uložení do CSV
        with open(output_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(all_data)

        print(f"Data byla uložena do souboru {output_file}.")

    except Exception as e:
        print(f"Nastala chyba: {e}")

# Spuštění
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Použití: python script.py <url> <output_file>")
    else:
        scrape_election_data(sys.argv[1], sys.argv[2])
