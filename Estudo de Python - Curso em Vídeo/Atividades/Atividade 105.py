def notas(*notas,sit=False):
    '''
    >> Identificar a média, maior e a menor nota
    :param notas: Inserir as notas (sem limites)
    :param sit: Situação da média das notas
    :return: Retorna um dicionario
    '''
    r = dict()
    r['total']=len(notas)
    r['maior']=max(notas)
    r['menor']=min(notas)
    r['media']=sum(notas)/len(notas)
    if sit:
        if r['media'] > 6:
            r['Situação'] = 'Boa!'
        elif r['media'] == 6:
            r['Situação'] = 'Mediana'
        elif r['media']<6:
            r['Situação'] = 'Ruim!'
    return r
    '''max=min=cont=soma=0
    for i in notas:
        soma+=i
        if cont == 0:
            max = i
        else:
            if i > max:
                max = i
        if cont == 0:
            min = i
        else:
            if i<min:
                min = i
        cont+=1
    media=soma/cont
    if media >6:
        situacao='Boa!'
    elif media==6:
        situacao='Mediana'
    else:
        situacao='Ruim!'
    dicionario = {'Total':len(notas),'maior':max,'menor':min,'média':media}
    if sit:
        dicionario['Situação']=situacao
    return dicionario
    '''
resp = notas(5.5,2.5,1.5, sit =True)
print(resp)