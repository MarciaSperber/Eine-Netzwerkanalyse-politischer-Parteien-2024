import pandas as pd
import re
import os

# Kriterien für jede Kategorie
categories = {
    'Friedenssicherung': [r'diplomat\w*', r'konfliktpräv\w*', r'abrüst\w*', r'frieden\w*', r'menschenrecht\w*', r'multilateral\w*', r'sicherheitspolit\w*', r'krisenintervent\w*', r'internationale zusammenarbeit', r'rüstungs\w*'],
    'Soziale Sicherheit': [r'sozialstaat\w*', r'grundsicher\w*', r'rente\w*', r'arbeitslos\w*', r'gesundheit\w*', r'\w*bildung\w*', r'armut\w*', r'familie\w*', r'inklus\w*', r'chancengleich\w*'],
    'Zuwanderung': [r'integration\w*', r'asyl\w*', r'fachkräfte\w*', r'einwanderung\w*', r'flüchtling\w*', r'staatsbürger\w*', r'migration\w*',  r'vielfalt\w*', r'toleran\w*', r'grenzkontrolle\w*'],
    'Klima- und Umweltschutz': [r'nachhaltig\w*', r'klima\w*', r'erneuerbar\w*', r'CO2\w*', r'biodivers\w*', r'umwelt\w*', r'ressource\w*', r'mobil\w*', r'kreislauf\w*', r'tier\w*'],
    'Wirtschaftswachstum': [r'innovati\w*', r'investition\w*', r'digital\w*', r'\w*unternehmen\w*', r'infrastruktur\w*', r'export\w*', r'arbeitsplätze\w*', r'wettbewerb\w*', r'steuer\w*', r'gründer\w*'],
    'Stabilität der Währung': [r'geld\w*', r'inflation\w*', r'zins\w*', r'wechselkurs\w*', r'zentralbank\w*', r'finanz\w*', r'haushalt\w*', r'schulden\w*', r'währung\w*', r'stabil\w*'],
    'Verbraucherschutz': [r'produkt\w*', r'transparen\w*', r'verbrauch\w*', r'\w*preis\w*', r'daten\w*' r'fair\w*', r'irreführend\w*', r'\w*rückruf\w*', r'\w*produkt\w*', r'zugang\w*'],
}

def calculate_relevance(text):
    text = text.lower()
    text = re.sub(r'\W+', ' ', text)

    # Zähle die Gesamtanzahl der Wörter im Text
    total_words = len(text.split())

    relevance = {category: 0 for category in categories}

    for category, criteria in categories.items():
        count = 0
        for kw in criteria:
            count += len(re.findall(kw, text))

        # Normalisierung auf einen Wert zwischen 0 und 1
        if total_words > 0:
            normalized_value = (count / total_words) * 35
            relevance[category] = min(normalized_value, 1)

    return relevance

def read_programms_of_parties(directory):
    parties_data = []

    for file in os.listdir(directory):
        if file.endswith('.txt'):
            path = os.path.join(directory, file)
            with open(path, 'r', encoding='utf-8') as f:
                programm_text = f.read()
                party_name = file[:-4]
                relevance = calculate_relevance(programm_text)
                relevance['Partei'] = party_name  # Füge den Parteinamen hinzu
                parties_data.append(relevance)

    return pd.DataFrame(parties_data)

# Verzeichnis mit den Wahlprogrammen festlegen
directory = 'C:/Users/Madousa/Documents/Uni Stuttgart/Master DH/Semester 2/Netzwerkanalyse/Wahlprogramme EUWahl 24'
parties_df = read_programms_of_parties(directory)

# Speichern der DataFrame als Excel-Datei
output_file_path = 'C:/Users/Madousa/Documents/parties_relevance.xlsx'
parties_df.to_excel(output_file_path, index=False)

print(f'Daten wurden erfolgreich in {output_file_path} gespeichert.')