# Guia do Aluno – Aula 05 (Shift Security Left / SCA / Credenciais)

1. Aceite o convite do **GitHub Classroom** (link enviado pelo professor).
2. Clone seu repositório:
   ```bash
   git clone <seu-repo-clone-url>
   cd <seu-repo>
   ```
3. Prepare o ambiente e rode testes:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -r requirements.txt -r requirements-dev.txt
   pytest -q
   ```
4. Crie uma pequena mudança (ex.: ajuste de mensagem), commite e faça *push*.
5. Acompanhe a pipeline em **Actions** (build + testes + gitleaks).
6. Quando o Dependabot criar um PR de atualização, revise, aprove e faça merge.
7. Verifique que o **artefato de build** `app-dist.zip` foi gerado na execução do CI.
