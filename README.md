# artigo_streamlit
Repositório do artigo do assíncrono da Tera sobre streamlit e modelos em produção.


Explicação dos arquivos

1) Procfile
- criar no notepad e salvar como "Procfile" (exatamente assim, com as aspas). Ao adicionar as aspas e não especificar a extensão, o notepad reconhece o arquivo sem extensão
- arquivo necessário na arquitetura do Heroku
- tradução: "executa o arquivo 'setup.sh' e 'app.py' como um aplicativo web".

2) setup.sh
- criar no notepad e salvar como .sh
- a extensão .sh representa um script a ser rodado no terminal (e.g. bash ou PowerShell)
- é necessário para as configurações de porta necessária para o streamlit
- linha a linha:
    '''mkdir ~/.streamlit/''':criar a pasta (comando 'mkdir') '.streamlit' na pasta raíz do computador (comando '~/')
    
    echo "\
