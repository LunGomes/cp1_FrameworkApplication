from fastapi import FastAPI, Form, Query
from fastapi.responses import HTMLResponse
from typing import Optional

app = FastAPI()

# base simulada
filmes = [
    {"id": 1, "titulo": "Toy Story", "genero": "Comédia", "ano": 1995,
        "img": "https://image.tmdb.org/t/p/w500/uXDfjJbdP4ijW5hWSBrPrlKpxab.jpg"},
    {"id": 2, "titulo": "Frozen", "genero": "Musical", "ano": 2013,
        "img": "https://image.tmdb.org/t/p/w500/kgwjIb2JDHRhNk13lmSxiClFjVk.jpg"},
    {"id": 3, "titulo": "O Rei Leão", "genero": "Drama", "ano": 1994,
        "img": "https://image.tmdb.org/t/p/w500/sKCr78MXSLixwmZ8DyJLrpMsd15.jpg"},
    {"id": 4, "titulo": "Procurando Nemo", "genero": "Aventura", "ano": 2003,
        "img": "https://image.tmdb.org/t/p/w500/eHuGQ10FUzK1mdOY69wF5pGgEf5.jpg"},
    {"id": 5, "titulo": "Shrek", "genero": "Comédia", "ano": 2001,
        "img": "https://image.tmdb.org/t/p/w500/iB64vpL3dIObOtMZgX3RqdVdQDc.jpg"},
    {"id": 6, "titulo": "Divertida Mente", "genero": "Drama", "ano": 2015,
        "img": "https://image.tmdb.org/t/p/w500/2H1TmgdfNtsKlU9jKdeNyYL5y8T.jpg"},
    {"id": 7, "titulo": "Moana", "genero": "Aventura", "ano": 2016,
        "img": "https://www.papodecinema.com.br/wp-content/uploads/2016/12/20200306-poster.webp"},
    {"id": 8, "titulo": "Up - Altas Aventuras", "genero": "Aventura", "ano": 2009,
        "img": "https://upload.wikimedia.org/wikipedia/pt/a/a8/Up_p%C3%B4ster.jpg"},
    {"id": 9, "titulo": "Os Incríveis", "genero": "Ação", "ano": 2004,
        "img": "https://image.tmdb.org/t/p/w500/2LqaLgk4Z226KkgPJuiOQ58wvrm.jpg"},
    {"id": 10, "titulo": "Encanto", "genero": "Musical", "ano": 2021,
        "img": "https://image.tmdb.org/t/p/w500/4j0PNHkMr5ax3IA8tjtxcmPU3QT.jpg"},
    {"id": 11, "titulo": "Viva", "genero": "Musical", "ano": 2017,
        "img": "https://image.tmdb.org/t/p/w500/gGEsBPAijhVUFoiNpgZXqRVWJt2.jpg"},
    {"id": 12, "titulo": "Madagascar", "genero": "Comédia", "ano": 2005,
        "img": "https://upload.wikimedia.org/wikipedia/pt/3/36/Madagascar_Theatrical_Poster.jpg"},
    {"id": 13, "titulo": "Kung Fu Panda", "genero": "Ação", "ano": 2008,
        "img": "https://image.tmdb.org/t/p/w500/wWt4JYXTg5Wr3xBW2phBrMKgp3x.jpg"},
    {"id": 14, "titulo": "Meu Malvado Favorito", "genero": "Comédia", "ano": 2010,
        "img": "https://br.web.img2.acsta.net/c_310_420/medias/nmedia/18/87/89/83/20028679.jpg"},
    {"id": 15, "titulo": "Minions", "genero": "Comédia", "ano": 2015,
        "img": "https://image.tmdb.org/t/p/w500/vlOgaxUiMOA8sPDG9n3VhQabnEi.jpg"},
    {"id": 16, "titulo": "Zootopia", "genero": "Aventura", "ano": 2016,
        "img": "https://cinephellas.com/wp-content/uploads/2018/05/zootopia.jpg"},
    {"id": 17, "titulo": "A Era do Gelo", "genero": "Comédia", "ano": 2002,
        "img": "https://br.web.img3.acsta.net/medias/nmedia/18/90/29/80/20109874.jpg"},
    {"id": 18, "titulo": "Ratatouille", "genero": "Comédia", "ano": 2007,
        "img": "https://image.tmdb.org/t/p/w500/t3vaWRPSf6WjDSamIkKDs1iQWna.jpg"},
    {"id": 19, "titulo": "Wall-E", "genero": "Drama", "ano": 2008,
        "img": "https://image.tmdb.org/t/p/w500/hbhFnRzzg6ZDmm8YAmxBnQpQIPh.jpg"},
    {"id": 20, "titulo": "Carros", "genero": "Aventura", "ano": 2006,
        "img": "https://image.tmdb.org/t/p/w500/qa6HCwP4Z15l3hpsASz3auugEW6.jpg"},
    {"id": 21, "titulo": "Uma aventura Lego", "genero": "Animação", "ano": 2014,
        "img": "https://br.web.img3.acsta.net/pictures/13/12/02/20/59/515779.jpg"},
]

@app.post("/cadastrar")
def cadastrar(
    titulo: str = Form(...),
    genero: str = Form(...),
    ano: int = Form(...),
    img: str = Form(...)
):
    novo = {
        "id": len(filmes) + 1,
        "titulo": titulo,
        "genero": genero,
        "ano": ano,
        "img": img
    }

    filmes.append(novo)

@app.get("/filme/{filme_id}")
def buscar_filme(filme_id: int):
    for filme in filmes:
        if filme["id"] == filme_id:
            return filme
    
    return {"erro": "Filme não listado"} 

@app.get("/", response_class=HTMLResponse)
def home(
    genero: Optional[str] = Query(default=None),
    q: Optional[str] = Query(default=None),
    ano_min: Optional[str] = Query(default=None),
    ano_max: Optional[str] = Query(default=None),
    ordem: Optional[str] = Query(default=None)
):
    lista_filmes = filmes

    # filtro por gênero
    if genero and genero.strip():
        lista_filmes = [
            f for f in lista_filmes
            if genero.lower() in f["genero"].lower()
        ]
        
    # filtro por ano mínimo
    if ano_min:
        lista_filmes = [
            f for f in lista_filmes
            if f["ano"] >= int(ano_min)
        ]

    # filtro por ano máximo
    if ano_max:
        lista_filmes = [
            f for f in lista_filmes
            if f["ano"] <= int(ano_max)
        ]

    # busca por nome
    if q and q.strip():
        lista_filmes = [
            f for f in lista_filmes
            if q.lower() in f["titulo"].lower()
        ]
        
    # filtra por ordem de lançamento
    if ordem == "asc":
        lista_filmes = sorted(lista_filmes, key=lambda f: f["ano"])
    elif ordem == "desc":
        lista_filmes = sorted(lista_filmes, key=lambda f: f["ano"], reverse=True)

    # FIM DOS FILTROS

    if not lista_filmes:
        html_filmes = """
        <h1 style="font-size:32px; text-align:center; width:100%;">
            😢 Nenhum filme encontrado
        </h1>
        """
    else:
        html_filmes = ""
        for filme in lista_filmes:
            html_filmes += f"""
            <div style="background:#F06C01;border-radius:10px;width:100%; max-width:200px; overflow:hidden;color:#fff">
                <img src="{filme['img']}" style="width:100%; height:300px; object-fit:cover;">
                <div style="padding:10px;">
                    <h3 style="margin:0; font-size:16px;">{filme['titulo']}</h3>
                    <p style="margin:5px 0;">🎭 {filme['genero']}</p>
                    <p style="margin:0;">📅 {filme['ano']}</p>
                </div>
            </div>
            """

    return f"""
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MobileFlix</title>
</head>

<body style="margin:30px; font-family: Arial; background:#A1071F; color:white;">

    <div >

        <!-- HEADER -->
        <div style="background:#F06C01; padding:20px; border-radius:10px; margin-bottom:20px; max-width:100%;">

            <div style="margin-bottom:20px;">
                <h1 style="color:#A1071F; margin:0;text-align:center">🎬 Kids Flix</h1>
            </div>

            <div style="display:flex; gap:20px; flex-wrap:wrap;">

                <!-- ESQUERDA: BUSCA -->
                <div style="flex:1; min-width:300px;">
    <h3 style="color:#A1071F;text-align:center">Buscar Filme</h3>

    <form method="get" style="display:flex; flex-direction:column; gap:10px;">
        
        <div style="display:flex; gap:10px; flex-wrap:wrap;">
            <input name="q" placeholder="Buscar filme..."
                style="padding:10px; border-radius:5px; border:none; flex:1">
                
            <input type="number" name="ano_min" placeholder="Ano mín"
                style="padding:10px; border-radius:5px; border:none; width:100px; flex:1">

            <input type="number" name="ano_max" placeholder="Ano máx"
                style="padding:10px; border-radius:5px; border:none; width:100px; flex:1">

            <select name="genero"
                style="flex:1; padding:10px; border-radius:5px; border:none;">
                <option value="">Todos os gêneros</option>
                <option value="Aventura">Aventura</option>
                <option value="Comédia">Comédia</option>
                <option value="Drama">Drama</option>
                <option value="Musical">Musical</option>
                <option value="Ação">Ação</option>
            </select>
            
            <select name="ordem" style="flex:1; padding:10px; border-radius:5px; border:none;">
                <option value="">Ordenar por</option>
                <option value="asc">Mais antigos</option>
                <option value="desc">Mais novos</option>
            </select>
        </div>

        <div style="display:flex; gap:10px; align-items:center;">
            <button style="background:#01F065; padding:10px; border:none; border-radius:5px; flex:1">
                Filtrar
            </button>

            <a href="/" style="background:#AAAAAA; padding:10px; border-radius:5px; text-align:center; text-decoration:none; color:white;">
                Limpar
            </a>
        </div>

    </form>
</div>

                <!-- DIREITA: CADASTRO -->
                <div style="flex:1; min-width:300px;">
                    <h3 style="color:#A1071F;text-align:center">Cadastrar Filme</h3>

                    <form onsubmit="adicionarFilme(event)" 
                        style="display:flex; gap:10px; flex-wrap:wrap;">
                        
                        <input id="titulo" placeholder="Título" required
                            style="padding:10px; border-radius:5px; border:none; flex:1; ">

                        <select id="genero" required
                            style="flex:1; padding:10px; border-radius:5px; border:none;">
                            
                            <option value="">Selecione o gênero</option>
                            <option value="Aventura">Aventura</option>
                            <option value="Comédia">Comédia</option>
                            <option value="Drama">Drama</option>
                            <option value="Musical">Musical</option>
                            <option value="Ação">Ação</option>
                        </select>

                        <input id="ano" type="number" placeholder="Ano" required
                            style="padding:10px; border-radius:5px; border:none; width:100px;">

                        <input id="img" placeholder="URL da imagem" required
                            style="padding:10px; border-radius:5px; border:none; flex:1;">

                        <button style="background:#01F065;padding:10px; border:none; border-radius:5px; flex:1;">
                            Cadastrar
                        </button>
                    </form>
                </div>

            </div>
        </div>

        <!-- LISTA -->
        <h3 style="color:#F06C01">Filmes</h3>

        <div style="display:flex; gap:20px; flex-wrap:wrap;justify-content:center">
            {html_filmes}
        </div>

    </div>

    <script>
    async function adicionarFilme(event){{
        event.preventDefault()

        let titulo = document.getElementById("titulo").value
        let genero = document.getElementById("genero").value
        let ano = document.getElementById("ano").value
        let img = document.getElementById("img").value

        let formData = new FormData()

        formData.append("titulo", titulo)
        formData.append("genero", genero)
        formData.append("ano", ano)
        formData.append("img", img)

        await fetch("/cadastrar", {{
            method: "POST",
            body: formData
        }})

        location.reload()
    }}
    </script>

</body>
</html>
"""