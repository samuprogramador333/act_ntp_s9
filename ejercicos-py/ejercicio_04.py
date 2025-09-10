import pandas as pd

def filtrar_texto():
    data = {
        'empleado': ['Ana', 'Luis', 'Sofía', 'Pedro', 'Marta', 'Carlos', 'Martina'],
        'salario': [55000, 48000, 62000, 75000, 49000, 51000, 68000],
        'edad': [31, 28, 45, 33, 29, 36, 42],
        'departamento': ['Ventas', 'Marketing', 'Ventas', 'IT', 'Marketing', 'IT', 'Recursos Humanos']
    }
    df = pd.DataFrame(data)
    print("DataFrame original de empleados:")
    print(df)
    print("-" * 50)
    filtro_nombre = df[df['empleado'].str.startswith('M')]
    print("Empleados cuyos nombres empiezan con 'M':")
    print(filtro_nombre)
    print("-" * 50)
    filtro_departamento = df[df['departamento'].str.contains('R', case=False)]
    print("Departamentos que contienen 'R':")
    print(filtro_departamento)
    print("-" * 50)

filtrar_texto()