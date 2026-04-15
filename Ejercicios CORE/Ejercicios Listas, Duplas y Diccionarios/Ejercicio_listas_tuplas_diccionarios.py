#Carga de Datos:
ventas = [
    {"fecha": "2023-01-01", "producto": "Laptop", "cantidad": 1, "precio": 1000.00},
    {"fecha": "2023-01-01", "producto": "Mouse", "cantidad": 2, "precio": 20.00},
    
    {"fecha": "2023-01-02", "producto": "Teclado", "cantidad": 1, "precio": 50.00},
    {"fecha": "2023-01-02", "producto": "Mouse", "cantidad": 1, "precio": 22.00},
    
    {"fecha": "2023-01-03", "producto": "Laptop", "cantidad": 2, "precio": 950.00},
    {"fecha": "2023-01-03", "producto": "Monitor", "cantidad": 1, "precio": 300.00},
    
    {"fecha": "2023-01-04", "producto": "Teclado", "cantidad": 2, "precio": 55.00},
    {"fecha": "2023-01-04", "producto": "Mouse", "cantidad": 3, "precio": 19.50},
    
    {"fecha": "2023-01-05", "producto": "Monitor", "cantidad": 2, "precio": 310.00},
    {"fecha": "2023-01-05", "producto": "Laptop", "cantidad": 1, "precio": 980.00}
]


#Cálculo de Ingresos Totales:
def calcular_ingresos_totales(ventas):
    ingresos_totales = 0
    for venta in ventas:
        ingresos_totales += venta["cantidad"] * venta["precio"]
    return ingresos_totales

ingresos = calcular_ingresos_totales(ventas)
print(f"Ingresos Totales: ${ingresos:.2f}")


#Análisis del Producto Más Vendido:
def calcular_ventas_por_producto(ventas):
    ventas_por_producto = {}
    for venta in ventas:
        producto = venta["producto"]
        cantidad = venta["cantidad"]

        if producto in ventas_por_producto:
            ventas_por_producto[producto] += cantidad
        else:
            ventas_por_producto[producto] = cantidad

    return ventas_por_producto

ventas_por_producto = calcular_ventas_por_producto(ventas)
producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)
print(ventas_por_producto)
print(f"\nProducto mas vendido: {producto_mas_vendido} con {ventas_por_producto[producto_mas_vendido]} unidades vendidas")

#Promedio de Precio por Producto
#Crea un diccionario llamado precios_por_producto donde las claves sean los nombres de los productos y los valores sean tuplas. Cada tupla debe contener dos elementos: la suma de los precios de venta de todas las unidades vendidas y la cantidad total de unidades vendidas.
def calcular_precios_por_producto(ventas):
    precios_por_producto = {}

    for venta in ventas:
        producto = venta["producto"]
        precio_total = venta["cantidad"] * venta["precio"]
        cantidad = venta["cantidad"]

        if producto in precios_por_producto:
            total_precio, total_cantidad = precios_por_producto[producto]
            precios_por_producto[producto] = (
                total_precio + precio_total,
                total_cantidad + cantidad
            )
        else:
            precios_por_producto[producto] = (precio_total, cantidad)

    return precios_por_producto

precios_por_producto = calcular_precios_por_producto(ventas)

def calcular_promedio_precio(precios_por_producto):
    promedio_precio = {}
    for producto, (precio_total, cantidad) in precios_por_producto.items():
        if cantidad > 0:
            promedio_precio[producto] = precio_total / cantidad
        else:
            promedio_precio[producto] = 0
    return promedio_precio

promedio_precio = calcular_promedio_precio(precios_por_producto)
print(f"\nPromedio de precio por producto:")
for producto, promedio in promedio_precio.items():
    print(f"{producto}: ${promedio:.2f}")

#Ventas por Día
def calcular_ingresos_por_dia(ventas):
    nuevo_diccionario = {}
    for venta in ventas:
        fecha = venta["fecha"]
        cantidad = venta["cantidad"] * venta["precio"]
        
        if fecha in nuevo_diccionario:
            nuevo_diccionario[fecha] += cantidad
        else:
            nuevo_diccionario[fecha] = cantidad
    return nuevo_diccionario

ventas_por_dia = calcular_ingresos_por_dia(ventas)
print(f"\nVentas por dia:")
for fecha, monto in ventas_por_dia.items():
    print(f"{fecha}: ${monto:.2f}")


#Representación de Datos:
def crear_resumen_ventas(ventas):
    resumen_ventas = {}
    for venta in ventas:
        producto = venta["producto"]
        cantidad = venta["cantidad"]
        ingresos = cantidad * venta["precio"]
        
        if producto not in resumen_ventas:
            resumen_ventas[producto] = {
                "cantidad_total": 0,
                "ingresos_totales": 0,
                "precio_promedio": 0
            }
        
        resumen_ventas[producto]["cantidad_total"] += cantidad
        resumen_ventas[producto]["ingresos_totales"] += ingresos
    
    for producto, datos in resumen_ventas.items():
        if datos["cantidad_total"] > 0:
            datos["precio_promedio"] = datos["ingresos_totales"] / datos["cantidad_total"]
    
    return resumen_ventas

resumen_ventas = crear_resumen_ventas(ventas)
print(f"\nResumen de ventas por producto:")
for producto, datos in resumen_ventas.items():
    print(f"{producto}: Cantidad Total: {datos['cantidad_total']}, Ingresos Totales: ${datos['ingresos_totales']:.2f}, Precio Promedio: ${datos['precio_promedio']:.2f}")