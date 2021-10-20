import pythoncom

# Conecta el objeto de aplicacion Excel existente
xlDispatch = pythoncom.connect('Excel.Application')

# Trae el tipo de objeto existente
typeInfo = xlDispatch.GetTypeInfo()

# Existe el metodo Workbook en la aplicacion Excel
workbook_id = xlDispatch.GetIDsOfNames('Workbooks')
# display(workbook_id)

# Existe el metodo Quit en la aplicacion Excel
quit_id = xlDispatch.GetIDsOfNames('Quit')
# display(quit_id)

# Define la DISPID de la propiedad Range
RangeID = xlDispatch.GetIDsOfNames('Range')

# Define la DISPID de la propiedad Undo
UndoID = xlDispatch.GetIDsOfNames('Undo')

# Define el LCID
LCID = 0x0

# Define las banderas para la llamada
wFlags = pythoncom.DISPATCH_PROPERTYGET

# define the type of our result sent back to us
resultTypeDesc = (24, 1) 


# No hay argumentos, por lo que no es necesario definir tipos
typeDescs = ()
args = ''

# Invoca el metodo
UndoDispatch = xlDispatch.InvokeTypes(UndoID, LCID, wFlags, resultTypeDesc, typeDescs)