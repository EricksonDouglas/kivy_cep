# kivy_cep

## Preparando o ambiente

```sh
#instale virtualenv e use o comando pra criar a pasta
$  virtualenv -p python3 cep_kivy
$  cd cep_kivy && source bin/activate
$ git clone https://github.com/EricksonDouglas/kivy_cep.git
$ cd kivy_cep && pip install -r requerimento.txt
```

## Executar modo Interativo

``` sh
# exemplo python3 main.py -c 123456
$ python3 main.py -c {numero do CEP}
```
## Executar com Interface Kivy
``` sh
$ python3 main.py -w
```
## Executar o TDD
``` sh
$ python3 main.py -t
```
## Vai executar a interface Kivy,  depois do teste unitário
``` sh
$ python3 main.py -t -w
```
