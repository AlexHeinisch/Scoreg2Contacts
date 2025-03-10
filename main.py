import pandas as pd
import numpy as np
import argparse
from config import settings

def get_vcard_string(title, surname, name, email, tel) -> str:
    middle_name = ''
    email_str = '' if pd.isna(email) else f'EMAIL;PREF;INTERNET:{email}\n'

    return f"""BEGIN:VCARD
VERSION:3.0
N:{name};{surname};{middle_name};{title};
TEL;TYPE=home,voice;VALUE=uri:tel:{tel}
ADR;TYPE=home;LABEL=""
{email_str}END:VCARD
"""

def process_excel(path) -> str:
    df = pd.read_excel(path)
    file_content = ''
    for _, row in df.iterrows():
        mother_name = row[settings.column_mother_name]
        mother_tel = row[settings.column_mother_tel]
        father_name = row[settings.column_father_name]
        father_tel = row[settings.column_father_tel]

        if not (mother_name is np.nan or mother_tel is np.nan):
            file_content += get_vcard_string(title=settings.mother_prefix, 
                                     surname=row[settings.column_child_surname],
                                     name=row[settings.column_child_name], 
                                     email=row[settings.column_mother_mail], tel=mother_tel)
        if not (father_name is np.nan or father_tel is np.nan):
            file_content += get_vcard_string(title=settings.father_prefix, 
                                     surname=row[settings.column_child_surname],
                                     name=row[settings.column_child_name], 
                                     email=row[settings.column_father_mail], tel=father_tel)
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
