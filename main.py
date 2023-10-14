import pandas as pd
import numpy as np

def get_vcard_string(surname, name, middle_name, title, email, tel,
                     street, zip, city, state, country) -> str:
    if pd.isna(middle_name):
        middle_name = ''
    result = \
f"""BEGIN:VCARD
VERSION:3.0
N:{name};{surname};{middle_name};{title};
TEL;TYPE=home,voice;VALUE=uri:tel:{tel}
ADR;TYPE=home;LABEL="{street}\n{zip} {city}\n{state} {country}":;;{street};{city};{state};{zip};{country}"""

    if not pd.isna(email):
        result += f'\nEMAIL;PREF;INTERNET:{email}'

    result += """
END:VCARD
"""
    return result

def process_excel(path) -> str:
    df = pd.read_excel(path)
    file_content = ''
    for _, row in df.iterrows():
        mother_name = row['Kontakt']
        mother_tel = row['Kontakt Telefon']
        father_name = row['Kontakt.1']
        father_tel = row['Kontakt Telefon.1']

        if not (mother_name is np.nan or mother_tel is np.nan):
            file_content += get_vcard_string(title='(Mutter)', 
                                     surname=row['Vorname'], name=row['Nachname'], 
                                     middle_name=row['Zweiter Name'], 
                                     email=row['Kontakt E-Mail'], tel=mother_tel,
                                     street=row['Strasse'], zip=row['PLZ'], country=row['Land'], 
                                     state=row['Bundesland'], city=row['Stadt'])
        if not (father_name is np.nan or father_tel is np.nan):
            file_content += get_vcard_string(title='(Vater)', 
                                     surname=row['Vorname'], name=row['Nachname'],
                                     middle_name=row['Zweiter Name'], 
                                     email=row['Kontakt E-Mail.1'], tel=father_tel, 
                                     street=row['Strasse'], zip=row['PLZ'], country=row['Land'], 
                                     state=row['Bundesland'], city=row['Stadt'])
    return file_content


if __name__ == '__main__':
    output_file = './contacts.vcf'
    input_file = 'input_files/scoreg.xlsx'
    content = process_excel(input_file)
    with open(output_file, 'w+') as fp:
        fp.write(content)
