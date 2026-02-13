# 🏥 Sistema de Datos Clínicos - GPS Management

Sistema web completo para gestión de atenciones médicas y datos clínicos.

## 🚀 Inicio Rápido (3 Pasos)

### Windows:
```cmd
1. Doble clic en: start.bat
2. Esperar a que abra el navegador o ir a: http://localhost:5000
3. ¡Listo!
```

### Linux/Mac:
```bash
1. Abrir terminal en esta carpeta
2. Ejecutar: ./start.sh
3. Abrir navegador en: http://localhost:5000
```

## 📋 Características

### ✨ Funcionalidades Principales

1. **📝 Formulario de Registro**
   - Campos organizados por categorías
   - Validaciones automáticas
   - Guardado en base de datos

2. **📊 Dashboard Interactivo**
   - Estadísticas en tiempo real
   - Gráficos de distribución
   - Métricas principales

3. **🗂️ Gestión de Registros**
   - Búsqueda y filtros avanzados
   - Edición y eliminación
   - Paginación automática
   - Exportación a Excel

### 📝 Campos del Sistema

**Información de Atención:**
- Fecha de Atención *
- Turno (M/T/N)
- UPS

**Ubicación:**
- Sector
- DISA
- Red
- Micro Red

**Paciente:**
- Género *
- Edad *
- Fecha Última Regla

**Datos Clínicos:**
- Peso (kg)
- Talla (cm)
- Hemoglobina (g/dL)

**Diagnóstico:**
- Descripción del Item

\* Campos obligatorios

## 💾 Base de Datos

El sistema incluye:
- ✅ Base de datos SQLite
- ✅ 1 registro de ejemplo precargado
- ✅ Script para cargar más datos desde Excel

### Cargar tus propios datos:

1. Coloca tu archivo Excel en esta carpeta
2. Asegúrate que tenga las columnas correctas (ver datos_ejemplo.xlsx)
3. Edita `cargar_datos_prueba.py` línea 136:
   ```python
   archivo_excel = 'TU_ARCHIVO.xlsx'
   ```
4. Ejecuta: `python cargar_datos_prueba.py`

## 🔧 Requisitos

- Python 3.8 o superior
- Las dependencias se instalan automáticamente

## 📁 Estructura del Proyecto

```
sistema_datos_clinicos/
├── app.py                      # Aplicación principal
├── requirements.txt            # Dependencias
├── datos_ejemplo.xlsx          # Archivo Excel de ejemplo
├── cargar_datos_prueba.py     # Script para cargar datos
├── start.sh / start.bat       # Scripts de inicio
├── templates/                  # Plantillas HTML
└── static/                     # Archivos estáticos
```

## 🎨 Tecnología

**Backend:** Flask 3.0, SQLAlchemy, SQLite, Pandas  
**Frontend:** Bootstrap 5, jQuery, Chart.js, SweetAlert2

## 📞 Soporte

**Desarrollado por:** GPS Management  
**Versión:** 1.0.0 | Enero 2025

Ver `INICIO_RAPIDO.md` y `DEMOSTRACION.md` para más detalles.
