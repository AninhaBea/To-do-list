# To-do-list Kodland

Um sistema simples de gerenciamento de tarefas no qual os professores/administradores conseguem gerenciar seus alunos e suas respectivas tarefas

## Instalação

### Pré-requisitos
- Python 3.8+
- pip

### Passos

1. **Clonar ou baixar o repositório**
2. **Criar um ambiente virtual**
3. **Ativar o ambiente virtual**
    - `.\venv\Scripts\activate`
4. **Instalar as dependências**
    - `pip install -r requirements.txt`
5. **Executar a aplicação**
    - `flask run`
6. **Acessar pelo navegador**

## Usuários Padrão

| Tipo | Usuário | Senha |
|------|---------|-------|
| Admin | Kodland | python |
| Admin | admin | admin |
| Aluno | aluno1 | 123 |
| Aluno | aluno2 | 321 |

## Funcionalidades

### Admin
- Pode adicionar novos usuários (administradores ou alunos)
- Pode ver todos os usuários
- Pode criar novas tarefas e atribui-las para alunos específicos
- Pode ver todas as tarefas

### Aluno
- Pode gerenciar suas tarefas, marcando como concluída ou pendente
- Pode ver todas as tarefas designadas a ele mesmo

## Notas

- Os dados são armazenados em arquivos JSON
- Modo debug ativado para desenvolvimento
