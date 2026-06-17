from PySide6.QtCore import QThread
from pathlib import Path
from PySide6.QtWidgets import QMainWindow, QFileDialog, QApplication, QMessageBox
from Assets.ui_main import Ui_GeradorConvite
from Assets.Gerador_TK import (
    ArquivoNaoSuportado,
    ArquivosNaoMencionados,
    ErroDeValidacaoConvite,
    GeradorConvite,
)
import traceback


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gerador de Convites")
        self.backend = GeradorConvite()
        self.Thread = None  # Será criada em start_process
        self.ui = Ui_GeradorConvite()
        self.ui.setupUi(self)

        self.setStyleSheet("""
QMainWindow {
    background-color: #0b1220;
}

QWidget {
    color: #e5e7eb;
    font-family: "Segoe UI";
    font-size: 13px;
}

/* =========================
   TITULOS PRINCIPAIS
========================= */

QLabel#label_2,
QLabel#label_4,
QLabel#label_7 {
    font-size: 16px;
    font-weight: 700;
    color: #f8fafc;
}

/* subtítulos de requisito */
QLabel#label_3,
QLabel#label_5,
QLabel#label_8 {
    color: #94a3b8;
    font-size: 12px;
}

/* =========================
   BOTÕES
========================= */

QPushButton {
    background-color: #2563eb;
    border: none;
    border-radius: 10px;
    padding: 8px 14px;
    font-weight: 600;
    color: white;
}

QPushButton:hover {
    background-color: #3b82f6;
}

QPushButton:pressed {
    background-color: #1d4ed8;
}

/* =========================
   LISTA DE CHAVES
========================= */

QListWidget {
    background-color: #111827;
    border: 1px solid #1f2937;
    border-radius: 12px;
    padding: 6px;
}

QListWidget::item {
    padding: 8px;
    margin: 2px;
    border-radius: 6px;
}

QListWidget::item:hover {
    background-color: #1f2937;
}

QListWidget::item:selected {
    background-color: #2563eb;
    color: white;
}

/* =========================
   LABELS DE PATH (importante)
========================= */

QLabel#invite_path,
QLabel#list_path,
QLabel#destination_path {
    background-color: #111827;
    border: 1px solid #1f2937;
    border-radius: 8px;
    padding: 6px;
    color: #93c5fd;
}

/* =========================
   PROGRESS BAR
========================= */

QProgressBar {
    background-color: #111827;
    border-radius: 8px;
    border: 1px solid #1f2937;
    text-align: center;
    height: 18px;
}

QProgressBar::chunk {
    background-color: #22c55e;
    border-radius: 8px;
}

/* =========================
   MENU
========================= */

QMenuBar {
    background-color: #0b1220;
    color: #e5e7eb;
}

QMenuBar::item:selected {
    background-color: #1f2937;
}

QMenu {
    background-color: #0f172a;
    border: 1px solid #1f2937;
}

QMenu::item:selected {
    background-color: #2563eb;
}
""")

        self.clipboard = QApplication.clipboard()
        self.ui.findDestination.clicked.connect(self.get_saida)
        self.ui.findInvite.clicked.connect(self.get_invite)
        self.ui.findList.clicked.connect(self.get_list)
        self.ui.generateInvites.clicked.connect(self.start_process)
        self.ui.key_list.itemDoubleClicked.connect(self.get_copy_item)
        # Conecta sinais do backend uma só vez
        self.backend.progress.connect(self.ui.invite_progress_bar.setValue)

    def _setup_thread(self):
        """Cria e conecta uma nova thread limpa a cada execução."""
        self.Thread = QThread()
        self.backend.moveToThread(self.Thread)
        self.Thread.started.connect(self.backend.run)
        self.backend.finished.connect(self.Thread.quit)
        # Devolve o backend para a thread principal ao terminar,
        # permitindo moveToThread funcionar corretamente na próxima execução
        self.backend.finished.connect(
            lambda: self.backend.moveToThread(QApplication.instance().thread())
        )
        self.backend.finished.connect(lambda: self.ui.generateInvites.setEnabled(True))

    def get_saida(self):
        pasta = QFileDialog.getExistingDirectory(self, "Selecione uma pasta de saída")
        if not pasta:
            return None
        path = Path(pasta)
        try:
            self.backend.load_saida(path)
        except FileNotFoundError as e:
            self.disparar_erro("A pasta de saída não foi encontrada", e)
        except Exception as e:
            self.disparar_erro("Houve um imprevisto", e)
        self.ui.destination_path.setText(f"Encontrado: {pasta}")

    def get_invite(self):
        arquivo, _ = QFileDialog.getOpenFileName(
            self, "Selecione um arquivo WORD (.docx)", "", "Word (*.docx)"
        )
        if not arquivo:
            return None
        try:
            self.backend.load_convite(Path(arquivo))
        except FileNotFoundError as e:
            return self.disparar_erro("O arquivo não foi encontrado", e)
        except ArquivoNaoSuportado as e:
            return self.disparar_erro("O arquivo não é suportado", e)
        except Exception as e:
            return self.disparar_erro("Aconteceu um erro imprevisto", e)
        self.ui.invite_path.setText(f"Encontrado: {arquivo}")

    def get_copy_item(self, item):
        text = item.text()
        self.clipboard.setText(text)

    def get_list(self):
        arquivo, _ = QFileDialog.getOpenFileName(
            self,
            "Selecione um arquivo de tabelas (.xlsx, .xls, .csv)",
            "",
            "Planilhas (*.xlsx *.xls *.csv)",
            # "Ver o que filtra arquivos de tabelas"
        )
        if not arquivo:
            return None
        try:
            self.backend.load_lista(Path(arquivo))
        except FileNotFoundError as e:
            return self.disparar_erro("Arquivo não encontrado", e)
        except ArquivoNaoSuportado as e:
            return self.disparar_erro("Arquivo não é suportado", e)
        except PermissionError as e:
            return self.disparar_erro(
                "Há algo que não permite ler/escrever arquivos, rode o aplicativo como administrador e tente novamente",
                e,
            )
        except Exception as e:
            return self.disparar_erro("Houve um erro inesperado", e)
        self.ui.list_path.setText(f"Encontrado: {arquivo}")
        keys = self.backend.get_keys()
        self.ui.key_list.clear()
        self.ui.key_list.addItems(keys)

    def start_process(self):
        try:
            self.backend.check_all_input()
            self.backend.convite_debug()
        except ArquivosNaoMencionados as e:
            return self.disparar_erro("Há arquivos que não foram mencionados", e)
        except FileNotFoundError as e:
            return self.disparar_erro(
                "Um arquivo foi apagado sem querer e não foi encontrado", e
            )
        except ErroDeValidacaoConvite as e:
            print("Houve um erro ao validar o convite", e.mensagem, e.detalhes)
            return self.disparar_erro(e.mensagem, e.detalhes)

        self.ui.invite_progress_bar.setValue(0)
        self.ui.generateInvites.setEnabled(False)
        self._setup_thread()
        self.Thread.start()

    def disparar_erro(self, texto_principal: str, exception: None | Exception | str):
        msgbox = QMessageBox(self)
        msgbox.setWindowTitle("Gerador de convites")
        msgbox.setText("Aconteceu um erro")
        msgbox.setInformativeText(texto_principal)
        if type(exception) is Exception:
            msgbox.setDetailedText("".join(traceback.format_exception(exception)))
        elif type(exception) is str:
            msgbox.setDetailedText(exception)
        msgbox.exec()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
