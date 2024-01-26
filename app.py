import uvicorn


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    # NOTE: reload=True is for development only, it means that in practice we need config file for setting environment variables
