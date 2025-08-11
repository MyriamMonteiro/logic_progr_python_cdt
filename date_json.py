#json_string = """ [
# {
# # {
# # "":"",
# # "":""
# # },
# # {
# # "":"",
# # "":""
# # }
# # }
# # ]
# # """


import json

json_string = """[
{
"nome_livro":"A queda do ceu",
"Editora":"Companhia das Letras",
"Autor(a)":"Davi Kopenawa e Bruce Albert",
"ano_edição":"2015",
"genero_literario":["Antropologia","Memorias","Cultura Indigena"]
},
{
"nome_livro":"Introducao a Logica de Programacao",
"Editora":"LTC (Livros Técnicos e Científicos Editora)",
"Autor(a)":"José Augusto N. G. Manzano",
"ano_edição":"1999",
"genero_literario":["Tecnica","Didatica","Educacao","Computacao"]
},
{
"nome_livro":"Necropolítica",
"Editora":"N-1 Edições",
"Autor(a)":"Achille Mbembe",
"ano_edição":"2018",
"genero_literario":["Filosofia","Ciências Sociais","Política"]
},
{
"nome_livro":"Design para Quem Não É Designer",
"Editora":"Alta Books",
"Autor(a)":"Robin Williams",
"ano_edição":"2014",
"genero_literario":["Design", "Comunicação Visual", "Didática"]
}
]
"""

dados = json.loads(json_string)

print(dados)
print('\n')

# import json
# dados = {'nome': 'Joao Silva', 'idade': 30,
#          'cidade': 'Sao Paulo', 'servico': 'Premium'}

# json_string = json.dumps(dados)

# print(json_string)

# #print(dados)