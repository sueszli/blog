here's a fun fact: according to the "universitäts- und hochschulstatistik- und bildungsdokumentationsverordnung (uhsbv)" § 4 [^legal1] [^legal2], the austrian "matriculation number" is an eight-digit sequence that encodes the type of university, the year of enrollment, and a unique identifier for the student within that year.

this means you can figure out a persons year of enrollment by using the following function:

```python
def get_enrollment_year(matriculation_number: str) -> int:
    matriculation_number = matriculation_number.strip()
    length = len(matriculation_number)

    assert length == 7 or length == 8
    if length == 8:
        year_digits = matriculation_number[1:3]
        institution_number = matriculation_number[:1]
    elif length == 7:
        year_digits = matriculation_number[0:2]
        institution_number = matriculation_number[:3]

    print(f"institution code: {institution_number}")

    current_year = int(str(2024)[2:])  # get the last two digits of the current year
    enrollment_year = int(year_digits)

    # assume the year is in the past or current year
    if enrollment_year > current_year:
        enrollment_year += 1900
    else:
        enrollment_year += 2000

    return enrollment_year

print(get_enrollment_year("11912007")
>>> institution code: 1
>>> 2019
```

here's a more functional implementation:

```python
get_enrollment_year = lambda m: (lambda d=m.strip(): int(d[1:3] if len(d)==8 else d[:2]) + (1900 if int(d[1:3] if len(d)==8 else d[:2]) > 24 else 2000))()

print(get_enrollment_year("11912007")
```

as an example, my matriculation number "11912007" can be broken down as follows:

- the first digit (1) indicates the type of university → equivalent to: TU Wien (using lookup table[^legal2]))
- the second and third digits (19) represent the last two digits of the year of enrollment → equivalent to: 2019
- the last five digits (12007) are a unique identifier for the student within that year → equivalent to: computer science. there seems to be a pattern based on a case study by the FSINF student club [^fsinf]

an ethical use-case of this function would be sorting students by seniority when looking for people to do group projects with.

# references

[^legal1]: Universitäts- und Hochschulstatistik- und Bildungsdokumentationsverordnung § 4, tagesaktuelle Fassung - https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20011989&Paragraf=4

[^legal2]: https://www.ris.bka.gv.at/Dokumente/BgblAuth/BGBLA_2004_II_288/COO_2026_100_2_112417.pdfsig

[^fsinf]: https://wiki.fsinf.at/wiki/Matrikelnummer
