import fastapi
from geocoder import osm
from pydantic import BaseModel

app = fastapi.FastAPI()

class Data(BaseModel):
    street_name : str

@app.get("/search")
def search(data : Data):
    res =  osm(data.street_name)
    if res.json != None:
    	return { "data" : res.json , "noResult" : False}
    return { "noResult" : True}