# sempre que quiser enxergar uma pasta 
# abaixo, coloque isto aqui no comeco do arquivo
# ele colocou no módulo2 para poder executar diretamente
# sem precisar descer um nível
try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../src'
            )
        )
    )
except ImportError:
    raise

from pacote1.modulo1 import variavel1