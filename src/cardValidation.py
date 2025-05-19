import re

def validate_credit_card(card_number):
    """
    Valida o número do cartão de crédito usando o algoritmo de Luhn
    e identifica a bandeira do cartão.

    :param card_number: Número do cartão de crédito.
    :return: Dicionário contendo a validade e a bandeira do cartão.
    """
    # Remove espaços e caracteres não numéricos
    card_number = re.sub(r'\D', '', card_number)

    # Função para validar o número do cartão com o algoritmo de Luhn
    def is_valid_luhn(card_number):
        total = 0
        reverse_digits = card_number[::-1]

        for i, digit in enumerate(reverse_digits):
            n = int(digit)
            if i % 2 == 1:  # Dobra os dígitos em posições alternadas
                n *= 2
                if n > 9:
                    n -= 9
            total += n

        return total % 10 == 0

    # Identificar a bandeira do cartão
    def get_card_brand(card_number):
        patterns = {
            "Visa": r"^4[0-9]{12}(?:[0-9]{3})?$",
            "MasterCard": r"^5[1-5][0-9]{14}$",
            "AmericanExpress": r"^3[47][0-9]{13}$",
            "DinersClub": r"^3(?:0[0-5]|[68][0-9])[0-9]{11}$",
            "Discover": r"^6(?:011|5[0-9]{2})[0-9]{12}$",
            "JCB": r"^(?:2131|1800|35\d{3})\d{11}$",
            "enRoute": r"^(2014|2149)\d{11}$",
            "Voyager": r"^8699[0-9]{11}$",
            "HiperCard": r"^(606282|3841)[0-9]{10,12}$",
            "Aura": r"^50[0-9]{14,17}$"
        }

        for brand, pattern in patterns.items():
            if re.match(pattern, card_number):
                return brand

        return "Unknown"

    is_valid = is_valid_luhn(card_number)
    brand = get_card_brand(card_number)

    return {
        "is_valid": is_valid,
        "brand": brand
    }


if __name__=="__main__":
    card_number = input("Digite o número do cartão de crédito: ")
    result = validate_credit_card(card_number)
    print(f"Cartão válido: {result['is_valid']}")
    print(f"Bandeira: {result['brand']}")
