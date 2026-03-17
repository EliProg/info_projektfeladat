<h1>Box mozdulatok felismerése és kritikája mesterséges intelligenciával.</h1>

#### Tartalomjegyzék
- [A projektről](#a-projektről)
- [Mediapipe](#mediapipe)
- [Volt projektek](#volt-projektek)
- [Eszközlista](#eszközlista)
- [Időbeosztás](#időbeosztás)
- [Források](#források)

## A projektről
A program célja, hogy akár előrefelvett, akár élő kamerfelvétel alapján, felismerje egy egyén box ütéseit, majd képes legyen ennek technikai formáját kritizálni. 

Több probléma megoldására szolgál, főként azok számára, akiknek nem elérhető megfelelő edzési visszajelzés, így rossz szokások kialalkulását tudják el tudják kerülni. Valamint, akár mindennapi használatra is fel lehet használni, hogy akár tapasztaltabb harcművészek is pontosan végezzék a gyakorlatokat.

Ezt, főként a **Mediapipe** testrész felismerő keretrendszerrel valósítjuk meg, mely pontos koordinákat köt egy detektált testhez. Egy mesterséges intelligencia modell kitanításával, és megfelelő megkötésekkel, lehetséges a program kivitele. A témája főként Computer Vision, valamint gépi tanulás.


[⬆ Vissza a tetejére](#tartalomjegyzék)

## Mediapipe

Egy nyíltforráskódú keretrendszer, melyet Python nyelvben használunk fel, már előre elkészített könyvtár felhasználásával. Egy detektált testre, koordinátákat helyez el, melyek alapján képes a test pozícióját követni. 


[⬆ Vissza a tetejére](#tartalomjegyzék)

## Volt projektek

[⬆ Vissza a tetejére](#tartalomjegyzék)

## Eszközlista

[⬆ Vissza a tetejére](#tartalomjegyzék)


## Időbeosztás
1. március 9-15
    - GitHub README

2. március 16-22
    - Adatgyűjtés.

3. március 23-29
    - Adatok tisztása, valamint modell feltanítása.

4. március 30 - április 5
    - Előre felvett videók alapján tesztelés, troubleshooting.

5. április 6-12
    - Komplexebb box logika implementálása a modell tudásbázisára.

6. április 13-19
    - Tesztelés, valamint esetleges YOLO integráció póz felismerésre.

7. április 20-26
    - Tovább fejlesztés, módosítások eszközlése.

8. április 27 - május 3
    - Esetleges csúszás behozása.
    
9. május 7
    - Bemutatás.

[⬆ Vissza a tetejére](#tartalomjegyzék)

## Források
[⬆ Vissza a tetejére](#tartalomjegyzék)
