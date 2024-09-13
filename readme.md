# Gerenciamento de Custos para Festa

Este projeto tem como objetivo realizar o gerenciamento dos custos de uma festa, categorizando as despesas em diferentes categorias como bebida, comida, funcionários, entre outros. Além disso, o sistema realiza a verificação das entradas fornecidas e gera uma planilha contendo todas as informações necessárias.

## Participantes
- **Matheus Rezende Milani Videira** - RA: 790809
- **Mauricio Herrera Fontes** - RA: 790986
- **Victor Germano Moreira Batista da Silva** - RA: 769775

## Video de demonstração

https://www.youtube.com/watch?v=z2hBGQN1aHo

## Funcionalidades

1. **Alocação de Custos**
   - Os custos são organizados em diferentes categorias, como:
     - Bebida
     - Comida
     - Funcionários
     - Entretenimento
     - Outros
     
2. **Validação de Entradas**
   - O sistema realiza a verificação dos dados inseridos pelos usuários. Caso haja qualquer erro ou falta de informações, o usuário é notificado com uma mensagem de erro apropriada.

3. **Geração de Planilha**
   - Após a alocação dos valores, o sistema compila os dados e gera uma planilha contendo:
     - Categorias
     - Valores alocados
     - Total de despesas
     - Qualquer outra informação relevante ao evento.

## Requisitos

- Python 3.x
- Bibliotecas necessárias:
  - antlr4-python3-runtime
  - xlsxwriter (para a geração de planilhas com fórmula)

### Realizado com
- Python 3.12
- Jdk 22
- antlr-4.13.2-complete
- antlr4-python3-runtime==4.13.2
- XlsxWriter==3.2.0
  
Para gerar os arquivos antlr com base no Programa.g4, entre na pasta do repositório e digite o comando abaixo:
```bash
java -cp "{caminho_ate_o_antlr}/antlr-4.13.2-complete.jar" org.antlr.v4.Tool -Dlanguage=Python3 -o antlr_generated Programa.g4
```
## Como executar

Execute os comandos abaixo:

1. Primeira instalação:
   ```bash
   python -m venv venv
   ./venv/Scripts/activate
   pip install -r requirements.txt
   ```
2. Para utilizar o compilador
   ```bash
   python main.py input.txt output.xlsx
   ```
