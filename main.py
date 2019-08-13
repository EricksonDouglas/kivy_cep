import argparse
from subprocess      import call
from validador import Validador

parser = argparse.ArgumentParser()
parser.add_argument("-w", "--window", action="store_true",help="Executar interface")
parser.add_argument("-t", "--test", action="store_true",help="Executar o TDD")
parser.add_argument("-c", "--cep",type=str,help="Resultado do cep interativo")
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
                text = "Não é valido\n{} é um digito repetitivo alternado em par".format(result["repetitivo"][0])
            elif len(result["repetitivo"])==2:
                if result["repetitivo"][0] == result["repetitivo"][1]:
                    text = "Não é valido\n{} é um digito repetitivo alternado em par".format(result["repetitivo"][0])
                else:
                    text = "Não é valido\nos números {r[0]} e {r[1]} são digito repetitivo alternado em par".format(r=result["repetitivo"])
            print("{} - {}".format(args.cep,text))
    else: print("{} - Cep Invalido".format(args.cep))
