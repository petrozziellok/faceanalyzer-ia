# 🧠 FaceAnalyzer IA

FaceAnalyzer IA é um aplicativo interativo em Python que utiliza visão computacional para analisar rostos humanos em tempo real, estimando **idade**, **gênero**, **etnia** e **emoções** com base em inteligência artificial.

> 💻 Projeto desenvolvido com foco educacional e prático para o primeiro portfólio na área de IA e visão computacional.

---

## ✨ Funcionalidades

✅ Captura de rosto via webcam  
✅ Estimativa de idade, gênero e etnia  
✅ Reconhecimento de emoção predominante  
✅ Interface gráfica em modo escuro e estilo neon  
✅ Suporte a tela cheia (F11)  
✅ Tradução automática dos resultados para português

## 🛠️ Tecnologias e bibliotecas

- [Python 3.10+](https://www.python.org)
- [DeepFace](https://github.com/serengil/deepface)
- [OpenCV](https://opencv.org/)
- [Tkinter (GUI)](https://docs.python.org/3/library/tkinter.html)
- [Pillow (Imagens)](https://python-pillow.org/)



## ⚙️ Instalação e uso

### 1. Clone o repositório

```bash
git clone https://github.com/petrozziellok/faceanalyzer-ia.git
cd faceanalyzer-ia
2. Crie o ambiente virtual
python -m venv venv
venv\Scripts\activate   # Windows

3. Instale as dependências
pip install -r requirements.txt

💡 Atalhos no app
F11: Ativa/Desativa modo tela cheia

Esc: Sai do modo tela cheia

Espaço: Captura a imagem da webcam

📌 Observações
A precisão da estimativa pode variar com iluminação, ângulo e qualidade da webcam.

A IA do DeepFace utiliza redes pré-treinadas que funcionam melhor com adultos.

Projeto ideal para uso pessoal, educacional e demonstrações de IA.

👨‍💻 Autor
Desenvolvido por Kauan Petrozziello
📧 Contato: [petrozziellok@gmail.com]