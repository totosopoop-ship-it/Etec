# EcoVision FAETEC

App em Python com Kivy pensado para impressionar em apresentação escolar. Ele junta geração de ideias, simulador de impacto e gerador de pitch em um visual moderno, tudo com dados salvos localmente.

## O que o app faz
- Painel com score de inovação
- Gerador de ideias de projeto
- Simulador de impacto ambiental/social
- Gerador de pitch para apresentação
- Histórico local salvo em JSON

## Rodar no celular com Pydroid 3
1. Instale o **Pydroid 3** no Android.
2. Abra o arquivo `main.py`.
3. Instale o pacote `kivy` dentro do Pydroid.
4. Toque em **Run**.

## Gerar APK pelo GitHub Actions usando o celular
1. Crie um repositório no GitHub.
2. Envie todos os arquivos desta pasta.
3. Vá em **Actions** no GitHub.
4. Execute o workflow **Build Android APK**.
5. Ao terminar, baixe o artefato gerado com o APK.

## Gerar APK no Linux/WSL
```bash
pip install buildozer cython
sudo apt update
sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses-dev libffi-dev libssl-dev
buildozer android debug
```

## Arquivos principais
- `main.py` -> app completo
- `buildozer.spec` -> configuração do APK
- `.github/workflows/build_apk.yml` -> build automático no GitHub
