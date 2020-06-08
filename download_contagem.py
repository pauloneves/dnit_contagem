import requests
import json
import time

URL_BASE = "http://servicos.dnit.gov.br/dadospnct/api/"
API_VH = "VolumeHora/{id_equipamento}?ano={ano}&mes={mes}&dia={dia}&_={timestamp}"
API_EQUIP = "Equipamentos/GetEquipamentos?uf=&_={timestamp}"
API_DIAS_EQUIP = "Equipamentos/GetDiasEquipamento?idEquipamento={id_equipamento}&ano={ano}&mes={mes}&_={timestamp}"
OUT_DIR = "dados/"


def atimestamp():
    return int(time.time() * 1e4)


def baixa(url):
    response = requests.get(url)
    assert (
        response.ok and response.json()["sucesso"]
    ), f"request não foi bem sucedida. Status: {response.status_code} e {response.json()['sucesso']}"
    dados = response.json()["dado"]
    assert len(dados) > 0, "Dados retornaram vazios, url deve estar errada: " + url
    return dados


def get_vh(id_equipamento, ano, mes, dia):
    timestamp = atimestamp()
    url = URL_BASE + API_VH.format_map(locals())
    return baixa(url)


def get_equipamentos():
    timestamp = atimestamp()
    url = URL_BASE + API_EQUIP.format_map(locals())
    return baixa(url)


def get_dias(id_equipamento, ano, mes):
    timestamp = atimestamp()
    url = URL_BASE + API_DIAS_EQUIP.format_map(locals())
    return baixa(url)


def get_equipamento():
    pass


def grava_contagem(estado, estrada, id_equipamento, dados):
    with open(
        OUT_DIR + f"{estado}_{estrada}_{id_equipamento}_contagem.json",
        "w",
        encoding="utf8",
    ) as f:
        json.dump(dados, f, indent=2)


def baixa_tudo():
    equip = get_equipamentos()
    equip.sort(key=lambda x: f'{x["uf"]}{x["br"]}{x["km"]}')
    for e in equip[:2]:
        id_equipamento = e["idEquipamento"]
        dados = []
        print(f"{e['localizacaoCombo']}")
        for ano_meses in e["mesesVmdm"]:
            ano = ano_meses["ano"]
            meses = ano_meses["meses"]
            for mes in meses:
                # print(f"\t{ano}-{mes:02d}")
                for dia in get_dias(id_equipamento, ano, mes):
                    print(f"\t{ano}-{mes:02d}-{dia:02d}")
                    vh = get_vh(id_equipamento, ano, mes, dia)
                    assert len(vh) > 0, "Dados diários não podem ser vazios"
                    dados += vh
        grava_contagem(e["uf"], e["br"], id_equipamento, dados)
        del e["mesesVmdm"]

    with open(OUT_DIR + f"equipamentos_contagem.json", "w", encoding="utf8") as f:
        json.dump(equip, f, indent=2)


if __name__ == "__main__":
    baixa_tudo()
