
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse


app = FastAPI()

db = {}
identity:int = 0
new_movie = {}


# Defining the data scheme
class MovieCreate(BaseModel):
    title: str
    director: str
    year: int= Field(gt = 1888)


# Building the endpoints

@app.post('/api/movies')
async def movie_store(movie:MovieCreate):
    new_movie = movie.model_dump()
    global identity
    identity =identity + 1
    new_movie.update({'is_watched': False, 'id': identity})
    db[identity] = new_movie
    return JSONResponse(status_code= 201,content ={
           "status": 'Success',
            "data": new_movie} )   
    

     
@app.get('/api/movies')
async def get_all( watch:bool | None = None):
    filtered_movie = []
    for movie in db.values():
        if watch is None or movie['is_watched'] == watch:
             filtered_movie.append(movie)
# Return ONLY after the loop is completely finished
    return {
        "status": "success",
        "results": len(filtered_movie),
        "data": filtered_movie  }          



@app.patch('/api/movies/{movie_id}')
async def update_movie(movie_id:int, watch: bool | None = None):
    if movie_id not in db:
        raise HTTPException(
            status_code= 404,
            detail= {'message': 'Movie is not found'})
    if watch is not None:
        db[movie_id]['is_watched'] = watch
    return db[movie_id]


@app.delete('/api/movies/{movie_id}')
async def delete_movie(movie_id:int):
    if movie_id not in  db:
        return JSONResponse(
                status_code=404,
                content='Movie not found'
            )
    del db[movie_id]
    return JSONResponse(status_code= 204,content='Success')
    



