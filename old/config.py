from pydantic_settings import BaseSettings

class Config(BaseSettings):
    mother_prefix: str = '(Mutter)'
    father_prefix: str = '(Vater)'

    column_child_name: str = 'Nachname'
    column_child_surname: str = 'Vorname'
    column_street: str = 'Strasse'
    column_zip: str = 'PLZ'
    column_city: str = 'Stadt'
    column_country: str = 'Land'
    column_state: str = 'Bundesland'
    column_mother_name: str = 'Kontakt 1'
    column_father_name: str = 'Kontakt 2'
    column_mother_tel: str = 'Kontakt 1 Telefon'
    column_father_tel: str = 'Kontakt 2 Telefon'
    column_mother_mail: str = 'Kontakt 1 Email'
    column_father_mail: str = 'Kontakt 2 Email'

settings = Config()
