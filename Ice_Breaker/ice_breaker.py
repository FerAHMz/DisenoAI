from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

information = """TenZ (nacido el 5 de mayo de 2001), es un canadiense streamer en línea y ex profesional Valorante y Contraataque: Ofensiva Global jugador.[3][4][5]

Comenzó su carrera en los deportes electrónicos en octubre de 2019 como Contraataque: Ofensiva Global jugador para Nube9. En abril de 2020, hizo la transición a Valorante, jugando para Cloud9. Se tomó un descanso del profesional Valorante en enero de 2021, se centrará en la carrera de transmisión a tiempo completo en Twitch. Más tarde en abril, fue prestado a Centinelas. Luego ganó el VCT Etapa Dos Masters en Reykjavík más tarde ese año. En junio de 2021, Sentinels compró su contrato Cloud9, donde permanecería hasta el final de su carrera profesional en septiembre de 2024.

Carrera
La carrera profesional de TenZ comenzó en julio de 2019 cuando, a la edad de 18 años, se unió a la Nube9 equipo en el tirador en primera persona título Contraataque: Ofensiva Global (CS:GO). Fue visto como un prodigio en ascenso en América del Norte. Anteriormente había defendido algunas organizaciones. Sin embargo, después de que el equipo no logró rendir a un alto nivel, TenZ fue enviado a la banca en octubre de ese año.[6][7][8]

TenZ comenzó la creación de contenido a tiempo completo en enero de 2020.[9] Sin embargo, en abril de 2020, tras la versión beta pública de Juegos de Riot' tirador en primera persona ValoranteTenZ anunció su decisión de retirarse de CS:GO y optó por la transición a Valorante, convirtiéndose así en el primer jugador profesional de Cloud9 en el título.[10][11]

En enero de 2021, TenZ anunció su salida del profesional Valorante centrarse en una carrera en la creación de contenido.[12] Sin embargo, su pausa fue de corta duración, ya que Cloud9 acordó prestarle a TenZ Centinelas en abril de 2021, tras la suspensión del jugador de los Centinelas Sinatraa.[13] Durante las dos primeras etapas del 2021 Valorante Tour de Campeones (VCT), TenZ compitió remotamente desde Canadá. Sentinels ganó el primer internacional Valorante torneo, el VCT Stage 2 Masters Reykjavík después de barrer Fnástico en las grandes finales por un puntaje de 3–0; TenZ fue nombrado MVP de las grandes finales.[14] El 2 de junio de 2021, Sentinels compró el contrato de TenZ, que según se informa se valora entre US$1.25 a $1.5 millones.[15][16]

Después de su primer trofeo internacional el 30 de mayo de 2021, TenZ y Sentinels no ganarían otro trofeo durante casi 3 años.

El 18 de abril de 2023, el entrenador en jefe de los Sentinels, Adam Kaplan, anunció que TenZ estaría temporalmente en la banca debido a una enfermedad y una lesión en la mano.[17]

El 24 de marzo de 2024, TenZ logró su segundo trofeo internacional, ganando el VCT Masters Madrid junto a Sentinels al derrotar Género.G 3-2. Con esta victoria, él es el segundo Valorante jugador en ganar dos trofeos Masters, y el único jugador en hacerlo bajo la misma organización. (Timofey "Chronicle" Khromov fue el primero en hacerlo Gambito y Fnástico.)[18]

El 14 de septiembre de 2024, TenZ anunció su retiro de profesional Valorante después de cuatro años de competir.

Vida personal
Ngo, nacido el 5 de mayo de 2001[19] es de Nanaimo, en la isla de Vancouver, Columbia Británica, y es de Vietnamita y Francés descenso.[1] Vivió en Canadá antes de mudarse Los Ángeles en enero de 2022.[14]

Ngo está actualmente comprometido con Shymko Kyedae, un creador de contenido. La pareja anunció su compromiso en agosto de 2022.[20][19]

Ngo declaró en una entrevista que tenía TDAHél no abordó completamente el trastorno hasta que se tomó un descanso de la competencia Valorante.[21]

Ngo también reveló en un video publicado en el canal oficial de YouTube de Sentinels que es protanomalía daltónicoy como resultado usa amarillo en lugar de rojo como su enemigo resalta el color Valorante.[22]"""

if __name__ == "__main__":
    load_dotenv()

    sumary_template = f"""
    Given the information {information} about a person from I want to create:
    1. A short sumary
    2. Two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables = ["information"], template = sumary_template
    )

    llm = ChatOpenAI(
        temperature = 0,
        model_name = "gpt-3.5-turbo"
    )

    chain = summary_prompt_template | llm

    res = chain.invoke(input = {"information": information})

    print(res)