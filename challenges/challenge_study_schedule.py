def study_schedule(permanence_period, target_time):    
    try:
        contador = 0

        for item in permanence_period:
            if item[0] <= target_time <= item[1]:
                contador += 1

        return contador
    except ValueError:
        return None
    except TypeError:
        return None


    
# lista_estudantes = [1, 2, 3, 4, 5, 6]
# lista_permanencia = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]

# print(study_schedule(lista_permanencia, 5))
# print(study_schedule(lista_permanencia, 4))
# print(study_schedule(lista_permanencia, 3))
# print(study_schedule(lista_permanencia, 2))
# print(study_schedule(lista_permanencia, 1))