import os
import sqlalchemy as sqla
from sqlalchemy import create_engine, text

# Verificando se o banco de dados existe e removendo
if os.path.exists("escola.db"):
    os.remove("escola.db")
    print("Banco de dados 'escola.db' removido.")

# Cria a engine de conexão com o banco de dados SQLite
engine = sqla.create_engine('sqlite:///escola.db')

# Usando o contexto `with` para gerenciar a transação
with engine.connect() as connection:
    with connection.begin():
        # Criar a tabela aluno
        connection.execute(text("""
            CREATE TABLE IF NOT EXISTS aluno (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL
            )
        """))

        # Criar a tabela disciplina com a chave estrangeira
        connection.execute(text("""
            CREATE TABLE IF NOT EXISTS disciplina (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_disciplina TEXT NOT NULL,
                nota REAL NOT NULL,
                aluno_id INTEGER,
                FOREIGN KEY (aluno_id) REFERENCES aluno(id)
            )
        """))

        # Inserir alunos
        connection.execute(text("""
            INSERT INTO aluno (nome, email) VALUES
            ('Paulo Torres', 'paulo@example.com'),
            ('Ana Silva', 'ana@example.com'),
            ('Carlos Oliveira', 'carlos@example.com')
        """))

        # Inserir disciplinas e notas
        connection.execute(text("""
            INSERT INTO disciplina (nome_disciplina, nota, aluno_id) VALUES
            ('Python para Dados', 85, 1),  -- Paulo Torres
            ('Estatística', 90, 1),         -- Paulo Torres
            ('Análise de Dados', 78, 2),    -- Ana Silva
            ('Machine Learning', 88, 3)      -- Carlos Oliveira
        """))

        # Atualizar a nota da disciplina "Python para Dados" do aluno "Paulo Torres"
        connection.execute(text("""
            UPDATE disciplina
            SET nota = (SELECT MAX(nota) FROM disciplina)
            WHERE nome_disciplina = 'Python para Dados' AND aluno_id = 1
        """))

print("Alunos e disciplinas inseridos e nota atualizada com sucesso!")
