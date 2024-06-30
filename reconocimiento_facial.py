import pandas as pd

# Crear planilla.xlsx
df_planilla = pd.DataFrame(columns=["Nombre", "CI", "Curso", "Actividad", "Fecha y Hora"])
df_planilla.to_excel("planilla.xlsx", index=False)

# Crear usuarios.xlsx
df_usuarios = pd.DataFrame(columns=["Nombre", "CI", "Contraseña"])
df_usuarios.to_excel("usuarios.xlsx", index=False)

