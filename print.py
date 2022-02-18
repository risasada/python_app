from plyer import notification


def notice(minute):
    notification.notify(
        title='目を休ませてください',
        message=f'{minute}分経ちました。',
        app_name=' Ai patch',
        app_icon='eye_icon.ico',
        timeout=20
    )


