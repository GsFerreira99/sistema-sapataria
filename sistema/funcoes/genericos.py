import locale
from PySide2.QtWidgets import QComboBox
from PySide2.QtCore import QDate

locale.setlocale(locale.LC_MONETARY, "pt_BR.UTF-8")


def filtro_dinheiro(valor):
    try:
        dinheiro = float(valor)
        return moeda(dinheiro)
    except:
        pass

    try:
        dinheiro = valor.replace(".", "")
        dinheiro = dinheiro.replace(",", ".")
        return moeda(dinheiro)
    except:
        pass

    return moeda(valor)


def converter_string_float(val):
    try:
        return float(val)
    except:
        try:
            return float(val.replace(",", "."))
        except:
            return float(0)


def data(data):
    try:
        string = data.strftime('%d-%m-%Y')
        return QDate(int(string[6:]), int(string[3:5]), int(string[:2]))
    except AttributeError:
        return data


def limpar_dinheiro(val):
    return converter_string_float(val.replace("R$ ", ""))


def limpar_porcento(val):
    try:
        val = val.replace("%", "")
        return converter_string_float(val)
    except:
        return converter_string_float(val)


def converter_string_int(val):
    try:
        return int(val)
    except:
        return 0


def mascara_porcento(val):
    limpo = limpar_porcento(val)
    return f"{limpo}%"


def moeda(valor):
    try:
        valor = float(valor)
    except:
        valor = limpar_dinheiro(valor)
    return locale.currency(valor, grouping=True)


def cpf_cnpj(val):
    if len(val) == 11:
        return f"{val[:3]}.{val[3:6]}.{val[6:9]}-{val[9:]}"
    elif len(val) == 14:
        return f"{val[:2]}.{val[2:5]}.{val[6:8]}/{val[8:12]}-{val[12:]}"
    else:
        return val


def celular(val):
    if len(val) == 11:
        return f"{val[:2]} {val[2:7]}-{val[7:]}"
    else:
        return val


def preencher_combo_box(dados: list, widget: QComboBox):
    widget.clear()
    widget.addItem('')
    widget.addItems(dados)
