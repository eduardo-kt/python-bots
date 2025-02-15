import zipfile
from pathlib import Path

# Diretório atual de trabalho
root_dir = Path.cwd()

# Arquivos e diretórios que devem ser excluídos do zipfile
exclude = {
    ".venv",
    "login_page_bot.zip",
    ".env",
}


def add_files_to_zip(
    zipf,
    path,
    exclude,
) -> None:
    """
    Adiciona arquivos ao arquivo zip, ignorando
    os que estão na lista de exclusão.
    """

    for file_path in path.rglob("*"):
        if file_path.name not in exclude:
            zipf.write(file_path, file_path.relative_to(path))


def create_zip(
    zip_name,
    root_dir,
    exclude,
) -> None:
    """Cria um arquivo zip com os arquivos do diretório especificado,
    excluindo certos arquivos."""
    with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as zipf:
        add_files_to_zip(zipf, root_dir, exclude)


if __name__ == "__main__":
    create_zip("login_page_bot.zip", root_dir, exclude)
