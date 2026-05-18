# Próximos Passos da Pesquisa — Maio a Julho

## Contexto

A partir dos resultados do grupo focal já coletados, a próxima etapa da pesquisa deve aprofundar a avaliação da documentação gerada pelo pipeline, agora com foco nas classes e métodos considerados mais relevantes pelos desenvolvedores.

O objetivo é evoluir o experimento em três frentes:

1. Redocumentação JavaDoc orientada pelas respostas do grupo focal;
2. Geração de especificação OpenAPI sem alteração do código-fonte;
3. Geração de documentação para testes manuais com apoio de LLM.

---

# Maio — Análise dos Resultados e Redocumentação

## 1. Identificar classes e métodos mais relevantes

Com base nas respostas do grupo focal, deve-se analisar quais classes e métodos os desenvolvedores consideraram mais importantes para receber documentação.

Essa etapa deve considerar:

- comentários feitos no GitLab;
- respostas abertas do grupo focal;
- percepção dos participantes sobre utilidade;
- classes com maior complexidade;
- métodos com maior relevância funcional;
- pontos em que a documentação gerada originalmente foi considerada insuficiente.

## 2. Redocumentar classes e métodos selecionados

Após identificar os elementos mais relevantes, essas classes e métodos devem ser redocumentados.

A nova documentação deve buscar corrigir os problemas apontados no grupo focal, especialmente:

- redundância;
- superficialidade;
- falta de valor semântico;
- inconsistência;
- ausência de explicação sobre regras de negócio;
- falta de clareza sobre entradas, saídas e comportamento esperado.

## 3. Consultar Michael sobre avaliação automática pela LLM

Deve-se conversar com Michael para verificar se a própria LLM pode avaliar quais classes e métodos são mais importantes para documentação.

A questão central é:

> A LLM consegue, com base no código-fonte, identificar automaticamente quais classes e métodos possuem maior relevância, complexidade ou necessidade documental?

Essa etapa pode gerar duas possibilidades metodológicas:

## Opção A — Seleção orientada pela LLM

A LLM identifica classes e métodos prioritários para documentação.

## Opção B — Seleção por escopo fixo

Caso a avaliação automática pela LLM não seja viável, o estudo pode focar em todos os métodos das classes de serviço.

Nesse caso, a justificativa metodológica seria:

> Classes de serviço concentram regras de negócio e, portanto, seus métodos devem possuir JavaDoc mais completo e semanticamente útil.

---

# Junho — OpenAPI e Documentação para Testes Manuais

## 4. Gerar especificação OpenAPI pelo pipeline

Após a etapa de redocumentação, o pipeline deve ser utilizado para gerar uma especificação OpenAPI.

Essa etapa não deve alterar o código-fonte.

O objetivo é produzir documentação externa de serviços, descrevendo:

- endpoints;
- operações;
- entradas;
- saídas;
- contratos;
- possíveis respostas;
- estrutura funcional dos serviços.

## 5. Gerar especificação de serviços

Além do JavaDoc, a pesquisa deve explorar a geração de documentação em nível de serviço.

Essa especificação deve representar o comportamento esperado dos serviços de forma mais próxima ao uso funcional do sistema.

Diferentemente do JavaDoc, essa documentação não fica acoplada ao código-fonte.

## 6. Gerar documentação para testes manuais com apoio da LLM

A partir de dois insumos:

- código-fonte;
- especificação OpenAPI;

a LLM deve gerar documentação para apoiar testes manuais.

Essa documentação pode incluir:

- cenários de teste;
- pré-condições;
- entradas esperadas;
- passos de execução;
- resultados esperados;
- validações funcionais;
- observações para o testador.

## 7. Avaliação inicial por um desenvolvedor

Em um primeiro momento, essa documentação de testes manuais será avaliada por um desenvolvedor.

O objetivo é verificar se ela é:

- compreensível;
- útil;
- executável;
- aderente ao comportamento do sistema;
- relevante para validação manual.

---

# Final de Junho até Primeira ou Segunda Semana de Julho — Validação com Desenvolvedores

## 8. Reunir novamente os desenvolvedores

Até a primeira semana de julho, ou no máximo até a segunda semana de julho, deve-se reunir novamente os desenvolvedores.

Essa nova reunião terá caráter avaliativo e comparativo.

## 9. Avaliar se o novo JavaDoc ficou mais adequado

Os desenvolvedores deverão avaliar se a nova documentação JavaDoc está mais adequada em relação à versão anterior.

A avaliação deve observar:

- clareza;
- valor semântico;
- redução de redundância;
- padronização;
- utilidade prática;
- explicação de regras de negócio;
- adequação ao contexto das classes e métodos.

## 10. Consultar o valor da especificação OpenAPI

Os desenvolvedores também deverão avaliar se a especificação OpenAPI gerada possui valor prático.

A discussão deve investigar:

- se a OpenAPI ajuda no entendimento dos serviços;
- se melhora a visão externa do sistema;
- se complementa o JavaDoc;
- se pode apoiar integração;
- se pode apoiar manutenção;
- se pode apoiar testes.

## 11. Verificar a importância da documentação para testes manuais

Por fim, deve-se avaliar com os desenvolvedores se a documentação para testes manuais é importante ou não.

A análise deve considerar:

- utilidade para validação funcional;
- clareza dos cenários;
- aplicabilidade prática;
- possibilidade de uso por desenvolvedores ou testadores;
- ganho em relação à ausência dessa documentação;
- limitações da documentação gerada pela LLM.

---

# Síntese do Cronograma

| Período | Atividade Principal | Resultado Esperado |
|---|---|---|
| Maio | Analisar resultados do grupo focal e identificar classes/métodos prioritários | Lista de elementos mais importantes para redocumentação |
| Maio | Redocumentar classes e métodos selecionados | Nova versão de JavaDocs |
| Maio | Consultar Michael sobre uso da LLM para priorização | Definição metodológica: LLM ou escopo fixo em services |
| Junho | Gerar especificação OpenAPI pelo pipeline | Documento OpenAPI sem alteração do código-fonte |
| Junho | Gerar especificação de serviços | Documentação externa dos serviços |
| Junho | Gerar documentação para testes manuais com LLM | Documento de apoio a testes manuais |
| Junho/Julho | Avaliação inicial por 1 desenvolvedor | Feedback preliminar |
| Até 1ª ou 2ª semana de julho | Reunir desenvolvedores novamente | Validação comparativa dos artefatos |
| Até 1ª ou 2ª semana de julho | Avaliar JavaDoc, OpenAPI e documentação de testes | Evidências finais para dissertação |

---

# Resultado Esperado da Próxima Etapa

Ao final dessa fase, a pesquisa deverá ter evidências sobre três tipos de documentação gerada ou apoiada por LLM:

1. **JavaDoc redocumentado**, voltado ao entendimento interno do código;
2. **OpenAPI**, voltada à especificação externa dos serviços;
3. **Documentação para testes manuais**, voltada à validação funcional.

Essa etapa permitirá comparar diferentes formas de documentação técnica e avaliar qual delas gera maior valor prático para os desenvolvedores.

---

# Contribuição Metodológica Esperada

A pesquisa deixará de avaliar apenas se a LLM consegue gerar JavaDoc e passará a investigar:

- quais partes do sistema realmente precisam de documentação;
- se a LLM consegue ajudar na priorização documental;
- se a documentação externa, como OpenAPI, agrega mais valor que documentação inline;
- se a LLM pode apoiar atividades de teste manual;
- como desenvolvedores percebem diferentes artefatos documentais gerados por IA.

---

# Formulação Científica da Próxima Etapa

A próxima etapa da pesquisa pode ser descrita assim:

> A partir dos resultados preliminares do grupo focal, será conduzida uma segunda fase experimental orientada à redocumentação seletiva de classes e métodos considerados prioritários. Essa fase investigará também a capacidade do pipeline em gerar especificações OpenAPI e documentação de apoio a testes manuais, sem alteração do código-fonte, com posterior avaliação por desenvolvedores quanto à utilidade, clareza e valor prático dos artefatos produzidos.
