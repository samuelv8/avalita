# Avalita / Branch do Caio

Para clonar o repositório (caso você ainda não o tenha):
```
git clone git@github.com:Magicos-de-CES-22/proj2.git Avalita
cd Avalita
git checkout caio
```

Para rodar o frontend, supondo que você está na pasta Avalita e usando a versão 14 do node (no linux, `nvm use 14`):
```
cd avalita_vue
npm install
npm run serve
```

Instalar dependências do backend, supondo que a pasta atual é Avalita:
```
python -m venv env
source env/bin/activate
pip install -r req.txt
```

Para rodar o backend, em um novo terminal cuja raiz é a pasta Avalita:
```
cd avalita_django
python manage.py migrate
python manage.py runserver
```

Agora é só acessar http://localhost:8080/ e ser feliz :)
