
---

# 🚀 **Projeto Flask + MySQL com Docker**

Este projeto é uma aplicação web simples utilizando **Flask**, **MySQL** e **Docker** para gerenciar a infraestrutura de forma prática e escalável.

## 📌 **Tecnologias Utilizadas**

- **Python 3.7**
- **Flask** (Framework Web)
- **MySQL 5.7** (Banco de Dados)
- **Docker e Docker Compose** (Gerenciamento de containers)
- **Bootstrap 4** (para estilização das páginas HTML)

---

## 📂 **Estrutura do Projeto**

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

## 🛠️ **Configuração e Execução**

### 🔹 **Pré-requisitos**

Antes de rodar o projeto, você precisará garantir que tenha os seguintes programas instalados:

- **[Docker](https://www.docker.com/get-started)**
- **[Docker Compose](https://docs.docker.com/compose/)**

### 🔹 **Passos para Rodar o Projeto**

1️⃣ **Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

2️⃣ **Construa e inicie os containers com Docker Compose:**
```bash
docker-compose up --build
```

3️⃣ **Acesse a aplicação no navegador:**
   Abra seu navegador e acesse a aplicação em:

   ```
   http://localhost:5000
   ```

4️⃣ **Verifique se o banco de dados MySQL está rodando:**
   Conecte-se ao MySQL dentro do container com o seguinte comando:

   ```bash
   docker exec -it mysql_container mysql -uuser -psenha123 -D teste
   ```

---

## 🔗 **Endpoints da API**

### 📝 **Cadastro de Usuário**

- **Rota:** `POST /cadastro`

**Corpo da Requisição (JSON):**
```json
{
  "nome": "João Silva",
  "email": "joao@email.com",
  "senha": "123456"
}
```

### 📃 **Listar Usuários**

- **Rota:** `GET /listar`

**Resposta (JSON):**
```json
[
  {"id": 1, "nome": "João Silva", "email": "joao@email.com"},
  {"id": 2, "nome": "Maria Souza", "email": "maria@email.com"}
]
```

---

## 🛑 **Parando os Containers**

Para parar a execução dos containers, basta rodar o comando:

```bash
docker-compose down
```

---

## 📌 **Observações Importantes**

- O arquivo `cypress.env.example.json` está disponível para referência das variáveis de ambiente necessárias para testes automatizados.
- Certifique-se de que as senhas e variáveis de ambiente no Docker estejam configuradas corretamente antes de rodar o projeto.

---

## 📝 **Licença**

Este projeto é **open-source** e pode ser modificado conforme necessário. 🚀

---

## ⚙️ **Executar o Projeto com Ambiente Virtual (Sem Docker Compose)**

Caso prefira rodar o projeto sem utilizar Docker Compose, siga as instruções abaixo:

### **Passo 1**: Clonar o Projeto
Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### **Passo 2**: Instalar as Dependências

Antes de rodar o projeto, é altamente recomendado que você utilize um **ambiente virtual** para garantir que as dependências do projeto sejam isoladas. O uso do **`venv`** impede que bibliotecas de diferentes projetos se misturem e evita conflitos de versões.

#### **Instalar Dependências em um Ambiente Virtual (`venv`)** (Recomendado)

1. **Criar um ambiente virtual**:

   Se você ainda não tem um ambiente virtual no seu projeto, crie um utilizando o comando abaixo. Isso cria uma pasta chamada `venv` onde todas as dependências serão instaladas de forma isolada.

   ```bash
   python -m venv venv
   ```

2. **Ativar o ambiente virtual**:

   - **No Windows**, use o comando:
     ```bash
     venv\Scripts\activate
     ```
   
   - **No macOS ou Linux**, use o comando:
     ```bash
     source venv/bin/activate
     ```

   Ao ativar o ambiente virtual, você verá o nome do ambiente virtual entre parênteses no seu terminal (exemplo: `(venv)`), indicando que o ambiente virtual está ativo.

3. **Instalar as dependências do projeto**:

   Com o ambiente virtual ativado, instale as dependências listadas no arquivo `requirements.txt` executando o seguinte comando:

   ```bash
   pip install -r requirements.txt
   ```

#### **Instalar Dependências Globalmente** (Alternativa, não recomendada)

Se você preferir não usar o ambiente virtual, pode instalar as dependências diretamente no seu ambiente global. Para isso, basta rodar o comando:

```bash
pip install -r requirements.txt
```

No entanto, **não é recomendado** instalar as dependências globalmente, pois isso pode gerar conflitos com outras versões de pacotes de projetos diferentes.

#### **Resumo**:

- **Recomendação**: Crie e ative um **ambiente virtual** para manter as dependências do projeto isoladas e evitar conflitos.
- **Comando**: `pip install -r requirements.txt` instala as dependências do projeto, seja em um ambiente virtual ou no global.

### **Passo 3**: Subir o Container MySQL

Suba o container MySQL utilizando o comando:

```bash
docker run --name mysql_container -e MYSQL_ROOT_PASSWORD=senha123 -e MYSQL_DATABASE=teste -p 3306:3306 -d mysql:5.7
```

### **Passo 4**: Copiar o Arquivo SQL para o Container

Copie o arquivo `entrypoint.sql` para dentro do contêiner:

```bash
docker cp /caminho/para/entrypoint.sql mysql_container:/tmp/entrypoint.sql
```

### **Passo 5**: Acessar o Container MySQL

Acesse o container MySQL:

```bash
docker exec -it mysql_container /bin/bash
```

### **Passo 6**: Conectar-se ao MySQL

Dentro do contêiner, conecte-se ao MySQL:

```bash
mysql -u root -p
```

Digite a senha quando solicitado.

### **Passo 7**: Criar o Banco de Dados e a Tabela

Execute o comando abaixo para rodar o script SQL e criar o banco de dados e a tabela:

```sql
source /tmp/entrypoint.sql;
```

### **Passo 8**: Obter o IP do Contêiner

Para obter o endereço IP do contêiner, execute o seguinte comando no terminal:

```bash
docker network inspect bridge <id_container>
```

- **Substitua** `<id_container>` pelo **ID** ou **nome** do seu contêiner. 
- **Importante:** No arquivo `app.py`, localize a configuração `app.config['MYSQL_DATABASE_HOST']` e altere o valor para o IP retornado (se estiver rodando em um ambiente local). Se estiver utilizando **Docker Compose**, altere para `db`, que é o nome do serviço no arquivo `docker-compose.yml`.

### **Passo 9**: Rodar o Flask

Na raiz do projeto, inicie o servidor Flask:

```bash
flask run
```

Agora, você pode acessar a aplicação em `http://localhost:5000`.

---

