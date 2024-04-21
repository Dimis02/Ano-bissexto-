#Desenvolva um programa em Python que determine se um determinado ano é bissexto ou não, levando em consideração as regras do calendário gregoriano. 
#Além disso, seu programa deve fornecer uma explicação detalhada do motivo pelo qual o ano é ou não é bissexto, com base nas seguintes condições:
#Um ano é bissexto se for divisível por 4, exceto quando também for divisível por 100, a menos que seja divisível por 400.
#Caso o ano seja bissexto, deve-se explicar que ele possui 366 dias.
#Se o ano não for bissexto, deve-se explicar que ele possui 365 dias.
#O programa deve solicitar ao usuário que insira o ano desejado e, em seguida, fornecer a resposta juntamente com a 
#explicação correspondente.

ano = int(input("Digite o ano para verificar se é bissexto: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    bissexto = True
else:
    bissexto = False

if bissexto:
    print(f"O ano {ano} é bissexto, pois atende às seguintes condições:")
    print("- É divisível por 4.")
    if ano % 100 == 0:
        print("- É divisível por 100.")
    else:
        print("- Não é divisível por 100.")
    if ano % 400 == 0:
        print("- É divisível por 400.")
    else:
        print("- Não é divisível por 400.")
    print("Portanto, ele possui 366 dias.")
else:
    print(f"O ano {ano} não é bissexto, pois não atende às condições para ser bissexto.")
    print("Portanto, ele possui 365 dias.")
