# Get-it — Projeto 1B (Django)

Reimplementação em Django do sistema de anotações Get-it (Projeto 1A), com sistema de tags (Many-to-One) e PostgreSQL.

## Link da aplicação publicada

TODO: adicionar o link do deploy no Render.

## Rodando localmente

1. Suba o container do PostgreSQL (ver `aulas/05-bd` do handout): banco `getit`, usuário `getituser`, senha `getitsenha`, porta `5432`.
2. Crie e ative um ambiente virtual, depois instale as dependências:
   ```
   pip install -r requirements.txt
   ```
3. Rode as migrações e suba o servidor:
   ```
   python manage.py migrate
   python manage.py runserver
   ```
4. Acesse http://localhost:8000/
