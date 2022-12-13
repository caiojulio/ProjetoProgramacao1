import sqlite3
import flet as ft

#banco=sqlite3.connect ('banco_projeto.db') # para criar o banco de dados
#cursor=banco.cursor()
#cursor.execute("CREATE TABLE usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT,email text, usuario text, senha text) ")

def main(page):  # funçao principal do flet
    page.title= "Criptografia de arquivo"
    
    dict_values= {
        'usuario': '',
        'email': '',
        'senha': ''}

    dict_valueslog={'usuariolog':'',
                    'senhalog':''}

    def aba_registro(e): #recarrega os elementos da pagina para o registro
        page.clean()

        def registrar(e): # vai estar no on_click para registrar novos usuarios apartir do input
            dict_values['usuario']= usuario.value 
            dict_values['email']= email.value 
            dict_values['senha']= senha.value
            
            for val in dict_values.values(): # checa se foi tudo preenchido pelo usuário
                if not val: 
                    page.banner.open=True
                    page.update()
                    return
            page.add(ft.Text('Registrado',size=20,weight='bold',color='green'))

            usuariob= dict_values['usuario']
            emailb= dict_values['email']
            senhab= dict_values['senha']

            banco=sqlite3.connect ('banco_projeto.db') # coloca o que foi digitado no banco de dados
            cursor=banco.cursor()
            cursor.execute("INSERT INTO usuarios VALUES (NULL,'"+emailb+"','"+usuariob+"','"+senhab+"' )")
            banco.commit()
            print (dict_values)
        
        titulo2=ft.Text(value='Registrar Usuário',size=20,weight='bold')  
        usuario= ft.TextField(label='Usuario')
        email=ft.TextField(label='Email')
        senha=ft.TextField(label='Digite sua Senha',password=True, can_reveal_password=True)
        botao_gerar=ft.FilledButton(text='Registrar',on_click=registrar)
        page.add(ft.Row(controls=[titulo2]),
                ft.Row(controls=[usuario]),
                ft.Row(controls=[email]),
                ft.Row(controls=[senha]),
                ft.Row(controls=[botao_gerar]))
                
        def fecha_banner(e): # banner que aparece caso todos o espaços não sejam preenchidos 
            page.banner.open=False
            page.update()
        page.banner=ft.Banner(
            bgcolor=ft.colors.AMBER_100,
            leading=ft.Icon(
                ft.icons.DANGEROUS_SHARP,                   
                color=ft.colors.RED_400,
                size=40
            ),
            content=ft.Text('Todos os campos devem ser preenchidos', color=ft.colors.BLACK),
            actions=[
                ft.TextButton(
                    'Entendi',
                    on_click=fecha_banner
                )
            ]
        )
    
    def aba_logar(e): # aba da parte de login 
        page.clean()
        
        def logar (e): # vai estar no on_click para logar 
            dict_valueslog['usuariolog']= usuariolog.value
            dict_valueslog['senhalog']= senhalog.value
            
            for val in dict_valueslog.values(): # checa se foi tudo preenchido pelo usuário
                if not val: 
                    page.banner.open=True
                    page.update()
                    return
        
            usuarioblog= dict_valueslog['usuariolog']
            senhablog= dict_valueslog['senhalog']
            
            # verificar se ta registrado o usuário
            banco=sqlite3.connect ('banco_projeto.db') 
            cursor=banco.cursor()
        
            try: 
                cursor.execute("SELECT senha FROM usuarios WHERE usuario='{}'".format(usuarioblog))
                senha_bd=cursor.fetchall()
                print(senha_bd[0][0])
            
            except: 
                print('erro')    
        
            if senhablog == senha_bd [0][0]: # se estiver registrado
                
                page.clean()
                def on_dialog_result(e: ft.FilePickerResultEvent):
                    if not e.files:
                        return
                    selected=e.files[0].path
                    source.value=selected
                    page.update()
        
                # INPUT
                input= ft.Text('Insira o arquivo', weight='bold',size=20)
                file_picker=ft.FilePicker(on_result=on_dialog_result)
                page.overlay.append(file_picker)
                page.update()
                botao_File_picker= ft.ElevatedButton(
                    "Selecione o arquivo...",
                    on_click=lambda _: file_picker.pick_files(allow_multiple=False)
                )
                source=ft.Text(value='', style="bodySmall")

                
                page.add(
                    ft.Row(controls=[input]),
                    ft.Row(controls= [botao_File_picker]),
                    ft.Row(controls=[source])

                )
                
            else: # caso nao esteja registrado
                page.add(ft.Text('Dados inseridos incorretos', size=20, weight='bold'))
                
            print(dict_valueslog)
        
        titulo= ft.Text(value='Entre na sua conta', size=20, weight='bold')
        usuariolog=ft.TextField(label='Nome de Usuário', autofocus=True)
        senhalog=ft.TextField(label='Senha', password=True, can_reveal_password=True)
        botao_gerarlog=ft.FilledButton(text='Entrar', on_click=logar)
            
        page.add(ft.Row(controls=[titulo]),
                ft.Row(controls=[usuariolog]),
                ft.Row(controls=[senhalog]),
                ft.Row(controls=[botao_gerarlog]))
                    
        def fecha_banner(e): # banner que aparece caso todos o espaços não sejam preenchidos 
            page.banner.open=False
            page.update()
        
        page.banner=ft.Banner(
        bgcolor=ft.colors.AMBER_100,
        leading=ft.Icon(
                    ft.icons.DANGEROUS_SHARP,                   
                    color=ft.colors.RED_400,
                    size=40
                ),
        content=ft.Text('Todos os campos devem ser preenchidos', color=ft.colors.BLACK),
        actions=[
                    ft.TextButton(
                        'Entendi',
                        on_click=fecha_banner
                    )
                ]
            )
        
    
    titulo1=ft.Text(value='Criptografia de arquivos',size=30,weight='bold')
    titulo= ft.Text(value='Entre na sua conta', size=20, weight='bold')
    novo_cad=ft.Text(value='  Não tem cadastro?')
    botao_cadastro=ft.TextButton(text='Cadastre-se!',on_click=aba_registro)
    botao_logar=ft.FilledButton(text='Login', on_click=aba_logar)

    page.add(ft.Row(controls=[titulo1]),
            ft.Row(controls=[titulo]),
            ft.Row(controls=[botao_logar, novo_cad,botao_cadastro]))
            
ft.app(target=main)