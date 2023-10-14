from pydantic_settings import BaseSettings

class Config(BaseSettings):
    mother_prefix = '(Mutter)'
    father_prefix = '(Vater)'

    column_child_name = 'Nachname'
    column_child_surname = 'Vorname'
    column_child_middlename = 'Zweiter Name'
    column_street = 'Strasse'
    column_zip = 'PLZ'
    column_city = 'Stadt'
    column_country = 'Land'
    column_state = 'Bundesland'
    column_mother_name = 'Kontakt'
    column_father_name = 'Kontakt.1'
    column_mother_tel = 'Kontakt Telefon'
    column_father_tel = 'Kontakt Telefon.1'
    column_mother_mail = 'Kontakt E-Mail'
    column_father_mail = 'Kontakt E-Mail.1'

settings = Config()
