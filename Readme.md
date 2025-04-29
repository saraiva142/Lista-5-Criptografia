# 🔐 Projeto S-DES (Simplified DES)

Este repositório contém uma implementação completa do algoritmo **S-DES (Simplified Data Encryption Standard)**, desenvolvido como atividade prática da disciplina de **Criptografia**.

A aplicação foi construída em **Python** com **Streamlit** para fornecer uma interface web interativa, permitindo cifrar e decifrar textos de 8 bits utilizando chaves de 10 bits.

---

## 📂 Estrutura do Projeto

- `main.py` — Interface do usuário feita em Streamlit (entrada de texto, chave e seleção de ação).
- `encrypt.py` — Código que realiza o processo de **cifragem** baseado no S-DES.
- `decrypt.py` — Código que realiza o processo de **decifragem** baseado no S-DES.

---

## 🚀 Como Executar o Projeto

1. Clone o repositório:

```bash
git clone https://github.com/saraiva142/Lista-5-Criptografia.git
```

2. Acesse a pasta do projeto:

```bash
cd S-Des
```

3. Instale as dependências necessárias:

```bash
pip install streamlit
```

4. Rode o aplicativo:

```bash
streamlit run main.py
```

---

## 🛠️ Funcionalidades Implementadas

- Geração manual das subchaves **K1** e **K2**.
- Permutações e rotações de bits sem uso de funções prontas de alto nível.
- Aplicação das operações:
  - Permutação inicial (**IP**)
  - Expansão/permutação (**E/P**)
  - Funções **S-boxes (S0, S1)** para substituição de bits
  - Permutação final (**P4**)
  - Permutação inversa (**IP⁻¹**)
- Implementação completa da estrutura de **Feistel** do S-DES.
- Interface gráfica com Streamlit para entrada de dados e visualização de resultados.

---

## 🎯 Objetivos de Aprendizado

- Entendimento prático da estrutura de cifradores de bloco.
- Implementação manual dos conceitos de permutação, substituição e expansão de bits.
- Organização de projeto Python modularizado.
- Desenvolvimento de aplicações web simples com Streamlit.

---

## 📸 Exemplo de Uso

1. Insira o texto plano (8 bits) e a chave (10 bits) na interface.
2. Escolha entre as opções "Cifrar" ou "Decifrar".
3. Visualize o resultado diretamente na página.

---

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais como parte da disciplina de **Criptografia**.

---

## 👨‍💻 Desenvolvido por

- João Saraiva

---

