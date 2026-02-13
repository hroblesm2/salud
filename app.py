from flask import Flask, render_template, request, jsonify, send_file
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pandas as pd
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///datos_clinicos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'gps-management-datos-clinicos-2025'

db = SQLAlchemy(app)

class AtencionClinica(db.Model):
    __tablename__ = 'atenciones_clinicas'
    
    id = db.Column(db.Integer, primary_key=True)
    
    # Datos de fecha y ubicación
    fecha_atencion = db.Column(db.DateTime, nullable=False)
    descripcion_ups = db.Column(db.String(200))
    descripcion_sector = db.Column(db.String(100))
    descripcion_disa = db.Column(db.String(100))
    descripcion_red = db.Column(db.String(100))
    descripcion_microred = db.Column(db.String(100))
    
    # Datos del paciente
    genero = db.Column(db.String(1))
    edad_reg = db.Column(db.Integer)
    id_turno = db.Column(db.String(10))
    
    # Descripción del item/diagnóstico
    descripcion_item = db.Column(db.Text)
    
    # Datos clínicos
    peso = db.Column(db.Float)
    talla = db.Column(db.Float)
    hemoglobina = db.Column(db.Float)
    fecha_ultima_regla = db.Column(db.DateTime, nullable=True)
    
    # Metadatos
    fecha_registro = db.Column(db.DateTime, default=datetime.now)
    usuario_registro = db.Column(db.String(100))
    
    def to_dict(self):
        return {
            'id': self.id,
            'fecha_atencion': self.fecha_atencion.strftime('%Y-%m-%d %H:%M:%S') if self.fecha_atencion else None,
            'descripcion_ups': self.descripcion_ups,
            'descripcion_sector': self.descripcion_sector,
            'descripcion_disa': self.descripcion_disa,
            'descripcion_red': self.descripcion_red,
            'descripcion_microred': self.descripcion_microred,
            'genero': self.genero,
            'edad_reg': self.edad_reg,
            'id_turno': self.id_turno,
            'descripcion_item': self.descripcion_item,
            'peso': self.peso,
            'talla': self.talla,
            'hemoglobina': self.hemoglobina,
            'fecha_ultima_regla': self.fecha_ultima_regla.strftime('%Y-%m-%d') if self.fecha_ultima_regla else None,
            'fecha_registro': self.fecha_registro.strftime('%Y-%m-%d %H:%M:%S') if self.fecha_registro else None,
            'usuario_registro': self.usuario_registro
        }

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route('/registros')
def registros():
    return render_template('registros.html')

@app.route('/api/guardar_atencion', methods=['POST'])
def guardar_atencion():
    try:
        data = request.json
        
        # Crear nueva atención
        atencion = AtencionClinica(
            fecha_atencion=datetime.strptime(data['fecha_atencion'], '%Y-%m-%d'),
            descripcion_ups=data.get('descripcion_ups'),
            descripcion_sector=data.get('descripcion_sector'),
            descripcion_disa=data.get('descripcion_disa'),
            descripcion_red=data.get('descripcion_red'),
            descripcion_microred=data.get('descripcion_microred'),
            genero=data.get('genero'),
            edad_reg=int(data.get('edad_reg', 0)) if data.get('edad_reg') else None,
            id_turno=data.get('id_turno'),
            descripcion_item=data.get('descripcion_item'),
            peso=float(data.get('peso', 0)) if data.get('peso') else None,
            talla=float(data.get('talla', 0)) if data.get('talla') else None,
            hemoglobina=float(data.get('hemoglobina', 0)) if data.get('hemoglobina') else None,
            fecha_ultima_regla=datetime.strptime(data['fecha_ultima_regla'], '%Y-%m-%d') if data.get('fecha_ultima_regla') else None,
            usuario_registro=data.get('usuario_registro', 'Sistema')
        )
        
        db.session.add(atencion)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Atención registrada exitosamente',
            'id': atencion.id
        })
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'message': f'Error al guardar: {str(e)}'
        }), 400

@app.route('/api/obtener_atenciones', methods=['GET'])
def obtener_atenciones():
    try:
        atenciones = AtencionClinica.query.order_by(AtencionClinica.fecha_atencion.desc()).all()
        return jsonify({
            'success': True,
            'data': [atencion.to_dict() for atencion in atenciones]
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error al obtener atenciones: {str(e)}'
        }), 400

@app.route('/api/obtener_atencion/<int:id>', methods=['GET'])
def obtener_atencion(id):
    try:
        atencion = AtencionClinica.query.get(id)
        if atencion:
            return jsonify({
                'success': True,
                'data': atencion.to_dict()
            })
        else:
            return jsonify({
                'success': False,
                'message': 'Atención no encontrada'
            }), 404
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error: {str(e)}'
        }), 400

@app.route('/api/actualizar_atencion/<int:id>', methods=['PUT'])
def actualizar_atencion(id):
    try:
        atencion = AtencionClinica.query.get(id)
        if not atencion:
            return jsonify({
                'success': False,
                'message': 'Atención no encontrada'
            }), 404
        
        data = request.json
        
        # Actualizar campos
        atencion.fecha_atencion = datetime.strptime(data['fecha_atencion'], '%Y-%m-%d')
        atencion.descripcion_ups = data.get('descripcion_ups')
        atencion.descripcion_sector = data.get('descripcion_sector')
        atencion.descripcion_disa = data.get('descripcion_disa')
        atencion.descripcion_red = data.get('descripcion_red')
        atencion.descripcion_microred = data.get('descripcion_microred')
        atencion.genero = data.get('genero')
        atencion.edad_reg = int(data.get('edad_reg', 0)) if data.get('edad_reg') else None
        atencion.id_turno = data.get('id_turno')
        atencion.descripcion_item = data.get('descripcion_item')
        atencion.peso = float(data.get('peso', 0)) if data.get('peso') else None
        atencion.talla = float(data.get('talla', 0)) if data.get('talla') else None
        atencion.hemoglobina = float(data.get('hemoglobina', 0)) if data.get('hemoglobina') else None
        atencion.fecha_ultima_regla = datetime.strptime(data['fecha_ultima_regla'], '%Y-%m-%d') if data.get('fecha_ultima_regla') else None
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Atención actualizada exitosamente'
        })
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'message': f'Error al actualizar: {str(e)}'
        }), 400

@app.route('/api/eliminar_atencion/<int:id>', methods=['DELETE'])
def eliminar_atencion(id):
    try:
        atencion = AtencionClinica.query.get(id)
        if not atencion:
            return jsonify({
                'success': False,
                'message': 'Atención no encontrada'
            }), 404
        
        db.session.delete(atencion)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Atención eliminada exitosamente'
        })
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'message': f'Error al eliminar: {str(e)}'
        }), 400

@app.route('/api/exportar_excel', methods=['GET'])
def exportar_excel():
    try:
        atenciones = AtencionClinica.query.all()
        
        data = []
        for atencion in atenciones:
            data.append({
                'ID': atencion.id,
                'Fecha_Atencion': atencion.fecha_atencion,
                'Descripcion_Ups': atencion.descripcion_ups,
                'Descripcion_Sector': atencion.descripcion_sector,
                'Descripcion_Disa': atencion.descripcion_disa,
                'Descripcion_Red': atencion.descripcion_red,
                'Descripcion_MicroRed': atencion.descripcion_microred,
                'Genero': atencion.genero,
                'Edad_Reg': atencion.edad_reg,
                'Id_Turno': atencion.id_turno,
                'Descripcion_Item': atencion.descripcion_item,
                'Peso': atencion.peso,
                'Talla': atencion.talla,
                'Hemoglobina': atencion.hemoglobina,
                'Fecha_Ultima_Regla': atencion.fecha_ultima_regla,
                'Fecha_Registro': atencion.fecha_registro,
                'Usuario_Registro': atencion.usuario_registro
            })
        
        df = pd.DataFrame(data)
        
        # Crear directorio de exportación si no existe
        export_dir = '/home/claude/exports'
        os.makedirs(export_dir, exist_ok=True)
        
        filename = f'datos_clinicos_{datetime.now().strftime("%Y%m%d_%H%M%S")}.xlsx'
        filepath = os.path.join(export_dir, filename)
        
        df.to_excel(filepath, index=False, engine='openpyxl')
        
        return send_file(filepath, as_attachment=True, download_name=filename)
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error al exportar: {str(e)}'
        }), 400

@app.route('/api/estadisticas', methods=['GET'])
def estadisticas():
    try:
        total_atenciones = AtencionClinica.query.count()
        
        # Estadísticas por género
        stats_genero = db.session.query(
            AtencionClinica.genero,
            db.func.count(AtencionClinica.id)
        ).group_by(AtencionClinica.genero).all()
        
        # Estadísticas por UPS
        stats_ups = db.session.query(
            AtencionClinica.descripcion_ups,
            db.func.count(AtencionClinica.id)
        ).group_by(AtencionClinica.descripcion_ups).all()
        
        # Promedios de datos clínicos
        promedios = db.session.query(
            db.func.avg(AtencionClinica.peso),
            db.func.avg(AtencionClinica.talla),
            db.func.avg(AtencionClinica.hemoglobina),
            db.func.avg(AtencionClinica.edad_reg)
        ).first()
        
        return jsonify({
            'success': True,
            'data': {
                'total_atenciones': total_atenciones,
                'por_genero': [{'genero': g[0], 'cantidad': g[1]} for g in stats_genero],
                'por_ups': [{'ups': u[0], 'cantidad': u[1]} for u in stats_ups if u[0]],
                'promedios': {
                    'peso': round(promedios[0], 2) if promedios[0] else 0,
                    'talla': round(promedios[1], 2) if promedios[1] else 0,
                    'hemoglobina': round(promedios[2], 2) if promedios[2] else 0,
                    'edad': round(promedios[3], 2) if promedios[3] else 0
                }
            }
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error al obtener estadísticas: {str(e)}'
        }), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
