import pandas as pd

def filtrar_isin():
    data = {
        'empleado': ['Ana', 'Luis', 'Sofía', 'Pedro', 'Marta', 'Carlos', 'Elena'],
        'salario': [55000, 48000, 62000, 75000, 49000, 51000, 68000],
        'edad': [31, 28, 45, 33, 29, 36, 42],
        'departamento': ['Ventas', 'Marketing', 'Ventas', 'IT', 'Marketing', 'IT', 'Ventas']
    }
    df = pd.DataFrame(data)
    print("DataFrame original de empleados:")
    print(df)
    print("-" * 50)
    departamentos_filtrar = ['IT', 'Ventas']
    filtro_departamento = df[df['departamento'].isin(departamentos_filtrar)]
    print(f"Empleados en los departamentos: {departamentos_filtrar}")
    print(filtro_departamento)
    print("-" * 50)
    edades_filtrar = [28, 35, 42]
    filtro_edad = df[df['edad'].isin(edades_filtrar)]
    print(f"Empleados con edades: {edades_filtrar}")
    print(filtro_edad)
    print("-" * 50)

filtrar_isin()