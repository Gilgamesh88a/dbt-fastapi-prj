from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from dbt.cli.main import dbtRunner

app = FastAPI()
app.mount("/documents", StaticFiles(directory="static", html=True), name="static")

# # initialize
# dbt = dbtRunner()

# # create CLI args as a list of strings
# cmd = 'docs serve --port=8081'
# cli_args = cmd.split(' ')


# # run the command
# res: dbtRunnerResult = dbt.invoke(cli_args)

# inspect the results
# for r in res.result:
#     print(f"{r.node.name}: {r.status}")