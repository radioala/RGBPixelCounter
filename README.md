
#Licznik Kolorów Pikseli
Ten skrypt w języku Python analizuje plik obrazu i liczy liczbę pikseli o różnych kolorach na podstawie zestawu zasad. Zasady określają, czy piksel jest sklasyfikowany jako czerwony, zielony, niebieski lub szary. Następnie skrypt zapisuje statystyki do pliku tekstowego.

#Jak to działa
Skrypt używa biblioteki Python Imaging Library (PIL) do otwarcia i przetworzenia obrazu. Zasady liczenia są następujące:

Jeśli wszystkie trzy wartości RGB są równe, piksel jest uważany za szary.
Jeśli zielony ma najwyższą wartość (lub jest równy czerwieni lub niebieskiemu), piksel jest zielony.
Jeśli czerwony ma najwyższą wartość (lub jest równy niebieskiemu), piksel jest czerwony.
Jeśli niebieski ma najwyższą wartość, piksel jest niebieski.
W przypadku remisu między dwoma kolorami, zielony ma pierwszeństwo przed czerwonym i niebieskim, a czerwony ma pierwszeństwo przed niebieskim.

#Użycie
Uruchom skrypt, wykonując funkcję main().
Podaj ścieżkę do pliku obrazu, gdy zostaniesz o to poproszony.
Podaj nazwę pliku wynikowego do zapisania statystyk (musi kończyć się '.txt').
Skrypt przetworzy obraz, policzy kolory pikseli i zapisze statystyki do określonego pliku tekstowego.
