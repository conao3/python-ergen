import typer

app = typer.Typer()


@app.command()
def ping(
    input_file: str = typer.Argument(..., help="Input file"),
):
    """
    Ping pong
    """
    typer.echo(f"Input file: {input_file}")



@app.callback()
def callback():
    pass


if __name__ == "__main__":
    app()
