import argparse
from subprocess      import call
from validador import Validador

parser = argparse.ArgumentParser()
parser.add_argument("-w", "--window", action="store_true",help="Executar interface")
parser.add_argument("-t", "--test", action="store_true",help="Executar o TDD")
parser.add_argument("-c", "--cep",type=str,help="Resultado do CEP interativo")
parser.add_argument("-lc", "--lista_cep",type=str,help="Resultado da lista de CEPs interativo")
parser.add_argument("-i", "--importar",type=str,help="Importar arquivo txt de CEPs")
parser.add_argument("-e", "--exportar",type=str,help="Exportar os resultados em txt")

args = parser.parse_args()
if args.window and args.test:
    call("python3 tdd.py && python3 kivyApp.py",shell=True)
elif args.test:
    call("python3 tdd.py",shell=True)
elif args.window:
    call("python3 kivyApp.py",shell=True)
elif args.cep:
    result = Validador.cep(args.cep)
    if result:
        if result["valido"] == 1: print("{} - É Valido".format(args.cep))
        else:
            if len(result["repetitivo"])==1:
                text = "Não é valido {} é um digito repetitivo alternado em par".format(result["repetitivo"][0])
            elif len(result["repetitivo"])==2:
                if result["repetitivo"][0] == result["repetitivo"][1]:
                    text = "Não é valido {} é um digito repetitivo alternado em par".format(result["repetitivo"][0])
                else:
                    text = "Não é valido os números {r[0]} e {r[1]} são digito repetitivo alternado em par".format(r=result["repetitivo"])
            print("{} - {}".format(args.cep,text))
    else: print("{} - Cep Incorreto".format(args.cep))
elif args.lista_cep:
    for cep in args.lista_cep.split(","):
        result = Validador.cep(cep)
        if result:
            if result["valido"] == 1: print("{} - É Valido".format(cep))
            else:
                if len(result["repetitivo"])==1:
                    text = "Não é valido {} é um digito repetitivo alternado em par".format(result["repetitivo"][0])
                elif len(result["repetitivo"])==2:
                    if result["repetitivo"][0] == result["repetitivo"][1]:
                        text = "Não é valido {} é um digito repetitivo alternado em par".format(result["repetitivo"][0])
                    else:
                        text = "Não é valido os números {r[0]} e {r[1]} são digito repetitivo alternado em par".format(r=result["repetitivo"])
                print("{} - {}".format(cep,text))
        else: print("{} - Cep Incorreto".format(cep))

elif args.importar and args.exportar:
    with open(args.exportar,"w") as arqwrite:
        with open(args.importar,"r") as arqfile:
            for cep in arqfile.read().split("\n")[:-1]:
                result = Validador.cep(cep)
                if result:
                    if result["valido"] == 1: arqwrite.write("{} - É Valido\n".format(cep))
                    else:
                        if len(result["repetitivo"])==1:
                            text = "Não é valido {} é um digito repetitivo alternado em par".format(result["repetitivo"][0])
                        elif len(result["repetitivo"])==2:
                            if result["repetitivo"][0] == result["repetitivo"][1]:
                                text = "Não é valido {} é um digito repetitivo alternado em par".format(result["repetitivo"][0])
                            else:
                                text = "Não é valido os números {r[0]} e {r[1]} são digito repetitivo alternado em par".format(r=result["repetitivo"])
                        arqwrite.write("{} - {}\n".format(cep,text))
                else: arqwrite.write("{} - Cep Incorreto\n".format(cep))


elif args.importar:
    with open(args.importar,"r") as arqfile:
        for cep in arqfile.read().split("\n")[:-1]:
            result = Validador.cep(cep)
            if result:
                if result["valido"] == 1: print("{} - É Valido".format(cep))
                else:
                    if len(result["repetitivo"])==1:
                        text = "Não é valido {} é um digito repetitivo alternado em par".format(result["repetitivo"][0])
                    elif len(result["repetitivo"])==2:
                        if result["repetitivo"][0] == result["repetitivo"][1]:
                            text = "Não é valido {} é um digito repetitivo alternado em par".format(result["repetitivo"][0])
                        else:
                            text = "Não é valido\nos números {r[0]} e {r[1]} são digito repetitivo alternado em par".format(r=result["repetitivo"])
                    print("{} - {}".format(cep,text))
            else: print("{} - Cep Incorreto".format(cep))
