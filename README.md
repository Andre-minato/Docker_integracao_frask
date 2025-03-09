# 🚀 Projeto Flask + MySQL com Docker

Este projeto é uma aplicação web simples utilizando Flask, MySQL e Docker para gerenciar a infraestrutura.

## 📌 Tecnologias Utilizadas
- **Python 3.7**
- **Flask** (Framework Web)
- **MySQL 5.7** (Banco de Dados)
- **Docker e Docker Compose**
- **Bootstrap 4** (para estilização das páginas HTML)

---

## 📂 Estrutura do Projeto
```
📁 projeto/
 ├── 📂 scripts/               # Scripts SQL de inicialização
 │   ├── entrypoint.sql        # Criação do banco e tabelas
 ├── 📂 templates/             # Arquivos HTML (Frontend)
 │   ├── index.html            # Página inicial
 │   ├── cadastro.html         # Formulário de cadastro
 │   ├── lista.html            # Lista de usuários
 ├── Dockerfile                # Configuração do container Flask
 ├── docker-compose.yml        # Orquestração dos containers
 ├── app.py                    # Código principal em Flask
 ├── requirements.txt          # Dependências do projeto
 ├── README.md                 # Documentação do projeto
```

---

## 🛠️ Configuração e Execução

### 🔹 **Pré-requisitos**
Certifique-se de ter instalado:
- **[Docker](https://www.docker.com/get-started)**
- **[Docker Compose](https://docs.docker.com/compose/)**

### 🔹 **Passos para rodar o projeto**
1️⃣ Clone o repositório:
```sh
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

2️⃣ Construa e inicie os containers:
```sh
docker-compose up --build
```

3️⃣ Acesse a aplicação no navegador:
```
http://localhost:5000
```

4️⃣ Para verificar se o banco está rodando, conecte-se ao MySQL:
```sh
docker exec -it mysql_container mysql -uuser -psenha123 -D teste
```

---

## 🔗 Endpoints da API

### 📝 **Cadastro de Usuário**
**Rota:** `POST /cadastro`

```json
{
  "nome": "João Silva",
  "email": "joao@email.com",
  "senha": "123456"
}
```

### 📃 **Listar Usuários**
**Rota:** `GET /listar`

**Resposta:**
```json
[
  {"id": 1, "nome": "João Silva", "email": "joao@email.com"},
  {"id": 2, "nome": "Maria Souza", "email": "maria@email.com"}
]
```

---

## 🛑 Parando os Containers

Para parar a execução dos containers, use:
```sh
docker-compose down
```

---

## 📌 Observação
- Um arquivo `cypress.env.example.json` está disponível para referência das variáveis de ambiente necessárias.

---

## 📝 Licença
Este projeto é open-source e pode ser modificado conforme necessário. 🚀

