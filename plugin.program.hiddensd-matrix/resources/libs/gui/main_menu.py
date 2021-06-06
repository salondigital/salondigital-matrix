import os

from resources.libs.common import directory
from resources.libs.common.config import CONFIG


class MainMenu:

    def get_listing(self):
        from resources.libs import check
        from resources.libs.common import logging
        from resources.libs.common import tools

        errors = int(logging.error_checking(count=True))
        errorsfound = str(errors) + ' Errore(s) Encontrados' if errors > 0 else 'Ninguno encontrado'

        if CONFIG.AUTOUPDATE == 'Yes':
            response = tools.open_url(CONFIG.BUILDFILE, check=True)

            if response:
                ver = check.check_wizard('version')
                if ver:
                    if ver > CONFIG.ADDON_VERSION:
                        directory.add_file(
                            '{0} [v{1}] [COLOR red][B][ATUALIZACION v{2}][/B][/COLOR]'.format(CONFIG.ADDONTITLE,
                                                                                        CONFIG.ADDON_VERSION, ver),
                            {'mode': 'wizardupdate'}, themeit=CONFIG.THEME2)
                    else:
                        directory.add_file('{0} [v{1}]'.format(CONFIG.ADDONTITLE, CONFIG.ADDON_VERSION),
                                           themeit=CONFIG.THEME2)
            else:
                directory.add_file('{0} [v{1}]'.format(CONFIG.ADDONTITLE, CONFIG.ADDON_VERSION),
                                   themeit=CONFIG.THEME2)
        else:
            directory.add_file('{0} [v{1}]'.format(CONFIG.ADDONTITLE, CONFIG.ADDON_VERSION), themeit=CONFIG.THEME2)
        if len(CONFIG.BUILDNAME) > 0:
            version = check.check_build(CONFIG.BUILDNAME, 'version')
            build = '{0} (v{1})'.format(CONFIG.BUILDNAME, CONFIG.BUILDVERSION)
            if version > CONFIG.BUILDVERSION:
                build = '{0} [COLOR red][B][ACTUALIZACION v{1}][/B][/COLOR]'.format(build, version)
            directory.add_dir(build, {'mode': 'viewbuild', 'name': CONFIG.BUILDNAME}, themeit=CONFIG.THEME4)

            from resources.libs.gui.build_menu import BuildMenu
            themefile = BuildMenu().theme_count(CONFIG.BUILDNAME)
            if themefile:
                directory.add_file('Ninguno' if CONFIG.BUILDTHEME == "" else CONFIG.BUILDTHEME, {'mode': 'theme', 'name': CONFIG.BUILDNAME},
                                   themeit=CONFIG.THEME5)
        else:
            directory.add_dir('Ninguna', {'mode': 'builds'}, themeit=CONFIG.THEME4)
        directory.add_separator()
        directory.add_dir('Instalacion', {'mode': 'builds'}, icon=CONFIG.ICONBUILDS, themeit=CONFIG.THEME1)
        directory.add_dir('Mantenimiento', {'mode': 'maint'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME1)
        if (tools.platform() == 'android' or CONFIG.DEVELOPER == 'true'):
            directory.add_dir('Instalar APK Android', {'mode': 'apk'}, icon=CONFIG.ICONAPK, themeit=CONFIG.THEME1)
        if tools.open_url(CONFIG.ADDONFILE, check=True) or os.path.exists(os.path.join(CONFIG.ADDON_PATH, 'resources', 'text', 'addons.json')):
            directory.add_dir('Instalador de Addons', {'mode': 'addons'}, icon=CONFIG.ICONADDONS, themeit=CONFIG.THEME1)
        #if tools.open_url(CONFIG.YOUTUBEFILE, check=True) and not CONFIG.YOUTUBETITLE == '':
        #    directory.add_dir(CONFIG.YOUTUBETITLE, {'mode': 'youtube'}, icon=CONFIG.ICONYOUTUBE, themeit=CONFIG.THEME1)
        directory.add_dir('Guardar datos', {'mode': 'savedata'}, icon=CONFIG.ICONSAVE, themeit=CONFIG.THEME1)
        directory.add_separator()
        if CONFIG.HIDECONTACT == 'No':
            directory.add_file('Contacto', {'mode': 'contact'}, icon=CONFIG.ICONCONTACT, themeit=CONFIG.THEME1)
        #directory.add_separator()
        #directory.add_file('Upload Log File', {'mode': 'uploadlog'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME1)
        #directory.add_file('View Errors in Log: {0}'.format(errorsfound), {'mode': 'viewerrorlog'}, icon=CONFIG.ICONMAINT,
        #                   themeit=CONFIG.THEME1)
        #if errors > 0:
        #    directory.add_file('View Last Error In Log', {'mode': 'viewerrorlast'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME1)
        #directory.add_separator()
        #directory.add_file('Settings', {'mode': 'settings', 'name': CONFIG.ADDON_ID}, icon=CONFIG.ICONSETTINGS, themeit=CONFIG.THEME1)
        #if CONFIG.DEVELOPER == 'true':
        #    directory.add_dir('Developer Menu', {'mode': 'developer'}, icon=CONFIG.ADDON_ICON, themeit=CONFIG.THEME1)
