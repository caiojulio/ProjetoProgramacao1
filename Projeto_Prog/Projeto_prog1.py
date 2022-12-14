import flet as ft
import sqlite3
from flet import AppBar,colors, Text, Page,Row,Container, margin, Card, Column,border_radius,padding,border, margin,LinearGradient, Icon,icons, Image,column, Alignment,alignment, RadialGradient, View, border,  FilledButton, ElevatedButton,UserControl,IconButton,TextField,SnackBar

def main(page: ft.Page):
    page.title = "pag_inicio"
    page.window_width=600
    page.window_height=700
    page.title= "Criptografia de arquivo"
    
    def GradienteGertaor(start,end):
        ColorGrandient=LinearGradient(
            begin=alignment.bottom_left,
            end=alignment.top_right,
            colors=[
                start,
                end,
            ],
        )
        return ColorGrandient
    
    def logar (usuariolog,senhalog): # vai estar no on_click para logar 
        dadoslog={
            'usuariolog':usuariolog,
            'senhalog': senhalog,
        }
        dadoslog['usuario']= usuariolog
        dadoslog['senha']= senhalog
            
        for val in dadoslog.values(): # checa se foi tudo preenchido pelo usuário
            if not val: 
                page.banner.open=True
                page.update()
                return
        
        usuarioblog= dadoslog['usuariolog']
        senhablog= dadoslog['senhalog']
            
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
            page.views.append(ft.Text('Dados inseridos incorretos', size=20, weight='bold'))
                
        print(dadoslog)
        

    def registrar(usuario,senha): #registro de login
        dados={
            'usuario':'',
            'senha': '',
        }
        dados['usuario']= usuario
        dados['senha']= senha
        for val in dados.values(): # checa se foi tudo preenchido pelo usuário
            if not val: 
                page.banner.open=True
                page.update()
                return
        page.add(ft.Text('Registrado',size=20,weight='bold',color='green'))

        usuariob= dados['usuario']
        senhab= dados['senha']

        banco=sqlite3.connect ('banco_projeto.db') # coloca o que foi digitado no banco de dados
        cursor=banco.cursor()
        try: # ve se o usuário ja esta registrado, para exitar dois iguais
                cursor.execute("SELECT usuario FROM usuarios WHERE usuario='{}'".format(usuariob))
                usuario_bd=cursor.fetchall()
                print(usuario_bd[0][0])
                page.add(ft.Text('Usuario ja registrado',size=20,weight='bold'))
                
        except:
            cursor.execute("INSERT INTO usuarios VALUES (NULL,'"+usuariob+"','"+senhab+"' )")
            banco.commit()
            page.add(ft.Text('Registrado',size=20,weight='bold',color='green'))
            print (dados)
    
    def excluir(e,id): 
        dict_valuesre= {
        'id': '',
        }

        dict_valuesre['id']= id
        
        for val in dict_valuesre.values(): # checa se foi tudo preenchido pelo usuário
                if not val: 
                    page.banner.open=True
                    page.update()
                    return
        
        idb= dict_valuesre['id']

        banco=sqlite3.connect ('banco_projeto.db') # coloca o que foi digitado no banco de dados
        cursor=banco.cursor()
        try:
            cursor.execute("DELETE FROM usuarios WHERE id ={}".format(idb))
            banco.commit()
            page.add(ft.Text('Usuário com id {} removido '.format(idb),size=20,weight='bold'))
        except: 
            page.add(ft.Text('Id inexistente',size=20,weight='bold'))
        


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
        ])


       
    
    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                    "/inicio",
                    horizontal_alignment='center', vertical_alignment='center',
                    controls=[Column(alignment='center', 
                    controls=[Card(
                            elevation=15,
                            content=Container(
                                width=550,
                                height=550,
                                padding=padding.all(30),
                                gradient=GradienteGertaor('#1b2631','#1a5276'),
                                border_radius=border_radius.all(20),
                                content=Column(
                                    horizontal_alignment='center',
                                    alignment='start',
                                    controls=[
                                        ft.Text(value='Criptografia de arquivos',
                                            size=32,
                                            weight='w700',
                                            text_align='center',
                                        ),
                                            Row(
                                                alignment='center',
                                                spacing=10,
                                                controls=[
                                                    FilledButton(content=Text("Login",
                                                    weight='w700',
                                                    ),
                                                    width=150,
                                                    height=40,
                                                    on_click=lambda __:page.go('/login'),
                                                ),
                                                FilledButton(content=Text("Cadastre-se",
                                                    weight='w700',
                                                    ),
                                                    width=150,
                                                    height=40,
                                                    on_click=lambda __:page.go('/registro'),
                                                ),
                                                FilledButton(
                                                    content=Text(
                                                        'Remover Usuario',
                                                        weight='w700'
                                                    ),
                                                    width=150,
                                                    height=40,
                                                    on_click=lambda __:page.go('/remover'
                                                    ),
                                                ), 
                                            ],
                                            ),
                                        ],
                                    )          
                                ),
                                )
                            ],
                        )
                    ]     
            
                )         
            )
        if page.route == "/login":
            usuario=TextField(label='Usuario', border='underline',width=320,text_size=16)
            senha=TextField(label='Senha', border='underline',width=320,text_size=16, password=True,can_reveal_password=True)

            page.views.append(View("/login",
            horizontal_alignment='center', vertical_alignment='center',
            controls=[Column(alignment='center', 
            controls=[Card(
                        elevation=15,
                        content=Container(
                            width=550,
                            height=550,
                            padding=padding.all(30),
                            gradient=GradienteGertaor('#1f2937','#111827'),
                            border_radius=border_radius.all(12),
                            content=Column(
                                horizontal_alignment='center',
                                alignment='start',
                                controls=[
                                    ft.Text(value='Criptografia de arquivos',
                                        size=32,
                                        weight='bold',
                                        text_align='center',
                                    ),
                                    ft.Text(value='Entre com seu usuario e senha',size=14,weight='bold',text_align='center',color='#64748b',),
                                        Container(padding=padding.only(bottom=20)),
                                        usuario,
                                        Container(padding=padding.only(bottom=10)),
                                        senha,
                                        Container(padding=padding.only(bottom=20)),
                                        Row(
                                            alignment='center',
                                            spacing=20,
                                            controls=[
                                                FilledButton(content=Text("Login",
                                                weight='w700',
                                                ),
                                                width=160,
                                                height=40,
                                                on_click=lambda e:logar(
                                                    usuario.value,
                                                    senha.value,
                                                ),
                                            ),
                                            FilledButton(
                                                content=Text(
                                                    'Voltar',
                                                    weight='w700'
                                                ),
                                                width=160,
                                                height=40,
                                                on_click=lambda __:page.go('/inicio'
                                                ),
                                              ), 
                                           ],
                                         ),
                                     ],
                                 )          
                               ),
                            )
                         ],
                     )
                ]     
        
            )         
        )



        if page.route == "/registro":
            usuario=TextField(label='Usuario', border='underline',width=320,text_size=16)
            senha=TextField(label='Senha', border='underline',width=320,text_size=16, password=True,can_reveal_password=True)

            page.views.append(View("/registro",
            horizontal_alignment='center', vertical_alignment='center',
            controls=[Column(alignment='center', 
            controls=[Card(
                        elevation=15,
                        content=Container(
                            width=550,
                            height=550,
                            padding=padding.all(30),
                            gradient=GradienteGertaor('#2f2937','#251867'),
                            border_radius=border_radius.all(12),
                            content=Column(
                                horizontal_alignment='center',
                                alignment='start',
                                controls=[
                                    ft.Text(value='Criptografia de arquivos',
                                        size=32,
                                        weight='bold',
                                        text_align='center',
                                    ),
                                    ft.Text(value='Registro De Usuario',size=14,weight='bold',text_align='center',color='#64748b',),
                                        Container(padding=padding.only(bottom=20)),
                                        usuario,
                                        Container(padding=padding.only(bottom=10)),
                                        senha,
                                        Container(padding=padding.only(bottom=20)),
                                        Row(
                                            alignment='center',
                                            spacing=20,
                                            controls=[
                                                FilledButton(content=Text("Cadastrar",
                                                weight='w700',
                                                ),
                                                width=160,
                                                height=40,
                                                on_click=lambda e:registrar(
                                                    usuario.value,
                                                    senha.value,
                                                ),
                                            ),
                                            FilledButton(
                                                content=Text(
                                                    'Voltar',
                                                    weight='w700'
                                                ),
                                                width=160,
                                                height=40,
                                                on_click=lambda __:page.go('/inicio'
                                                ),
                                              ), 
                                           ],
                                         ),
                                     ],
                                 )          
                               ),
                            )
                         ],
                     )
                ]     
        
            )         
        )   

        if page.route == "/remover":
            id=TextField(label='Id do usuario', border='underline',width=320,text_size=14)
           
            page.views.append(View("/Remoção",
            horizontal_alignment='center', vertical_alignment='center',
            controls=[Column(alignment='center', 
            controls=[Card(
                        elevation=15,
                        content=Container(
                            width=550,
                            height=550,
                            padding=padding.all(30),
                            gradient=GradienteGertaor('#424949','#641e16'),
                            border_radius=border_radius.all(12),
                            content=Column(
                                horizontal_alignment='center',
                                alignment='start',
                                controls=[
                                    ft.Text(value='Criptografia de arquivos',
                                        size=32,
                                        weight='bold',
                                        text_align='center',
                                    ),
                                    ft.Text(value='Remoção de usuario',size=14,weight='bold',text_align='center',color='#64748b',),
                                        Container(padding=padding.only(bottom=20)),
                                        id,
                                        Container(padding=padding.only(bottom=20)),
                                        Row(
                                            alignment='center',
                                            spacing=20,
                                            controls=[
                                                FilledButton(content=Text("Remover",
                                                weight='w700',
                                                ),
                                                width=160,
                                                height=40,
                                                on_click=lambda e:excluir(
                                                    id.value
                                    
                                                ),
                                            ),
                                            FilledButton(
                                                content=Text(
                                                    'Voltar',
                                                    weight='w700'
                                                ),
                                                width=160,
                                                height=40,
                                                on_click=lambda __:page.go('/inicio'
                                                ),
                                              ), 
                                           ],
                                         ),
                                     ],
                                 )          
                               ),
                            )
                         ],
                     )
                ]     
        
            )         
        )   
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)