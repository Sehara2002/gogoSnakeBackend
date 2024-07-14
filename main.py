from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()


origins = [
    "http://192.168.43.126:3001", # Add more origins as needed
]

# Add the CORS middleware to your FastAPI app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins
    allow_credentials=True,  # Allow cookies to be included in cross-origin requests
    allow_methods=["*"],  # List of allowed HTTP methods
    allow_headers=["*"],  # List of allowed headers
)
loadcell_data = []
@app.get("/loadcell/{data}")
def getload(data: bool):
    print(f"Loadcell Data: {data}")
    loadcell_data.append(data)
    return {"LoadCellData": data}

@app.post("/sendLoadData")
def sendLoad():
    print(f"data to be Sent {loadcell_data[len(loadcell_data)-1]}")
    return {"load_Cell_data":loadcell_data[len(loadcell_data)-1]}


@app.get("/")
def loader():
    print("Hello World")
    return {"Message":"Hello World"}