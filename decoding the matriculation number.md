the european matriculation number, a unique identifier assigned to students upon enrollment at universities, is structured to encode specific information about the student's enrollment.

i'd like to take a moment and shine some light on the potential privacy implications of this encoding, particularly focusing on the leakage of personal information and its potential misuse.

according to the "universitäts- und hochschulstatistik- und bildungsdokumentationsverordnung (uhsbv)" § 4 [^legal1] [^legal2], the matriculation number is an eight-digit sequence that encodes the type of university, the year of enrollment, and a unique identifier for the student within that year.

**for example**, the matriculation number "11912007" can be broken down as follows:

- the first digit (1) indicates the type of university → in this case, the technical university of vienna (see: [^legal2])
- the second and third digits (19) represent the last two digits of the year of enrollment → in this case, the year 2019.
- the last five digits (12007) are a unique identifier for the student within that year. [^fsinf]

the structure of the matriculation number allows for the derivation of personal information, such as the approximate age of the student based on their enrollment year.

this information can potentially be used maliciously, for instance, to guess passwords if students use their birthdate as part of their password.

additionally, the matriculation number can be linked to other personal data, facilitating the derivation of more critical information about the student.

using the matriculation number 11912007 as an example, one can infer that the student enrolled in 2019 at a university (likely the technical university of vienna, given the range of numbers assigned to it). this information, combined with publicly available data or social engineering, could potentially be used to find personal accounts, identify peers from the same year, or even guess elements of the student's password if it includes their birthdate.

**in conclusion** the encoding of personal information within matriculation numbers presents a nuanced privacy concern. while the primary purpose of these numbers is administrative, their structure inadvertently facilitates the derivation of personal data. this case study highlights the importance of considering privacy implications in the design of identification systems, especially in contexts where such identifiers are widely used and potentially accessible to the public.

[^legal1]: Universitäts- und Hochschulstatistik- und Bildungsdokumentationsverordnung § 4, tagesaktuelle Fassung - https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20011989&Paragraf=4

[^legal2]: https://www.ris.bka.gv.at/Dokumente/BgblAuth/BGBLA_2004_II_288/COO_2026_100_2_112417.pdfsig

[^fsinf]: https://wiki.fsinf.at/wiki/Matrikelnummer
