# Madlibs con scelte multiple
import random

temi = {
    "avventura": {
        "template": "L'esploratore {nome} trovò un {oggetto} {aggettivo} nella {luogo}.",
        "richieste": ["nome", "oggetto", "aggettivo", "luogo"]
    },
    "cucina": {
        "template": "Lo chef {nome} preparò un {piatto} {aggettivo} con {ingrediente}.",
        "richieste": ["nome", "piatto", "aggettivo", "ingrediente"]
    }
}
