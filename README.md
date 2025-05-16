# Sistema de Biblioteca

Sistema de gerenciamento de biblioteca desenvolvido em Flask, com funcionalidades completas de CRUD para livros, autores, categorias, clientes e empréstimos.

## 🚀 Funcionalidades

### Livros
- Cadastro completo de livros
- Associação com autores e categorias
- Controle de quantidade disponível
- Status de disponibilidade

### Autores
- Cadastro de autores
- Listagem de livros por autor
- Edição e exclusão de autores

### Categorias
- Cadastro de categorias
- Organização de livros por categoria
- Edição e exclusão de categorias

### Clientes
- Cadastro de clientes com dados completos
- Histórico de empréstimos
- Controle de empréstimos ativos

### Empréstimos
- Registro de empréstimos
- Data prevista de devolução
- Status de atraso
- Devolução de livros
- Histórico completo

## 🛠️ Tecnologias Utilizadas

- **Backend**: Flask 2.3.3
- **Database**: SQLAlchemy 2.0.23
- **ORM**: Flask-SQLAlchemy 3.1.1
- **Migrations**: Flask-Migrate 4.0.5
- **Serialização**: Marshmallow 3.20.1
- **Validação**: Email-validator 2.1.0
- **Interface**: Bootstrap 5

## 📋 Pré-requisitos

- Python 3.8+
- pip (gerenciador de pacotes Python)
- Ambiente virtual (recomendado)

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITÓRIO]
cd projeto_biblioteca
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
```bash
# Crie um arquivo .env na raiz do projeto
FLASK_APP=app
FLASK_ENV=development
DATABASE_URL=sqlite:///database.db
```

5. Execute as migrações:
```bash
flask db upgrade
```

6. Popule o banco de dados com dados iniciais:
```bash
python scripts/populate_db.py
```

7. Inicie o servidor:
```bash
flask run
```

## 📦 Estrutura do Projeto

```
projeto_biblioteca/
├── app/
│   ├── controllers/     # Controladores da aplicação
│   ├── models/         # Modelos e schemas
│   ├── repositories/   # Camada de acesso a dados
│   ├── services/       # Lógica de negócios
│   ├── templates/      # Templates HTML
│   └── utils/          # Utilitários e exceções
├── migrations/         # Migrações do banco de dados
├── scripts/           # Scripts auxiliares
├── .env               # Variáveis de ambiente
├── config.py          # Configurações da aplicação
└── requirements.txt   # Dependências do projeto
```

## 🔐 Segurança

- Validação de dados em todas as operações
- Proteção contra SQL Injection
- Validação de emails
- Controle de acesso
- Sanitização de inputs

## 📝 Regras de Negócio

### Empréstimos
- Não é possível emprestar livros sem estoque
- Data prevista de devolução não pode ser no passado
- Cliente não pode ter mais de 3 empréstimos ativos
- Livros devolvidos com atraso são marcados automaticamente

### Livros
- Quantidade não pode ser negativa
- Livro não pode ser excluído se tiver empréstimos ativos
- Autor e categoria são obrigatórios

### Clientes
- Email deve ser único
- Telefone é obrigatório
- Não pode ser excluído com empréstimos ativos

## 🤝 Contribuindo

1. Faça um Fork do projeto
2. Crie uma Branch para sua Feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## ✨ Melhorias Futuras

- [ ] Implementar sistema de multas
- [ ] Adicionar relatórios e estatísticas
- [ ] Implementar busca avançada
- [ ] Adicionar sistema de reservas
- [ ] Implementar notificações de devolução
- [ ] Adicionar autenticação de usuários
- [ ] Implementar API REST
- [ ] Adicionar testes automatizados

## 💡 Dicas para rodar em outro ambiente

- Certifique-se de criar o arquivo `.env` na raiz do projeto, conforme instruções acima. Não versionar esse arquivo.
- O diretório `venv/` (ambiente virtual) não deve ser versionado. Crie um novo ambiente virtual na nova máquina.
- Sempre execute as migrações (`flask db upgrade`) e popule o banco de dados (`python scripts/populate_db.py`) ao rodar o projeto em uma nova máquina.
- Se encontrar erros de indentação ou de dependências, revise os arquivos conforme necessário e reinstale as dependências com `pip install -r requirements.txt`.
- O arquivo do banco de dados (`instance/database.db`) é gerado automaticamente, não precisa ser copiado entre máquinas.