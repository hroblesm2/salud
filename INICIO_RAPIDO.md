# 🚀 GUÍA RÁPIDA DE INICIO

## Sistema de Datos Clínicos - GPS Management

### ⚡ Inicio Rápido (3 pasos)

#### Windows:
```cmd
1. Hacer doble clic en: start.bat
2. Esperar a que se abra el navegador o ir a: http://localhost:5000
3. ¡Listo para usar!
```

#### Linux/Mac:
```bash
1. Abrir terminal en esta carpeta
2. Ejecutar: ./start.sh
3. Abrir navegador en: http://localhost:5000
```

### 📊 Ya incluye 100 registros de prueba

El sistema viene precargado con 100 registros de ejemplo del archivo Excel original para que puedas probarlo inmediatamente.

### 🎯 Funcionalidades Disponibles

1. **Dashboard** (http://localhost:5000)
   - Estadísticas en tiempo real
   - Gráficos interactivos
   - Métricas principales

2. **Nueva Atención** (http://localhost:5000/formulario)
   - Formulario completo validado
   - Guardado automático en base de datos
   - Campos condicionales inteligentes

3. **Registros** (http://localhost:5000/registros)
   - Ver todos los registros
   - Buscar y filtrar
   - Editar y eliminar
   - Exportar a Excel

### 💾 Estructura de Campos

**Información de Atención:**
- Fecha de Atención
- Turno (M/T/N)
- UPS

**Ubicación:**
- Sector
- DISA
- Red  
- Micro Red

**Datos del Paciente:**
- Género
- Edad
- Fecha Última Regla (FUR)

**Datos Clínicos:**
- Peso (kg)
- Talla (cm)
- Hemoglobina (g/dL)

**Diagnóstico:**
- Descripción del Item

### 📁 Archivos Importantes

- `app.py` - Aplicación principal
- `templates/` - Páginas HTML
- `static/` - Estilos y recursos
- `instance/datos_clinicos.db` - Base de datos con registros
- `cargar_datos_prueba.py` - Script para cargar más datos
- `requirements.txt` - Dependencias Python

### 🔧 Requisitos

- Python 3.8 o superior
- Las dependencias se instalan automáticamente al ejecutar start.sh o start.bat

### 📞 Soporte

Sistema desarrollado por GPS Management
Para consultas: Referirse a README.md completo

### 🎓 Tips de Uso

1. Los filtros en la página de Registros funcionan en tiempo real
2. Puedes exportar a Excel desde el Dashboard o desde Registros
3. El sistema guarda automáticamente cada vez que presionas "Guardar"
4. Los gráficos se actualizan automáticamente con cada nuevo registro

### 🔄 Cargar Más Datos

Si quieres cargar más datos del Excel original:

```bash
python cargar_datos_prueba.py
```

El script cargará hasta 100 registros del archivo Excel. Puedes modificar el límite en el código.

---

**¡Disfruta del sistema!** 🎉
