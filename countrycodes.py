def getCountryCode(code):
    country_codes = {
        '+51': 'PE',  # Perú
        '+56': 'CL',  # Chile
        '+54': 'AR',  # Argentina
        '+52': 'MX',  # México
        '+34': 'ES',  # España
        '+591': 'BO', # Bolivia
        '+55': 'BR',  # Brasil
        '+57': 'CO',  # Colombia
        '+593': 'EC', # Ecuador
        '+507': 'PA', # Panamá
        '+595': 'PY', # Paraguay
        '+598': 'UY', # Uruguay
        '+58': 'VE',  # Venezuela
        '+506': 'CR', # Costa Rica
        '+504': 'HN', # Honduras
        '+1': 'US',   # Estados Unidos
        '+1': 'CA',   # Canadá
        '+44': 'GB',  # Reino Unido
        '+61': 'AU',  # Australia
        '+64': 'NZ',  # Nueva Zelanda
        '+81': 'JP',  # Japón
        '+82': 'KR',  # Corea del Sur
        '+86': 'CN',  # China
        '+91': 'IN',  # India
        '+7': 'RU',   # Rusia
        '+33': 'FR',  # Francia
        '+49': 'DE',  # Alemania
        '+39': 'IT',  # Italia
        '+47': 'NO',  # Noruega
        '+46': 'SE',  # Suecia
        '+31': 'NL',  # Países Bajos
        '+32': 'BE',  # Bélgica
        '+41': 'CH',  # Suiza
        '+43': 'AT',  # Austria
        '+420': 'CZ', # República Checa
        '+48': 'PL',  # Polonia
        '+351': 'PT', # Portugal
        '+30': 'GR',  # Grecia
        '+90': 'TR',  # Turquía
        '+234': 'NG', # Nigeria
        '+27': 'ZA',  # Sudáfrica
        '+53': 'CU',  # Cuba
        '+62': 'ID',  # Indonesia
        '+60': 'MY',  # Malasia
        '+65': 'SG',  # Singapur
        '+63': 'PH',  # Filipinas
        '+66': 'TH',  # Tailandia
        '+855': 'KH', # Camboya
        '+84': 'VN',  # Vietnam
        '+92': 'PK',  # Pakistán
        '+98': 'IR',  # Irán
        '+20': 'EG',  # Egipto
        '+212': 'MA', # Marruecos
        '+216': 'TN', # Túnez
        '+971': 'AE', # Emiratos Árabes Unidos
        '+972': 'IL', # Israel
        '+90': 'TR',  # Turquía
        '+64': 'NZ',  # Nueva Zelanda
    }

    if code in country_codes:
        return country_codes[code]
    else:
        return False