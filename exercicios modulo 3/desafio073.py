brasileirao = ('palmeiras', 'sao paulo', 'fluminense', 'flamengo', 'bahia', 'athletico pr', 'coritiba', 'gremio', 'vasco', 'vitoria', 'corinthians', 'internacional', 'atletico mg', 'bragantino', 'chapecoense', 'santos', 'botafogo', 'mirassol', 'remo', 'cruzeiro')

print(f'os primeiros cinco times do brasileirao são: {brasileirao[:5]}')
print(f'a zona de rebaixamento é composta por: {brasileirao[16:]}')
print(f'os times em ordem alfabetica: {sorted(brasileirao)}')
print(f'o chapecoense está na {brasileirao.index('chapecoense')+1}ª posição')