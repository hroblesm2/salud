# 🎯 DEMOSTRACIÓN DEL SISTEMA

## Sistema de Datos Clínicos - GPS Management

### 📸 Recorrido Visual por el Sistema

---

## 1. 🏠 DASHBOARD PRINCIPAL

**URL:** http://localhost:5000

### Características:
- **4 Tarjetas de Métricas:**
  - Total de Atenciones
  - Peso Promedio
  - Talla Promedio
  - Edad Promedio

- **2 Gráficos Interactivos:**
  - Distribución por Género (gráfico de pastel)
  - Top 10 Atenciones por UPS (gráfico de barras)

- **Botones de Acción Rápida:**
  - Nueva Atención
  - Ver Registros
  - Exportar a Excel

### Datos Mostrados:
Con los 100 registros cargados, verás:
- Distribución de pacientes por género
- Servicios más utilizados (OBSTETRICIA, MEDICINA GENERAL, etc.)
- Promedios de signos vitales

---

## 2. 📝 FORMULARIO DE NUEVA ATENCIÓN

**URL:** http://localhost:5000/formulario

### Secciones del Formulario:

#### 📅 Información de Atención
```
- Fecha de Atención (requerido)
- Turno: Mañana / Tarde / Noche
- UPS: OBSTETRICIA, MEDICINA GENERAL, etc.
```

#### 📍 Ubicación del Establecimiento
```
- Sector: MINSA, ESSALUD, etc.
- DISA: LIMA CENTRO, LIMA SUR, etc.
- Red: LIMA CIUDAD, etc.
- Micro Red: C.S. SAN SEBASTIAN, etc.
```

#### 👤 Datos del Paciente
```
- Género: Masculino / Femenino (requerido)
- Edad: 0-120 años (requerido)
- Fecha Última Regla: Solo para género Femenino
```

#### 💉 Datos Clínicos
```
- Peso: en kilogramos (0.00 kg)
- Talla: en centímetros (0.00 cm)
- Hemoglobina: en g/dL (0.0 g/dL)
```

#### 🩺 Diagnóstico/Procedimiento
```
- Descripción del Item: Campo de texto amplio para diagnósticos
  Ejemplo: "GESTANTE CON FACTOR DE RIESGO CONTROL 3ER. TRIMESTRE"
```

### Validaciones Automáticas:
- ✅ Campos obligatorios marcados con asterisco (*)
- ✅ Fecha última regla se habilita solo para género Femenino
- ✅ Rangos numéricos válidos
- ✅ Formato de fecha correcto
- ✅ Confirmación visual al guardar

---

## 3. 📊 GESTIÓN DE REGISTROS

**URL:** http://localhost:5000/registros

### Panel de Filtros:
```
[ Buscar... ] [ Género ▼ ] [ Desde: ] [ Hasta: ] [Filtrar] [Limpiar]
```

### Tabla Interactiva:
Columnas visibles:
- ID
- Fecha Atención
- UPS
- Género
- Edad
- Peso (kg)
- Talla (cm)
- Hemoglobina
- Diagnóstico (truncado)
- Acciones (👁️ Ver | ✏️ Editar | 🗑️ Eliminar)

### Funcionalidades:

#### 🔍 Filtros:
1. **Búsqueda General:** Busca en todos los campos
2. **Por Género:** Masculino / Femenino
3. **Por Fecha:** Rango de fechas de atención
4. **Tiempo Real:** Búsqueda mientras escribes

#### 👁️ Ver Detalle:
Muestra todos los datos en un modal organizado:
- Información completa de la atención
- Datos del paciente
- Datos clínicos
- Diagnóstico completo
- Metadatos (fecha de registro, usuario)

#### ✏️ Editar:
- Modal con formulario prellenado
- Todos los campos editables
- Guardado con confirmación

#### 🗑️ Eliminar:
- Confirmación antes de eliminar
- Acción irreversible
- Notificación de éxito

#### 📄 Paginación:
- 10 registros por página
- Navegación: [Anterior] [1] [2] [3] ... [Siguiente]
- Información: "Mostrando 1 a 10 de 100 registros"

---

## 4. 📥 EXPORTACIÓN A EXCEL

### Desde Dashboard:
- Botón "Exportar a Excel"
- Genera archivo con todos los registros

### Desde Registros:
- Botón en la cabecera de la tabla
- Mismo formato de exportación

### Formato del Excel:
```
Columnas:
- ID
- Fecha_Atencion
- Descripcion_Ups
- Descripcion_Sector
- Descripcion_Disa
- Descripcion_Red
- Descripcion_MicroRed
- Genero
- Edad_Reg
- Id_Turno
- Descripcion_Item
- Peso
- Talla
- Hemoglobina
- Fecha_Ultima_Regla
- Fecha_Registro
- Usuario_Registro
```

### Nombre del Archivo:
`datos_clinicos_YYYY-MM-DD.xlsx`

---

## 5. 🎨 CARACTERÍSTICAS DE DISEÑO

### Interfaz Moderna:
- ✨ Diseño Bootstrap 5
- 🎨 Paleta de colores profesional
- 📱 100% Responsive (móvil, tablet, desktop)
- 🖼️ Iconos Bootstrap Icons
- 💫 Animaciones suaves

### Experiencia de Usuario:
- ⚡ Carga rápida
- 🔔 Notificaciones SweetAlert2
- 📊 Gráficos Chart.js interactivos
- 🎯 Navegación intuitiva
- ♿ Accesible

### Colores:
- Primario: Azul (#0d6efd)
- Éxito: Verde (#28a745)
- Advertencia: Amarillo (#ffc107)
- Peligro: Rojo (#dc3545)
- Info: Cyan (#17a2b8)

---

## 6. 💻 TECNOLOGÍA

### Backend:
```python
- Flask 3.0
- SQLAlchemy
- SQLite
- Pandas
- OpenPyXL
```

### Frontend:
```javascript
- Bootstrap 5.3
- jQuery 3.7
- Chart.js
- SweetAlert2
- Bootstrap Icons
```

---

## 7. 📊 DATOS DE EJEMPLO

Los 100 registros cargados incluyen:

### Distribución Típica:
- **Género:** Aprox. 70-80% Femenino (OBSTETRICIA)
- **UPS:** OBSTETRICIA, MEDICINA GENERAL, etc.
- **Edades:** 20-70 años
- **Peso:** 45-95 kg
- **Talla:** 140-180 cm
- **Hemoglobina:** 10-15 g/dL

### Diagnósticos Comunes:
- Control prenatal
- Gestante con factores de riesgo
- Hipertensión esencial
- Consejerías de salud

---

## 8. 🔐 SEGURIDAD

### Implementado:
- ✅ Validación de datos en backend
- ✅ ORM SQLAlchemy (prevención SQL Injection)
- ✅ Sanitización de entradas
- ✅ Manejo de errores robusto
- ✅ CSRF Protection (Flask)

---

## 9. 🚀 RENDIMIENTO

### Optimizaciones:
- Base de datos indexada
- Paginación de resultados
- Carga asíncrona de datos
- Caché de consultas
- Consultas optimizadas

### Capacidad:
- Soporta miles de registros
- Búsqueda rápida con índices
- Exportación eficiente
- Gráficos renderizados client-side

---

## 10. 📱 RESPONSIVE DESIGN

### Desktop (1920x1080):
- Dashboard completo con 4 columnas
- Tabla amplia
- Todos los elementos visibles

### Tablet (768x1024):
- Dashboard en 2 columnas
- Tabla adaptada
- Navegación colapsable

### Móvil (375x667):
- Dashboard en 1 columna
- Tabla scrolleable horizontal
- Menú hamburguesa
- Formulario optimizado

---

## 🎯 CASOS DE USO

### 1. Registro Diario de Atenciones
```
Escenario: Personal médico registra atenciones del día
Flujo:
1. Ir a "Nueva Atención"
2. Llenar formulario con datos del paciente
3. Guardar
4. Repetir para cada paciente
```

### 2. Consulta de Historial
```
Escenario: Buscar atenciones de un paciente específico
Flujo:
1. Ir a "Registros"
2. Usar filtros (fecha, género, etc.)
3. Ver detalle del registro
4. Exportar si es necesario
```

### 3. Análisis Estadístico
```
Escenario: Revisión mensual de indicadores
Flujo:
1. Ir a Dashboard
2. Revisar métricas generales
3. Analizar gráficos
4. Exportar datos para análisis externo
```

### 4. Corrección de Datos
```
Escenario: Se detecta un error en un registro
Flujo:
1. Ir a "Registros"
2. Buscar el registro
3. Click en "Editar"
4. Corregir datos
5. Guardar cambios
```

---

## 💡 TIPS Y TRUCOS

### Atajos de Teclado:
- `Tab` - Navegar entre campos
- `Enter` - Enviar formulario (en campos de texto)
- `Esc` - Cerrar modales

### Filtros Avanzados:
- Combina múltiples filtros para búsquedas específicas
- Usa el filtro de fecha para reportes mensuales
- La búsqueda general busca en TODOS los campos

### Exportación:
- Exporta regularmente para respaldos
- Usa Excel para análisis avanzados con tablas dinámicas
- El archivo incluye TODOS los registros, no solo los filtrados

### Mantenimiento:
- Elimina registros duplicados periódicamente
- Revisa la base de datos en `/instance/datos_clinicos.db`
- Haz respaldo del archivo .db regularmente

---

## 📞 SOPORTE Y AYUDA

### ¿Problemas al iniciar?
1. Verifica que Python 3.8+ esté instalado
2. Ejecuta `pip install -r requirements.txt`
3. Verifica que el puerto 5000 esté libre

### ¿Datos no se guardan?
1. Revisa la consola para errores
2. Verifica permisos de escritura en `/instance/`
3. Comprueba que los campos obligatorios estén llenos

### ¿Gráficos no cargan?
1. Verifica conexión a internet (para CDNs)
2. Revisa la consola del navegador (F12)
3. Limpia caché del navegador

---

**Sistema desarrollado con ❤️ por GPS Management**
**Versión: 1.0.0 | Enero 2025**
