from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Ruta para Linux
    csv_path = '/mnt/c/Users/jcoello/Downloads/flask-render-integration-main/flask-render-integration/DataFiles/ejercicio1.csv'

    # Verificar si el archivo existe
    if not os.path.exists(csv_path):
        return "Error: El archivo CSV no se encontró."

    try:
        # Cargar el archivo CSV
        data = pd.read_csv(csv_path)

        # Verificar que las columnas existan
        if 'Department' not in data.columns or 'Salary' not in data.columns:
            return "Error: El archivo CSV no tiene las columnas esperadas."

        # Análisis: calcular el salario promedio por departamento
        salary_by_dept = data.groupby('Department')['Salary'].mean().reset_index()

        # Convertir a diccionario para pasarlo al HTML
        salary_data = salary_by_dept.to_dict(orient='records')

        return render_template('home.html', data=salary_data)

    except Exception as e:
        return f"Error al procesar el archivo: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)

