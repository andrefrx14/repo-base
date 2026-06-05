# POST-MORTEM

## Resumo

A equipe utilizou branches de feature, release e hotfix para simular um fluxo de desenvolvimento colaborativo.

## Uso de Rebase

Foi utilizado rebase nas branches `feature/dev-a` e `feature/dev-b` antes da abertura dos Pull Requests. Um conflito foi gerado e resolvido corretamente.

## Uso de Merge

Foram utilizados Pull Requests para integrar as funcionalidades na branch `develop`. Posteriormente, foi criada uma release e um hotfix.

## Dificuldades Encontradas

- Configuração inicial das branches.
- Resolução de conflitos de rebase.
- Configuração correta dos Pull Requests.

## Lições Aprendidas

- O rebase ajuda a manter o histórico organizado.
- Pull Requests facilitam a revisão do código.
- Hotfixes devem ser integrados tanto em `main` quanto em `develop`.