from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

meu_livro = {}

class Livro(BaseModel):
    nome_livro: str
    autor_livro: str
    ano_livro: int

@app.get("/livros/")
def get_livros():
    if not meu_livro:
        return {"mensagem": "Não existe nenhum livro!"}
    return {"livros": meu_livro} 

@app.post("/adiciona/")
def post_livros(id_livro: int, livro: Livro):
    if id_livro in meu_livro:
        raise HTTPException(status_code=400, detail="Esse livro já existe")
    meu_livro[id_livro] = livro.dict()
    return {"mensagem": "O livro foi criado com sucesso!"}

@app.put("/atualiza/{id_livro}")
def put_livros(id_livro: int, livro: Livro):
    if id_livro not in meu_livro:
        raise HTTPException(status_code=404, detail="Esse livro não foi encontrado!")
    meu_livro[id_livro] = livro.dict()
    return {"mensagem": "As informações do livro foram atualizadas com sucesso!"}

@app.delete("/deletar/{id_livro}")
def delete_livro(id_livro: int):
    if id_livro not in meu_livro:
        raise HTTPException(status_code=404, detail="Esse livro não foi encontrado!")
    del meu_livro[id_livro]
    return {"mensagem": "O livro foi deletado com sucesso!"}


