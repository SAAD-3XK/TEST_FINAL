import typer

def main(name:str = typer.Option(...)):
    print(f"Hello {name}")

if __name__ == "__main__":
    typer.run(main)

#to run this file, open CLI, and type: python3 typer_example.py --name Saad