# Desafio para Engenheiro de ML - Globo
Repositório criado para o desafio de engenharia de machine learning da Globo

## Descrição do desafio
### Contexto
Sua tarefa é ajudar o time de recomendação a desenvolver a oferta de recomendação do Leia Mais do g1, a qual toma como base uma matéria que o usuário está lendo para recomendar matérias similares.

Exemplo: https://g1.globo.com/pe/caruaru-regiao/noticia/2024/09/11/deolane-bezerra-segue-presa-apos-audiencia-de-custodia.ghtml

### Tarefa do time
Com base no dataset anexado, criar uma função, **em Python**, para retornar recomendações de matérias similares dada à matéria que o usuário está lendo. As recomendações serão exibidas no componente "Veja Mais".
Como existem outras ofertas de recomendação no g1, o approach desenvolvido para o "Veja Mais" deve considerar **apenas similaridade de conteúdo**, sendo uma oferta exclusivamente content-based. Aspectos relacionados ao perfil e consumo das pessoas usuárias não precisam ser considerados.
Cada matéria é identificada por sua url e a lista de matérias recomendadas deve conter 10 itens.

#### Premissas
1. Você tem um dataset com as informações textuais das matérias, com a seguinte estrutura:
    - url: str
    - title: str
    - embedding: List[float]

2. A saída da sua solução deve ser um arquivo csv com a seguinte estrutura:
    - url: str
    - recommended_urls: List[List[str, float]]

## Execução do código
### Configução
Para executar o código é necessário configurar um ambiente python com as bibliotecas necessárias.
Recomenda-se o uso da versão 3.12 do Python, usada no desenvolvimento deste repositório.
Seguir os passos para configuração de ambiente:
1. Criar um ambiente virtual com o comando `python -m venv .venv`
2. Ativar o ambiente criado `source .venv/bin/activate`
3. Instalar as bibliotecas necessárias `pip install -r requirements.txt`
4. Executar o script principal `python src/main.py`

### Outputs
1. **similarities.log** - Arquivo com os logs de execução do script para histórico
2. **src/data/recommendations.csv** - Arquivo CSV com o output da função conforme _"Premissas, item 2"_

## Premissas da solução desenvolvida
1. O script usa o embedding providenciado no dataset como base para o cálculo de similaridade
2. A similaridade é calculada usando a distância entre cossenos, recomendada para vetores multidimensionais como no caso de uso de embedding
3. O script irá retornar sempre 10 recomendações para cada matéria, conforme indicado na sessão _"Tarefa do time"_ sem um limite mínimo de similaridade
4. Para gerar o arquivo CSV de saída, cada matéria do dataset de entrada foi passada pela função de similaridade encontrando outras 10 matérias e desconsiderando ela mesma