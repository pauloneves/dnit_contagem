# Baixa contagens do DNIT

O DNIT tem mais de 300 pontos de contagem contínua pelo Brasil. Fora isto, faz contagens eventuais pelo de acordo com a necessidade.

Também disponibilizei os [dados até 2018 no Kaggle](https://www.kaggle.com/pauloeduneves/dnit-contagem-de-trfego-rodovias-federais/) onde podem ser baixados mais rapidamente. 

Os dados foram baixados pelo arquivo [download_contagem.py]](download_contagem.py). O programa baixa pela api do website do DNIT. Os dados são baixados sequencialmente para não sobrecarregar seus servidores. Demora cerca de 2 dias para baixar tudo. 

O formato é bem próximo doque está publicado pela api do site. Json não é o melhor formato, mas pode ser lido usando o método `pd.read_json` do pandas (biblioteca Python). Pode-se ver um exemplo de uso dos dados no [notebook eda.ipynb](eda.ipynb).


## Descrição das contagens	

Os metadados são autoexplicativos pelo nome dos cabeçalhos. Abaixo detalho o que é mais difícil de descobrir.

### Sentido

- C) Crescente na kilometragem da via
- D) Decrescente na km da via

# Classe de veículos e sua descrição
	
- A) Ônibus/Cam de 2 eixos
- B) Ônibus/Cam de 3 eixos
- C) Caminhão de 4 eixos
- D) Caminhão de 5 eixos
- E) Caminhão de 6 eixos
- F) Caminhão de 7 eixos
- G) Caminhão de 8 eixos
- H) Caminhão de 9 eixos
- I) Passeio
- J) Moto
- L) Outros

# Equipamentos (`equipamentos_contagem.json`)

- duplo indica se é pista dupla ou simples