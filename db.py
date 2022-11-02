import sqlite3


def connect_to_db():
    conn = sqlite3.connect('agenda.db')
    return conn


def criar_tabela_contatos():
    try:
        conn = connect_to_db()
        conn.execute('''
        CREATE TABLE contatos(
            id INTEGER PRIMARY KEY NOT NULL,
            nome TEXT NOT NULL,
            empresa TEXT NOT NULL,
            telefone TEXT NOT NULL,
            email TEXT NOT NULL
            );
        ''')
        conn.commit()
        print('Tabela criada com sucesso!')
    except:
        print('Erro na criação da tabela')
    finally:
        conn.close()


def criar_contato(contato):
    contato_criado = {}
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO contatos (nome, empresa, telefone, email) VALUES (?, ?, ?, ?)", (contato['nome'],
                                                                                                     contato['empresa'],
                                                                                                     contato[
                                                                                                         'telefone'],
                                                                                                     contato['email']))
        conn.commit()
        contato_criado = get_contato_by_id(cursor.lastrowid)
    except:
        conn.rollback()
    finally:
        conn.close()
    return contato


def get_contatos():
    contatos = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM contatos")
        rows = cursor.fetchall()

        for i in rows:
            contato = {"id": i["id"], "nome": i["nome"], "empresa": i["empresa"], "telefone": i["telefone"],
                       "email": i["email"]}
            contatos.append(contato)

    except:
        contatos = []

    return contatos


def get_contato_by_id(id):
    contato = {}
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM contatos WEHRE id = ?", (id))
        row = cursor.fetchone()

        contato["id"] = row["id"]
        contato["nome"] = row["nome"]
        contato["empresa"] = row["empresa"]
        contato["telefone"] = row["telefone"]
        contato["email"] = row["email"]
    except:
        contato = {}

    return contato


def get_contato_by_filter(filter):
    contatos = []
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM contatos WHERE nome = ? OR empresa = ? OR email = ?", (filter))
        rows = cursor.fetchall()

        for i in rows:
            contato = {}
            contato["id"] = i["id"]
            contato["nome"] = i["nome"]
            contato["empresa"] = i["empresa"]
            contato["telefone"] = i["telefone"]
            contato["email"] = i["email"]
            contatos.append(contato)
    except:
        contatos = []

    return contatos


def update_contato(contato):
    contato_atualizado = {}
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE contatos SET name = ?, empresa = ?, telefone = ?, email = ? WHERE id = ?",
                       (contato["nome"], contato["empresa"], contato["telefone"], contato["email"], contato["id"],))
        conn.commit()

        # Retornar o usuário atualizado
        contato_atualizado = get_contato_by_id(contato["id"])
    except:
        conn.rollback()
        contato_atualizado = {}
    finally:
        conn.close()

    return contato_atualizado


def delete_contato(id):
    retorno = {}
    try:
        conn = connect_to_db()
        conn.execute("DELETE FROM contatos WHERE id = ?", (id,))
        conn.commit()
        retorno["status"] = "Contato excluído!"
    except:
        conn.rollback()
        retorno["status"] = "Não foi possível excluir este contato!"
    finally:
        conn.close()

    return retorno
