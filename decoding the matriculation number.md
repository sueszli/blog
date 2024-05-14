the **matriculation number**, a unique identifier assigned to students upon enrollment at universities, is structured to encode specific information about the student's enrollment.

i'd like to take a moment and shine some light on the potential privacy implications of this encoding, particularly focusing on the **leakage of personal information** and its potential misuse.

according to the "universitäts- und hochschulstatistik- und bildungsdokumentationsverordnung (uhsbv)" § 4 [^legal1] [^legal2], the matriculation number is an eight-digit sequence that encodes the type of university, the year of enrollment, and a unique identifier for the student within that year.

**for example**, my matriculation number "11912007" can be broken down as follows:

- the first digit (1) indicates the type of university → meaning the TU Wien (using the lookup table: [^legal2])
- the second and third digits (19) represent the last two digits of the year of enrollment → meaning 2019
- the last five digits (12007) are a unique identifier for the student within that year → most likely meaning computer science. there seems to be a pattern based on a case study by the FSINF student club [^fsinf]

this information, combined with publicly available data, could potentially be used to find personal accounts, identify peers from the same year or even guess elements of the student's password if it includes their birthdate.

**in conclusion** the encoding of personal information within matriculation numbers presents a nuanced privacy concern. and while human error remains the weakest link in any institution (even among security and privacy experts!) it's crucial to study specific details like these, especially in contexts where such identifiers are widely used and potentially accessible to the public.

[^legal1]: Universitäts- und Hochschulstatistik- und Bildungsdokumentationsverordnung § 4, tagesaktuelle Fassung - https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20011989&Paragraf=4

[^legal2]: https://www.ris.bka.gv.at/Dokumente/BgblAuth/BGBLA_2004_II_288/COO_2026_100_2_112417.pdfsig

[^fsinf]: https://wiki.fsinf.at/wiki/Matrikelnummer
