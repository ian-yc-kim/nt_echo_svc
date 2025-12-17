from fastapi import FastAPI

app = FastAPI(debug=True, root_path=nt_echo_svc)

# add routers