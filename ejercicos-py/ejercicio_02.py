import pandas as pd

def filtros_logicos():
    data = {
        'empleado': ['Ana', 'Luis', 'Sofía', 'Pedro', 'Marta', 'Carlos'],
        'salario': [55000, 48000, 62000, 75000, 49000, 51000],
        'edad': [31, 28, 45, 33, 29, 36],
        'departamento': ['Ventas', 'Marketing', 'Ventas', 'IT', 'Marketing', 'IT']
    }
    df = pd.DataFrame(data)
    print("DataFrame original de empleados:")
    print(df)
    print("-" * 50)
    filtro_and = df[(df['departamento'] == 'IT') & (df['salario'] > 60000)]
    print("Empleados de IT con salario > 60,000:")
    print(filtro_and)
    print("-" * 50)
    filtro_or = df[(df['departamento'] == 'Ventas') | (df['edad'] > 40)]
    print("Empleados de Ventas O mayores de 40 años:")
    print(filtro_or)
    print("-" * 50)
    filtro_not = df[~(df['departamento'] == 'Marketing')]
    print("Empleados que NO son de Marketing:")
    print(filtro_not)
    print("-" * 50)

filtros_logicos()