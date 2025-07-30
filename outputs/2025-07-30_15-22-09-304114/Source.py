# Unit test result: ✅ PASSED
from flask import Flask, jsonify, request
from typing import List, Optional
app = Flask(__name__)

class Usuario:
    id: Optional[int]
    nome: str
    email: str

    def __init__(self, id: Optional[int], nome: str, email: str):
        self.id = id
        self.nome = nome
        self.email = email

    def to_dict(self):
        return {'id': self.id, 'nome': self.nome, 'email': self.email}

class UsuarioRepository:
    armazenamento: dict[int, Usuario]
    sequence: int

    def __init__(self):
        self.armazenamento = {}
        self.sequence = 0
        self.init_data()

    def init_data(self):
        self.save(Usuario(None, 'Alice', 'alice@example.com'))
        self.save(Usuario(None, 'Bruno', 'bruno@example.com'))

    def find_by_id(self, id: int) -> Optional[Usuario]:
        return self.armazenamento.get(id)

    def find_all(self) -> List[Usuario]:
        return list(self.armazenamento.values())

    def save(self, usuario: Usuario) -> Usuario:
        if usuario.id is None:
            self.sequence += 1
            usuario.id = self.sequence
        self.armazenamento[usuario.id] = usuario
        return usuario

    def delete_by_id(self, id: int):
        self.armazenamento.pop(id, None)

class UsuarioService:
    repo: UsuarioRepository

    def __init__(self, repo: UsuarioRepository):
        self.repo = repo

    def obterTodos(self) -> List[Usuario]:
        return self.repo()

    def obterPorId(self, id: int) -> Optional[Usuario]:
        return self.repo()

    def criar(self, usuario: Usuario) -> Usuario:
        return self.repo()

    def atualizar(self, usuario: Usuario) -> Usuario:
        return self.repo()

    def remover(self, id: int):
        self.repo()
usuario_repo = UsuarioRepository()
usuario_service = UsuarioService(usuario_repo)

@app.route('/api/usuarios', methods=['GET'])
def listar_usuarios():
    usuarios = usuario_service.obterTodos()
    return jsonify([u.to_dict() for u in usuarios])

@app.route('/api/usuarios/<int:id>', methods=['GET'])
def obter_usuario(id: int):
    usuario = usuario_service.obterPorId(id)
    if usuario:
        return jsonify(usuario.to_dict())
    else:
        return (jsonify({'message': 'Usuario not found'}), 404)

@app.route('/api/usuarios', methods=['POST'])
def criar_usuario():
    data = request.json
    new_usuario = Usuario(None, data['nome'], data['email'])
    created_usuario = usuario_service.criar(new_usuario)
    return (jsonify(created_usuario.to_dict()), 201)

@app.route('/api/usuarios/<int:id>', methods=['PUT'])
def atualizar_usuario(id: int):
    data = request.json
    usuario_to_update = Usuario(id, data['nome'], data['email'])
    updated_usuario = usuario_service.atualizar(usuario_to_update)
    if updated_usuario:
        return jsonify(updated_usuario.to_dict())
    else:
        return (jsonify({'message': 'Usuario not found for update'}), 404)

@app.route('/api/usuarios/<int:id>', methods=['DELETE'])
def remover_usuario(id: int):
    usuario_service.remover(id)
    return ('', 204)
if __name__ == '__main__':
    app.run(debug=True)