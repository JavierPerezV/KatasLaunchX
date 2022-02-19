def agua_restante(astronautas, agua, dias):
    for argumento in [astronautas, agua, dias]:
        try:
            argumento/ 10
        except TypeError:
            raise TypeError(f"Todos los argumentos deben de ser enteros, se obtuvo: '{argumento}'")
    
    uso_diario = astronautas * 11
    total_usado = uso_diario * dias
    total_restante = agua - total_usado
    if total_restante < 0:
        raise RuntimeError(f"No hay suficiente agua para {astronautas} los astronautas despues de {dias} dias!")
    return f"Agua total despues de {dias} dias es: {total_restante} litros."

agua_restante(5,100,2)
