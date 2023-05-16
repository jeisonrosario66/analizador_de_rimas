
## analizador_de_rimas
Algoritmo capaz de identificar rimas en un texto.
Dicho texto debe de estar en un formato `4x4` que consiste en estructura de 4 lineas

Ejemplo de un formato `4x4`
```
De nada de lo que hago me arrepiento
A no ser que lo que hago lo haya hecho de espaldas al pensamiento
Y como eso no ha pasado de momento
Que tú catalogues mis fallos de errores me importa un pimiento
```
Ejemplo de salida del programa
![Captura](https://github.com/jeisonrosario66/analizador_de_rimas/assets/96961824/6d2ef4fe-1391-4386-bf62-f2709e29f7e2)

`Solitario: Taquigrafia`

## requirements.txt
- colorama
- unidecode
## Ejecutar programa

Para correr el programa ejecuta

```bash
  pip install -r requirements.txt
  python funciones.py
```


## Objeto `Func`
Este objeto es el encargado de hacer el trabajo requerido para identificar las rimas, cuenta con varios métodos

- `reader()`
- `diccionarioCreate(num)`
- `rimador_complemento(linea)`
- `rimador(num)`
- `run()`

---

Para instanciar el objeto solo se requiere un parámetro, el archivo de texto con el texto en formato `4x4` 

`obj = Func(archivo.txt)`

El método `obj.run()` desencadena todo el funcionamiento del programa

![Captura](https://user-images.githubusercontent.com/96961824/225124004-d5476f0f-1eb0-4190-8181-031bb8b41dfe.PNG)

## Autor

- [@jeisonrosario66](https://github.com/jeisonrosario66)



