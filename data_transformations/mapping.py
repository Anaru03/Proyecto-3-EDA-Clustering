import pandas as pd
def standardize_value(x):
    """Convierte valores numéricos a enteros y luego a string, 
    de modo que 1.0 -> "1" y si ya es string se mantiene."""
    try:
        # Si se puede convertir a float, conviértelo a int y luego a str
        return str(int(float(x)))
    except:
        return str(x)
def decode_column(df, column_name, mapping_dict):
    # Imprimir algunos valores antes de decodificar para debug
    print(f"Antes de decodificar {column_name}:")
    print(df[column_name].head(3))
    # Convertir a cadena, quitar el sufijo ".0" y aplicar el mapeo
    df[column_name] = (
        df[column_name]
        .astype(str)
        .str.replace(r'\.0$', '', regex=True)
        .apply(lambda x: mapping_dict.get(x, x))
    )
    print(f"Después de decodificar {column_name}:")
    print(df[column_name].head(3))
    return df

def decode_ocupacion(value):
    if pd.isna(value):
        return value
    try:
        # Convertir el valor a número y luego a string sin decimales
        value_str = str(int(float(value)))
    except Exception as e:
        return value
    # Extraer los dos últimos dígitos
    code = value_str[-2:]
    return ocupacion_mapping.get(code, value_str)

# -----------------------------
# Diccionarios de mapeo
# -----------------------------

# Departamento de registro (y de ocurrencia, pues son iguales)
departamento_registro_mapping = {
    "1": "Guatemala",
    "2": "El Progreso",
    "3": "Sacatepéquez",
    "4": "Chimaltenango",
    "5": "Escuintla",
    "6": "Santa Rosa",
    "7": "Sololá",
    "8": "Totonicapán",
    "9": "Quetzaltenango",
    "10": "Suchitepéquez",
    "11": "Retalhuleu",
    "12": "San Marcos",
    "13": "Huehuetenango",
    "14": "Quiché",
    "15": "Baja Verapaz",
    "16": "Alta Verapaz",
    "17": "Petén",
    "18": "Izabal",
    "19": "Zacapa",
    "20": "Chiquimula",
    "21": "Jalapa",
    "22": "Jutiapa"
}


# Departamento de residencia (incluye opción de extranjero)

# Municipio de registro, ocurrencia, nacimiento y residencia
# (Se muestra un subconjunto representativo; completar según el diccionario completo)
municipio_registro_mapping = {
    "0101": "Guatemala",
    "0102": "Santa Catarina Pinula",
    "0103": "San José Pinula",
    "0104": "San José del Golfo",
    "0105": "Palencia",
    "0106": "Chinautla",
    "0107": "San Pedro Ayampuc",
    "0108": "Mixco",
    "0109": "San Pedro Sacatepéquez",
    "0110": "San Juan Sacatepéquez",
    "0111": "San Raymundo",
    "0112": "Chuarrancho",
    "0113": "Fraijanes",
    "0114": "Amatitlán",
    "0115": "Villa Nueva",
    "0116": "Villa Canales",
    "0117": "Petapa",
    "0201": "Guastatoya",
    "0202": "Morazán",
    "0203": "San Agustín Acasaguastlán",
    "0204": "San Cristóbal Acasaguastlán",
    "0205": "El Jícaro",
    "0206": "Sansare",
    "0207": "Sanarate",
    "0208": "San Antonio la Paz",
    "0301": "Antigua Guatemala",
    "0302": "Jocotenango",
    "0303": "Pastores",
    "0304": "Sumpango",
    "0305": "Santo Domingo Xenacoj",
    "0306": "Santiago Sacatepéquez",
    "0307": "San Bartolomé Milpas Altas",
    "0308": "San Lucas Sacatepéquez",
    "0309": "Santa Lucía Milpas Altas",
    "0310": "Magdalena Milpas Altas",
    "0311": "Santa María de Jesús",
    "0312": "Ciudad Vieja",
    "0313": "San Miguel Dueñas",
    "0314": "Alotenango",
    "0315": "San Antonio Aguas Calientes",
    "0316": "Santa Catarina Barahona",
    "0401": "Chimaltenango",
    "0402": "San José Poaquil",
    "0403": "San Martín Jilotepeque",
    "0404": "Comalapa",
    "0405": "Santa Apolonia",
    "0406": "Tecpán Guatemala",
    "0407": "Patzún",
    "0408": "Pochuta",
    "0409": "Patzicía",
    "0410": "Santa Cruz Balanyá",
    "0411": "Acatenango",
    "0412": "Yepocapa",
    "0413": "San Andrés Itzapa",
    "0414": "Parramos",
    "0415": "Zaragoza",
    "0416": "El Tejar",
    "0501": "Escuintla",
    "0502": "Santa Lucía Cotzumalguapa",
    "0503": "La Democracia",
    "0504": "Siquinalá",
    "0505": "Masagua",
    "0506": "Tiquisate",
    "0507": "La Gomera",
    "0508": "Guanagazapa",
    "0509": "San José",
    "0510": "Iztapa",
    "0511": "Palín",
    "0512": "San Vicente Pacaya",
    "0513": "Nueva Concepción",
    "0514": "Sipacate",
    "0601": "Cuilapa",
    "0602": "Barberena",
    "0603": "Santa Rosa de Lima",
    "0604": "Casillas",
    "0605": "San Rafael las Flores",
    "0606": "Oratorio",
    "0607": "San Juan Tecuaco",
    "0608": "Chiquimulilla",
    "0609": "Taxisco",
    "0610": "Santa María Ixhuatán",
    "0611": "Guazacapán",
    "0612": "Santa Cruz Naranjo",
    "0613": "Pueblo Nuevo Viñas",
    "0614": "Nueva Santa Rosa",
    "0701": "Sololá",
    "0702": "San José Chacayá",
    "0703": "Santa María Visitación",
    "0704": "Santa Lucía Utatlán",
    "0705": "Nahualá",
    "0706": "Santa Catarina Ixtahuacán",
    "0707": "Santa Clara la Laguna",
    "0708": "Concepción",
    "0709": "San Andrés Semetabaj",
    "0710": "Panajachel",
    "0711": "Santa Catarina Palopó",
    "0712": "San Antonio Palopó",
    "0713": "San Lucas Tolimán",
    "0714": "Santa Cruz la Laguna",
    "0715": "San Pablo la Laguna",
    "0716": "San Marcos la Laguna",
    "0717": "San Juan la Laguna",
    "0718": "San Pedro la Laguna",
    "0719": "Santiago Atitlán",
    "0801": "Totonicapán",
    "0802": "San Cristóbal Totonicapán",
    "0803": "San Francisco el Alto",
    "0804": "San Andrés Xecul",
    "0805": "Momostenango",
    "0806": "Santa María Chiquimula",
    "0807": "Santa Lucía la Reforma",
    "0808": "San Bartolo",
    "0901": "Quetzaltenango",
    "0902": "Salcajá",
    "0903": "Olintepeque",
    "0904": "San Carlos Sija",
    "0905": "Sibilia",
    "0906": "Cabricán",
    "0907": "Cajolá",
    "0908": "San Miguel Siguilá",
    "0909": "Ostuncalco",
    "0910": "San Mateo",
    "0911": "Concepción Chiquirichapa",
    "0912": "San Martín Sacatepéquez",
    "0913": "Almolonga",
    "0914": "Cantel",
    "0915": "Huitán",
    "0916": "Zunil",
    "0917": "Colomba",
    "0918": "San Francisco la Unión",
    "0919": "El Palmar",
    "0920": "Coatepeque",
    "0921": "Génova",
    "0922": "Flores Costa Cuca",
    "0923": "La Esperanza",
    "0924": "Palestina de los Altos",
    "1001": "Mazatenango",
    "1002": "Cuyotenango",
    "1003": "San Francisco Zapotitlán",
    "1004": "San Bernardino",
    "1005": "San José el Idolo",
    "1006": "Santo Domingo Suchitepéquez",
    "1007": "San Lorenzo",
    "1008": "Samayac",
    "1009": "San Pablo Jocopilas",
    "1010": "San Antonio Suchitepéquez",
    "1011": "San Miguel Panán",
    "1012": "San Gabriel",
    "1013": "Chicacao",
    "1014": "Patulul",
    "1015": "Santa Bárbara",
    "1016": "San Juan Bautista",
    "1017": "Santo Tomás la Unión",
    "1018": "Zunilito",
    "1019": "Pueblo Nuevo",
    "1020": "Río Bravo",
    "1021": "San José La Máquina",
    "1101": "Retalhuleu",
    "1102": "San Sebastián",
    "1103": "Santa Cruz Muluá",
    "1104": "San Martín Zapotitlán",
    "1105": "San Felipe",
    "1106": "San Andrés Villa Seca",
    "1107": "Champerico",
    "1108": "Nuevo San Carlos",
    "1109": "El Asintal",
    "1201": "San Marcos",
    "1202": "San Pedro Sacatepéquez",
    "1203": "San Antonio Sacatepéquez",
    "1204": "Comitancillo",
    "1205": "San Miguel Ixtahuacán",
    "1206": "Concepción Tutuapa",
    "1207": "Tacaná",
    "1208": "Sibinal",
    "1209": "Tajumulco",
    "1210": "Tejutla",
    "1211": "San Rafael Pié de la Cuesta",
    "1212": "Nuevo Progreso",
    "1213": "El Tumbador",
    "1214": "El Rodeo",
    "1215": "Malacatán",
    "1216": "Catarina",
    "1217": "Ayutla",
    "1218": "Ocós",
    "1219": "San Pablo",
    "1220": "El Quetzal",
    "1221": "La Reforma",
    "1222": "Pajapita",
    "1223": "Ixchiguán",
    "1224": "San José Ojetenán",
    "1225": "San Cristóbal Cucho",
    "1226": "Sipacapa",
    "1227": "Esquipulas Palo Gordo",
    "1228": "Río Blanco",
    "1229": "San Lorenzo",
    "1230": "La Blanca",
    "1301": "Huehuetenango",
    "1302": "Chiantla",
    "1303": "Malacatancito",
    "1304": "Cuilco",
    "1305": "Nentón",
    "1306": "San Pedro Necta",
    "1307": "Jacaltenango",
    "1308": "Soloma",
    "1309": "Ixtahuacán",
    "1310": "Santa Bárbara",
    "1311": "La Libertad",
    "1312": "La Democracia",
    "1313": "San Miguel Acatán",
    "1314": "San Rafael la Independencia",
    "1315": "Todos Santos Cuchumatán",
    "1316": "San Juan Atitán",
    "1317": "Santa Eulalia",
    "1318": "San Mateo Ixtatán",
    "1319": "Colotenango",
    "1320": "San Sebastián Huehuetenango",
    "1321": "Tectitán",
    "1322": "Concepción Huista",
    "1323": "San Juan Ixcoy",
    "1324": "San Antonio Huista",
    "1325": "San Sebastián Coatán",
    "1326": "Barillas",
    "1327": "Aguacatán",
    "1328": "San Rafael Petzal",
    "1329": "San Gaspar Ixchil",
    "1330": "Santiago Chimaltenango",
    "1331": "Santa Ana Huista",
    "1332": "Unión Cantinil",
    "1333": "Petatán",
    "1401": "Santa Cruz del Quiché",
    "1402": "Chiché",
    "1403": "Chinique",
    "1404": "Zacualpa",
    "1405": "Chajul",
    "1406": "Chichicastenango",
    "1407": "Patzité",
    "1408": "San Antonio Ilotenango",
    "1409": "San Pedro Jocopilas",
    "1410": "Cunén",
    "1411": "San Juan Cotzal",
    "1412": "Joyabaj",
    "1413": "Nebaj",
    "1414": "San Andrés Sajcabajá",
    "1415": "Uspantán",
    "1416": "Sacapulas",
    "1417": "San Bartolomé Jocotenango",
    "1418": "Canillá",
    "1419": "Chicamán",
    "1420": "Ixcán",
    "1421": "Pachalum",
    "1501": "Salamá",
    "1502": "San Miguel Chicaj",
    "1503": "Rabinal",
    "1504": "Cubulco",
    "1505": "Granados",
    "1506": "El Chol",
    "1507": "San Jerónimo",
    "1508": "Purulhá",
    "1601": "Cobán",
    "1602": "Santa Cruz Verapaz",
    "1603": "San Cristóbal Verapaz",
    "1604": "Tactic",
    "1605": "Tamahú",
    "1606": "Tucurú",
    "1607": "Panzós",
    "1608": "Senahú",
    "1609": "San Pedro Carchá",
    "1610": "San Juan Chamelco",
    "1611": "Lanquín",
    "1612": "Cahabón",
    "1613": "Chisec",
    "1614": "Chahal",
    "1615": "Fray Bartolomé de las Casas",
    "1616": "Santa Catalina la Tinta",
    "1617": "Raxruhá",
    "1701": "Flores",
    "1702": "San José",
    "1703": "San Benito",
    "1704": "San Andrés",
    "1705": "La Libertad",
    "1706": "San Francisco",
    "1707": "Santa Ana",
    "1708": "Dolores",
    "1709": "San Luis",
    "1710": "Sayaxché",
    "1711": "Melchor de Mencos",
    "1712": "Poptún",
    "1713": "Las Cruces",
    "1714": "El Chal",
    "1801": "Puerto Barrios",
    "1802": "Livingston",
    "1803": "El Estor",
    "1804": "Morales",
    "1805": "Los Amates",
    "1901": "Zacapa",
    "1902": "Estanzuela",
    "1903": "Río Hondo",
    "1904": "Gualán",
    "1905": "Teculután",
    "1906": "Usumatlán",
    "1907": "Cabañas",
    "1908": "San Diego",
    "1909": "La Unión",
    "1910": "Huité",
    "1911": "San Jorge",
    "2001": "Chiquimula",
    "2002": "San José La Arada",
    "2003": "San Juan Ermita",
    "2004": "Jocotán",
    "2005": "Camotán",
    "2006": "Olopa",
    "2007": "Esquipulas",
    "2008": "Concepción Las Minas",
    "2009": "Quetzaltepeque",
    "2010": "San Jacinto",
    "2011": "Ipala",
    "2101": "Jalapa",
    "2102": "San Pedro Pinula",
    "2103": "San Luis Jilotepeque",
    "2104": "San Manuel Chaparrón",
    "2105": "San Carlos Alzatate",
    "2106": "Monjas",
    "2107": "Mataquescuintla",
    "2201": "Jutiapa",
    "2202": "El Progreso",
    "2203": "Santa Catarina Mita",
    "2204": "Agua Blanca",
    "2205": "Asunción Mita",
    "2206": "Yupiltepeque",
    "2207": "Atescatempa",
    "2208": "Jerez",
    "2209": "El Adelanto",
    "2210": "Zapotitlán",
    "2211": "Comapa",
    "2212": "Jalpatagua",
    "2213": "Conguaco",
    "2214": "Moyuta",
    "2215": "Pasaco",
    "2216": "San José Acatempa",
    "2217": "Quesada",
    "2300": "Extranjero",
    "9999": "Ignorado"
}


# Mes (para registro y ocurrencia)
mes_mapping = {
    "1": "Enero",
    "2": "Febrero",
    "3": "Marzo",
    "4": "Abril",
    "5": "Mayo",
    "6": "Junio",
    "7": "Julio",
    "8": "Agosto",
    "9": "Septiembre",
    "10": "Octubre",
    "11": "Noviembre",
    "12": "Diciembre"
}

# Año: Se asume que se mantienen los valores numéricos (por ejemplo, 2021, 2022)
# Sexo del difunto(a)
sexo_mapping = {
    "1": "Hombre",
    "2": "Mujer"
}


# Día de ocurrencia (se mapea a string para facilitar la lectura)
dia_mapping = {i: str(i) for i in range(1, 32)}

# Periodo de edad del difunto(a)
periodo_edad_mapping = {
    "1": "Menos de un mes",
    "2": "1 a 11 meses",
    "3": "1 año y más",
    "9": "Ignorado"
}

# Pueblo de pertenencia del difunto(a)
pueblo_mapping = {
    "1": "Maya",
    "2": "Garífuna",
    "3": "Xinka",
    "4": "Mestizo / Ladino",
    "5": "Otro",
    "9": "Ignorado"
}

# Estado civil del difunto(a)
estado_civil_mapping = {
    "1": "Soltero",
    "2": "Casado",
    "3": "Unido",
    "9": "Ignorado"
}


# Escolaridad del difunto(a)
escolaridad_mapping = {
    "1": "Ninguno",
    "2": "Primaria",
    "3": "Básica",
    "4": "Diversificado",
    "5": "Universitario",
    "6": "Post grado",
    "9": "Ignorado"
}
# Departamento de nacimiento (origen) – se usa para Dnadif
departamento_nacimiento_mapping = {
    "1": "Guatemala",
    "2": "El Progreso",
    "3": "Sacatepéquez",
    "4": "Chimaltenango",
    "5": "Escuintla",
    "6": "Santa Rosa",
    "7": "Sololá",
    "8": "Totonicapán",
    "9": "Quetzaltenango",
    "10": "Suchitepéquez",
    "11": "Retalhuleu",
    "12": "San Marcos",
    "13": "Huehuetenango",
    "14": "Quiché",
    "15": "Baja Verapaz",
    "16": "Alta Verapaz",
    "17": "Petén",
    "18": "Izabal",
    "19": "Zacapa",
    "20": "Chiquimula",
    "21": "Jalapa",
    "22": "Jutiapa",
    "23": "Extranjero",
    "99": "Ignorado"
}

# Ocupación (Subgrupos CIUO-08) del difunto(a)
ocupacion_mapping = {
    "01": "Oficiales de las fuerzas armadas",
    "03": "Otros miembros de las fuerzas armadas",
    "11": "Directores ejecutivos, personal directivo de administración pública, miembros del poder ejecutivo y cuerpos legislativos",
    "12": "Directores administradores y comerciales",
    "13": "Directores y gerentes de producción y operaciones",
    "14": "Gerentes de hoteles, restaurantes, comercios y otros servicios",
    "21": "Profesionales de las ciencias y de la ingeniería",
    "22": "Profesionales de la salud",
    "23": "Profesionales de la enseñanza",
    "24": "Especialistas en organización de la administración publica y de empresas",
    "25": "Profesionales de tecnología de la información y las comunicaciones",
    "26": "Profesionales en derecho, en ciencias sociales y culturales",
    "31": "Profesionales de las ciencias y la ingeniería de nivel medio",
    "32": "Profesionales de nivel medio de la salud",
    "33": "Profesionales de nivel medio en operaciones financieras y administrativas",
    "34": "Profesionales de nivel medio de servicios jurídicos, sociales, culturales y afines",
    "35": "Técnicos de la tecnología de la información y las comunicaciones",
    "41": "Oficinistas",
    "42": "Empleados en trato directo con el público",
    "43": "Empleados contables y encargados del registro de materiales",
    "44": "Otro personal de apoyo administrativo",
    "51": "Trabajadores de los servicios personales",
    "52": "Vendedores",
    "53": "Trabajadores de los cuidados personales",
    "54": "Personal de los servicios de protección",
    "61": "Agricultores y trabajadores calificados de explotaciones agropecuarias con destino al mercado",
    "62": "Trabajadores forestales calificados, pescadores y cazadores",
    "63": "Trabajadores agropecuarios, pescadores, cazadores y recolectores de subsistencia",
    "71": "Oficiales y operarios de la construcción excluyendo electricistas",
    "72": "Oficiales y operarios de la metalurgia, la construcción mecánica y afines",
    "73": "Artesanos y operarios de las artes gráficas",
    "74": "Trabajadores especializados en electricidad y la elecrotecnología",
    "75": "Operarios y oficiales de procesamiento de alimentos, de la confección, ebanistas, otros artesanos y afines",
    "81": "Operadores de instalaciones fijas y máquinas",
    "82": "Ensambladores",
    "83": "Conductores de vehículos y operadores de equipos pesados móviles",
    "91": "Limpiadores y asistentes",
    "92": "Peones agropecuarios, pesqueros y forestales",
    "93": "Peones de la minería, la construcción, la industria manufacturera y el transporte",
    "94": "Ayudantes de preparación de alimentos",
    "95": "Vendedores ambulantes de servicios y afines",
    "96": "Recolectores de desechos y otras ocupaciones elementales",
    "97": "No especificado en otro grupo",
    "99": "Ignorado"
}
municipio_nacimiento_mapping = municipio_registro_mapping.copy()

pais_nacimiento_mapping = {
    10: "Turquia",
    32: "Argentina",
    36: "Australia",
    40: "Austria",
    56: "Bélgica",
    68: "Bolivia",
    76: "Brasil",
    84: "Belice",
    124: "Canadá",
    152: "Chile",
    156: "China",
    170: "Colombia",
    188: "Costa Rica",
    192: "Cuba",
    218: "Ecuador",
    222: "El Salvador",
    233: "Estonia",
    276: "Alemania",
    292: "Gibraltar",
    300: "Grecia",
    320: "Guatemala",
    324: "Guinea",
    332: "Haití",
    340: "Honduras",
    380: "Italia",
    392: "Japón",
    400: "Jordania",
    410: "República De Corea",
    422: "Líbano",
    484: "México",
    568: "G. Bretaña E Irl. Del N.",
    586: "Pakistán",
    604: "Perú",
    608: "Filipinas",
    616: "Polonia",
    620: "Portugal",
    630: "Puerto Rico",
    718: "Holanda (Paises Bajos)",
    720: "Nicaragua",
    724: "España",
    725: "Checoslovaquia",
    756: "Suiza",
    804: "Ucrania",
    840: "Estados Unidos De América",
    858: "Uruguay",
    862: "Rep. Boliv. De Venezuela",
    1020: "Francia",
    1021: "India",
    1026: "Panamá",
    1043: "República de China (Taiwan)",
    9999: "Ignorado"
}
# Agregamos la clave 0 para que se decodifique correctamente:
pais_nacimiento_mapping[0] = "Guatemala"


# Nacionalidad del difunto(a) (se asume igual que pais de nacimiento)
nacionalidad_mapping = pais_nacimiento_mapping.copy()

# Pais de residencia del difunto(a)
pais_residencia_mapping = {
    "124": "Canadá",
    "170": "Colombia",
    "192": "Cuba",
    "222": "El Salvador",
    "276": "Alemania",
    "320": "Guatemala",
    "332": "Haití",
    "340": "Honduras",
    "380": "Italia",
    "484": "México",
    "604": "Perú",
    "608": "Filipinas",
    "720": "Nicaragua",
    "840": "Estados Unidos De América",
    "9999": "Ignorado"
}
# Asistencia recibida
asistencia_mapping = {
    "1": "Médica",
    "2": "Paramédica",
    "3": "Comadrona",
    "4": "Empírica",
    "5": "Ninguna",
    "9": "Ignorado"
}
# Sitio de ocurrencia
sitio_ocurrencia_mapping = {
    "1": "Hospital público",
    "2": "Hospital privado",
    "3": "Centro de salud",
    "4": "Seguro social",
    "5": "Vía pública",
    "6": "Domicilio",
    "7": "Lugar de trabajo",
    "8": "Otro",
    "9": "Ignorado"
}

# Pais de residencia
pais_residencia_mapping = {
    "124": "Canadá",
    "170": "Colombia",
    "192": "Cuba",
    "222": "El Salvador",
    "276": "Alemania",
    "320": "Guatemala",
    "332": "Haití",
    "340": "Honduras",
    "380": "Italia",
    "484": "México",
    "604": "Perú",
    "608": "Filipinas",
    "720": "Nicaragua",
    "840": "Estados Unidos De América",
    "9999": "Ignorado"
}

# Quien certifica
quien_certifica_mapping = {
    "1": "Medico",
    "2": "Paramedico",
    "3": "Autoridad",
    "9": "Ignorado"
}
departamento_residencia_mapping = departamento_registro_mapping.copy()
municipio_residencia_mapping = municipio_registro_mapping.copy()
departamento_nacimiento_mapping = {
    "1": "Guatemala",
    "2": "El Progreso",
    "3": "Sacatepéquez",
    "4": "Chimaltenango",
    "5": "Escuintla",
    "6": "Santa Rosa",
    "7": "Sololá",
    "8": "Totonicapán",
    "9": "Quetzaltenango",
    "10": "Suchitepéquez",
    "11": "Retalhuleu",
    "12": "San Marcos",
    "13": "Huehuetenango",
    "14": "Quiché",
    "15": "Baja Verapaz",
    "16": "Alta Verapaz",
    "17": "Petén",
    "18": "Izabal",
    "19": "Zacapa",
    "20": "Chiquimula",
    "21": "Jalapa",
    "22": "Jutiapa",
    "23": "Extranjero",
    "99": "Ignorado"
}
# -----------------------------
# Lectura del dataset y decodificación
# -----------------------------
def decode_mnadif(x):
    """
    Convierte el código de municipio de nacimiento a una cadena de 4 dígitos y lo mapea.
    """
    try:
        if pd.notnull(x):
            # Convertir a entero (en caso de números en formato float) y a string de 4 dígitos
            s = str(int(float(x))).zfill(4)
            return municipio_nacimiento_mapping.get(s, s)
        else:
            return x
    except Exception as e:
        return x

def decode_nacdif(x):
    """
    Convierte el código a entero y lo mapea en el diccionario de país de nacimiento.
    """
    try:
        if pd.notnull(x):
            code = int(float(x))
            return pais_nacimiento_mapping.get(code, str(code))
        else:
            return x
    except Exception as e:
        return x
# Prueba cambiar encoding si aparecen caracteres extraños; por ejemplo, usa 'latin1'
df = pd.read_csv(
    'C:/Users/rodri/Documents/Data-Mining/Proyecto-3-EDA-Clustering/data/master.csv',
    low_memory=False, 
    encoding='utf-8'
)
df.rename(columns=lambda x: x.replace('AÃ±', 'Añ'), inplace=True)

print("Available columns in the dataset:")
print(df.columns.tolist())

# 
# Para Mnadif: Aseguramos que el código tenga 4 dígitos y luego mapeamos
print("Antes de decodificar Mnadif:")
print(df['Mnadif'].head())
df['Mnadif'] = df['Mnadif'].apply(decode_mnadif)
print("Después de decodificar Mnadif:")
print(df['Mnadif'].head())

# Para Nacdif: Convertimos el código a entero y mapeamos
print("Antes de decodificar Nacdif:")
print(df['Nacdif'].head())
df['Nacdif'] = df['Nacdif'].apply(decode_nacdif)
print("Después de decodificar Nacdif:")
print(df['Nacdif'].head())

# (Opcional) Para Escodif y Puedif, si no tienen datos, podemos dejarlo así o asignar un valor por defecto.
# Por ejemplo:
df['Escodif'] = df['Escodif'].fillna("Ignorado")
df['Puedif'] = df['Puedif'].fillna("Ignorado")

# --- Guardar el DataFrame actualizado ---
# Use chunked writing to avoid memory issues
print("Guardando el archivo CSV en chunks para evitar problemas de memoria...")
chunk_size = 10000  # Adjust based on your system's memory

# Create the file with headers
df.iloc[0:0].to_csv('C:/Users/rodri/Documents/Data-Mining/Proyecto-3-EDA-Clustering/data/merged_data_decoded_master.csv',
                    index=False, encoding='utf-8')

# Append data in chunks
for i in range(0, len(df), chunk_size):
    print(f"Guardando chunk {i//chunk_size + 1} de {(len(df) // chunk_size) + 1}...")
    df.iloc[i:i+chunk_size].to_csv(
        'C:/Users/rodri/Documents/Data-Mining/Proyecto-3-EDA-Clustering/data/merged_data_decoded_master.csv',
        mode='a', header=False, index=False, encoding='utf-8'
    )

print("Actualización de columnas completada y archivo guardado.")