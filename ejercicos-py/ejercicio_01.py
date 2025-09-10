import pandas as pd

def filtros_empleados():
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
    salario_mayor_50k = df[df['salario'] > 50000]
    print("Empleados con salario mayor a 50,000:")
    print(salario_mayor_50k)
    print("-" * 50)
    menores_35 = df[df['edad'] < 35]
    print("Empleados menores de 35 años:")
    print(menores_35)
    print("-" * 50)
    departamento_it = df[df['departamento'] == 'IT']
    print("Empleados del departamento 'IT':")
    print(departamento_it)
    print("-" * 50)

filtros_empleados()