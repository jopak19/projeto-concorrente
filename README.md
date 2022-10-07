## Programa de requisições concorrentes

O programa realiza requisições concorrentes (usando threads) para um determinado site, medindo o tempo de resposta de cada conjunto de requests (cenários) e gerando um arquivo csv com os resultados. O objetivo é comparar os resultados com um programa equivalente que realiza requisições sequenciais.

### Requisitos

Para rodar o programa é necessário ter o Python 3 instalado. O programa foi testado com a versão 3.9.1.

### Como rodar

Para rodar o programa, basta executar o arquivo `concorrente.py` com o Python 3. Por exemplo:
    
```
python3 main.py
```