vector_palabra = ['casa', 'puerta', 'ventana', 'mesa', 'silla','casa','casa']
palabra = 'casa'

print ('Palabra', vector_palabra)

def contar_Palabra_repetida(palabra,vector_palabra):
     if vector_palabra == []:
          return 0
     elif vector_palabra[0]
     return 1+ 
contar_Palabra_repetida(palabra,vector_palabra[1:])
     else:
      return contar_Palabra_repetida(palabra,vector_palabra[1:])
    

resultado = contar_Palabra_repetida(palabra,vector_palabra)
print(f'La palabra{'casa'} aparece {resultado} veces en el vector')