# Guia do Professor – Configuração no GitHub Classroom

1. Crie uma organização ou use a existente da disciplina.
2. Crie um repositório **template** a partir deste ZIP (importar o conteúdo deste template).
3. No **GitHub Classroom**:
   - Crie uma **Assignment** do tipo Individual.
   - Em **Template repository**, selecione o repositório criado no passo 2.
   - (Opcional) Defina testes de *autograding* se desejar.
4. No repositório **template**, valide:
   - **Settings > Code security**: habilite *Secret scanning* e *Push protection*.
   - **Actions**: permita *Workflows*.
5. Envie o link da assignment aos alunos.
6. Acompanhe em **Classroom** o status de cada aluno (submissões e pipelines).

## Critérios sugeridos de avaliação
- CI verde (build + testes).
- Artefato publicado.
- PR de Dependabot tratado.
- Boas práticas de commits e README atualizado.
