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
game_data = {
    "player01Score":0,
    "player01Shooting":0,
    "player02Score":0,
    "player02Shooting":0
}
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
def fetch_game_data(request: Request):
    file_data = request.json()
    print(f"Data Received from Board: {file_data}")
    return file_data

@app.get("/game_data")
def get_game_data():
    return {game_data}