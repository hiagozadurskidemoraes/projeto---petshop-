# 🐾 PetCare - Sistema de Gestão para Petshop

Sistema completo de gerenciamento para petshops, desenvolvido em Python com Flask, SQLite e front-end responsivo.

## 📋 Sobre o Projeto

O PetCare é uma aplicação web full-stack que permite o gerenciamento completo de um petshop, incluindo cadastro de clientes, animais, produtos, serviços e atendimentos, além de um site institucional público para apresentação do negócio.

## ✨ Funcionalidades

### Site Público
- Página institucional com banner, serviços, depoimentos e localização
- Catálogo de produtos e serviços com imagens dinâmicas por categoria
- Design responsivo e moderno

### Painel Administrativo
- Sistema de autenticação com cadastro e login (senhas criptografadas)
- CRUD completo de clientes e seus animais
- CRUD completo de produtos e serviços
- Registro de atendimentos com vínculo entre cliente, animal e serviço/produto
- Relatório de faturamento total
- Busca de clientes em tempo real

## 🛠️ Tecnologias Utilizadas

- **Python 3.14**
- **Flask** — framework web
- **SQLite** — banco de dados
- **Werkzeug** — hash de senhas
- **HTML5 / CSS3** — front-end
- **JavaScript** — interatividade (animações, contadores, busca)
- **Font Awesome** — ícones

## 📂 Estrutura do Projeto
projeto-petshop/

├── app.py                 # Aplicação Flask principal

├── banco.py                # Conexão e inicialização do banco de dados

├── clientes.py              # Lógica de clientes (terminal)

├── produtos.py              # Lógica de produtos (terminal)

├── atendimentos.py          # Lógica de atendimentos (terminal)

├── petshop.py               # Menu principal (versão terminal)

├── templates/                # Páginas HTML (Jinja2)

└── static/

└── style.css            # Estilos do site
## 🚀 Como Executar

1. Clone o repositório
```bash
git clone https://github.com/hiagozadurskidemoraes/projeto---petshop-.git
```

2. Instale as dependências
```bash
pip install flask
```

3. Execute a aplicação
```bash
python app.py
```

4. Acesse no navegador

## 👤 Autor

Desenvolvido por Hiago Zadurski de Moraes e João Paulo como projeto acadêmico de Raciocínio Algorítmico (PUCPR).

## 📄 Licença

Este projeto é livre para uso educacional e comercial.