import pandas as pd

def combinar_filtros():
    data = {
        'empleado': ['Ana', 'Luis', 'Sofía', 'Pedro', 'Marta', 'Carlos', 'Elena', 'Laura'],
        'salario': [55000, 48000, 62000, 75000, 49000, 51000, 68000, 85000],
        'edad': [31, 28, 45, 33, 29, 36, 42, 38],
        'departamento': ['Ventas', 'Marketing', 'Ventas', 'IT', 'Marketing', 'IT', 'Ventas', 'Recursos Humanos']
    }
    df = pd.DataFrame(data)
    print("DataFrame original de empleados:")
    print(df)
    print("-" * 50)
    filtro_combinado_1 = df[
        (df['departamento'] == 'IT') & 
        (df['edad'] > 30) & 
        (df['salario'] > 60000)
    ]
    print("Empleados de IT, mayores de 30 años y con salario > 60,000:")
    print(filtro_combinado_1)
    print("-" * 50)
    filtro_combinado_2 = df[
        (df['empleado'].str.startswith('L')) | 
        (df['departamento'] == 'Recursos Humanos')
    ]
    print("Empleados con nombre que empieza con 'L' o que son de Recursos Humanos:")
    print(filtro_combinado_2)
    print("-" * 50)

combinar_filtros()