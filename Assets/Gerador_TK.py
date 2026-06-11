from docxtpl import DocxTemplate
import pandas as pd
import Utils
from pathlib import Path
from jinja2 import TemplateSyntaxError, UndefinedError
from PySide6.QtCore import QObject, Signal


class ArquivosNaoMencionados(Exception):
    pass


class ArquivoNaoSuportado(FileExistsError):
    pass


class ErroDeValidacaoConvite(Exception):
    def __init__(self, mensagem: str, detalhes: str | Exception) -> None:
        super().__init__(mensagem)
        self.detalhes = detalhes
        self.mensagem = mensagem


class GeradorConvite(QObject):
    progress = Signal(int)
    finished = Signal()
    status = Signal(str)

    def __init__(self):
        super().__init__()

        self.path_convite = None
        self.path_saida = None
        self.path_lista = None

        self.lista = []

    def load_convite(self, path_convite: Path):
        if not path_convite.exists():
            raise ConviteNaoEncontrado("Arquivo do convite não encontrado!")
        if path_convite.suffix != ".docx":
            raise ArquivoNaoSuportado("Arquivo do convite não é documento Word")
        self.path_convite = path_convite

    def load_lista(self, path_lista: Path):

        if not path_lista.exists():
            raise PlaniliaNaoEncontrada("Planília não encontrada")
        self.path_lista = path_lista

        pandas_lista = None

        match self.path_lista.suffix:
            case ".xlsx" | ".xlx":
                pandas_lista = pd.read_excel(self.path_lista.as_posix())
            case ".csv":
                pandas_lista = pd.read_csv(self.path_lista.as_posix())
            case _:
                raise ArquivoNaoSuportado("Planília não é um arquivo de Planília")

        self.lista.clear()
        pandas_lista.columns = [
            coluna.strip().lower().replace(" ", "_").replace("-", "_")
            for coluna in pandas_lista.columns
        ]
        for _, linha in pandas_lista.iterrows():
            self.lista.append(Utils.limpar_valores(linha.to_dict()))

    def load_saida(self, path_saida: Path):

        self.path_saida = path_saida

        if not path_saida.exists():
            path_saida.mkdir(exist_ok=True, parents=True)

    def get_keys(self):
        if not self.lista:
            return []

        keys = self.lista[0].keys()
        keys_formatted = []

        for key in keys:
            keys_formatted.append("{{ " + key + " }}")

        return keys_formatted

    def check_all_input(self):
        if (
            self.path_convite is None
            or self.path_saida is None
            or self.path_lista is None
        ):
            raise ArquivosNaoMencionados(
                f"Um dos arquivos são inexistentes: \nconvite: %s\nlista: %s\npasta de destino: %s"
                % (self.path_convite, self.path_lista, self.path_saida)
            )
        if not self.path_convite.exists():
            raise FileNotFoundError("Arquivo não encontrado: Convite")
        if not self.path_lista.exists():
            raise FileNotFoundError("Arquivo não encontrado: Planília")
        if not self.path_saida.exists():
            raise FileNotFoundError("Arquivo não encontrado: Pasta de destino")
        return True

    def convite_debug(self):
        if self.path_convite is None or not self.path_convite.exists():
            raise FileNotFoundError("Arquivo de convite não encontrado")

        keys = self.get_keys()

        if keys == []:
            raise FileNotFoundError("Arquivo de planília não foi carregada")

        try:
            convite = DocxTemplate(self.path_convite.as_posix())
            convite.render(self.lista[0])
            return True
        except TemplateSyntaxError as e:
            raise ErroDeValidacaoConvite(
                "Erro de sintaxe em convite",
                "Linha de número: %d\nMensagem do Jinja2:\n %s" % (e.lineno, e.message),
            )
        except UndefinedError as e:
            raise ErroDeValidacaoConvite(
                "Uma Palavra-chave não existe na planília",
                "Mensagem do Jinja2:\n %s" % (e.message),
            )
        except PermissionError as e:
            raise ErroDeValidacaoConvite(
                "Erro de permissão de leitura/escrita. Rode o aplicativo como administrador",
                e,
            )
        except Exception as e:
            raise ErroDeValidacaoConvite(
                "Há um erro inesperado em algum dos arquivos", e
            )

    def run(self):
        self.check_all_input()
        convite = DocxTemplate(self.path_convite.as_posix())
        total = len(self.lista)
        for i, linha in enumerate(self.lista, 1):
            convite.render(linha)
            convite.save(self.path_saida / f"convite{i}.docx")
            progresso = int((i / total) * 100)
            self.progress.emit(progresso)
            self.status.emit(f"Gerando {i}/{total}")

        self.finished.emit()
