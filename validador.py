import re


class Validador:

    def cep(num):
        def _verificador():
            if len(result) == 0:
                return {"valido": 1}
            else:
                return {"valido":0,"repetitivo":result}

        if (num.isnumeric()) and 100000<int(num)<999999:
            index_par,index_impar = num[::2],num[::-2]
            re_repetido = re.compile(r".*(.).*\1")
            result = list()
            if index_par[0] in index_par[1:] or index_par[-1] in index_par[:-1]:
                result.append(int(re_repetido.match(index_par).group(1)))
            if index_impar[0] in index_impar[1:] or index_impar[-1] in index_impar[:-1]:
                result.append(int(re_repetido.match(index_impar).group(1)))

            return _verificador()
        else:
            return None
