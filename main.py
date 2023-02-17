class Auto:
  cantidadCreados = 0

  def __init__(self, modelo, precio, asientos, marca, motor, registro):
    self.modelo = modelo
    self.precio = precio
    self.asientos = asientos
    self.marca = marca
    self.motor = motor
    self.registro = registro

  def cantidadAsientos(self):
    totalAsientos = 0

    for asiento in self.asientos:
      if asiento != None:
        totalAsientos += 1
    
    return totalAsientos

  def verificarIntegridad(self):
    if self.motor and self.motor.registro != self.registro:
      return "Las piezas no son originales"

    for asiento in self.asientos:
      if asiento and asiento.registro != self.registro:
        return "Las piezas no son originales"

    return "Auto original"


class Asiento:
  def __init__(self, color, precio, registro):
    self.color = color
    self.precio = precio
    self.registro = registro

  def cambiarColor(self, color):
    validColors = ["rojo", "verde", "amarillo", "negro", "blanco"]
    
    for validColor in validColors:
      if validColor == color:
        self.color = color


class Motor:
  def __init__(self, numeroCilindros, tipo, registro):
    self.numeroCilindros = numeroCilindros
    self.tipo = tipo
    self.registro = registro

  def cambiarRegistro(self, registro):
    self.registro = registro

  def asignarTipo(self, tipo):
    validTipos = ["electrico", "gasolina"]

    if validTipos.count(tipo) >= 1:
      self.tipo = tipo
