import flet as ft

def main(page: ft.Page):
    # 1. Configuración de la Ventana (Sintaxis actualizada)
    page.title = "App Inventario"
    page.window.width = 380  # CORRECCIÓN: Ahora es window.width
    page.window.height = 700 # CORRECCIÓN: Ahora es window.height
    page.padding = 20
    page.bgcolor = ft.Colors.GREY_50 

    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.Icons.STORE),
        title=ft.Text("Inventario CUN", color=ft.Colors.WHITE),
        bgcolor=ft.Colors.BLUE_900,
        center_title=True,
    )

    # 2. Contenedor Dinámico (El "Cuerpo" de la app que va a cambiar)
    cuerpo = ft.Container(
        content=ft.Text("Pantalla de Inicio", size=30, weight=ft.FontWeight.BOLD),
        alignment=ft.Alignment(0, 0), # CORRECCIÓN INFALIBLE: Coordenadas 0,0 es el Centro
        expand=True # Permite que ocupe todo el espacio sobrante
    )

    # 3. Lógica del Menú (Controlador de Eventos)
    def cambiar_pestana(e):
        indice = e.control.selected_index
        
        if indice == 0:
            cuerpo.content = ft.Text("Pantalla de Inicio", size=30, weight=ft.FontWeight.BOLD)
        elif indice == 1:
            cuerpo.content = ft.Text("Módulo Agregar", size=30, weight=ft.FontWeight.BOLD)
        elif indice == 2:
            cuerpo.content = ft.Text("Módulo Listar", size=30, weight=ft.FontWeight.BOLD)
            
        page.update() # Refresca la pantalla para mostrar el cambio

    # 4. Barra de Navegación Inferior
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Inicio"),
            ft.NavigationBarDestination(icon=ft.Icons.ADD_CIRCLE, label="Agregar"),
            ft.NavigationBarDestination(icon=ft.Icons.LIST_ALT, label="Listar"),
        ],
        on_change=cambiar_pestana, # Enlazamos el evento a nuestra función
        selected_index=0 # Por defecto arranca en la pestaña 0 (Inicio)
    )

    # 5. Renderizar en pantalla
    page.add(cuerpo)

# Iniciar la aplicación
ft.run(main)