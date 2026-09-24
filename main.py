from fastapi import FastAPI, HTTPException
from Config.database import get_connection

#se crea la instancia FastAPI
app = FastAPI(
    tittle = "Clase CSR",   
    description = "Primera conexion entre FASTAPI y Postgres",
    version = "1.0"
)

@app.get("/db-test")
def probar_bas_datos():
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                Curso.execute("""
                SELECT current.database() AS base_datos,
                Current_user AS usuario,
                NOW() AS fecha_hora,
                """)
        resultado = cursor.fetchone() 
        return{
            "conexion":"Correcta",
            "informacion":resultado
    }
    except Exception as error:
        raise HTTPException(
            Status_Code = 500,
            detail =f"No fue posible conectarse con postgres{error}"
        )
@app.get("/estudiantes")
def obtener_estudiantes():
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""
                SELECT 
                id,
                nombre,
                correo,
                creado_en
                FROM estudiantes
                ORDER BY id;
                """)
        estudiantes=cursor.fetchall()
        return estudiantes
    except Exception as error:
        raise HTTPException(
            Status_Code = 500,
            detail =f"Error al consiltar estudiantes{error}"
        )
@app.get("/maestros")
def obtener_maestros():
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""
                SELECT 
                id,
                nombre,
                correo,
                turno
                FROM maestros
                ORDER BY id;
                """)
        maestros=cursor.fetchall()
        return maestros
    except Exception as error:
        raise HTTPException(
            Status_Code = 500,
            detail =f"Error al consiltar maestros{error}"
        )
@app.get("/personal")
def obtener_personal():
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""
                SELECT 
                id,
                nombre,
                area,
                turno
                FROM personal
                ORDER BY id;
                """)
        personal=cursor.fetchall()
        return personal
    except Exception as error:
        raise HTTPException(
            Status_Code = 500,
            detail =f"Error al consiltar personal{error}"
        )