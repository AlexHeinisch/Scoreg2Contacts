import pandas as pd
import numpy as np
import argparse

def get_vcard_string(surname, name, middle_name, title, email, tel,
                     street, zip, city, state, country) -> str:
    if pd.isna(middle_name):
        middle_name = ''
    email_str = '' if pd.isna(email) else f'EMAIL;PREF;INTERNET:{email}\n'

    return f"""BEGIN:VCARD
VERSION:3.0
N:{name};{surname};{middle_name};{title};
TEL;TYPE=home,voice;VALUE=uri:tel:{tel}
ADR;TYPE=home;LABEL="{street}\n{zip} {city}\n{state} {country}":;;{street};{city};{state};{zip};{country}
{email_str}END:VCARD
"""

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
    parser = argparse.ArgumentParser(
        prog='Scoreg2Contacts',
        description='A program used to create parental contact information given an excel file from SCOREG.'
    )
    parser.add_argument('-i', '--input-file', required=True,
                        type=str, help='Path to the SCOREG-Excel file that is parsed.')
    parser.add_argument('-o', '--output-file', required=True,
                        type=str, help='Path and name of the output file that shall be created.')
    args = parser.parse_args()
    
    content = process_excel(args.input_file)
    with open(args.output_file, 'w+') as fp:
        fp.write(content)
