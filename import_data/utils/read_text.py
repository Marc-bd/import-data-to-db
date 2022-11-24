from .convert_data import convert_date, convert_hour
import json
from .write_json import write_json
from .format_name import remove_special_characters
import ipdb

return_data = []


def read_text(file_text):

    try:
        with open(file_text, "r") as txt:
            for line in txt:
                line_data = {
                    "tipo": int(line[0]),
                    "data": convert_date(line[1:9]),
                    "valor": int(line[9:19]) / 100,
                    "cpf": line[19:30],
                    "cartao": line[30:42],
                    "hora": convert_hour(line[42:48]),
                    "Dono da Loja": remove_special_characters(line[48:62]),
                    "Nome Loja": remove_special_characters(line[62:81]),
                }
                return_data.append(line_data)

    except FileNotFoundError:
        return "File doesnt Exist"

    return write_json(file={file_text}, data=return_data)
