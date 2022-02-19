
def main(archivo):
    try:
        file = open(archivo,'r')
        print("-> Configuracion intalada correctamente!\n")
        file.close()
    except FileNotFoundError:
        print("-> Archivo de configuracion no encontrado\n")
    except PermissionError:
        print("-> No se puede leer el archivo de configuracion\n")
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")



if __name__ == '__main__':
    print("Primer error: FileNotFoundError ")
    main("config.txt")
    #----------------------------------------------------------------
    print("Sin errores:")
    main("config/config.txt")
    #----------------------------------------------------------------
    print("Segundo error: PermissionError ")
    main("config")
    #----------------------------------------------------------------

