from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
    "https://gogosnake.onrender.com",
    "http://localhost:3000"
    # Add more origins as needed
]

# Add the CORS middleware to your FastAPI app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins
    allow_credentials=True,  # Allow cookies to be included in cross-origin requests
    allow_methods=["*"],  # List of allowed HTTP methods
    allow_headers=["*"],  # List of allowed headers
)
loadcell_data = [False]
game_data = [{}]
timeoutState = [False]
crashedState = [False]
runcommand = [False]
@app.get("/loadcell/{data}")
def getload(data: bool):
    print(f"Loadcell Data: {data}")
    loadcell_data.append(data)
    return {"LoadCellData": data}

@app.get("/sendLoadData")
def sendLoad():
    print(f"data to be Sent {loadcell_data[len(loadcell_data)-1]}")
    return {"load_Cell_data":loadcell_data[len(loadcell_data)-1]}


@app.get("/")
def loader():
    print("Hello World")
    return {"Message":"Hello World"}

@app.post("/getGameData")
async def fetch_game_data(request: Request):
    file_data = await request.json()
    #print(f"Data Received from Board: {file_data}")
    game_data.append(file_data)
    return file_data

@app.get("/game_data")
def get_game_data():
    return game_data[len(game_data)-1]

@app.get("/timeOutState/{state}")
async def getFrontTimeout(state: bool):
    print(f"Timeout state : {state}")
    timeoutState.append(state)
    return {"Message":"Data Received"}

@app.get("/sendTimeOut")
async def sendTimeOut():
    lastState = timeoutState[len(timeoutState)-1]
    print(lastState)
    timeoutState.pop()
    timeoutState.append(False)
    return {"Timeout":lastState}

@app.get("/gotCrashed/{data}")
def gotCrashed(data: bool):
    print("Line number 66",data)
    crashedState.append(data)
    return {"CrashedState":data}

@app.get("/sendCrashed")
def sendCrashed():
    print("Crashed State: ",crashedState[len(crashedState)-1])
    return {"crashedState":crashedState[len(crashedState)-1]}

@app.get("/run/{state}")
async def runCommand(state:bool):
    runcommand.append(state)
    print("Run Command",state)
    return {"runCommand":state}

@app.get("/runstate")
async def runState():
    lastcommnd = runcommand[len(runcommand)-1]
    runcommand.append(False)
    print("RunState",lastcommnd)
    return {"RunState":lastcommnd}