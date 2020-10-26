# artigo_streamlit
Repositório do artigo do assíncrono da Tera sobre [Streamlit](https://www.streamlit.io/) e modelos em produção.


### Explicação dos arquivos**

**1) Procfile**
* criar no notepad e salvar como "Procfile" (exatamente assim, com as aspas). Ao adicionar as aspas e não especificar a extensão, o notepad reconhece o arquivo sem extensão
* arquivo necessário na arquitetura do Heroku
* tradução: "executa o arquivo 'setup.sh' e 'app.py' como um aplicativo web".

**2) setup.sh**
* criar no notepad e salvar como .sh
* a extensão .sh representa um script a ser rodado no terminal (e.g. bash ou PowerShell)
* problema de portas: o streamlit, por padrão, cria a aplicação na porta 8501 (i.e. http://localhost:8501). Entretanto, o Heroku designa portas de forma automática, o que pode resultar em uma incompatibilidade de portas. Utilizando o `port = $PORT`
