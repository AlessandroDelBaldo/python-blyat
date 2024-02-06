def calcola_importo(fatture:list[dict])->list[float]|None:
    totale_importo = 0
    totale_importo_scontato = 0
    for fattura in fatture:
        importo = fattura["importo"]
        sconto_fattura = fattura["sconto_fattura"]
        importo_scontato = importo - (importo * sconto_fattura / 100)
        fattura["importo_scontato"] = importo_scontato
        totale_importo += importo
        totale_importo_scontato += importo_scontato
        return [totale_importo, totale_importo_scontato]

fatture=[
{"id":"Monticelli",
"importo":245.78,
"sconto_fattura":10
},
{"id":"Kola",
"importo":325.71,
"sconto_fattura":12
},
{"id":"Romagna",
"importo":245.78,
"sconto_fattura":8
},
{"id":"Bilancioni",
"importo":245.78,
"sconto_fattura":15
},
{"id":"Sanchi",
"importo":245.78,
"sconto_fattura":5
},
{"id":"Pontellini",
"importo":245.78,
"sconto_fattura":18
},
{"id":"Clementi",
"importo":245.78,
"sconto_fattura":20
},
{"id":"Arlotti",
"importo":245.78,
"sconto_fattura":19
},
{"id":"Nedria",
"importo":245.78,
"sconto_fattura":7
},
{"id":"Santini",
"importo":245.78,
"sconto_fattura":22
},
]

calcola_importo(fatture)

for i in fatture:
    print(i)
