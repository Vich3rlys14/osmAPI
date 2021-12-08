import uvicorn
PORT = 7000
HOST = "0.0.0.0"
if "__main__" == __name__ :
	uvicorn.run ("main:app" , port = PORT , reload=True , host=HOST)