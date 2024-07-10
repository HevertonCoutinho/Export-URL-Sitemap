# Gerador de Sitemaps em Python

## export-all.py
Este script Python permite exportar URLs de vários sitemaps para um único arquivo de texto.

### Como Usar
1. **Instalação de Dependências**:
   Certifique-se de ter o Python instalado em seu sistema. Instale as dependências necessárias usando o comando:  
2. **Execução do Script**:
- Abra o arquivo `export-all.py` em um editor de texto ou IDE Python.
- Modifique a lista `sitemap_urls` para conter os URLs dos sitemaps que você deseja unificar.
- Especifique o nome do arquivo de saída `output_file` onde os URLs serão exportados.
- Execute o script usando o seguinte comando no terminal:
  ```
  python export-all.py
  ```
3. **Resultado**:
- O script irá baixar os sitemaps especificados, extrair os URLs de cada um deles e salvar todos os URLs em um arquivo de texto especificado.


## export-slice.py
Este script Python permite exportar URLs de sitemaps individuais para arquivos separados, com base na quantidade de sitemaps fornecidos.

### Como Usar
1. **Instalação de Dependências**:
Certifique-se de ter o Python instalado em seu sistema. Instale as dependências necessárias usando o comando:
2. **Execução do Script**:
- Abra o arquivo `export-slice.py` em um editor de texto ou IDE Python.
- Modifique a lista `sitemap_urls` para conter os URLs dos sitemaps que você deseja dividir em arquivos separados.
- Execute o script usando o seguinte comando no terminal:
  ```
  python export-slice.py
  ```
3. **Resultado**:
- O script irá baixar cada sitemap especificado, extrair os URLs de cada um deles e salvar os URLs em arquivos separados, numerados sequencialmente.

### Contribuição
Sinta-se à vontade para contribuir com melhorias através de pull requests.
