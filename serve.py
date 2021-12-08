import uvicorn
PORT = 7000
if "__main__" == __name__ :
	uvicorn.run ("main:app" , port = PORT , reload=True)