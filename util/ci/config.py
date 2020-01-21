from os import getenv, path

qt_version = "5.14.0"
qtc_version = "4.11.0"
os_name = getenv('OS', 'linux')
qt_modules = ['qtbase', 'qttools', 'icu']
plugin_name = 'QtcDbViewer'
pro_file = path.abspath(path.dirname(__file__) + '/../../qtc-dbviewer.pro')
ts_files_dir = path.abspath(path.dirname(__file__) + '/../../translation')
