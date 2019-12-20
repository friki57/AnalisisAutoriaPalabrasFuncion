def generarExcel(x,y):
    import xlsxwriter
    libro = xlsxwriter.Workbook('Datos.xlsx');
    hoja = libro.add_worksheet();
    fila = 0;
    columna = 0;
    for dato in x:
        hoja.write(fila,columna,dato);
        fila += 1;
    columna = 1;
    fila=0;
    for dato in y:
        hoja.write(fila,columna,dato);
        fila += 1;
    libro.close();

txt = open("datos.txt","r");
contenido = txt.read();
txt.close();

contenido = contenido.replace('\n',' ');

print(contenido);

arreglo = contenido.split(' ')

print(arreglo)

palabras = [];

for a in arreglo:
    if a not in palabras and a != '':
        palabras.append(a);

print(palabras)

frecuencia = [];

for p in palabras:
    num = 0;
    for a in arreglo:
        if a == p:
            num+=1
    frecuencia.append(num);

funciones = [];

#
# for p in palabras:
#     f = funcion();
#     f.pala = p;
#     f.frec = frecuencia[i];
#     i+=1;
#     funciones.append(f);
#
# for f in funciones:
#     f.imp();

print(" .......................................")
print(palabras,frecuencia)
for o in range(len(palabras)-1):
    for i in range(len(palabras)-1):
        if(frecuencia[i]<frecuencia[i+1]):
            print(palabras[i],frecuencia[i],palabras[i+1],frecuencia[i+1])
            aux = frecuencia[i];
            frecuencia[i]=frecuencia[i+1]
            frecuencia[i+1]=aux;
            aux = palabras[i];
            palabras[i] =palabras[i+1];
            palabras[i+1] = aux;

generarExcel(palabras,frecuencia);
