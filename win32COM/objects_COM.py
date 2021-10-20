import pythoncom

# Debe ser 0
context = pythoncom.CreateBindCtx(0)

# Trae la tabla de objetos en ejecucion
running_coms = pythoncom.GetRunningObjectTable()

# Enumera todos los apodos in la tabla
monikers = running_coms.EnumRunning()

# Recorre todos apodos
for moniker in monikers:
    print('-'*100)
    print(moniker.GetDisplayName(context, moniker))