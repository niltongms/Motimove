## MotiMove – Motivação em Movimento 

Uma solução tecnológica que busca tornar a prática esportiva mais **engajadora e acessível**.  
A plataforma propõe um sistema **gamificado de desafios e recompensas**, estimulando a constância e promovendo a conexão entre os usuários.

Com funcionalidades como:

- 🎯 Desafios individuais e coletivos  
- 🏆 Rankings e prêmios  
- 🤝 Integração com redes sociais  

O **MotiMove** incentivará a construção de **hábitos saudáveis** de forma dinâmica e motivadora.



---

## Funcionalidades principais

* Cadastro, leitura, atualização e exclusão (CRUD) de usuários
* Registro de atividades físicas com cálculo de pontos baseado no tipo e tempo da atividade
* Persistência dos dados em arquivo JSON (`usuarios.json`)
* Ranking simples baseado na soma dos pontos de cada usuário
* Tratamento básico de erros para entradas inválidas
* Interface via terminal, fácil e rápida de usar

---

## Pré-requisitos

* Python 3 instalado (3.6 ou superior recomendado)
* Editor de texto para visualizar/modificar o arquivo JSON (opcional)

---

## Instalação

1. Clone este repositório ou copie o código para seu computador.

2. Crie um ambiente virtual (opcional, mas recomendado):

```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux / macOS
.venv\Scripts\activate     # Windows PowerShell
```

3. (Opcional) Instale dependências, se houver. O app terminal básico usa apenas a biblioteca padrão Python, então nenhuma instalação extra é necessária.

4. Certifique-se de que o arquivo `usuarios.json` exista na mesma pasta do script. Se não existir, crie com conteúdo inicial vazio:

```json
{}
```

---

## Como usar

Execute o script principal no terminal:

```bash
python3 motimove.py
```

---

## Como funciona o CRUD

### 1. Cadastro de usuário (Create)

* Você pode criar um novo usuário fornecendo nome, idade, gênero, estado e bairro.
* O usuário será salvo no arquivo JSON para uso futuro.

### 2. Listar usuários (Read)

* Visualize todos os usuários cadastrados.
* Mostra dados básicos e total de pontos acumulados.

### 3. Atualizar usuário (Update)

* Modifique informações de um usuário existente, como idade, gênero, localização.

### 4. Excluir usuário (Delete)

* Remova um usuário do sistema. Seus dados de atividades serão apagados também.

---

## Registro e consulta de atividades

* Você pode adicionar atividades físicas para qualquer usuário cadastrado.
* Cada atividade possui tipo (corrida, academia, caminhada etc.), duração e opcionalmente distância.
* O sistema calcula pontos baseados nas regras definidas e armazena na lista de atividades do usuário.

---

## Ranking diário

* O sistema exibe um ranking simples baseado na soma dos pontos das atividades registradas para o dia.
* Motiva a competição saudável entre usuários.

---

## Estrutura dos dados no arquivo JSON

O arquivo `usuarios.json` mantém um dicionário no formato:

```json
{
  "nome_usuario": {
    "idade": "30",
    "genero": "M",
    "estado": "SP",
    "bairro": "Centro",
    "atividades": [
      {
        "tipo": "corrida",
        "tempo": 30,
        "distancia": 5.0,
        "pontos": 80
      }
    ]
  }
}
```

---

## Observações importantes

* Sempre encerre o programa normalmente para garantir que os dados sejam salvos no arquivo JSON.
* Cuidado para não editar manualmente o arquivo JSON com formatos inválidos.
* O app foi feito para uso simples no terminal, sem interface gráfica.

---

## Próximos passos (opcional)

* Adicionar autenticação de usuários
* Implementar histórico completo de atividades
* Exportar relatórios de desempenho
* Migrar para uma interface web simples (exemplo usando Flask)

---

## Contato

Para dúvidas, sugestões ou contribuições, abra uma issue no GitHub ou envie mensagem para o mantenedor.

---


