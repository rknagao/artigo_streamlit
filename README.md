# Artigo Streamlit 101: o básico para colocar seu projeto no ar
Repositório do [artigo assíncrono da Tera](https://medium.com/@rknagao/streamlit-101-o-b%C3%A1sico-para-colocar-seu-projeto-no-ar-38a71bd641eb) sobre [Streamlit](https://www.streamlit.io/) e modelos em produção.


### Explicação dos arquivos

**1) Procfile**
* criar no notepad e salvar como "Procfile" (exatamente assim, com as aspas). Ao adicionar as aspas e não especificar a extensão, o notepad reconhece o arquivo sem extensão
* arquivo necessário na arquitetura do Heroku
* tradução: "executa o arquivo 'setup.sh' e 'app.py' como um aplicativo web".

**2) setup.sh**
* criar no notepad e salvar como .sh
* a extensão .sh representa um script a ser rodado no terminal (e.g. bash ou PowerShell)
* problema de portas: o streamlit, por padrão, cria a aplicação na porta 8501 (i.e. http://localhost:8501). Entretanto, o Heroku designa portas de forma automática, o que pode resultar em uma incompatibilidade de portas. Utilizando o `port = $PORT`
