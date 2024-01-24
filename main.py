from PIL import Image


def count_pixel_colors(image_path):
    """
    Oblicza ilość pikseli w różnych kolorach na podstawie reguły:
    
    jeśli wszystkie 3 wartości RGB są jednakowe piksel jest szary, 
    jeśli G jest największe (albo największe na równi z R lub B) piksel jest zielony, 
    jeśli R jest największe (lub największe na równi z B) piksel jest czerwony, 
    a jeśli B jest największe, piksel jest niebieski. 
    Inaczej mówiąc zawsze kanał z największą wartością wygrywa, j
    eśli jest remis między 3 kolorami to piksel jest szary, 
    a jeśli jest remis między 2 kolorami to G pokonuje R i B, a R pokonuje B.

    Parameters:
    - image_path (str): Ścieżka do pliku obrazu.

    Returns:
    Tuple: Krotka zawierająca liczbę czerwonych, zielonych, niebieskich, szarych pikseli i łączną liczbę pikseli.
    """
    try:
        image = Image.open(image_path)
        
        if image.mode != "RGB":
            image = image.convert("RGB")
            
        pixel_data = list(image.getdata())
        red_count = 0
        green_count = 0
        blue_count = 0
        gray_count = 0

        for pixel in pixel_data:
            r, g, b = pixel
            # jeśli wszystkie 3 wartości RGB są jednakowe piksel jest szary
            if r == g == b:
                gray_count += 1
            # jeśli G jest największe (albo największe na równi z R lub B) piksel jest zielony
            elif g >= r and g >= b:
                green_count += 1
            # jeśli R jest największe (lub największe na równi z B) piksel jest czerwony
            elif r >= g and r >= b:
                red_count += 1
            # a jeśli B jest największe, piksel jest niebieski
            elif b > g and b > r:
                blue_count += 1
            else:
              print(f"Coś poszło nie tak, pixel: {pixel} nie spełnia żadnej zasady")

        total_pixels = red_count + green_count + blue_count + gray_count
        return red_count, green_count, blue_count, gray_count, total_pixels
        
    except Exception as e:
        print(f"Wystąpił błąd przy otwieraniu obrazka: {e}")
        return 0, 0, 0, 0, 0
    
def save_results_to_file(file, image_path, red_count, green_count, blue_count, gray_count, total_pixels):
    """
    Zapisuje wyniki statystyk do pliku output (pliku .txt). Sprawdza czy plik o danej nazwie już istnieje. Jeśli tak pyta
    użykownika czy chce go nadpisać

    Parameters:
    - file (str): Ścieżka do pliku wynikowego.
    - image_path (str): Ścieżka do pliku obrazka.
    - red_count (int): Liczba czerwonych pikseli.
    - green_count (int): Liczba zielonych pikseli.
    - blue_count (int): Liczba niebieskich pikseli.
    - gray_count (int): Liczba szarych pikseli.
    - total_pixels (int): Łączna liczba pikseli.
    """
    try:
        with open(file, "x") as output:
            output.write(f"Nazwa obrazka: {image_path}\n")
            output.write(f"Liczba czerwonych pikseli: {red_count}\n")
            output.write(f"Liczba zielonych pikseli: {green_count}\n")
            output.write(f"Liczba niebieskich pikseli: {blue_count}\n")
            output.write(f"Liczba szarych pikseli: {gray_count}\n")
            output.write(f"Łączna liczba pikseli: {total_pixels}\n")
        print(f"Statystyki zostały zapisane do pliku: {file}")
    except FileExistsError:
        overwrite = input(f"Plik o podnaej nazwie {file} już istnieje. Jeśli chcesz go napisać wciśnij 'T'").upper()
        if overwrite == 'T':
            with open(file, "w") as output:
                output.write(f"Nazwa obrazka: {image_path}\n")
                output.write(f"Liczba czerwonych pikseli: {red_count}\n")
                output.write(f"Liczba zielonych pikseli: {green_count}\n")
                output.write(f"Liczba niebieskich pikseli: {blue_count}\n")
                output.write(f"Liczba szarych pikseli: {gray_count}\n")
                output.write(f"Łączna liczba pikseli: {total_pixels}\n")
            print(f"Statystyki zostały zapisane do pliku: {file}")
        else:
            print("Plik nie został nadpisany.")

def check_image_existence(image_path):
    """
    Sprawdza czy istnieje ścieżka do obrazka podana przez użytkownika.

    Parameters:
    - image_path (str): Ścieżka do  obrazka.

    Returns:
    bool: True, jeśli obrazek istnieje, False w przeciwnym razie.
    """
    try:
        with open(image_path, "rb"):
            pass
        return True
    except FileNotFoundError:
        print("Obrazek o podanej nazwie nie istnieje")
        return False
    except Exception as e:
        print(f"Wystąpił błąd przy otwieraniu obrazka: {e}")
        return False
        
    
def main():
    """
    Główna funkcja programu, pobiera nazwę pliku obrazka, oblicza statystyki i zapisuje wyniki do pliku tekstowego.
    """
    # wczytywanie nazwy obrazka
    image_path = input("Podaj nazwę obrazka: ")
    while not check_image_existence(image_path):
        image_path = input("Podaj poprawną nazwę obrazka: ")
    # wczytywanie nazwy pliku
    output_file = input("Podaj nazwę pliku do zapisu wyników (txt): ")
    while not output_file.endswith(".txt"):
        output_file = input("Plik musi kończyć się '.txt'. Podaj poprawną nazwę pliku do zapisu wyników (txt): ")
    # obliczenie liczby pixeli
    red_count, green_count, blue_count, gray_count, total_pixels = count_pixel_colors(image_path)
    # zapisywanie statystyk do pliku 
    save_results_to_file(output_file,image_path,red_count, green_count, blue_count, gray_count, total_pixels)


if __name__ == "__main__":
    main()
