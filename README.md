# Validación de Direcciones IP con Python

## Descripción

Este proyecto consiste en desarrollar una función en Python para validar direcciones IPv4 y comprobar el funcionamiento mediante pruebas unitarias utilizando el módulo `unittest`.

## Requisitos

- Python 3.8 o superior
- Editor de código (opcional) Recomendado VSC

## Estructura del proyecto

```
.
├── validar_ip.py
├── test_validar_ip.py
└── README.md
```

## Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/usuario/validar-ip.git
```

2. Entrar al directorio del proyecto:

```bash
cd validar-ip
```

3. Verificar que Python esté instalado:

```bash
python --version
```

## Uso

Para ejecutar la función:

```bash
python validar_ip.py
```

Para ejecutar las pruebas unitarias:

```bash
python -m unittest test_validar_ip.py
```

## Casos de prueba

Las pruebas verifican los siguientes escenarios:

- IP válida (192.168.1.1)
- Octeto mayor a 255
- Dirección con letras
- Dirección con menos de 4 partes
- Dirección con más de 4 partes

## Resultado esperado

Al ejecutar las pruebas se debe obtener una salida similar a:

```text
.....
----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
```

## Autor

Carolina Méndez

## Licencia

Este proyecto está bajo la licencia MIT.
