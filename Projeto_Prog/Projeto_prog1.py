import sqlite3
import flet as ft

#banco=sqlite3.connect ('banco_projeto.db') # para criar o banco de dados
#cursor=banco.cursor()
#cursor.execute("CREATE TABLE usuarios (email text, usuario text, senha text) ")

def main(page):  # funçao principal do flet
    page.title= "Criptografia de arquivo"
    
    dict_values= {
        'usuario': '',
        'email': '',
        'senha': ''
    }
    def gera_registro(e): # função que vai estar no on_click
        dict_values['usuario']= usuario.value 
        dict_values['email']= email.value 
        dict_values['senha']= senha.value
        
        for val in dict_values.values (): # checa se foi tudo preenchido pelo usuário
            if not val: 
                page.banner.open=True
                page.update()
                return
        page.add(ft.Text('Registrado'))

        usuariob= dict_values['usuario']
        emailb= dict_values['email']
        senhab= dict_values['senha']

        banco=sqlite3.connect ('banco_projeto.db') # coloca o que foi digitado no banco de dados
        cursor=banco.cursor()
        cursor.execute("INSERT INTO usuarios VALUES ('"+emailb+"','"+usuariob+"','"+senhab+"' )")
        banco.commit()
        print (dict_values)
    
    def fecha_banner(e): # banner que aparece caso todos o espaços não foram preenchidos 
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

    titulo= ft.Text(value='Registrar Usuário', size=20, weight='bold')
    usuario= ft.TextField(label='Nome de Usuário',)
    email=ft.TextField(label='Email', autofocus=True)
    senha=ft.TextField(label='Senha',password=True, can_reveal_password=True)
    

    botao_gerar=ft.FilledButton(text='Registrar', on_click=gera_registro)

    page.add(
        ft.Row(
            controls=[titulo]
        ),
        ft.Row(
            controls=[email]
        ),
        ft.Row(
            controls=[usuario]
        ),
        ft.Row(
            controls=[senha]
        ),
        ft.Row(
            controls=[botao_gerar]
        )
    )

ft.app(target=main)