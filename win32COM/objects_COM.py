import pythoncom
import win32com.client

# Debe ser 0
context = pythoncom.CreateBindCtx(0)

# Trae la tabla de objetos en ejecucion
running_coms = pythoncom.GetRunningObjectTable()

# Enumera todos los apodos in la tabla
monikers = running_coms.EnumRunning()

# Recorre todos apodos
for moniker in monikers:
    print('-'*100)

    # imprime el nombre del display
    print(moniker.GetDisplayName(context, moniker))

Microsoft_Excel = win32com.client.gencache.EnsureDispatch('{00024505-0016-0000-C000-000000000046}')