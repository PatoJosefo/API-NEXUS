# NEXUS


---

# Índice

* [Projeto](#projeto)
* [Requisitos Funcionais e Não Funcionais](#requisitos-funcionais-e-não-funcionais)
* [Tecnologias e Ferramentas Utilizadas](#tecnologias-e-ferramentas-utilizadas)
* [Sprints](#sprints)
* [Backlog](#backlog)
* [Backlog do Produto](#backlog-do-produto)
* [Registro de Atividade das Sprints ](#registro-de-atividade-das-sprints)
* [Protótipo do Figma](#protótipo-do-figma)
* [Autores](#autores)

---

# Projeto
> **Status do projeto**  
> O objetivo deste projeto é desenvolver uma plataforma web que disponibilize informações sobre o desempenho dos municípios do Estado de São Paulo no comércio exterior, com base nos dados abertos do Ministério do Desenvolvimento, Indústria, Comércio e Serviços. Essa ferramenta fornecerá aos tomadores de decisão dados claros e acessíveis, permitindo a identificação de municípios que estejam em ascensão, estagnação ou declínio no mercado internacional.

---

# Requisitos Funcionais e Não Funcionais
🔗[Clique aqui para visualizar os requisitos do produto](https://docs.google.com/spreadsheets/d/1E7RuFhJ5bi-8nax7y87k7zGJ2A_NBVDxnHbVd0v4pT0/edit?gid=1719630846#gid=1719630846)


<table style="width: 100%; border-collapse: collapse;">
    <thead>
        <tr>
            <th style="border: 1px solid #ddd; text-align: center;">ID</th>
            <th style="border: 1px solid #ddd;">Requisitos Funcionais</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border: 1px solid #ddd; text-align: center;">RF01</td>
            <td style="border: 1px solid #ddd;">Segmentação de Município: Apresenta informações detalhadas acerca de cada município do estado de São Paulo</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd; text-align: center;">RF02</td>
            <td style="border: 1px solid #ddd;">Busca e filtros: Ferramentas que permitam buscar cargas por código NCM e aplicar filtros personalizados para análise específica</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd; text-align: center;">RF03</td>
            <td style="border: 1px solid #ddd;">Painel de Estatísticas: Visualização gráfica interatica, apresentando a evolução da balança comercial dos municípios no período de 2019 a 2024</td>
        </tr>
    </tbody>
        <td>
        </td>
        <td>
        </td>
    <thead>
        <tr>
            <th style="border: 1px solid #ddd; text-align: center;">ID</th>
            <th style="border: 1px solid #ddd;">Requisitos Não Funcionais</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border: 1px solid #ddd; text-align: center;">RNF01</td>
            <td style="border: 1px solid #ddd;">Utilizar a ferramenta Google Colab para preparar a base de dados do projeto</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd; text-align: center;">RNF02</td>
            <td style="border: 1px solid #ddd;">O sistemma deve ser respossivo para todos os dispositivos.</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd; text-align: center;">RNF03</td>
            <td style="border: 1px solid #ddd;">O HTML5 deve ser utilizado para a arquitetura da informação do site</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd; text-align: center;">RNF04</td>
            <td style="border: 1px solid #ddd;">Utilizar o GIthub para ter controle sob a versão dos artefatos do projeto</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd; text-align: center;">RNF05</td>
            <td style="border: 1px solid #ddd;">Desenvolver o back-end utilizando a linguagem Python</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd; text-align: center;">RNF06</td>
            <td style="border: 1px solid #ddd;">O CSS3 deve ser utilizado para definição do layout e demais características de renderizações</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd; text-align: center;">RNF07</td>
            <td style="border: 1px solid #ddd;">Desenvolver uma interface interativa e de fácil compreensão</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd; text-align: center;">RNF08</td>
            <td style="border: 1px solid #ddd;">O MSQL/MariaDB devem ser utilizados como sistemas gerenciadores de banco de dados</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd; text-align: center;">RNF09</td>
            <td style="border: 1px solid #ddd;">Evitar a utilização de framework de mapeamento objeto-relacional para implementação de operações em banco de dados</td>
        </tr>
    </tbody>
</table>

---

#  Tecnologias e Ferramentas Utilizadas


<div align="center">
  <table>
  <tr>
    <td align="center" width="70">
      <img src="documentation/images/figma.svg" width="48" height="48" alt="HTML" />
      <span>FIGMA</span>
    </td>
    <td align="center" width="70">
      <img src="documentation/images/html5.svg" width="48" height="48" alt="HTML" />
      <span>HTML5</span>
    </td>
    <td align="center" width="70">
      <img src="documentation/images/css3.svg" width="48" height="48" alt="HTML" />
      <span>CSS3</span>
    </td>
    <td align="center" width="70">
      <img src="documentation/images/python.svg" width="48" height="48" alt="HTML" />
      <span>PYTHON</span>
    </td>
    <td align="center" width="70">
      <img src="documentation/images/google-sheets.svg" width="48" height="48" alt="HTML" />
      <span>SHEETS</span>
    </td>
    <td align="center" width="70">
      <img src="documentation/images/google-colab.svg" width="48" height="48" alt="HTML" />
      <span>COLAB</span>
    </td>
    <td align="center" width="70">
      <img src="documentation/images/jira.png" width="48" height="48" alt="HTML" />
      <span>JIRA</span>
    </td>
    <td align="center" width="70">
      <img src="documentation/images/discord.png" width="48" height="48" alt="HTML" />
      <span>DISCORD</span>
    </td>
    </tr>
    </table>
</div>   

---

# Sprints

<table style="width: 100%; border-collapse: collapse;">
    <thead>
        <tr>
            <th style="border: 1px solid #ddd;">Sprint</th>
            <th style="border: 1px solid #ddd;">Previsão</th>
            <th style="border: 1px solid #ddd;">Status</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border: 1px solid #ddd;">Kick Off</td>
            <td style="border: 1px solid #ddd;">24/02/2025 - 28/02/2025</td>
            <td style="border: 1px solid #ddd;">Concluído</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd;">Sprint 1</td>
            <td style="border: 1px solid #ddd;">10/03/2025 - 30/03/2025</td>
            <td style="border: 1px solid #ddd;">Concluído</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd;">Sprint 2</td>
            <td style="border: 1px solid #ddd;">07/04/2025 - 27/04/2025</td>
            <td style="border: 1px solid #ddd;">Em expectativa</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd;">Sprint 3</td>
            <td style="border: 1px solid #ddd;">05/05/2025 - 25/05/2025</td>
            <td style="border: 1px solid #ddd;">Em expectativa</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd;">Feira de Soluções</td>
            <td style="border: 1px solid #ddd;">29/06/2025</td>
            <td style="border: 1px solid #ddd;">Em expectativa</td>
        </tr>
    </tbody>
</table>    

---

# Backlog 
🔗[Clique aqui para visualizar o backlog do produto](https://docs.google.com/spreadsheets/d/1E7RuFhJ5bi-8nax7y87k7zGJ2A_NBVDxnHbVd0v4pT0/edit?gid=0#gid=0)

---

# Backlog do Produto

<table style="width: 100%; border-collapse: collapse;">
    <thead>
        <tr>
            <th style="border: 1px solid #ddd; text-align: center">Requisito</th>
            <th style="border: 1px solid #ddd; text-align: center">User Story</th>
            <th style="border: 1px solid #ddd; text-align: center;">Prioridade</th>
            <th style="border: 1px solid #ddd; text-align: center;">Estimativa</th>
            <th style="border: 1px solid #ddd; text-align: center;">Sprint</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border: 1px solid #ddd;">Lista de dados de exportação de todos os municípios de São Paulo</td>
            <td style="border: 1px solid #ddd;">Eu, como usuário, gostaria de visualizar uma lista dos municípios do estado de São Paulo e suas exportações, para entender os padrões de comércio internacional</td>
            <td style="border: 1px solid #ddd; text-align: center;">Alta</td>
            <td style="border: 1px solid #ddd; text-align: center;">13</td>
            <td style="border: 1px solid #ddd; text-align: center;">1</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd;">Filtrar as cargas dos municípios de São Paulo entre os anos de 2019 até 2024</td>
            <td style="border: 1px solid #ddd;">Eu, como usuário, gostaria de filtrar as cargas exportadas mensalmente entre os anos de 2019 a 2024 nos municípios de São Paulo, para ter mais conhecimento sobre as cargas exportadas entre esse período de tempo</td>
            <td style="border: 1px solid #ddd; text-align: center;">Alta</td>
            <td style="border: 1px solid #ddd; text-align: center;">13</td>
            <td style="border: 1px solid #ddd; text-align: center;">2</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd;">Criar um gráfico de exportação dos municípios de São Paulo</td>
            <td style="border: 1px solid #ddd;">Eu, como usuário, gostaria de um gráfico onde fosse possível visualizar os dados de exportação de cada município do estado de São Paulo, para ter mais conhecimento sobre as exportções municipais</td>
            <td style="border: 1px solid #ddd; text-align: center;">Alta</td>
            <td style="border: 1px solid #ddd; text-align: center;">13</td>
            <td style="border: 1px solid #ddd; text-align: center;">1</td>
        </tr>
        <tr> 
            <td style="border: 1px solid #ddd;">Criar um gráfico com as 5 maiores exportações de cada município</td>
            <td style="border: 1px solid #ddd;">Eu, como usuário, gostaria de um gráfico onde fosse possível visualizar os dados das 5 maiores exportações de cada município do estado de São Paulo,  para ter maior conhecimento sobre as exportações de cada município</td>
            <td style="border: 1px solid #ddd; text-align: center;">Alta</td>
            <td style="border: 1px solid #ddd; text-align: center;">13</td>
            <td style="border: 1px solid #ddd; text-align: center;">1</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd;">Comparar desempenho comercial de municípios</td>
            <td style="border: 1px solid #ddd;">Eu, como usuário, gostaria de comparar o desempenho comercial de cada município do estado de São Paulo, para ter maior conhecimento sobre as disparidades entre o mercado de cada município detalhadamente</td>
            <td style="border: 1px solid #ddd; text-align: center;">Alta</td>
            <td style="border: 1px solid #ddd; text-align: center;">8</td>
            <td style="border: 1px solid #ddd; text-align: center;">2</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd;">Produtos mais exportados dos municípios do estado de São Paulo</td>
            <td style="border: 1px solid #ddd;">Eu, como usuário, gostaria de filtrar os produtos mais exportados provenientes de cada município do estado de São Paulo, para ter mais conhecimento sobre os produtos mais importantes para  o mercado de cada município</td>
            <td style="border: 1px solid #ddd; text-align: center;">Alta</td>
            <td style="border: 1px solid #ddd; text-align: center;">13</td>
            <td style="border: 1px solid #ddd; text-align: center;">3</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd;">Diversidade de produtos exportados</td>
            <td style="border: 1px solid #ddd;">Eu, como usuário, gostaria de visualizar a diversidade de produtos exportados pelos municípios de São Paulo, para ter maior conhecimento sobre os produtos de cada município</td>
            <td style="border: 1px solid #ddd; text-align: center;">Alta</td>
            <td style="border: 1px solid #ddd; text-align: center;">8</td>
            <td style="border: 1px solid #ddd; text-align: center;">3</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd;">Exibir valores da balança comercial</td>
            <td style="border: 1px solid #ddd;">Eu, como usuário, gostaria de visualizar os valores da balança comercial provenientes do estado de São Paulo, para ter maior conhecimento sobre as diferenças entre as exportações e importações</td>
            <td style="border: 1px solid #ddd; text-align: center;">Alta</td>
            <td style="border: 1px solid #ddd; text-align: center;">8</td>
            <td style="border: 1px solid #ddd; text-align: center;">3</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd;">Exibir padrões de variações sazonais de oferta e demanda que afetam empresas</td>
            <td style="border: 1px solid #ddd;">Eu, como usuário, gostaria de visualizar os padrões de variações sazonais de oferta e demanda que afetam empresas, para ter maior conhecimento sobre como as empresas são afetadas</td>
            <td style="border: 1px solid #ddd; text-align: center;">Alta</td>
            <td style="border: 1px solid #ddd; text-align: center;">8</td>
            <td style="border: 1px solid #ddd; text-align: center;">2</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd;">Mapeamento dos principais fornecedores de cada município de São Paulo</td>
            <td style="border: 1px solid #ddd;">Eu, como usuário, gostaria de visualizar um mapa que apresente dados acerca dos principais fornecedores de cada município, para ter maior conhecimento sobre os maiores fornecedores do estado de São Paulo</td>
            <td style="border: 1px solid #ddd; text-align: center;">Alta</td>
            <td style="border: 1px solid #ddd; text-align: center;">13</td>
            <td style="border: 1px solid #ddd; text-align: center;">2</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd;">Apresentar riscos ocasionais causados pela dependência de mercados específicos</td>
            <td style="border: 1px solid #ddd;">Eu, como usuário, gostaria de visualizar os riscos ocasionais causados pela dependência de mercados específicos, para compreender os riscos ocasionais</td>
            <td style="border: 1px solid #ddd; text-align: center;">Alta</td>
            <td style="border: 1px solid #ddd; text-align: center;">5</td>
            <td style="border: 1px solid #ddd; text-align: center;">3</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd;">Criar projeções do desempenho comercial futuro de cada município de São Paulo</td>
            <td style="border: 1px solid #ddd;">Eu, como usuário, gostaria de visualizar projeções do desempenho comercial futuro de cada município, para entender melhor o comércio do estado de São Paulo</td>
            <td style="border: 1px solid #ddd; text-align: center;">Alta</td>
            <td style="border: 1px solid #ddd; text-align: center;">8</td>
            <td style="border: 1px solid #ddd; text-align: center;">3</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd;">Correção da inflação</td>
            <td style="border: 1px solid #ddd;">Eu, como usuário, gostaria de visualizar a correção da inflação para análise de dados econômicos, para ter maior conhecimento sobre os ajustes para compensação da perda de valor da moeda</td>
            <td style="border: 1px solid #ddd; text-align: center;">Alta</td>
            <td style="border: 1px solid #ddd; text-align: center;">8</td>
            <td style="border: 1px solid #ddd; text-align: center;">3</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd;">Ferramenta de busca para filtrar cargas por código NCM e aplicar filtros</td>
            <td style="border: 1px solid #ddd;">Eu, como usuário, gostaria de ter acesso a uma ferramenta de pesquisa onde fosse possível filtrar cargas mediante seus códigos NCM e aplicar filtros, para ter uma obtenção de informações facilitada</td>
            <td style="border: 1px solid #ddd; text-align: center;">Alta</td>
            <td style="border: 1px solid #ddd; text-align: center;">13</td>
            <td style="border: 1px solid #ddd; text-align: center;">2</td>
        </tr>
    </tbody>
</table>


---

# Registro de Atividade das Sprints 

## Sprint 1
- [x] Criação de um protótipo do Figma

- [x] Desenvolvimento de um gráfico de exportação de cada município
      
- [x] Desenvimento de um gráfico com as 5 maiores exportações de cada município
      
- [x] Desenvolvimento de uma lista de exportações dos municípios
      
- [x] Criação de um Figma funcional e responsivo



## Sprint 2
- [ ] Filtrar cargas dos municípios de SP (2019-2024)

- [ ] Comparar desempenho comercial dos municípios

- [ ] Exibir variações sazonais de oferta e demanda

- [ ] Mapear principais fornecedores de SP



## Sprint 3
- [ ] Identificar produtos mais exportados por município

- [ ] Visualizar diversidade de produtos exportados

- [ ] Exibir balança comercial de SP

- [ ] Analisar riscos da dependência de mercados

- [ ] Projeções de desempenho comercial futuro

- [ ] Visualizar correção da inflação para análise econômica


---

# Protótipo do Figma
🔗[Clique aqui para visualizar o modelo do projeto](https://www.figma.com/design/hDo9erWlNFuP3vs8ZiT6Ic/API?m=auto&t=nKZ6A3GWMeeH2L9A-1)

https://github.com/user-attachments/assets/28ca1c90-a0d0-4bd8-8c1a-a757d02f225a

---

# Autores

<table style="width: 100%; border-collapse: collapse;">
    <thead>
        <tr>
            <th style="border: 1px solid #ddd;">Função</th>
            <th style="border: 1px solid #ddd;">Nome</th>
            <th style="border: 1px solid #ddd; text-align: center;">GitHub</th>
            <th style="border: 1px solid #ddd; text-align: center;">LinkedIn</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border: 1px solid #ddd;">Scrum Master (SM)</td>
            <td style="border: 1px solid #ddd;">Maria Fernanda de Oliveira Laboissiere</td>
            <td style="border: 1px solid #ddd; text-align: center;">
                <a href="https://github.com/mariaflbss" target="_blank">
                    <img src="https://img.shields.io/badge/GitHub-111217?style=flat-square&logo=github&logoColor=white" alt="GitHub Badge"/>
                </a>
                 <td style="border: 1px solid #ddd; text-align: center;">
                <a href="https://www.linkedin.com/in/maria-fernanda-de-oliveira-laboissiere-25362b353" target="_blank">
                    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn Badge"/>
                </a>
            </td>
        </tr> 
        <tr>
            <td style="border: 1px solid #ddd;">Product Owner (PO)</td>
            <td style="border: 1px solid #ddd;">Rafael Guimarães da Silva Oliveira</td>
            <td style="border: 1px solid #ddd; text-align: center;">
                <a href="https://github.com/PatoJosefo" target="_blank">
                    <img src="https://img.shields.io/badge/GitHub-111217?style=flat-square&logo=github&logoColor=white" alt="GitHub Badge"/>
                </a>
                 <td style="border: 1px solid #ddd; text-align: center;">
                <a href="https://br.linkedin.com/in/rafael-oliveira-3603a7355" target="_blank">
                    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn Badge"/>
                </a>
            </td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd;">Team Member</td>
            <td style="border: 1px solid #ddd;">Giovanni Martins de Melo Neves</td>
            <td style="border: 1px solid #ddd; text-align: center;">
                <a href="https://github.com/Giommn" target="_blank">
                    <img src="https://img.shields.io/badge/GitHub-111217?style=flat-square&logo=github&logoColor=white" alt="GitHub Badge"/>
                </a>
                 <td style="border: 1px solid #ddd; text-align: center;">
                <a href="https://www.linkedin.com/in/giovanni-martins-216995356" target="_blank">
                    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn Badge"/>
                </a>
            </td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd;">Team Member</td>
            <td style="border: 1px solid #ddd;">Heloisa Cardillo Lima</td>
            <td style="border: 1px solid #ddd; text-align: center;">
                <a href="https://github.com/heloisa-cardillo" target="_blank">
                    <img src="https://img.shields.io/badge/GitHub-111217?style=flat-square&logo=github&logoColor=white" alt="GitHub Badge"/>
                </a>
                 <td style="border: 1px solid #ddd; text-align: center;">
                <a href="https://www.linkedin.com/in/heloisa-cardillo-lima" target="_blank">
                    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn Badge"/>
                </a>
            </td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd;">Team Member</td>
            <td style="border: 1px solid #ddd;">João Eduardo Oliveira Santos</td>
            <td style="border: 1px solid #ddd; text-align: center;">
                <a href="https://github.com/joao-ed252" target="_blank">
                    <img src="https://img.shields.io/badge/GitHub-111217?style=flat-square&logo=github&logoColor=white" alt="GitHub Badge"/>
                </a>
                 <td style="border: 1px solid #ddd; text-align: center;">
                <a href="https://www.linkedin.com/in/jo%C3%A3o-eduardo-o-9110332a2" target="_blank">
                    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn Badge"/>
                </a>
            </td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd;">Team Member</td>
            <td style="border: 1px solid #ddd;">Talita de Lania Marques</td>
            <td style="border: 1px solid #ddd; text-align: center;">
                <a href="https://github.com/talitamarques30" target="_blank">
                    <img src="https://img.shields.io/badge/GitHub-111217?style=flat-square&logo=github&logoColor=white" alt="GitHub Badge"/>
                </a>
                 <td style="border: 1px solid #ddd; text-align: center;">
                <a href="https://br.linkedin.com/in/talitamarques30" target="_blank">
                    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn Badge"/>
                </a>
            </td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd;">Team Member</td>
            <td style="border: 1px solid #ddd;">Victor Chagas de Jesus</td>
            <td style="border: 1px solid #ddd; text-align: center;">
                <a href="https://github.com/victorchagas-93" target="_blank">
                    <img src="https://img.shields.io/badge/GitHub-111217?style=flat-square&logo=github&logoColor=white" alt="GitHub Badge"/>
                </a>
                 <td style="border: 1px solid #ddd; text-align: center;">
                <a href="https://www.linkedin.com/in/victorchagas93" target="_blank">
                    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn Badge"/>
                </a>
            </td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd;">Team Member</td>
            <td style="border: 1px solid #ddd;">Vinicius Silva Moreira</td>
            <td style="border: 1px solid #ddd; text-align: center;">
                <a href="https://github.com/vinismoreira" target="_blank">
                    <img src="https://img.shields.io/badge/GitHub-111217?style=flat-square&logo=github&logoColor=white" alt="GitHub Badge"/>
                </a>
                 <td style="border: 1px solid #ddd; text-align: center;">
                <a href="www.linkedin.com/in/vinicius-moreira-806105350" target="_blank">
                    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn Badge"/>
                </a>
            </td>
        </tr>
    </thead>
</table>

---
[Voltar ao topo](#nexus)
