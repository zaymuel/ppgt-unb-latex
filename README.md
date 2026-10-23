# Modelo LaTeX para Dissertações e Teses do PPGT/UnB

Modelo $\LaTeX$ oficial e atualizado para elaboração de dissertações de mestrado e teses de doutorado do [Programa de Pós-Graduação em Transportes (PPGT)](http://www.ppgt.unb.br) do Departamento de Engenharia Civil e Ambiental da [Faculdade de Tecnologia (FT)](http://ft.unb.br) da [Universidade de Brasília (UnB)](http://unb.br).

---

## 1. Introdução

Este modelo foi adaptado e customizado a partir do template da FT/UnB para atender estritamente às especificações normativas vigentes do PPGT (versão agosto/2026), incluindo:

- **Cabeçalhos de Capítulos centralizados**: Em maiúsculas e negrito (`1 INTRODUÇÃO`).
- **Hierarquia tipográfica**: 14pt para capítulos e 12pt para seções/subseções.
- **Espaçamento e Parágrafos**: Espaçamento entre linhas de 1,5, sem recuo na primeira linha e com 18pt de espaçamento entre parágrafos.
- **Lista de Quadros**: Suporte nativo ao elemento `Quadro` (distinto de Tabelas) com geração de `LISTA DE QUADROS` pré-textual.
- **Elementos Pré-textuais completos**: Declaração de uso de ferramentas de Inteligência Artificial Generativa (IAG), Folha de Aprovação no padrão PPGT, Ficha Catalográfica BCE e Termo de Cessão de Direitos.
- **Bibliografia e Citações**: Gerenciamento moderno via **BibLaTeX + Biber** com estilo Autor-Data compatível com as diretrizes do PPGT (unificação por `&`, *et al.* em itálico, `v. X (Y)` e paginação `p.`).

> [!IMPORTANT]
> Este template é a base recomendada para todas as dissertações e teses desenvolvidas no âmbito do PPGT/UnB.

---

## 2. Editores Recomendados

Você pode utilizar qualquer editor compatível com codificação UTF-8:

1. **Overleaf**: Plataforma em nuvem colaborativa. Muito boa mas sujeita a limites de uso (incentiva o uso de versões pagas). Muito útil se você não quiser a dor de cabeça de instalar e configurar o LaTeX localmente ([overleaf.com](https://www.overleaf.com/)).  

   **Como carregar o arquivo .zip no Overleaf:**
   - Baixe o arquivo `.zip` com os arquivos do projeto.
   - No painel inicial (*Dashboard*) do Overleaf, clique em **New Project** $\rightarrow$ **Upload Project**.
   - Arraste e solte o arquivo `.zip` para carregar o projeto.
   - No menu lateral superior esquerdo (**Menu**), certifique-se de que o **Compiler** está definido como `pdfLaTeX`, **TeX Live version** como `2026` (ou mais recente) e **Main document** como `principal.tex`.
   - Clique em **Recompile** (ou pressione `Ctrl + Enter`).
   - *Nota sobre arquivos extras:* Você pode excluir o arquivo `Makefile` no Overleaf se desejar, mas **mantenha o `.latexmkrc`**, pois o Overleaf precisa dele para compilar a Lista de Símbolos e Siglas automaticamente.
2. **Visual Studio Code (Recomendado)**: Com a extensão oficial **LaTeX Workshop**. Para usuários mais experientes, que toleram a configuração manual de compilação e preferem um ambiente leve e moderno ([code.visualstudio.com](https://code.visualstudio.com/)).  
   - **Dica**: Instale a extensão **LaTeX Workshop** e configure o `latexmk` como compilador padrão. Certifique-se de que o cursor do mouse esteja clicado dentro do arquivo `.tex` base (nesse caso, o `principal.tex`) do atual projeto antes de compilar.
3. **TeXstudio**: Editor dedicado com visualizador de PDF integrado ([texstudio.org](http://www.texstudio.org)).

---

## 3. Instalação Local

> [!NOTE]
> Caso você esteja usando o Overleaf, ignore esta seção. O Overleaf compila automaticamente o projeto com base no arquivo `principal.tex`.

### Distribuição LaTeX

Para compilar o documento em seu computador, é necessário ter uma distribuição $\LaTeX$ instalada:

#### Windows

- Baixe e instale o [MiKTeX](http://miktex.org).
- Recomenda-se a instalação do [Strawberry Perl](https://strawberryperl.com/) para viabilizar a compilação automática contínua via `latexmk`.

#### Linux

- Instale a distribuição completa via terminal:
  - **Debian / Ubuntu / Mint**: `sudo apt-get install texlive-full`
  - **Fedora / RHEL**: `sudo dnf install texlive-scheme-full`
  - **Arch Linux**: `sudo pacman -S texlive-meta`

#### macOS

- Baixe e instale o [MacTeX](https://tug.org/mactex/).

### Compiladores e Ferramentas Adicionais

#### Opção A: Pelo Editor (VS Code / TeXstudio)

Basta abrir o arquivo `principal.tex` e utilizar o comando padrão de compilação do seu editor. O arquivo `.latexmkrc` presente na raiz cuidará da compilação de índices e siglas automaticamente.

#### Opção B: Pelo Terminal / Linha de Comando (com `latexmk`)

```bash
latexmk -pdf principal.tex
```

#### Opção C: Via `Makefile` (Linux / macOS)

```bash
make        # Compila principal.tex e gera principal.pdf
make clean  # Limpa arquivos temporários e auxiliares
```

#### Opção D: Compilação Manual Sequencial (100% sem Perl no Windows)

Caso o seu computador não possua o Perl instalado para rodar o `latexmk`, execute os comandos nativos sequenciais no PowerShell ou Prompt de Comando:

```powershell
pdflatex -interaction=nonstopmode principal.tex
biber principal
makeindex principal.nlo -s nomencl.ist -o principal.nls
pdflatex -interaction=nonstopmode principal.tex
pdflatex -interaction=nonstopmode principal.tex
```

---

## 5. Conversão Direta de PDF para Word (.docx)

Caso seu orientador solicite o documento em formato editável do Microsoft Word:

1. Abra o **Microsoft Word** na tela inicial vazia (**com nenhum documento aberto**).
2. **Arraste o arquivo `principal.pdf` gerado diretamente para o centro da janela do Word**.
3. O Word executará a reconstrução automática de layout, convertendo títulos, parágrafos, tabelas e equações em um arquivo `.docx` perfeitamente editável.

---

## 6. Estrutura do Projeto

O repositório está organizado de forma modular para manter a raiz limpa:

```text
├── principal.tex                  # Arquivo principal (boilerplate limpo da sua dissertação)
├── manual-usuario.tex             # Manual completo do usuário e guia de transição Word -> LaTeX
├── Makefile                       # Automação de compilação e limpeza via terminal
├── .latexmkrc                     # Configuração multiplataforma do latexmk (makeindex/nomencl)
├── formatacao/                    # Estilos, tipografia e diretrizes visuais
│   ├── ppgt-unb-format.sty        # Pacote mestre de formatação oficial do PPGT
│   ├── hifenizacao.tex            # Regras manuais de separação silábica e termos técnicos
│   └── logotipos/                 # Logomarcas oficiais da UnB em PDF vetorial
├── capitulos/                     # Capítulos reais da sua dissertação/tese
│   ├── capitulo1-introducao.tex
│   ├── capitulo2-revisao.tex
│   ├── capitulo3-materiais-metodos.tex
│   ├── capitulo4-resultados-analise.tex
│   ├── capitulo5-conclusao.tex
│   ├── zz-apendices.tex           # Apêndices (produzidos pelo próprio autor)
│   └── zz-anexos.tex              # Anexos (documentos externos / autorizações)
├── capitulos-pretextuais/         # Elementos pré-textuais da dissertação
│   ├── 00-declaracao_iag.tex      # Declaração obrigatória de uso de ferramentas de IAG
│   ├── 00-dedicatoria.tex         # Dedicatória (opcional)
│   ├── 00-agradecimentos.tex      # Agradecimentos (opcional)
│   ├── 00-resumo.tex              # Resumo em língua portuguesa e palavras-chave
│   ├── 00-abstract.tex            # Abstract em língua inglesa e keywords
│   └── 00-resumoestendido.tex     # Resumo estendido em português (obrigatório se o texto for em inglês)
├── bibliografia/
│   └── referencias.bib            # Banco de dados de referências no formato BibLaTeX
└── imagens/                       # Diretório reservado para imagens, figuras e gráficos
```

---

## 7. Configuração Inicial dos Metadados

No preâmbulo de `principal.tex`, preencha as variáveis institucionais:

- **Idioma do Trabalho (Português vs. Inglês)**:  
  Por padrão, o template está em português (`\selectlanguage{brazilian}`). Caso vá redigir sua pesquisa em inglês:
  1. Comente `\selectlanguage{brazilian}` e descomente `\selectlanguage{english}` no preâmbulo de `principal.tex` (o template traduzirá títulos de capítulos, tabelas, figuras e sumário automaticamente);
  2. Descomente `\include{capitulos-pretextuais/00-resumoestendido}` na seção pré-textual (linha 170), que é uma seção obrigatória pela Resolução CEPE/UnB para dissertações em inglês.
- **Título do Trabalho**: `\title{Seu Título Aqui}`.  
  *Aviso crítico:* O título **não deve ultrapassar 5 linhas** para não comprometer a caixa geométrica da capa.
- **Autor e Partículas**:

  ```latex
  \ultimosobrenomeautor{Sobrenome}
  \prenomesautor{Nome e Outros Sobrenomes}
  ```

- **Código Cutter da BCE**: Acesse [https://ficha.bce.unb.br/ficha/](https://ficha.bce.unb.br/ficha/), gere sua ficha na BCE e preencha o código fornecido (ex.: `\codigocutter{M379d}`).
- **Data da Defesa**: Preencha estritamente no formato `\date{AAAA-MM-DD}` (ex: `\date{2026-10-23}`). O template extrai o dia, mês por extenso e ano automaticamente.
- **Orientador e Coorientador**:
  - `\orientadorficha{Nome}` e `\orientadorfichainverso{Sobrenome, Nome}`
  - O bloco de coorientador é opcional e vem comentado por padrão; descomente apenas se houver coorientador.

---

## 8. Citações e Referências

O template adota o sistema **Autor-Data** configurado em conformidade com as exigências do PPGT:

- **Citação Narrativa / Integrada ao texto**: `\citet{chave}`  
  *Exemplo:* `Segundo \citet{davis2004}...` $\rightarrow$ *Segundo Davis (2004)...*
- **Citação Parentética (fim de frase)**: `\citep{chave}`  
  *Exemplo:* `...conforme a literatura \citep{davis2004}.` $\rightarrow$ *...conforme a literatura (DAVIS, 2004).*
- **Base Limpa**: Todas as referências em `bibliografia/referencias.bib` são exemplos didáticos. Você pode apagar seu conteúdo e colar suas próprias referências exportadas do Zotero, Mendeley ou Google Acadêmico.

Para mais informações, consulte o guia completo no arquivo `manual-usuario.tex` ou o arquivo `bibliografia/referencias.bib`.

---

## 9. Autoria e Licença

- **Autor original da base FT-UnB**: [Prof. D.Sc. Geovany Araújo Borges (UnB)](https://lara.unb.br/~gaborges/).
- **Colaboradores históricos**: Nathalie Pinheiro, André Calmon, Renan Utida, [Manoel Campos da Silva Filho](https://github.com/manoelcampos), Gabriel Amaro Baxto.
- **Adequação às Normas PPGT, Motor Biber e Modelo Dual (2026)**: [Samuel Seixas Martin](https://github.com/zaymuel).
- **Licença**: [Creative Commons Attribution-NonCommercial 4.0 (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/).
