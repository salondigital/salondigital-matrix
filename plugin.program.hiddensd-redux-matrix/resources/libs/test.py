import xbmc

try:  # Python 3
    import zipfile
except ImportError:  # Python 2
    from resources.libs import zipfile

from resources.libs.common.config import CONFIG


def str_test(teststr):
    a = (teststr.lower()).split(' ')
    if 'test' in a:
        return True
    else:
        return False


def test_theme(path):
    from resources.libs.common import logging

    zfile = zipfile.ZipFile(path, allowZip64=True)
    for item in zfile.infolist():
        logging.log(str(item.filename))
        if '/settings.xml' in item.filename:
            return True
    return False


def test_gui(path):
    zfile = zipfile.ZipFile(path, allowZip64=True)
    for item in zfile.infolist():
        if '/guisettings.xml' in item.filename:
            return True
    return False


def test_notify():
    from resources.libs.common import logging
    from resources.libs.common import tools
    from resources.libs.gui import window

    response = tools.open_url(CONFIG.NOTIFICATION, check=True)

    if response:
        try:
            id, msg = window.split_notify(CONFIG.NOTIFICATION)
            if not id:
                logging.log_notify(CONFIG.ADDONTITLE,
                                   "[COLOR {0}]Notification: Not Formatted Correctly[/COLOR]".format(CONFIG.COLOR2))
                return
            window.show_notification(msg, test=True)
        except Exception as e:
            logging.log("Error on Notifications Window: {0}".format(str(e)), level=xbmc.LOGERROR)
    else:
        logging.log_notify(CONFIG.ADDONTITLE,
                           "[COLOR {0}]Invalid URL for Notification[/COLOR]".format(CONFIG.COLOR2))


def test_update():
    from resources.libs import check
    from resources.libs.gui import window

    if CONFIG.BUILDNAME == "":
        window.show_update_window()
    else:
        window.show_update_window(CONFIG.BUILDNAME, CONFIG.BUILDVERSION, CONFIG.BUILDLATEST, check.check_build(CONFIG.BUILDNAME, 'icon'), check.check_build(CONFIG.BUILDNAME, 'fanart'))


def test_first_run():
    from resources.libs.gui import window
    
    window.show_build_prompt()


def test_save_data_settings():
    from resources.libs.gui import window

    window.show_save_data_settings()
