#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
########################################################################
#                     Lanzador Flameshot v.0.2.1                       #
########################################################################
#                                                                      #
# Si se ha utilizado el instalador, la aplicación debería aparecer en  #
# el menú de aplicaciones, en caso contrarío, ejecutar mediante el     #
# comando python u otorgando permisos de ejecución y utilizando ./     #
#                                                                      #
# Se puede mirar, copiar o modificar lo que se quiera                  #
#                                                                      #
# Iván Rincón 2017                                                     #
########################################################################
 
import gettext
import os
import wx
from ConfigParser import ConfigParser
 
# Variables
rutaArchivoConfig = os.getenv("HOME") + "/.config/lanzador-flameshot/Lanzador.cfg"

if os.path.exists("/usr/local/bin/flameshot"):
    rutaFlameshot = "/usr/local/bin/flameshot"
elif os.path.exists("/usr/bin/flameshot"):
    rutaFlameshot = "/usr/bin/flameshot"

if os.path.exists("/usr/local/share/icons/flameshot.png"):
    rutaIcono = "/usr/local/share/icons/flameshot.png"
elif os.path.exists("/usr/share/icons/flameshot.png"):
    rutaIcono = "/usr/share/icons/flameshot.png"

# Clases
config = ConfigParser()
 
 
class LanzadorFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = wx.CLOSE_BOX | wx.MINIMIZE_BOX  # | wx.STAY_ON_TOP
        wx.Frame.__init__(self, *args, **kwds)
        self.labelModoCapura = wx.StaticText(self, wx.ID_ANY, _("Modo de captura"), style=wx.ALIGN_LEFT)
        self.labelArea = wx.StaticText(self, wx.ID_ANY, _(u"\u00c1rea:"))
        self.comboboxArea = wx.ComboBox(self, wx.ID_ANY, choices=[_("Pantalla completa"), _(u"Secci\u00f3n rectangular")
                                                                  ], style=wx.CB_READONLY)
        self.labelDemora = wx.StaticText(self, wx.ID_ANY, _("Demora"))
        self.spinCtrlSegundos = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=300, style=wx.TE_READONLY)
        self.labelSegundos = wx.StaticText(self, wx.ID_ANY, _("segundos"), style=wx.ALIGN_RIGHT)
        self.static_line_2 = wx.StaticLine(self, wx.ID_ANY)
        self.label_5 = wx.StaticText(self, wx.ID_ANY, _("Ruta guardado:"))
        self.textCtrlRutaGuardado = wx.TextCtrl(self, wx.ID_ANY, "")
        self.buttonDirDialog = wx.Button(self, wx.ID_ANY, _("..."))
        self.static_line_3 = wx.StaticLine(self, wx.ID_ANY)
        self.buttonRealizarCaptura = wx.Button(self, wx.ID_ANY, _("Realizar captura"))
        self.buttonPreferencias = wx.Button(self, wx.ID_PREFERENCES, "")
        self.buttonSalir = wx.Button(self, wx.ID_EXIT, "")
 
        self.__set_properties()
        self.__do_layout()
        self.setConfig()
 
        self.Bind(wx.EVT_COMBOBOX, self.OnComboBoxAreaClick, self.comboboxArea)
        self.Bind(wx.EVT_SPINCTRL, self.OnSpinCtrlSegundosClick, self.spinCtrlSegundos)
        self.Bind(wx.EVT_TEXT, self.OnTextCtrlRutaGuardadoClick, self.textCtrlRutaGuardado)
        self.Bind(wx.EVT_BUTTON, self.OnButtonClickDialogClick, self.buttonDirDialog)
        self.Bind(wx.EVT_BUTTON, self.OnButtonRealizarCapturaClick, self.buttonRealizarCaptura)
        self.Bind(wx.EVT_BUTTON, self.OnButtonPreferenciasClick, self.buttonPreferencias)
        self.Bind(wx.EVT_BUTTON, self.OnButtonSalirClick, self.buttonSalir)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
 
    def __set_properties(self):
        self.SetTitle(_("Flameshot"))
        _icon = wx.NullIcon
        #  icon.CopyFromBitmap(wx.Bitmap(os.getenv("HOME") + "/.local/share/icons/flameshot.png", wx.BITMAP_TYPE_ANY))
        _icon.CopyFromBitmap(wx.Bitmap(rutaIcono, wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.SetSize((251, 245))
        self.labelModoCapura.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.labelArea.SetMinSize((71, 30))
        self.comboboxArea.SetMinSize((160, 30))
        self.comboboxArea.SetSelection(0)
        self.labelDemora.SetMinSize((71, 30))
        self.spinCtrlSegundos.SetMinSize((50, 28))
        self.labelSegundos.SetMinSize((65, 18))
        self.label_5.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.textCtrlRutaGuardado.SetMinSize((215, 30))
        self.textCtrlRutaGuardado.SetValue(os.getenv("HOME"))
        self.buttonDirDialog.SetMinSize((25, 30))
        self.buttonRealizarCaptura.SetMinSize((242, 35))
        self.buttonPreferencias.SetMinSize((121, 30))
        self.buttonSalir.SetMinSize((121, 30))
 
    def __do_layout(self):
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
 
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(self.labelModoCapura, 0, wx.BOTTOM | wx.TOP, 5)
        sizer_2.Add(self.labelArea, 1, wx.BOTTOM, 5)
        sizer_2.Add((20, 20), 0, 0, 0)
        sizer_2.Add(self.comboboxArea, 0, wx.ALIGN_RIGHT | wx.BOTTOM | wx.RIGHT, 5)
        sizer_1.Add(sizer_2, 1, wx.ALIGN_RIGHT, 0)
        sizer_3.Add(self.labelDemora, 1, 0, 5)
        sizer_3.Add((35, 20), 0, 0, 0)
        sizer_3.Add(self.spinCtrlSegundos, 0, wx.ALIGN_RIGHT, 0)
        sizer_3.Add((20, 20), 0, wx.ALIGN_RIGHT, 0)
        sizer_3.Add(self.labelSegundos, 0, wx.ALIGN_RIGHT | wx.RIGHT, 5)
        sizer_1.Add(sizer_3, 1, wx.ALIGN_RIGHT | wx.SHAPED, 0)
        sizer_1.Add(self.static_line_2, 0, 0, 0)
        sizer_1.Add(self.label_5, 0, wx.BOTTOM | wx.TOP, 5)
        sizer_4.Add(self.textCtrlRutaGuardado, 0, wx.ALIGN_RIGHT, 0)
        sizer_4.Add((10, 20), 0, wx.ALIGN_RIGHT, 0)
        sizer_4.Add(self.buttonDirDialog, 0, wx.ALIGN_RIGHT | wx.RIGHT, 5)
        sizer_1.Add(sizer_4, 1, wx.ALIGN_RIGHT, 0)
        sizer_1.Add(self.static_line_3, 0, wx.EXPAND, 0)
        sizer_1.Add(self.buttonRealizarCaptura, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 3)
        sizer_5.Add(self.buttonPreferencias, 0, wx.EXPAND, 0)
        sizer_5.Add((2, 10), 0, 0, 0)
        sizer_5.Add(self.buttonSalir, 0, wx.ALIGN_RIGHT | wx.EXPAND, 0)
        sizer_1.Add(sizer_5, 1, wx.ALIGN_CENTER_HORIZONTAL, 0)
        self.SetSizer(sizer_1)
        self.Layout()
 
    def OnClose(self, event):

        with open(rutaArchivoConfig.encode('utf8', 'replace'), "w") as archivoConfig:
            config.write(archivoConfig)
        self.Destroy()
 
    def OnComboBoxAreaClick(self, event):
 
        indice = self.comboboxArea.GetSelection()
 
        config.read(rutaArchivoConfig)
        config.set("Configuracion", "indiceCombo", indice)
 
        event.Skip()
 
    def OnSpinCtrlSegundosClick(self, event):
 
        retardo = self.spinCtrlSegundos.GetValue()
 
        config.read(rutaArchivoConfig)
        config.set("Configuracion", "retardo", retardo)
 
        event.Skip()
 
    def OnTextCtrlRutaGuardadoClick(self, event):
 
        ruta = self.textCtrlRutaGuardado.GetValue().encode("utf8")
 
        config.read(rutaArchivoConfig)
        config.set("Configuracion", "rutaGuardado", ruta)
 
        event.Skip()
 
    def OnButtonClickDialogClick(self, event):
 
        dlg = wx.DirDialog(None, "Seleccione un directorio", os.getenv("HOME"),
                           wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dlg.ShowModal() == wx.ID_OK:
            self.textCtrlRutaGuardado.SetValue(dlg.GetPath())
            config.read(rutaArchivoConfig)
            config.set("Configuracion", "rutaGuardado", dlg.GetPath())
        event.Skip()
 
    def OnButtonRealizarCapturaClick(self, event):
 
        if self.checkFlameshot() == wx.ID_NO: return
 
        import re
        import commands
 
        ruta = self.textCtrlRutaGuardado.GetValue()
 
        # TODO: Probar de nuevo con and
        if not os.path.exists(ruta):
 
            if bool(re.match(r"(\/[\w^ ]+)+\/?([\w.])+[^.]$", ruta)):
                os.makedirs(ruta)
 
            else:
                self.msgDlg(ruta + "\n\nno es un nombre de directorio válido".decode("utf8"))
                return
 
        salida = commands.getoutput(self.setArgumentos())
 
        if salida != "":
            self.msgDlg(salida.replace("See 'flameshot --help'.", ""))
 
        self.OnClose(event)
 
        event.Skip()
 
    def OnButtonPreferenciasClick(self, event):
 
        os.system(rutaFlameshot + " config")
        event.Skip()
 
    def OnButtonSalirClick(self, event):
 
        self.OnClose(event)
        event.Skip()
 
    def setConfig(self):
 
        if os.path.exists(rutaArchivoConfig):
            config.read(rutaArchivoConfig)
            self.comboboxArea.SetSelection(config.getint("Configuracion", "indiceCombo"))
            self.spinCtrlSegundos.SetValue(config.getint("Configuracion", "retardo"))
            self.textCtrlRutaGuardado.SetValue(config.get("Configuracion", "rutaGuardado"))
 
        else:
 
            # TODO: pasar el testFlameshot() aquí
 
            ruta = rutaArchivoConfig.replace("Lanzador.cfg", "")
 
            if not os.path.exists(ruta):
                os.makedirs(ruta)
 
            config.add_section("Configuracion")
            config.set("Configuracion", "indiceCombo", 0)
            config.set("Configuracion", "retardo", 0)
            config.set("Configuracion", "rutaGuardado", os.getenv("HOME"))
            config.set("Configuracion", "copiaClipboard", 0)  # Sin implementar (modo full)
 
            with open(rutaArchivoConfig, "wb") as archivoConfig:  # w: sobrescritura: si no existe crea. b: binario
                config.write(archivoConfig)
 
    def setArgumentos(self):
 
        argumentos = list()
        argumentos.append(rutaFlameshot)
        argumentos.append("-d " + str(self.spinCtrlSegundos.GetValue() * 1000))
        argumentos.append("-p " + self.textCtrlRutaGuardado.GetValue().encode("utf8"))
 
        if self.comboboxArea.GetSelection():  # Se le toma como bool al tener sólo 2 posibilidades
            argumentos.insert(1, "gui")
        else:
            argumentos.insert(1, "full")
 
        return " ".join(argumentos)
 
    def checkFlameshot(self):
 
        if not os.path.exists("/usr/local/bin/flameshot") and not os.path.exists("/usr/bin/flameshot"):
            return self.msgDlg("Parece que Flameshot no está instalado.\n\n¿Desea continuar?".decode("utf8"),
                               wx.YES_NO, wx.ICON_QUESTION)
 
    def msgDlg(self, mensaje, botones=wx.OK, simbolo=wx.ICON_EXCLAMATION):
        d = wx.MessageDialog(self, mensaje, "Flameshot", botones | simbolo)
        res = d.ShowModal()
        d.Destroy()
        return res
 
 
# Final de la clase LanzadorFrame
 
class LanzadorFlameshot(wx.App):
 
    def OnInit(self):
        frame_ppal = LanzadorFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(frame_ppal)
        frame_ppal.Show()
        return True
 
 
# Final de la clase LanzadorFlameshot
 
if __name__ == "__main__":
 
    gettext.install("appLanzador")
 
    appLanzador = LanzadorFlameshot(0)
    appLanzador.MainLoop()
