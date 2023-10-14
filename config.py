from pydantic_settings import BaseSettings

class Config(BaseSettings):
    mother_prefix: str = '(Mutter)'
    father_prefix: str = '(Vater)'

    column_child_name: str = 'Nachname'
    column_child_surname: str = 'Vorname'
    column_child_middlename: str = 'Zweiter Name'
    column_street: str = 'Strasse'
    column_zip: str = 'PLZ'
    column_city: str = 'Stadt'
    column_country: str = 'Land'
    column_state: str = 'Bundesland'
    column_mother_name: str = 'Kontakt'
    column_father_name: str = 'Kontakt.1'
    column_mother_tel: str = 'Kontakt Telefon'
    column_father_tel: str = 'Kontakt Telefon.1'
    column_mother_mail: str = 'Kontakt E-Mail'
    column_father_mail: str = 'Kontakt E-Mail.1'

settings = Config()
