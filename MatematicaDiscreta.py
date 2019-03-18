def tratarExpressao(expre):
    expressao=expre.strip('{}')
    return expressao.split(',')

def RetratarExpre(lista):
    expre='{'
    for i,valor in enumerate(lista):
        if i < len(lista)-1:
            expre+=valor+','
        else:
            expre+=valor+'}'
    return expre

def RetrataConjunto(lista):
    del(lista[0])
    expre='{ {},'
    for c in lista:
        expre+='{'
        for i,valor in enumerate(c):
            if i < len(c)-1:
                expre+=valor+','
            else:
                expre+=valor+'},'
    return expre+'}'

def Uniao(valor1,valor2):
    for i in valor2:
        if i not in valor1:
            valor1.append(i)
    return valor1

def Interseccao(valor1,valor2):
    interseccao=[]
    for i in valor2:
        if i in valor1:
            interseccao.append(i)
    return interseccao

def Diferenca(valor1,valor2):
    dife=[]
    for i in valor1:
        if i not in valor2:
            dife.append(i)
    return dife

def Complemento(valor1,valor2):
    compe=[]
    for i in valor1:
        if i not in valor2:
            compe.append(i)
    return compe

def ConjuntosDasPartes(listaEntrada, listaInicial=None):
    listaInicial = listaInicial or []
    yield listaInicial
    if len(listaEntrada) == 0:
        return
    for i, sublista in enumerate(listaEntrada):
        for listaRetornada in ConjuntosDasPartes(listaEntrada[i + 1:], listaInicial + [sublista]):
            yield listaRetornada
        
def ProdutoCartesiano(valor1,valor2):
    pro=[]
    for i in valor1:
        for c in valor2:
            pr='('+i+','+c+')'
            pro.append(pr)
    return pro

def UniaoDisjunta(valor1,valor2):
    uniao=[]
    for i in valor1:
        va=i+'A'
        uniao.append(va)
    for i in valor2:
        va=i+'B'
        uniao.append(va)
    return uniao


expre1='{1,2,3,4}'
expre2='{5,6,3,4,7,9}'

print('Conjunto A=',expre1)
print('Conjunto B=',expre2)

uniao=Uniao(tratarExpressao(expre1),tratarExpressao(expre2))
print('\n União: ',RetratarExpre(uniao))

inter=Interseccao(tratarExpressao(expre1),tratarExpressao(expre2))
print('\n Intersecção: ',RetratarExpre(inter))

dife=Diferenca(tratarExpressao(expre1),tratarExpressao(expre2))
print('\n Diferença A-B:',RetratarExpre(dife))

comple=Complemento(tratarExpressao(expre1),tratarExpressao(expre2))
print('\n Complemento : ~B =',RetratarExpre(comple))

conju=list(ConjuntosDasPartes(tratarExpressao(expre1)))
print('\n ConjuntosDasPartes : A =',RetrataConjunto(conju))

pro=ProdutoCartesiano(tratarExpressao(expre1),tratarExpressao(expre2))
print('\n Produto Cartesiano: ',RetratarExpre(pro))

uniao=UniaoDisjunta(tratarExpressao(expre1),tratarExpressao(expre2))
print('\n  União Disjunta: A+B=',RetratarExpre(uniao))
