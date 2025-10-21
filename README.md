# Casa_Python_JuliaZ
Este projeto é um sistema de cadastro e gerenciamento de comidas nordestinas, desenvolvido em Python com Tkinter para a interface gráfica e SQLite como banco de dados local.
O objetivo é permitir o controle completo de registros (criação, leitura, atualização e exclusão) de comidas e movimentações, além de autenticação de usuários e persistência dos dados. O projeto foi criado como exercício prático de integração entre interface gráfica, banco de dados e boas práticas de modularização de código em Python.

<br>

## ⚙️ Funcionalidades principais

* Login de usuários com validação no banco de dados;

* Cadastro de casas com campos como endereço, preço e status;

* Listagem completa de registros em tabela;

* Atualização e remoção de dados;
  
* Banco SQLite criado automaticamente a partir do arquivo db_init.sql;

* Organização modular do código em múltiplos arquivos (main.py, login.py, db.py, utils.py);

<br>

## 🧩 Estrutura de pastas

├── comidas.py            # Módulo relacionado ao controle ou cadastro de comidas (parte extra do sistema)
│
├── comidasdb.sqlite      # Banco de dados SQLite utilizado pelo sistema (gerado automaticamente)
│
├── db_init.sql           # Script SQL responsável por criar as tabelas iniciais do banco
│
├── db.py                 # Módulo de conexão e manipulação do banco de dados (criação, inserção, leitura, etc.)
│
├── estoque.py            # Script voltado ao controle de estoque (provavelmente vinculado a casas ou comidas)
│
├── login.py              # Tela e lógica de autenticação de usuários (verificação de login e senha)
│
├── main.py               # Arquivo principal que inicializa a aplicação e faz a integração entre os módulos
│
└── utils.py              # Funções auxiliares, como centralização de janelas e validações de interface

<br>

## 🚀 Passo a passo de criação do projeto
### 1. Criação da interface base (Tkinter)

* Criou-se a janela principal (App) com layout organizado e botões de navegação.

* Implementou-se a função centralizarjanela() em utils.py para centralizar janelas na tela.

<br>

### 2. Implementação do banco de dados (SQLite)

* Criado o arquivo db.py com a função ensuredb(), responsável por:

* Verificar se o banco existe (os.path.exists());

* Caso não exista, ler e executar o script db_init.sql;

* Inicializar as tabelas necessárias (por exemplo: usuarios, comidas).

<br>

### 3. Criação do script SQL (db_init.sql)

* Contém os comandos CREATE TABLE com a estrutura das tabelas principais. Exemplo:

```sql
-- Ativa a verificação de integridade referencial (chaves estrangeiras).
PRAGMA foreign_keys = ON;

-- Tabela de usuários
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- Identificador único gerado automaticamente
    usuario TEXT UNIQUE,                   -- Nome de usuário único (login)
    senha TEXT,                           -- Senha do usuário (em texto simples aqui)
    nome_completo TEXT                    -- Nome completo do usuário
);

-- Tabela de comidas nordestinas
CREATE TABLE IF NOT EXISTS comidas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,    -- Identificador único da comida
    codigo TEXT UNIQUE,                       -- Código único do prato/comida
    nome TEXT,                               -- Nome da comida
    descricao TEXT,                          -- Descrição detalhada
    categoria TEXT,                          -- Categoria (ex: prato principal, salgado)
    origem TEXT,                             -- Origem regional da comida
    ingredientes TEXT,                       -- Ingredientes usados
    porcao TEXT,                            -- Porção sugerida (ex: 300g)
    calorias REAL,                          -- Quantidade de calorias
    quantidade INTEGER DEFAULT 0,           -- Quantidade atual em estoque (padrão 0)
    estoque_minimo INTEGER DEFAULT 0        -- Quantidade mínima para alerta (padrão 0)
);

-- Tabela de movimentações (histórico de estoque)
CREATE TABLE IF NOT EXISTS movimentacoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Identificador único da movimentação
    comida_id INTEGER,                      -- ID da comida movimentada
    usuario_id INTEGER,                     -- ID do usuário que realizou movimentação
    tipo TEXT,                             -- Tipo de movimentação ("entrada" ou "saída")
    quantidade INTEGER,                    -- Quantidade movimentada
    data TEXT,                            -- Data da movimentação (formato texto)
    observacao TEXT,                      -- Observação adicional

    FOREIGN KEY(comida_id) REFERENCES comidas(id),
    FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
);

-- Inserção de usuários iniciais (sistema terá esses usuários cadastrados)
INSERT OR IGNORE INTO usuarios (id, usuario, senha, nome_completo) VALUES
(1, 'vendedor1', '123', 'Helena Silva'),
(2, 'vendedor2', '123', 'Cecilia Lima'),
(3, 'vendedor3', '123', 'Ravi Santos');

-- Inserção de comidas iniciais no sistema
INSERT OR IGNORE INTO comidas (id, codigo, nome, descricao, categoria, origem, ingredientes, porcao, calorias, quantidade, estoque_minimo) VALUES
(1, 'C001', 'Baião de Dois', 'Arroz com feijão verde, queijo coalho e carne seca.', 'Prato Principal', 'Ceará', 'Arroz, feijão, queijo coalho, carne seca', '300g', 480, 15, 3),
(2, 'C002', 'Carne de Sol com Macaxeira', 'Carne de sol acebolada servida com macaxeira frita ou cozida.', 'Prato Principal', 'Nordeste (Geral)', 'Carne de sol, macaxeira, manteiga de garrafa, cebola roxa', '450g', 700, 25, 8),
(3, 'C003', 'Vatapá', 'Creme de pão com camarão seco, leite de coco e azeite de dendê.', 'Acompanhamento', 'Bahia', 'Pão, camarão seco, leite de coco, azeite de dendê, amendoim', '250g', 450, 18, 6);

-- Inserção de movimentações iniciais no estoque
INSERT OR IGNORE INTO movimentacoes (id, comida_id, usuario_id, tipo, quantidade, data, observacao) VALUES
(1, 1, 1, 'entrada', 5, '2025-09-01', 'Reposição estoque mensal Baião de Dois'),
(2, 2, 2, 'saída', 2, '2025-09-05', 'Venda para evento do dia 10/10'),
(3, 3, 3, 'entrada', 10, '2025-09-10', 'Novo lote de camarão');

```

* Observação: ajuste as colunas conforme a necessidade do seu projeto antes de executar.

<br>

### 4. Tela de Login (login.py)

* Verifica login e senha diretamente no banco de dados.

* Exibe mensagens de erro quando o login é inválido.

* Redireciona para a tela principal após autenticação bem-sucedida.

<br>

### 5. CRUD das Comidas (main.py)

* Formulário com campos para adicionar/editar uma comida: origem, descrição, porção, categoria, etc.

* Botões para Salvar, Editar, Excluir e Listar registros.

* Uso do Treeview (Tkinter) para exibir os dados em forma de tabela.

<br>

### 6. Teste e correção de erros (exemplos)

* Corrigidos erros de API do OS:

  ``os.path.exist`` → ``os.path.exists``

* Ajustes em nomes de colunas:

``username`` → ``login``

``password`` → ``senha``

* Verificação da presença de db_init.sql para criação automática do banco.

<br> 


# 💻 Telas e Testes de Funcionalidades

## Login
<img width="1919" height="1006" alt="Captura de tela 2025-10-21 120744" src="https://github.com/user-attachments/assets/bb2bc5e6-42d5-49fb-be5d-82a32769945b" />


## Página principal
<img width="1919" height="1005" alt="Captura de tela 2025-10-21 120759" src="https://github.com/user-attachments/assets/06098fb7-2897-4709-95f7-cd032bc613de" />


## Gestão de estoque
<img width="1919" height="1016" alt="Captura de tela 2025-10-21 120857" src="https://github.com/user-attachments/assets/97ed5913-1ac0-42d1-b1ec-0c468217b1c1" />


## Adicionando nova movimentação
Para testar o CRUD, foi adicionada uma movimentação em um dos produtos.
<br>
<img width="597" height="490" alt="Captura de tela 2025-10-21 120939" src="https://github.com/user-attachments/assets/0d227a3d-43d7-48f0-b47f-81910cf0a2cf" />


## Movimentação adicionada com sucesso
<img width="1919" height="1011" alt="Captura de tela 2025-10-21 120951" src="https://github.com/user-attachments/assets/98e630e7-d085-494c-a671-91a7886c129a" />


## Ver histórico de movimentações
<img width="470" height="223" alt="Captura de tela 2025-10-21 121005" src="https://github.com/user-attachments/assets/0044066d-37a8-4648-a1b7-28cb745f5dc3" />


## Movimentações 
<img width="1919" height="1014" alt="Captura de tela 2025-10-21 121048" src="https://github.com/user-attachments/assets/ce487960-33d4-40bc-9f7d-260fe769606d" />


## Cadastro de comidas
<img width="1919" height="1005" alt="Captura de tela 2025-10-21 121119" src="https://github.com/user-attachments/assets/217fd3bf-3259-47eb-9b87-07122812a04d" />



## Modificação de comida existente
<img width="1916" height="1011" alt="Captura de tela 2025-10-21 121152" src="https://github.com/user-attachments/assets/8ef52e64-59ea-47d5-bc35-c7fd2c5cd56d" />


## Tabela de adicionar novo alimento
<img width="1919" height="1009" alt="Captura de tela 2025-10-21 121212" src="https://github.com/user-attachments/assets/a673dba7-705e-4c25-acce-aa4eba65666d" />


## Comida adicionada com sucesso
<img width="1919" height="1010" alt="Captura de tela 2025-10-21 140751" src="https://github.com/user-attachments/assets/10ccf0c7-827e-43c1-99d7-c604563f5711" />


## Comida excluida
<img width="1919" height="1010" alt="Captura de tela 2025-10-21 140925" src="https://github.com/user-attachments/assets/4281f924-d22f-4a40-9ea7-4ffca023518a" />



## Barra de pesquisa
<img width="1919" height="1003" alt="Captura de tela 2025-10-21 141049" src="https://github.com/user-attachments/assets/360282e6-06b0-4295-be26-0614694a10ee" />


## Botão de logout
<img width="1919" height="1008" alt="Captura de tela 2025-10-21 141338" src="https://github.com/user-attachments/assets/75eb375d-3d89-42cb-8e24-3260ba5d2562" />


## Volta para a página de login
<img width="1919" height="1009" alt="Captura de tela 2025-10-21 141350" src="https://github.com/user-attachments/assets/f5c6bc19-0bf6-4e04-a9bf-8a1dbdff772d" />
