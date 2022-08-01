# kobe-endpoint

Este pacote é parte das tarefas solicitadas pela empresa Kobe durante uma entrevista técnica.

O pacote roda um endpoint que retorna um conjunto de chave e valor no header da requisição através do response.

Passo opcional, mas recomendado. Crie um venv para instalar o pacote:

```
mkdir kobe
cd kobe
python3 -m venv venv
source venv/bin/activate
```

Para instalar o pacote, utilize o comando a seguir:

```
pip install --no-cache-dir kobe --index-url=https://lllmanriquelll.github.io/kobe-endpoint/simple
```

O endpoint deve ser executado com os seguintes parâmetros:

```
uvicorn kobe.main:app --reload
```

Para baixar o pacote e rodar o pytest, clone o repositório abaixo:

```
git clone https://github.com/lllmanriquelll/kobe-endpoint.git
```

Acesse o diretório clonado:

```
cd kobe-endpoint/
```

Instale os pacotes necessários, caso ainda os tenha:

 ```
 pip install -r requirements.txt
 ```

Execute o pytest indicando o diretório com o teste:

```
pytest -r kobe/tests/
```