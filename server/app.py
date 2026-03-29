from my_env.server.app import app


def main() -> None:
    import uvicorn

    uvicorn.run("my_env.server.app:app", host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
