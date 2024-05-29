from fastapi import FastAPI
from starlette.responses import RedirectResponse
from starlette.requests import Request

app = FastAPI()

CLIENT_ID = "60b1bda3790825235c9a"

@app.get("/")
async def github_login(request: Request):
    a=1
    while(a<10):
        if a==5:
            response = RedirectResponse(f'https://github.com/login/oauth/authorize?client_id={CLIENT_ID}&scope=repo%20read%3Auser')
            await response(request)
            print (1737)
        else:
            print(a)
        a=a+1


@app.get("/github")
def test(code: str):
    return code


# Run the FastAPI application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8050)
