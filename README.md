Análise de Tendências de Imigração para o Canadá
Este projeto contém um script Python que analisa dados de imigração de países da América Latina para o Canadá, focando nos quatro maiores países: Brasil, Argentina, Peru e Colômbia. O gráfico gerado exibe as tendências de imigração desses países, apresentando o total de imigrantes de cada um, ordenados de forma ascendente.

O que o código faz?
Carrega os dados: O script lê um arquivo CSV contendo dados de imigração para o Canadá a partir do caminho especificado no código. O arquivo é lido usando a biblioteca pandas.

Filtra os dados: O script filtra os dados para incluir apenas os quatro países da América Latina: Brasil, Argentina, Peru e Colômbia.

Ordena os dados: Os dados são ordenados com base no número total de imigrantes, de forma ascendente.

Criação do gráfico: O código utiliza as bibliotecas matplotlib e seaborn para criar um gráfico de barras horizontal. O eixo Y exibe os nomes dos países, enquanto o eixo X mostra o número total de imigrantes.

Exibe o gráfico: O gráfico é exibido na tela com os valores totais de imigrantes mostrados ao lado de cada barra.

Salva a imagem: O gráfico gerado é salvo como um arquivo PNG no diretório do projeto com o nome tendencias_imigracao.png.

Como executar o código
Pré-requisitos:

Python 3.x
As bibliotecas pandas, matplotlib e seaborn instaladas. Se não tiver essas bibliotecas, instale-as utilizando o seguinte comando:
bash
Copiar código
pip install pandas matplotlib seaborn
Passos para executar:

Altere o caminho do arquivo CSV no código para o caminho correto onde o arquivo de dados está localizado no seu sistema.
Execute o script Python.
bash
Copiar código
python nome_do_script.py
O gráfico será exibido na tela e também será salvo como um arquivo PNG no diretório do projeto.

Exemplo de Saída
O gráfico gerado mostrará os países Brasil, Argentina, Peru e Colômbia no eixo Y, com barras horizontais representando o total de imigrantes de cada país. Os valores totais serão exibidos ao lado das barras para uma visualização clara.

Arquivos do Projeto
nome_do_script.py: Contém o código para gerar o gráfico e salvar a imagem.
tendencias_imigracao.png: Imagem gerada pelo script (será salva no mesmo diretório).

![image](https://github.com/user-attachments/assets/c32e6657-0b04-4a22-9efe-1e0838be98db)

