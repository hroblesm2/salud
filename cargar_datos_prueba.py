"""
Script para cargar datos de prueba desde el archivo Excel original
"""
import pandas as pd
from app import app, db, AtencionClinica
from datetime import datetime

def cargar_datos_excel(filepath, limite=50):
    """
    Carga datos desde el archivo Excel al sistema
    
    Args:
        filepath: Ruta al archivo Excel
        limite: Número máximo de registros a cargar (default: 50)
    """
    print(f"Cargando datos desde: {filepath}")
    
    try:
        # Leer el archivo Excel directamente (formato simplificado)
        df = pd.read_excel(filepath)
        
        print(f"Columnas leídas: {list(df.columns)[:5]}...")
        
        # Renombrar columnas para que coincidan con el modelo
        column_mapping = {
            'Fecha_Atencion': 'fecha_atencion',
            'Descripcion_Ups': 'descripcion_ups',
            'Descripcion_Sector': 'descripcion_sector',
            'Descripcion_Disa': 'descripcion_disa',
            'Descripcion_Red': 'descripcion_red',
            'Descripcion_MicroRed': 'descripcion_microred',
            'Genero': 'genero',
            'Edad_Reg': 'edad_reg',
            'Id_Turno': 'id_turno',
            'Descripcion_Item': 'descripcion_item',
            'Peso': 'peso',
            'Talla': 'talla',
            'Hemoglobina': 'hemoglobina',
            'Fecha_Ultima_Regla': 'fecha_ultima_regla'
        }
        
        # Seleccionar solo las columnas que nos interesan
        columnas_disponibles = [col for col in column_mapping.keys() if col in df.columns]
        df = df[columnas_disponibles].copy()
        df.rename(columns=column_mapping, inplace=True)
        
        # Limpiar datos
        df = df.dropna(subset=['fecha_atencion'])  # Eliminar registros sin fecha
        
        # Limitar el número de registros
        df = df.head(limite)
        
        print(f"Procesando {len(df)} registros...")
        
        with app.app_context():
            # Limpiar tabla si existe
            AtencionClinica.query.delete()
            db.session.commit()
            
            registros_guardados = 0
            
            for idx, row in df.iterrows():
                try:
                    # Convertir fechas
                    fecha_atencion = pd.to_datetime(row['fecha_atencion']) if pd.notna(row.get('fecha_atencion')) else None
                    fecha_ultima_regla = pd.to_datetime(row['fecha_ultima_regla']) if pd.notna(row.get('fecha_ultima_regla')) else None
                    
                    # Crear registro
                    atencion = AtencionClinica(
                        fecha_atencion=fecha_atencion,
                        descripcion_ups=str(row.get('descripcion_ups')) if pd.notna(row.get('descripcion_ups')) else None,
                        descripcion_sector=str(row.get('descripcion_sector')) if pd.notna(row.get('descripcion_sector')) else None,
                        descripcion_disa=str(row.get('descripcion_disa')) if pd.notna(row.get('descripcion_disa')) else None,
                        descripcion_red=str(row.get('descripcion_red')) if pd.notna(row.get('descripcion_red')) else None,
                        descripcion_microred=str(row.get('descripcion_microred')) if pd.notna(row.get('descripcion_microred')) else None,
                        genero=str(row.get('genero')) if pd.notna(row.get('genero')) else None,
                        edad_reg=int(row.get('edad_reg')) if pd.notna(row.get('edad_reg')) else None,
                        id_turno=str(row.get('id_turno')) if pd.notna(row.get('id_turno')) else None,
                        descripcion_item=str(row.get('descripcion_item')) if pd.notna(row.get('descripcion_item')) else None,
                        peso=float(row.get('peso')) if pd.notna(row.get('peso')) else None,
                        talla=float(row.get('talla')) if pd.notna(row.get('talla')) else None,
                        hemoglobina=float(row.get('hemoglobina')) if pd.notna(row.get('hemoglobina')) else None,
                        fecha_ultima_regla=fecha_ultima_regla,
                        usuario_registro='Sistema - Carga Inicial'
                    )
                    
                    db.session.add(atencion)
                    registros_guardados += 1
                    
                    if registros_guardados % 10 == 0:
                        print(f"  Guardados {registros_guardados} registros...")
                    
                except Exception as e:
                    print(f"  Error en registro {idx + 1}: {str(e)}")
                    continue
            
            db.session.commit()
            print(f"\n✓ Carga completada: {registros_guardados} registros guardados exitosamente")
            
    except Exception as e:
        print(f"✗ Error al cargar datos: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    # Ruta al archivo Excel
    archivo_excel = 'datos_ejemplo.xlsx'
    
    print("="*60)
    print("Sistema de Datos Clínicos - Carga de Datos de Prueba")
    print("="*60)
    print()
    
    cargar_datos_excel(archivo_excel, limite=100)
    
    print()
    print("="*60)
    print("Proceso finalizado")
    print("="*60)
