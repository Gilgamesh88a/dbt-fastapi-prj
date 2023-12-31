from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from dbt.cli.main import dbtRunner, dbtRunnerResult

dbt = dbtRunner()

lst_cmd = [
    'deps'
    'compile',
    'docs generate'
]

def dbt_cmd(str_cmd: str) -> dbtRunnerResult:
    return dbt.invoke(str_cmd.split(' '))

for _ in lst_cmd:
    dbt_cmd(_)

app = FastAPI()

@app.get("/")
def get_homepage():
    return dict(status='welcome page')

app.mount(
    "/dbt_docs", # --> sub-path of the "sub-app" will be mounted on
    StaticFiles( # ---> https://www.starlette.io/staticfiles/
        directory="target", # name of the dir that contains the static files
        html=True), # --> `Starlette`: Automatically loads index.html for directories if such file exist.
    name="static") # --> used internally by fastapi



# inspect the results
# for r in res.result:
#     print(f"{r.node.name}: {r.status}")