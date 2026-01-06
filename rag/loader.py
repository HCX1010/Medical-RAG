from langchain_community.document_loaders import CSVLoader

def load_csv(path: str):
    loader = CSVLoader(file_path=path, encoding="utf-8", csv_args={"delimiter": ","})
    return loader.load()
