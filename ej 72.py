import pandas as pd

# Crear el DataFrame
datos = {
    "Producto": ["bimbo", "alpura", "vuala", "sabritas"],
    "Precio": [45, 27, 20, 15],
    "Cantidad": [400, 350, 273, 320]
}

df = pd.DataFrame(datos)
print("📋 DataFrame:\n", df)

# Mostrar estadísticos principales
print("\n📈 Estadísticos:")
print(df.describe())
