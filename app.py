import flet as ft

def main(page: ft.Page):
    page.scroll = True

    ### CONTAINERS ### 
    bounce_in_rotation_1 = ft.Container(
        ft.Text("BOUNCE IN\nROTATION", style=ft.TextThemeStyle.TITLE_SMALL,color=ft.colors.WHITE),
        alignment=ft.alignment.center,
        width=150,
        height=150,
        border_radius=24,
        gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=['#171022','#5C2372','#1D0912'])
    )
    bounce_in_rotation_2 = ft.Container(
        ft.Text("BOUNCE IN\nROTATION", style=ft.TextThemeStyle.TITLE_SMALL,color=ft.colors.WHITE),
        alignment=ft.alignment.center,
        width=150,
        height=150,
        border_radius=24,
        gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=['#171022','#735924','#1D0912'])        
    )

    bounce_in_scale_1 = ft.Container(
        ft.Text("BOUNCE IN\nSCALE", style=ft.TextThemeStyle.TITLE_SMALL,color=ft.colors.WHITE),
        alignment=ft.alignment.center,
        width=150,
        height=150,
        border_radius=24,
        gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=['#171022','#5C2372','#1D0912'])
    )
    bounce_in_scale_2 = ft.Container(
        ft.Text("BOUNCE IN\nSCALE", style=ft.TextThemeStyle.TITLE_SMALL,color=ft.colors.WHITE),
        alignment=ft.alignment.center,
        width=150,
        height=150,
        border_radius=24,
        gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=['#171022','#735924','#1D0912'])  
    )

    bounce_in_fade_1 = ft.Container(
        ft.Text("BOUNCE IN\nFADE", style=ft.TextThemeStyle.TITLE_SMALL,color=ft.colors.WHITE),
        alignment=ft.alignment.center,
        width=150,
        height=150,
        border_radius=24,
        gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=['#171022','#5C2372','#1D0912'])
    )
    bounce_in_fade_2 = ft.Container(
        ft.Text("BOUNCE IN\nFADE", style=ft.TextThemeStyle.TITLE_SMALL,color=ft.colors.WHITE),
        alignment=ft.alignment.center,
        width=150,
        height=150,
        border_radius=24,
        gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=['#171022','#735924','#1D0912'])  
    )

    bounce_in_out_rotation_1 = ft.Container(
    ft.Text("BOUNCE IN OUT\nROTATION", style=ft.TextThemeStyle.TITLE_SMALL,color=ft.colors.WHITE),
    alignment=ft.alignment.center,
    width=150,
    height=150,
    border_radius=24,
    gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=['#171022','#5C2372','#1D0912'])
    )
    bounce_in_out_rotation_2 = ft.Container(
        ft.Text("BOUNCE IN OUT\nROTATION", style=ft.TextThemeStyle.TITLE_SMALL,color=ft.colors.WHITE),
        alignment=ft.alignment.center,
        width=150,
        height=150,
        border_radius=24,
        gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=['#171022','#735924','#1D0912'])        
    )

    bounce_in_out_scale_1 = ft.Container(
        ft.Text("BOUNCE IN OUT\nSCALE", style=ft.TextThemeStyle.TITLE_SMALL,color=ft.colors.WHITE),
        alignment=ft.alignment.center,
        width=150,
        height=150,
        border_radius=24,
        gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=['#171022','#5C2372','#1D0912'])
    )
    bounce_in_out_scale_2 = ft.Container(
        ft.Text("BOUNCE IN OUT\nSCALE", style=ft.TextThemeStyle.TITLE_SMALL,color=ft.colors.WHITE),
        alignment=ft.alignment.center,
        width=150,
        height=150,
        border_radius=24,
        gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=['#171022','#735924','#1D0912'])  
    )

    bounce_in_out_fade_1 = ft.Container(
        ft.Text("BOUNCE IN OUT\nFADE", style=ft.TextThemeStyle.TITLE_SMALL,color=ft.colors.WHITE),
        alignment=ft.alignment.center,
        width=150,
        height=150,
        border_radius=24,
        gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=['#171022','#5C2372','#1D0912'])
    )
    bounce_in_out_fade_2 = ft.Container(
        ft.Text("BOUNCE IN OUT\nFADE", style=ft.TextThemeStyle.TITLE_SMALL,color=ft.colors.WHITE),
        alignment=ft.alignment.center,
        width=150,
        height=150,
        border_radius=24,
        gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=['#171022','#735924','#1D0912'])  
    )

    bounce_out_rotation_1 = ft.Container(
    ft.Text("OUNCE OUT\nROTATION", style=ft.TextThemeStyle.TITLE_SMALL,color=ft.colors.WHITE),
    alignment=ft.alignment.center,
    width=150,
    height=150,
    border_radius=24,
    gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=['#171022','#5C2372','#1D0912'])
    )
    bounce_out_rotation_2 = ft.Container(
        ft.Text("OUNCE OUT\nROTATION", style=ft.TextThemeStyle.TITLE_SMALL,color=ft.colors.WHITE),
        alignment=ft.alignment.center,
        width=150,
        height=150,
        border_radius=24,
        gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=['#171022','#735924','#1D0912'])        
    )

    bounce_out_scale_1 = ft.Container(
        ft.Text("OUNCE OUT\nSCALE", style=ft.TextThemeStyle.TITLE_SMALL,color=ft.colors.WHITE),
        alignment=ft.alignment.center,
        width=150,
        height=150,
        border_radius=24,
        gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=['#171022','#5C2372','#1D0912'])
    )
    bounce_out_scale_2 = ft.Container(
        ft.Text("OUNCE OUT\nSCALE", style=ft.TextThemeStyle.TITLE_SMALL,color=ft.colors.WHITE),
        alignment=ft.alignment.center,
        width=150,
        height=150,
        border_radius=24,
        gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=['#171022','#735924','#1D0912'])  
    )

    bounce_out_fade_1 = ft.Container(
        ft.Text("OUNCE OUT\nFADE", style=ft.TextThemeStyle.TITLE_SMALL,color=ft.colors.WHITE),
        alignment=ft.alignment.center,
        width=150,
        height=150,
        border_radius=24,
        gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=['#171022','#5C2372','#1D0912'])
    )
    bounce_out_fade_2 = ft.Container(
        ft.Text("OUNCE OUT\nFADE", style=ft.TextThemeStyle.TITLE_SMALL,color=ft.colors.WHITE),
        alignment=ft.alignment.center,
        width=150,
        height=150,
        border_radius=24,
        gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=['#171022','#735924','#1D0912'])  
    )

    decelerate_rotation_1 = ft.Container(
        ft.Text("DECELERATE\nROTATION", style=ft.TextThemeStyle.TITLE_SMALL,color=ft.colors.WHITE),
        alignment=ft.alignment.center,
        width=150,
        height=150,
        border_radius=24,
        gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=['#171022','#5C2372','#1D0912'])
    )
    decelerate_rotation_2 = ft.Container(
        ft.Text("DECELERATE\nROTATION", style=ft.TextThemeStyle.TITLE_SMALL,color=ft.colors.WHITE),
        alignment=ft.alignment.center,
        width=150,
        height=150,
        border_radius=24,
        gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=['#171022','#735924','#1D0912'])  
    )  
    decelerate_scale_1 = ft.Container(
        ft.Text("DECELERATE\nSCALE", style=ft.TextThemeStyle.TITLE_SMALL,color=ft.colors.WHITE),
        alignment=ft.alignment.center,
        width=150,
        height=150,
        border_radius=24,
        gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=['#171022','#5C2372','#1D0912'])
    )
    decelerate_scale_2 = ft.Container(
        ft.Text("DECELERATE\nSCALE", style=ft.TextThemeStyle.TITLE_SMALL,color=ft.colors.WHITE),
        alignment=ft.alignment.center,
        width=150,
        height=150,
        border_radius=24,
        gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=['#171022','#735924','#1D0912'])  
    )
    decelerate_fade_1 = ft.Container(
        ft.Text("DECELERATE\nFADE", style=ft.TextThemeStyle.TITLE_SMALL,color=ft.colors.WHITE),
        alignment=ft.alignment.center,
        width=150,
        height=150,
        border_radius=24,
        gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=['#171022','#5C2372','#1D0912'])
    )
    decelerate_fade_2 = ft.Container(
        ft.Text("DECELERATE\nFADE", style=ft.TextThemeStyle.TITLE_SMALL,color=ft.colors.WHITE),
        alignment=ft.alignment.center,
        width=150,
        height=150,
        border_radius=24,
        gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=['#171022','#735924','#1D0912'])  
    )  

    ease_rotation_1 = ft.Container(
        ft.Text("EASE\nROTATION", style=ft.TextThemeStyle.TITLE_SMALL,color=ft.colors.WHITE),
        alignment=ft.alignment.center,
        width=150,
        height=150,
        border_radius=24,
        gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=['#171022','#5C2372','#1D0912'])
    )
    ease_rotation_2 = ft.Container(
        ft.Text("EASE\nROTATION", style=ft.TextThemeStyle.TITLE_SMALL,color=ft.colors.WHITE),
        alignment=ft.alignment.center,
        width=150,
        height=150,
        border_radius=24,
        gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=['#171022','#735924','#1D0912'])        
    )

    ease_scale_1 = ft.Container(
        ft.Text("EASE\nSCALE", style=ft.TextThemeStyle.TITLE_SMALL,color=ft.colors.WHITE),
        alignment=ft.alignment.center,
        width=150,
        height=150,
        border_radius=24,
        gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=['#171022','#5C2372','#1D0912'])
    )
    ease_scale_2 = ft.Container(
        ft.Text("EASE\nSCALE", style=ft.TextThemeStyle.TITLE_SMALL,color=ft.colors.WHITE),
        alignment=ft.alignment.center,
        width=150,
        height=150,
        border_radius=24,
        gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=['#171022','#735924','#1D0912'])  
    )

    ease_fade_1 = ft.Container(
        ft.Text("EASE\nFADE", style=ft.TextThemeStyle.TITLE_SMALL,color=ft.colors.WHITE),
        alignment=ft.alignment.center,
        width=150,
        height=150,
        border_radius=24,
        gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=['#171022','#5C2372','#1D0912'])
    )
    ease_fade_2 = ft.Container(
        ft.Text("EASE\nFADE", style=ft.TextThemeStyle.TITLE_SMALL,color=ft.colors.WHITE),
        alignment=ft.alignment.center,
        width=150,
        height=150,
        border_radius=24,
        gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=['#171022','#735924','#1D0912'])  
    )

    ease_in_rotation_1 = ft.Container(
        ft.Text("Bounce In\nROTATION", style=ft.TextThemeStyle.TITLE_SMALL,color=ft.colors.WHITE),
        alignment=ft.alignment.center,
        width=150,
        height=150,
        border_radius=24,
        gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=['#171022','#5C2372','#1D0912'])
    )
    ease_in_rotation_2 = ft.Container(
        ft.Text("Bounce In\nROTATION", style=ft.TextThemeStyle.TITLE_SMALL,color=ft.colors.WHITE),
        alignment=ft.alignment.center,
        width=150,
        height=150,
        border_radius=24,
        gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=['#171022','#735924','#1D0912'])        
    )

    ease_in_scale_1 = ft.Container(
        ft.Text("Bounce In\nSCALE", style=ft.TextThemeStyle.TITLE_SMALL,color=ft.colors.WHITE),
        alignment=ft.alignment.center,
        width=150,
        height=150,
        border_radius=24,
        gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=['#171022','#5C2372','#1D0912'])
    )
    ease_in_scale_2 = ft.Container(
        ft.Text("Bounce In\nSCALE", style=ft.TextThemeStyle.TITLE_SMALL,color=ft.colors.WHITE),
        alignment=ft.alignment.center,
        width=150,
        height=150,
        border_radius=24,
        gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=['#171022','#735924','#1D0912'])  
    )

    ease_in_fade_1 = ft.Container(
        ft.Text("Bounce In\nFADE", style=ft.TextThemeStyle.TITLE_SMALL,color=ft.colors.WHITE),
        alignment=ft.alignment.center,
        width=150,
        height=150,
        border_radius=24,
        gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=['#171022','#5C2372','#1D0912'])
    )
    ease_in_fade_2 = ft.Container(
        ft.Text("Bounce In\nFADE", style=ft.TextThemeStyle.TITLE_SMALL,color=ft.colors.WHITE),
        alignment=ft.alignment.center,
        width=150,
        height=150,
        border_radius=24,
        gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=['#171022','#735924','#1D0912'])  
    )

    ease_in_back_rotation_1 = ft.Container(
        ft.Text("BOUNCE IN BACK\nROTATION", style=ft.TextThemeStyle.TITLE_SMALL,color=ft.colors.WHITE),
        alignment=ft.alignment.center,
        width=150,
        height=150,
        border_radius=24,
        gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=['#171022','#5C2372','#1D0912'])
    )
    ease_in_back_rotation_2 = ft.Container(
        ft.Text("BOUNCE IN BACK\nROTATION", style=ft.TextThemeStyle.TITLE_SMALL,color=ft.colors.WHITE),
        alignment=ft.alignment.center,
        width=150,
        height=150,
        border_radius=24,
        gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=['#171022','#735924','#1D0912'])        
    )

    ease_in_back_scale_1 = ft.Container(
        ft.Text("BOUNCE IN BACK\nSCALE", style=ft.TextThemeStyle.TITLE_SMALL,color=ft.colors.WHITE),
        alignment=ft.alignment.center,
        width=150,
        height=150,
        border_radius=24,
        gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=['#171022','#5C2372','#1D0912'])
    )
    ease_in_back_scale_2 = ft.Container(
        ft.Text("BOUNCE IN BACK\nSCALE", style=ft.TextThemeStyle.TITLE_SMALL,color=ft.colors.WHITE),
        alignment=ft.alignment.center,
        width=150,
        height=150,
        border_radius=24,
        gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=['#171022','#735924','#1D0912'])  
    )

    ease_in_back_fade_1 = ft.Container(
        ft.Text("BOUNCE IN BACK\nFADE", style=ft.TextThemeStyle.TITLE_SMALL,color=ft.colors.WHITE),
        alignment=ft.alignment.center,
        width=150,
        height=150,
        border_radius=24,
        gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=['#171022','#5C2372','#1D0912'])
    )
    ease_in_back_fade_2 = ft.Container(
        ft.Text("BOUNCE IN BACK\nFADE", style=ft.TextThemeStyle.TITLE_SMALL,color=ft.colors.WHITE),
        alignment=ft.alignment.center,
        width=150,
        height=150,
        border_radius=24,
        gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=['#171022','#735924','#1D0912'])  
    )

    ### SWITCHES ###
    bounce_in_rotation_sw = ft.AnimatedSwitcher(
        bounce_in_rotation_1,
        transition=ft.AnimatedSwitcherTransition.ROTATION,
        duration=1000,
        reverse_duration=1000,
        switch_in_curve=ft.AnimationCurve.BOUNCE_IN,
        switch_out_curve=ft.AnimationCurve.BOUNCE_IN,
    )
    bounce_in_scale_sw = ft.AnimatedSwitcher(
        bounce_in_scale_1,
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=1000,
        reverse_duration=1000,
        switch_in_curve=ft.AnimationCurve.BOUNCE_IN,
        switch_out_curve=ft.AnimationCurve.BOUNCE_IN,
    )
    bounce_in_fade_sw = ft.AnimatedSwitcher(
        bounce_in_fade_1,
        transition=ft.AnimatedSwitcherTransition.FADE,
        duration=1000,
        reverse_duration=1000,
        switch_in_curve=ft.AnimationCurve.BOUNCE_IN,
        switch_out_curve=ft.AnimationCurve.BOUNCE_IN,
    )

    bounce_in_out_rotation_sw = ft.AnimatedSwitcher(
        bounce_in_out_rotation_1,
        transition=ft.AnimatedSwitcherTransition.ROTATION,
        duration=1000,
        reverse_duration=1000,
        switch_in_curve=ft.AnimationCurve.BOUNCE_IN_OUT,
        switch_out_curve=ft.AnimationCurve.BOUNCE_IN_OUT,
    )
    bounce_in_out_scale_sw = ft.AnimatedSwitcher(
        bounce_in_out_scale_1,
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=1000,
        reverse_duration=1000,
        switch_in_curve=ft.AnimationCurve.BOUNCE_IN_OUT,
        switch_out_curve=ft.AnimationCurve.BOUNCE_IN_OUT,
    )
    bounce_in_out_fade_sw = ft.AnimatedSwitcher(
        bounce_in_out_fade_1,
        transition=ft.AnimatedSwitcherTransition.FADE,
        duration=1000,
        reverse_duration=1000,
        switch_in_curve=ft.AnimationCurve.BOUNCE_IN_OUT,
        switch_out_curve=ft.AnimationCurve.BOUNCE_IN_OUT,
    )

    bounce_out_rotation_sw = ft.AnimatedSwitcher(
        bounce_out_rotation_1,
        transition=ft.AnimatedSwitcherTransition.ROTATION,
        duration=1000,
        reverse_duration=1000,
        switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,
        switch_out_curve=ft.AnimationCurve.BOUNCE_OUT,
    )
    bounce_out_scale_sw = ft.AnimatedSwitcher(
        bounce_out_scale_1,
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=1000,
        reverse_duration=1000,
        switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,
        switch_out_curve=ft.AnimationCurve.BOUNCE_OUT,
    )
    bounce_out_fade_sw = ft.AnimatedSwitcher(
        bounce_out_fade_1,
        transition=ft.AnimatedSwitcherTransition.FADE,
        duration=1000,
        reverse_duration=1000,
        switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,
        switch_out_curve=ft.AnimationCurve.BOUNCE_OUT,
    )

    decelerate_rotation_sw = ft.AnimatedSwitcher(
        decelerate_rotation_1,
        transition=ft.AnimatedSwitcherTransition.ROTATION,
        duration=1000,
        reverse_duration=1000,
        switch_in_curve=ft.AnimationCurve.DECELERATE,
        switch_out_curve=ft.AnimationCurve.DECELERATE,
    )
    decelerate_scale_sw = ft.AnimatedSwitcher(
        decelerate_scale_1,
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=1000,
        reverse_duration=1000,
        switch_in_curve=ft.AnimationCurve.DECELERATE,
        switch_out_curve=ft.AnimationCurve.DECELERATE,
    )
    decelerate_fade_sw = ft.AnimatedSwitcher(
        decelerate_fade_1,
        transition=ft.AnimatedSwitcherTransition.FADE,
        duration=1000,
        reverse_duration=1000,
        switch_in_curve=ft.AnimationCurve.DECELERATE,
        switch_out_curve=ft.AnimationCurve.DECELERATE,
    )

    ease_rotation_sw = ft.AnimatedSwitcher(
        ease_rotation_1,
        transition=ft.AnimatedSwitcherTransition.ROTATION,
        duration=1000,
        reverse_duration=1000,
        switch_in_curve=ft.AnimationCurve.EASE,
        switch_out_curve=ft.AnimationCurve.EASE,
    )
    ease_scale_sw = ft.AnimatedSwitcher(
        ease_scale_1,
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=1000,
        reverse_duration=1000,
        switch_in_curve=ft.AnimationCurve.EASE,
        switch_out_curve=ft.AnimationCurve.EASE,
    )
    ease_fade_sw = ft.AnimatedSwitcher(
        ease_fade_1,
        transition=ft.AnimatedSwitcherTransition.FADE,
        duration=1000,
        reverse_duration=1000,
        switch_in_curve=ft.AnimationCurve.EASE,
        switch_out_curve=ft.AnimationCurve.EASE,
    )

    ease_in_rotation_sw = ft.AnimatedSwitcher(
        ease_in_rotation_1,
        transition=ft.AnimatedSwitcherTransition.ROTATION,
        duration=1000,
        reverse_duration=1000,
        switch_in_curve=ft.AnimationCurve.EASE_IN,
        switch_out_curve=ft.AnimationCurve.EASE_IN,
    )
    ease_in_scale_sw = ft.AnimatedSwitcher(
        ease_in_scale_1,
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=1000,
        reverse_duration=1000,
        switch_in_curve=ft.AnimationCurve.EASE_IN,
        switch_out_curve=ft.AnimationCurve.EASE_IN,
    )
    ease_in_fade_sw = ft.AnimatedSwitcher(
        ease_in_fade_1,
        transition=ft.AnimatedSwitcherTransition.FADE,
        duration=1000,
        reverse_duration=1000,
        switch_in_curve=ft.AnimationCurve.EASE_IN,
        switch_out_curve=ft.AnimationCurve.EASE_IN,
    )

    ease_in_back_rotation_sw = ft.AnimatedSwitcher(
        ease_in_back_rotation_1,
        transition=ft.AnimatedSwitcherTransition.ROTATION,
        duration=1000,
        reverse_duration=1000,
        switch_in_curve=ft.AnimationCurve.EASE_IN_BACK,
        switch_out_curve=ft.AnimationCurve.EASE_IN_BACK,
    )
    ease_in_back_scale_sw = ft.AnimatedSwitcher(
        ease_in_back_scale_1,
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=1000,
        reverse_duration=1000,
        switch_in_curve=ft.AnimationCurve.EASE_IN_BACK,
        switch_out_curve=ft.AnimationCurve.EASE_IN_BACK,
    )
    ease_in_back_fade_sw = ft.AnimatedSwitcher(
        ease_in_back_fade_1,
        transition=ft.AnimatedSwitcherTransition.FADE,
        duration=1000,
        reverse_duration=1000,
        switch_in_curve=ft.AnimationCurve.EASE_IN_BACK,
        switch_out_curve=ft.AnimationCurve.EASE_IN_BACK,
    )

    ### FUNCTIONS ###
    def f_bounce_in_rotation(e):
        bounce_in_rotation_sw.content = bounce_in_rotation_2 if bounce_in_rotation_sw.content == bounce_in_rotation_1 else bounce_in_rotation_1
        bounce_in_rotation_sw.update()
    def f_bounce_in_scale(e):
        bounce_in_scale_sw.content = bounce_in_scale_2 if bounce_in_scale_sw.content == bounce_in_scale_1 else bounce_in_scale_1
        bounce_in_scale_sw.update()
    def f_bounce_in_fade(e):
        bounce_in_fade_sw.content = bounce_in_fade_2 if bounce_in_fade_sw.content == bounce_in_fade_1 else bounce_in_fade_1
        bounce_in_fade_sw.update()

    def f_bounce_in_out_rotation(e):
        bounce_in_out_rotation_sw.content = bounce_in_out_rotation_2 if bounce_in_out_rotation_sw.content == bounce_in_out_rotation_1 else bounce_in_out_rotation_1
        bounce_in_out_rotation_sw.update()
    def f_bounce_in_out_scale(e):
        bounce_in_out_scale_sw.content = bounce_in_out_scale_2 if bounce_in_out_scale_sw.content == bounce_in_out_scale_1 else bounce_in_out_scale_1
        bounce_in_out_scale_sw.update()
    def f_bounce_in_out_fade(e):
        bounce_in_out_fade_sw.content = bounce_in_out_fade_2 if bounce_in_out_fade_sw.content == bounce_in_out_fade_1 else bounce_in_out_fade_1
        bounce_in_out_fade_sw.update()

    def f_bounce_out_rotation(e):
        bounce_out_rotation_sw.content = bounce_out_rotation_2 if bounce_out_rotation_sw.content == bounce_out_rotation_1 else bounce_out_rotation_1
        bounce_out_rotation_sw.update()
    def f_bounce_out_scale(e):
        bounce_out_scale_sw.content = bounce_out_scale_2 if bounce_out_scale_sw.content == bounce_out_scale_1 else bounce_out_scale_1
        bounce_out_scale_sw.update()
    def f_bounce_out_fade(e):
        bounce_out_fade_sw.content = bounce_out_fade_2 if bounce_out_fade_sw.content == bounce_out_fade_1 else bounce_out_fade_1
        bounce_out_fade_sw.update()

    def f_decelerate_rotation(e):
        decelerate_rotation_sw.content = decelerate_rotation_2 if decelerate_rotation_sw.content == decelerate_rotation_1 else decelerate_rotation_1
        decelerate_rotation_sw.update()
    def f_decelerate_scale(e):
        decelerate_scale_sw.content = decelerate_scale_2 if decelerate_scale_sw.content == decelerate_scale_1 else decelerate_scale_1
        decelerate_scale_sw.update()
    def f_decelerate_fade(e):
        decelerate_fade_sw.content = decelerate_fade_2 if decelerate_fade_sw.content == decelerate_fade_1 else decelerate_fade_1
        decelerate_fade_sw.update()

    def f_ease_rotation(e):
        ease_rotation_sw.content = ease_rotation_2 if ease_rotation_sw.content == ease_rotation_1 else ease_rotation_1
        ease_rotation_sw.update()
    def f_ease_scale(e):
        ease_scale_sw.content = ease_scale_2 if ease_scale_sw.content == ease_scale_1 else ease_scale_1
        ease_scale_sw.update()
    def f_ease_fade(e):
        ease_fade_sw.content = ease_fade_2 if ease_fade_sw.content == ease_fade_1 else ease_fade_1
        ease_fade_sw.update()  

    def f_ease_in_rotation(e):
        ease_in_rotation_sw.content = ease_in_rotation_2 if ease_in_rotation_sw.content == ease_in_rotation_1 else ease_in_rotation_1
        ease_in_rotation_sw.update()
    def f_ease_in_scale(e):
        ease_in_scale_sw.content = ease_in_scale_2 if ease_in_scale_sw.content == ease_in_scale_1 else ease_in_scale_1
        ease_in_scale_sw.update()
    def f_ease_in_fade(e):
        ease_in_fade_sw.content = ease_in_fade_2 if ease_in_fade_sw.content == ease_in_fade_1 else ease_in_fade_1
        ease_in_fade_sw.update() 

    def f_ease_in_back_rotation(e):
        ease_in_back_rotation_sw.content = ease_in_back_rotation_2 if ease_in_back_rotation_sw.content == ease_in_back_rotation_1 else ease_in_back_rotation_1
        ease_in_back_rotation_sw.update()
    def f_ease_in_back_scale(e):
        ease_in_back_scale_sw.content = ease_in_back_scale_2 if ease_in_back_scale_sw.content == ease_in_back_scale_1 else ease_in_back_scale_1
        ease_in_back_scale_sw.update()
    def f_ease_in_back_fade(e):
        ease_in_back_fade_sw.content = ease_in_back_fade_2 if ease_in_back_fade_sw.content == ease_in_back_fade_1 else ease_in_back_fade_1
        ease_in_back_fade_sw.update() 

    #################
        
    page.add(
        ft.Row([bounce_in_rotation_sw,ft.ElevatedButton("BOUNCE_IN_ROTATION", on_click=f_bounce_in_rotation),
                bounce_in_scale_sw,ft.ElevatedButton("BOUNCE_IN_SCALE", on_click=f_bounce_in_scale),
                bounce_in_fade_sw,ft.ElevatedButton("BOUNCE_IN_FADE", on_click=f_bounce_in_fade)],alignment=ft.MainAxisAlignment.SPACE_AROUND),
        ft.Row([bounce_in_out_rotation_sw,ft.ElevatedButton("BOUNCE_IN_OUT_ROTATION", on_click=f_bounce_in_out_rotation),
                bounce_in_out_scale_sw,ft.ElevatedButton("BOUNCE_IN_OUT_SCALE", on_click=f_bounce_in_out_scale),
                bounce_in_out_fade_sw,ft.ElevatedButton("BOUNCE_IN_OUT_FADE", on_click=f_bounce_in_out_fade)],alignment=ft.MainAxisAlignment.SPACE_AROUND),
        ft.Row([bounce_out_rotation_sw,ft.ElevatedButton("BOUNCE_OUT_ROTATION", on_click=f_bounce_out_rotation),
                bounce_out_scale_sw,ft.ElevatedButton("BOUNCE_OUT_SCALE", on_click=f_bounce_out_scale),
                bounce_out_fade_sw,ft.ElevatedButton("BOUNCE_OUT_FADE", on_click=f_bounce_out_fade)],alignment=ft.MainAxisAlignment.SPACE_AROUND),
        ft.Row([decelerate_rotation_sw,ft.ElevatedButton("DECELERATE_ROTATION", on_click=f_decelerate_rotation),
                decelerate_scale_sw,ft.ElevatedButton("DECELERATE_SCALE", on_click=f_decelerate_scale),
                decelerate_fade_sw,ft.ElevatedButton("DECELERATE_FADE", on_click=f_decelerate_fade)],alignment=ft.MainAxisAlignment.SPACE_AROUND),
        ft.Row([ease_rotation_sw,ft.ElevatedButton("EASE_ROTATION", on_click=f_ease_rotation),
                ease_scale_sw,ft.ElevatedButton("EASE_SCALE", on_click=f_ease_scale),
                ease_fade_sw,ft.ElevatedButton("EASE_FADE", on_click=f_ease_fade)],alignment=ft.MainAxisAlignment.SPACE_AROUND),
        ft.Row([ease_in_rotation_sw,ft.ElevatedButton("EASE_IN_ROTATION", on_click=f_ease_in_rotation),
                ease_in_scale_sw,ft.ElevatedButton("EASE_IN_SCALE", on_click=f_ease_in_scale),
                ease_in_fade_sw,ft.ElevatedButton("EASE_IN_FADE", on_click=f_ease_in_fade)],alignment=ft.MainAxisAlignment.SPACE_AROUND),
        ft.Row([ease_in_back_rotation_sw,ft.ElevatedButton("EASE_IN_BACK_ROTATION", on_click=f_ease_in_back_rotation),
                ease_in_back_scale_sw,ft.ElevatedButton("EASE_IN_BACK_SCALE", on_click=f_ease_in_back_scale),
                ease_in_back_fade_sw,ft.ElevatedButton("EASE_IN_BACK_FADE", on_click=f_ease_in_back_fade)],alignment=ft.MainAxisAlignment.SPACE_AROUND)
    )

ft.app(target=main)