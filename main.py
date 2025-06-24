import cv2
from deepface import DeepFace
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import numpy as np

# Traduções
traducao_genero = {
    "Man": "Masculino",
    "Woman": "Feminino"
}
traducao_etnia = {
    "white": "Branco",
    "black": "Negro",
    "asian": "Asiático",
    "latino hispanic": "Latino",
    "middle eastern": "Oriente Médio",
    "indian": "Indiano"
}
traducao_emocao = {
    "angry": "Raiva",
    "disgust": "Nojo",
    "fear": "Medo",
    "happy": "Feliz",
    "sad": "Tristeza",
    "surprise": "Surpresa",
    "neutral": "Neutro"
}

class FaceAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FaceAnalyzer AI")
        self.tema_escuro = True  # Começa com tema escuro
        self.tela_cheia = False
        
        # Configuração inicial
        self.root.geometry("1200x800")
        self.root.minsize(1000, 700)
        self.root.configure(bg="#1a1a1a")
        
        # Ícone da aplicação
        try:
            self.root.iconbitmap("face_icon.ico")  # Substitua pelo caminho do seu ícone
        except:
            pass
            
        # Configuração de estilo
        self.setup_styles()
        
        # Criar widgets
        self.criar_widgets()
        
        # Aplicar tema inicial
        self.aplicar_tema()
        
        # Configurar eventos
        self.root.bind("<F11>", self.alternar_tela_cheia)
        self.root.bind("<Escape>", self.sair_tela_cheia)
        
        # Centralizar janela
        self.centralizar_janela()

    def setup_styles(self):
        self.styles = {
            "neon_azul": "#00ffff",
            "neon_roxo": "#9d00ff",
            "neon_rosa": "#ff00ff",
            "neon_verde": "#39ff14",
            "neon_amarelo": "#fff01f",
            "fundo_escuro": "#121212",
            "fundo_card": "#1e1e1e",
            "fundo_claro": "#f5f5f5",
            "texto_claro": "#ffffff",
            "texto_escuro": "#333333",
            "borda": "#333333",
            "hover_azul": "#00b3b3",
            "hover_roxo": "#7a00cc",
            "hover_rosa": "#cc00cc",
            "hover_verde": "#2ecc40"
        }
        
        # Estilo para os botões
        style = ttk.Style()
        style.theme_use('clam')
        
        style.configure('TButton', 
                        font=('Segoe UI', 12, 'bold'),
                        borderwidth=1,
                        relief="solid",
                        padding=10)
        
        style.map('Neon.TButton',
            foreground=[('active', self.styles["texto_claro"]), ('!active', self.styles["neon_azul"])],
            background=[('active', self.styles["hover_azul"]), ('!active', self.styles["fundo_card"])],
            bordercolor=[('active', self.styles["neon_azul"])]
        )
        
        style.map('Rosa.TButton',
            foreground=[('active', self.styles["texto_claro"]), ('!active', self.styles["neon_rosa"])],
            background=[('active', self.styles["hover_rosa"]), ('!active', self.styles["fundo_card"])],
            bordercolor=[('active', self.styles["neon_rosa"])]
        )
        
        style.map('Verde.TButton',
            foreground=[('active', self.styles["texto_claro"]), ('!active', self.styles["neon_verde"])],
            background=[('active', self.styles["hover_verde"]), ('!active', self.styles["fundo_card"])],
            bordercolor=[('active', self.styles["neon_verde"])]
        )

    def criar_widgets(self):
        # Frame principal
        self.main_frame = tk.Frame(self.root, bg=self.styles["fundo_escuro"])
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Cabeçalho
        self.header_frame = tk.Frame(self.main_frame, bg=self.styles["fundo_escuro"])
        self.header_frame.pack(fill="x", pady=(0, 20))
        
        self.label_titulo = tk.Label(
            self.header_frame, 
            text="FaceAnalyzer AI",
            font=("Segoe UI", 36, "bold"),
            bg=self.styles["fundo_escuro"],
            fg=self.styles["neon_azul"]
        )
        self.label_titulo.pack(side="left")
        
        self.btn_tema = ttk.Button(
            self.header_frame,
            text="Modo Claro",
            style="Neon.TButton",
            command=self.alternar_tema
        )
        self.btn_tema.pack(side="right", padx=10)
        
        # Corpo principal
        self.body_frame = tk.Frame(self.main_frame, bg=self.styles["fundo_escuro"])
        self.body_frame.pack(fill="both", expand=True)
        
        # Painel esquerdo (imagem)
        self.left_panel = tk.Frame(
            self.body_frame, 
            bg=self.styles["fundo_card"],
            bd=2,
            relief="solid",
            highlightbackground=self.styles["neon_azul"],
            highlightthickness=1
        )
        self.left_panel.pack(side="left", fill="both", expand=True, padx=(0, 20))
        
        self.label_imagem = tk.Label(
            self.left_panel,
            text="Nenhuma imagem capturada",
            font=("Segoe UI", 14),
            bg=self.styles["fundo_card"],
            fg=self.styles["texto_claro"],
            width=40,
            height=20
        )
        self.label_imagem.pack(pady=20, padx=20, fill="both", expand=True)
        
        # Painel direito (resultados)
        self.right_panel = tk.Frame(
            self.body_frame, 
            bg=self.styles["fundo_card"],
            bd=2,
            relief="solid",
            highlightbackground=self.styles["neon_azul"],
            highlightthickness=1
        )
        self.right_panel.pack(side="right", fill="both", expand=True)
        
        self.label_resultado_titulo = tk.Label(
            self.right_panel,
            text="Resultados da Análise",
            font=("Segoe UI", 18, "bold"),
            bg=self.styles["fundo_card"],
            fg=self.styles["neon_azul"],
            pady=10
        )
        self.label_resultado_titulo.pack(fill="x")
        
        self.label_resultado = tk.Label(
            self.right_panel,
            text="Capture uma imagem para analisar",
            font=("Segoe UI", 14),
            bg=self.styles["fundo_card"],
            fg=self.styles["texto_claro"],
            justify="left",
            anchor="nw",
            padx=20,
            pady=10
        )
        self.label_resultado.pack(fill="both", expand=True)
        
        # Rodapé (botões)
        self.footer_frame = tk.Frame(self.main_frame, bg=self.styles["fundo_escuro"])
        self.footer_frame.pack(fill="x", pady=(20, 0))
        
        self.btn_capturar = ttk.Button(
            self.footer_frame,
            text="📸 Capturar Rosto",
            style="Rosa.TButton",
            command=self.capturar_e_analisar
        )
        self.btn_capturar.pack(side="left", padx=10)
        
        self.btn_sair = ttk.Button(
            self.footer_frame,
            text="Sair",
            style="Verde.TButton",
            command=self.root.quit
        )
        self.btn_sair.pack(side="right", padx=10)
        
        # Barra de status
        self.status_bar = tk.Label(
            self.main_frame,
            text="Pronto",
            font=("Segoe UI", 10),
            bg=self.styles["fundo_escuro"],
            fg=self.styles["neon_verde"],
            anchor="w"
        )
        self.status_bar.pack(fill="x", pady=(10, 0))

    def aplicar_tema(self):
        if self.tema_escuro:
            # Tema escuro
            bg = self.styles["fundo_escuro"]
            fg_titulo = self.styles["neon_azul"]
            btn_text = "Modo Claro"
            card_bg = self.styles["fundo_card"]
            text_color = self.styles["texto_claro"]
        else:
            # Tema claro
            bg = self.styles["fundo_claro"]
            fg_titulo = "#2c3e50"
            btn_text = "Modo Escuro"
            card_bg = "#ffffff"
            text_color = self.styles["texto_escuro"]
            
        # Aplicar cores
        self.main_frame.config(bg=bg)
        self.header_frame.config(bg=bg)
        self.body_frame.config(bg=bg)
        self.footer_frame.config(bg=bg)
        self.status_bar.config(bg=bg, fg=self.styles["neon_verde"] if self.tema_escuro else "#27ae60")
        
        self.label_titulo.config(bg=bg, fg=fg_titulo)
        self.btn_tema.config(text=btn_text)
        
        self.left_panel.config(bg=card_bg, highlightbackground=fg_titulo)
        self.right_panel.config(bg=card_bg, highlightbackground=fg_titulo)
        
        self.label_imagem.config(bg=card_bg, fg=text_color)
        self.label_resultado_titulo.config(bg=card_bg, fg=fg_titulo)
        self.label_resultado.config(bg=card_bg, fg=text_color)

    def alternar_tema(self):
        self.tema_escuro = not self.tema_escuro
        self.aplicar_tema()

    def alternar_tela_cheia(self, event=None):
        self.tela_cheia = not self.tela_cheia
        self.root.attributes("-fullscreen", self.tela_cheia)

    def sair_tela_cheia(self, event=None):
        self.tela_cheia = False
        self.root.attributes("-fullscreen", False)

    def centralizar_janela(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def atualizar_status(self, mensagem):
        self.status_bar.config(text=mensagem)
        self.root.update_idletasks()

    def capturar_e_analisar(self):
        self.atualizar_status("Preparando câmera...")
        
        cam = cv2.VideoCapture(0)
        if not cam.isOpened():
            messagebox.showerror("Erro", "Não foi possível acessar a câmera.")
            self.atualizar_status("Erro ao acessar câmera")
            return
            
        self.atualizar_status("Pressione ESPAÇO para capturar ou ESC para cancelar")

        # Janela de visualização personalizada
        cv2.namedWindow("FaceAnalyzer - Captura", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("FaceAnalyzer - Captura", 800, 600)
        
        while True:
            ret, frame = cam.read()
            if not ret:
                break
                
            # Espelhar a imagem para efeito de espelho
            frame = cv2.flip(frame, 1)
            
            # Adicionar overlay estilizado
            overlay = frame.copy()
            cv2.rectangle(overlay, (0, 0), (frame.shape[1], 60), (0, 0, 0), -1)
            cv2.addWeighted(overlay, 0.5, frame, 0.5, 0, frame)
            
            # Adicionar texto
            cv2.putText(frame, "FaceAnalyzer - Captura", (20, 40), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            cv2.putText(frame, "Pressione ESPACO para capturar", (20, frame.shape[0]-40), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
            
            cv2.imshow("FaceAnalyzer - Captura", frame)
            
            key = cv2.waitKey(1)
            if key == ord(' '):  # Espaço para capturar
                break
            elif key == 27:      # ESC para cancelar
                cam.release()
                cv2.destroyAllWindows()
                self.atualizar_status("Captura cancelada")
                return

        cam.release()
        cv2.destroyAllWindows()
        
        # Salvar a imagem capturada
        cv2.imwrite("captura.jpg", frame)
        
        # Mostrar a imagem capturada na interface
        img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        img = img.resize((400, 400), Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)
        
        self.label_imagem.config(image=img_tk, text="")
        self.label_imagem.image = img_tk
        
        # Analisar a imagem
        self.analisar_imagem("captura.jpg")

    def analisar_imagem(self, image_path):
        self.atualizar_status("Analisando imagem...")
        
        try:
            result = DeepFace.analyze(
                img_path=image_path,
                actions=['age', 'gender', 'race', 'emotion'],
                enforce_detection=False
            )

            dados = result[0]
            idade = int(dados["age"])
            if idade > 80 or idade < 5:
                idade_texto = f"{idade}+ (estimativa imprecisa)"
            else:
                idade_texto = f"{idade} anos"

            genero_dominante = max(dados["gender"], key=dados["gender"].get)
            etnia = dados["dominant_race"]
            emocao = dados["dominant_emotion"]

            genero_traduzido = traducao_genero.get(genero_dominante, genero_dominante)
            etnia_traduzida = traducao_etnia.get(etnia, etnia)
            emocao_traduzida = traducao_emocao.get(emocao, emocao)

            # Criar resultado formatado com emojis e estilo
            resultado = (
                f"📅 Idade estimada: {idade_texto}\n\n"
                f"🧑 Gênero: {genero_traduzido}\n\n"
                f"🌎 Etnia predominante: {etnia_traduzida}\n\n"
                f"😊 Emoção: {emocao_traduzida}\n\n"
                f"🔍 Análise concluída com sucesso!"
            )

            self.label_resultado.config(text=resultado)
            self.atualizar_status("Análise concluída - " + 
                                f"Idade: {idade_texto}, " +
                                f"Gênero: {genero_traduzido}, " +
                                f"Emoção: {emocao_traduzida}")

        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao analisar imagem.\n\nErro: {str(e)}")
            self.atualizar_status(f"Erro na análise: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FaceAnalyzerApp(root)
    root.mainloop()