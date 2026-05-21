import pandas as pd

def cargar_datos(archivo):
    """Carga los datos de ventas desde un archivo CSV"""
    df = pd.read_csv(archivo)
    df['fecha'] = pd.to_datetime(df['fecha'])
    df['total_venta'] = df['cantidad'] * df['precio_unitario']
    return df

def calcular_ventas_totales_por_producto(df):
    """Calcula las ventas totales por producto"""
    print("\n=== VENTAS TOTALES POR PRODUCTO ===")
    ventas_producto = df.groupby('producto')['total_venta'].sum()
    print(ventas_producto)
    return ventas_producto

def calcular_promedio_ventas_diarias(df):
    """Calcula el promedio de ventas diarias"""
    print("\n=== PROMEDIO DE VENTAS DIARIAS ===")
    promedio = df['total_venta'].mean()
    print(f"$ {promedio:.2f}")
    return promedio

def identificar_producto_mas_vendido(df):
    """Identifica el producto más vendido por cantidad"""
    print("\n=== PRODUCTO MÁS VENDIDO ===")
    producto_top = df.groupby('producto')['cantidad'].sum().idxmax()
    cantidad_top = df.groupby('producto')['cantidad'].sum().max()
    print(f"Producto: {producto_top} - Cantidad: {cantidad_top} unidades")
    return producto_top, cantidad_top

def generar_reporte(df):
    """Genera un reporte completo de ventas"""
    print("\n" + "="*50)
    print("          REPORTE DE ANÁLISIS DE VENTAS")
    print("="*50)
    print(f"Período analizado: {df['fecha'].min().date()} a {df['fecha'].max().date()}")
    print(f"Total de registros: {len(df)}")
    print(f"Ingresos totales: $ {df['total_venta'].sum():.2f}")
    
    calcular_ventas_totales_por_producto(df)
    calcular_promedio_ventas_diarias(df)
    identificar_producto_mas_vendido(df)
    print("="*50)

def main():
    # Cargar datos
    archivo = "data/ventas.csv"
    df = cargar_datos(archivo)
    
    # Generar reporte
    generar_reporte(df)

if __name__ == "__main__":
    main()
