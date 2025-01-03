# **DW para área de CX no MAGALU**⬇️:
Segue abaixo um breve resumo da implantação de um DW na área de CX do Magalu realizado por mim.

## **FLUXOGRAMA DO PROJETO**⬇️:

![image](https://github.com/user-attachments/assets/4cf35ab0-4913-4cb2-81bc-57d5fce64187)


## **PROBLEMAS ANTES DA SOLUÇÃO**⬇️:

### **RETRABALHO E CUSTO ALTO**: 
Após analisar uma semana da rotina da área, percebi que, por falta de comunicação e também por falta de uma orientação, os analistas acabavam executando uma mesma consulta no meio de suas 5 consultas diárias, que tinha um processamento de em média 500 GB! O Google cobra $5,00 por Terabyte processado. Isso significa que só uma consulta de 500 GB executada pelos 6 analistas gera um custo médio mensal de $315 Dólares (($2,50 * 6 ) * 21 - dias úteis no mês) 

### **TRABALHO MANUAL**:
Após o time fazer toda extração de dados no BQ, eles investiam muito tempo para carregar o csv no excel via power query, fazer às transformações como procv e etc. Isso levava em média 02 à 04 horas diárias, pois dependia muito do excel não travar por falta de memória, erro de fórmula ou algo do tipo.

[![N|Solid](https://filestore.community.support.microsoft.com/api/images/9ccf9577-9d29-4fdb-9d49-c5ae0c5cd8da)](https://nodesource.com/products/nsolid)

## **RESULTADOS COM ESSA SOLUÇÃO**⬇️:
> [!IMPORTANT]
> Lembrando que na época, o Google cobrava $5,00 dólares por Terabyte processado no BigQuery

![image](https://github.com/user-attachments/assets/4e748b3c-41ce-4371-ac9c-b706433cd417)

## **VISUALIZAÇÕES CRIADAS EM CIMA DO DW**⬇️:
> [!WARNING]
> Essas imagens abaixo são apenas um TEMPLATE de algumas visões que criei quando atuava no MAGALU. Todos os dados, templates que estão nesse repositório são **FICTICIO**, e, para evitar problemas fúturos, mesmo SENDO dados aleatórios, descidi CENSURAR para evitar teorias da conspiração ou algo do tipo.

![image](https://user-images.githubusercontent.com/78058494/230523054-7d14b938-ef14-45e0-8907-20ce4f33bcca.png)
![image](https://user-images.githubusercontent.com/78058494/230523877-8d6515a7-b1a7-492c-9e24-5ba202fffdf4.png)
![image](https://github.com/user-attachments/assets/169f50a0-cc53-498c-be7f-d7b298410263)
![image](https://github.com/user-attachments/assets/cf5d7bf8-d4b9-48ba-8bf6-8af18d7b3bf8)
![image](https://github.com/user-attachments/assets/3e7edfe0-45c6-431f-98e6-dd63c6087e03)
![image](https://github.com/user-attachments/assets/ffac8c31-95cb-40bb-9678-3da85489552a)

## **TECNOLOGIA UTILIZADAS NESSE PROJETO**⬇️:
* PYTHON
* SQL
* TABLEAU

### ⚠️**OBSERVAÇÕES IMPORTANTES️**⬇️:
> [!WARNING]
> Quero deixar bem claro que neste reposítorio, **não existe NENHUMA informação referente à empresa MAGALU**. **Todos os dados e informações foram geradas de forma aleatória com objetivo de apresentar o case dessa solução**. Para qualquer informação, estou à disposição.
