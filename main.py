import flet as sh
def Natiq(page: sh.Page):
    page.horizontal_alignment = sh.CrossAxisAlignment.CENTER
    sh.Row.alignment
    page.title = "Chat Group"
    page.bgcolor = "red"
    page.bgcolor = "black"
    inp = None
    def send(e):
        global inp
        data = inp.value 
        inp.value = ""
        page.add(sh.Text(f"HP: {data}"))
    def delete(event):
        page.clean()
        content()
    def content():
        global inp
        inp = sh.TextField(label="Mesaj yaz...")
        btn = sh.TextButton(text="Gonder")
        delete_btn = sh.TextButton("DELETE")
        page.add(inp)
        page.add(btn)
        page.add(delete_btn)
        btn.on_click = send
        delete_btn.on_click = delete   
    content()
sh.app(Natiq)