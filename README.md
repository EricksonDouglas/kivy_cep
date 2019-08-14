# **kivy_cep**

## Preparando o ambiente

```sh
#instale virtualenv e use o comando pra criar a pasta
$ virtualenv -p python3 cep_kivy
$ cd cep_kivy && source bin/activate
$ git clone https://github.com/EricksonDouglas/kivy_cep.git
$ cd kivy_cep && pip install -r requerimento.txt
```

## Vai executar a interface Kivy,  depois do teste unitário
``` sh
$ python3 main.py -t -w
```
## Executar com Interface Kivy
``` sh
$ python3 main.py -w
```
## Executar o TDD
``` sh
$ python3 main.py -t
```
## Executar modo Interativo
``` sh
# Validar só um CEP
# exemplo python3 main.py -c 123456
$ python3 main.py -c {numero do CEP}

# Validar uma lista de CEPs
# exemplo python3 main.py -lc 123456,123423,142356
$ python3 main -lc {lista de CEPs}

# Validar um arquivo com uma lista de CEPs
# exemplo python3 main.py -i lista_cep.txt
$ python3 main.py -i {nome do arquivo}

# Exportando os resultado para um arquivo
# exemplo python3 main.py -i importar_cep.txt -e exportar_cep.txt
$ python3 main.py -i {nome do arquivo - Entrada} -e {nome do arquivo - Saida}

# ou usando o comando do linux
# exemplo python3 main.py -i importar_cep.txt > exportar_cep.txt
$ python3 main.py -i {nome do arquivo - Entrada} > {nome do arquivo - Saida}

# ou pode usar o arquivo exportado, e adicionar mais
# exemplo python3 main.py -c 123456 >> exportar_cep.txt
$ python3 main.py -c {cep} >> {nome do arquivo - Saida}
```
