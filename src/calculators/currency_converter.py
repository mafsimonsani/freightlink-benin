# currency_converter.py
# English: Convert CFA to USD and vice-versa

# def cfa_to_usd(cfa_amount, exchange_rate=620.0):
#     """Convert CFA francs to US Dollars"""
#     return cfa_amount / exchange_rate

# def usd_to_cfa(usd_amount, exchange_rate=620.0):
#     """Convert US Dollars to CFA Francs"""
#     return usd_amount * exchange_rate

# Français: Convertir CFA en USD et vice versa
def cfa_vers_usd(montant_cfa, taux_change=620.0):
    """Convertir des Francs CFA en Dollars US"""
    return montant_cfa / taux_change

def usd_vers_cfa(montant_usd, taux_change=620.0):
    """Convertir des Dollars US en Francs CFA"""
    return montant_usd * taux_change

# Test the functions
if __name__ == "__main__":
    # English test
    # print("1, 000, 000 CFA =", cfa_to_usd(1000000), "USD")
    # print("1000 USD =", usd_to_cfa(1000), "CFA")
    
    # Test français
    print("1 000 000 CFA =", cfa_vers_usd(1000000), "USD")
    print("1000 USD =", usd_vers_cfa(1000), "CFA")