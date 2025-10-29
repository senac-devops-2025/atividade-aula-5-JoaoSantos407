# Segurança e Proteção de Credenciais

- Nunca commitar segredos (tokens, senhas, chaves). Use `.env` (local) e variáveis de ambiente.
- Habilite em **Settings > Code security** do repositório:
  - **Secret scanning**
  - **Push protection**
- A pipeline executa **Gitleaks** para detectar credenciais acidentalmente incluídas.
- SCA (Dependabot) está habilitado para `pip` e `github-actions` via `.github/dependabot.yml`.

## Como reportar
Abra um Issue com o rótulo `security` descrevendo o achado (sem expor segredos).
