from fastapi import FastAPI, HTTPException, UploadFile, File
from typing import List
import shutil


from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
    "http://localhost:1234",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/uploadfile/")
async def create_upload_file(files: List[UploadFile]):
    return {"filenames": [file.filename for file in files]}    


   


    




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
