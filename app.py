import flet as ft

class Painel(ft.UserControl):
    def __init__(self,n,w,h,br,trans,ac):
        super().__init__()
        self.n=n
        self.w=w
        self.h=h
        self.br=br
        self.trans=trans
        self.ac=ac
    
    def build(self):

        self.c1 = ft.Container(
            ft.Text(self.n, style=ft.TextThemeStyle.TITLE_SMALL,color=ft.colors.WHITE),
            alignment=ft.alignment.center,
            width=self.w,
            height=self.h,
            border_radius=self.br,
            gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=['#171022','#5C2372','#1D0912'])
        )

        self.c2 = ft.Container(
            ft.Text(self.n, style=ft.TextThemeStyle.TITLE_SMALL,color=ft.colors.WHITE),
            alignment=ft.alignment.center,
            width=self.w,
            height=self.h,
            border_radius=self.br,
            gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=['#171022','#735924','#1D0912'])
        )

        self.sw = ft.AnimatedSwitcher(
            self.c1,
            transition=self.trans,
            duration=1000,
            reverse_duration=1000,
            switch_in_curve=self.ac,
            switch_out_curve=self.ac,
        )

        def f_(e):
            self.sw.content = self.c2 if self.sw.content == self.c1 else self.c1
            self.sw.update()

        return ft.Row([self.sw,ft.ElevatedButton(self.n, on_click=f_)])  
    
def main(page:ft.Page):
    page.scroll = True

    largura = 250
    altura = 50
    borda_redonda = 12

    page.add(Painel(n='BOUNCE IN ROTATION',w=largura,h=altura,br=borda_redonda,trans=ft.AnimatedSwitcherTransition.ROTATION,ac=ft.AnimationCurve.BOUNCE_IN),
             Painel(n='BOUNCE IN SCALE',w=largura,h=altura,br=borda_redonda,trans=ft.AnimatedSwitcherTransition.SCALE,ac=ft.AnimationCurve.BOUNCE_IN),
             Painel(n='BOUNCE IN FADE',w=largura,h=altura,br=borda_redonda,trans=ft.AnimatedSwitcherTransition.FADE,ac=ft.AnimationCurve.BOUNCE_IN),
             ft.Divider(),
             Painel(n='BOUNCE IN OUT ROTATION',w=largura,h=altura,br=borda_redonda,trans=ft.AnimatedSwitcherTransition.ROTATION,ac=ft.AnimationCurve.BOUNCE_IN_OUT),
             Painel(n='BOUNCE IN OUT SCALE',w=largura,h=altura,br=borda_redonda,trans=ft.AnimatedSwitcherTransition.SCALE,ac=ft.AnimationCurve.BOUNCE_IN_OUT),
             Painel(n='BOUNCE IN OUT FADE',w=largura,h=altura,br=borda_redonda,trans=ft.AnimatedSwitcherTransition.FADE,ac=ft.AnimationCurve.BOUNCE_IN_OUT),
             ft.Divider(),
             Painel(n='BOUNCE OUT ROTATION',w=largura,h=altura,br=borda_redonda,trans=ft.AnimatedSwitcherTransition.ROTATION,ac=ft.AnimationCurve.BOUNCE_OUT),
             Painel(n='BOUNCE OUT SCALE',w=largura,h=altura,br=borda_redonda,trans=ft.AnimatedSwitcherTransition.SCALE,ac=ft.AnimationCurve.BOUNCE_OUT),
             Painel(n='BOUNCE OUT FADE',w=largura,h=altura,br=borda_redonda,trans=ft.AnimatedSwitcherTransition.FADE,ac=ft.AnimationCurve.BOUNCE_OUT),
             ft.Divider(),
             Painel(n='DECELERATE ROTATION',w=largura,h=altura,br=borda_redonda,trans=ft.AnimatedSwitcherTransition.ROTATION,ac=ft.AnimationCurve.DECELERATE),
             Painel(n='DECELERATE SCALE',w=largura,h=altura,br=borda_redonda,trans=ft.AnimatedSwitcherTransition.SCALE,ac=ft.AnimationCurve.DECELERATE),
             Painel(n='DECELERATE FADE',w=largura,h=altura,br=borda_redonda,trans=ft.AnimatedSwitcherTransition.FADE,ac=ft.AnimationCurve.DECELERATE),
             ft.Divider(),
             Painel(n='EASE ROTATION',w=largura,h=altura,br=borda_redonda,trans=ft.AnimatedSwitcherTransition.ROTATION,ac=ft.AnimationCurve.EASE),
             Painel(n='EASE SCALE',w=largura,h=altura,br=borda_redonda,trans=ft.AnimatedSwitcherTransition.SCALE,ac=ft.AnimationCurve.EASE),
             Painel(n='EASE FADE',w=largura,h=altura,br=borda_redonda,trans=ft.AnimatedSwitcherTransition.FADE,ac=ft.AnimationCurve.EASE),
             ft.Divider(),
             Painel(n='EASE IN ROTATION',w=largura,h=altura,br=borda_redonda,trans=ft.AnimatedSwitcherTransition.ROTATION,ac=ft.AnimationCurve.EASE_IN),
             Painel(n='EASE IN SCALE',w=largura,h=altura,br=borda_redonda,trans=ft.AnimatedSwitcherTransition.SCALE,ac=ft.AnimationCurve.EASE_IN),
             Painel(n='EASE IN FADE',w=largura,h=altura,br=borda_redonda,trans=ft.AnimatedSwitcherTransition.FADE,ac=ft.AnimationCurve.EASE_IN),
             ft.Divider(),
             Painel(n='EASE IN BACK ROTATION',w=largura,h=altura,br=borda_redonda,trans=ft.AnimatedSwitcherTransition.ROTATION,ac=ft.AnimationCurve.EASE_IN_BACK),
             Painel(n='EASE IN BACK SCALE',w=largura,h=altura,br=borda_redonda,trans=ft.AnimatedSwitcherTransition.SCALE,ac=ft.AnimationCurve.EASE_IN_BACK),
             Painel(n='EASE IN BACK FADE',w=largura,h=altura,br=borda_redonda,trans=ft.AnimatedSwitcherTransition.FADE,ac=ft.AnimationCurve.EASE_IN_BACK),
             ft.Divider(),
             Painel(n='EASE IN CIRC ROTATION',w=largura,h=altura,br=borda_redonda,trans=ft.AnimatedSwitcherTransition.ROTATION,ac=ft.AnimationCurve.EASE_IN_CIRC),
             Painel(n='EASE IN CIRC SCALE',w=largura,h=altura,br=borda_redonda,trans=ft.AnimatedSwitcherTransition.SCALE,ac=ft.AnimationCurve.EASE_IN_CIRC),
             Painel(n='EASE IN CIRC FADE',w=largura,h=altura,br=borda_redonda,trans=ft.AnimatedSwitcherTransition.FADE,ac=ft.AnimationCurve.EASE_IN_CIRC))

ft.app(target=main)
