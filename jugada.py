def jugada_uno(mano, carta_descubierta):
    """
    Dada una `mano` de cartas que tiene un jugador del juego "Uno" y la carta que está descubierta sobre la mesa 
    (`carta_descubierta`), retorna True si el jugador puede hacer una jugada, o False en caso contrario.
    """
    color_descubierta, numero_descubierta = carta_descubierta.split()

    for carta in mano:
        color, numero = carta.split()
        if color == color_descubierta or numero == numero_descubierta:
            return True

    return False

print(jugada_uno(["rojo 5", "azul 4", "verde 2"], "amarillo 6"))
